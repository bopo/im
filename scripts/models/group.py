# -*- coding: utf-8 -*-
import logging

import redis


def execute(db, sql):
    try:
        # 执行sql语句
        cursor = db.cursor()
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        return cursor
    except:
        # 如果发生错误则回滚
        print('error:', )
        db.rollback()

    return None


def db_update(db, sql):
    cursor = execute(db, sql)
    return cursor


def db_insert(db, sql):
    cursor = execute(db, sql)
    return cursor.lastrowid if hasattr(cursor, 'lastrowid') else cursor


def db_delete(db, sql):
    cursor = execute(db, sql)
    return cursor.lastrowid if hasattr(cursor, 'lastrowid') else cursor


def db_fetchall(db, sql):
    cursor = execute(db, sql)
    return cursor.fetchall()


def db_fetchone(db, sql):
    cursor = execute(db, sql)
    return cursor.fetchone()


class Group(object):
    # 外部指定groupid
    @staticmethod
    def create_group_ext(db, group_id, appid, master, name, is_super, members):
        # db.begin()
        s = 1 if is_super else 0
        sql = "INSERT INTO `group`(`id`, `appid`, `master`, `name`, `super`) VALUES('%s', '%s', '%s', '%s', '%s')" % (
            group_id, appid, master, name, s)

        db_insert(db, sql)
        return group_id

    # 使用自增的groupid
    @staticmethod
    def create_group(db, appid, master, name, is_super, members):
        print(members)
        s = 1 if is_super else 0
        sql = "INSERT INTO `group`(`appid`, `master`, `name`, `super`) VALUES('%s','%s', '%s', '%s')" % (appid, master, name, s)
        gid = db_insert(db, sql)

        if gid:
            for m in members:
                sql = "INSERT INTO `group_member`(`group_id`, `uid`) VALUES('%s', '%s')" % (gid, m)
                db_insert(db, sql)

        return gid

    @staticmethod
    def update_group_name(db, gid, name):
        sql = "UPDATE `group` SET name='%s' WHERE `id`='%s'" % (name, gid)
        db_update(db, sql)

    @staticmethod
    def update_group_notice(db, group_id, notice):
        sql = "UPDATE `group` SET notice=%s WHERE id=%s" % (notice, group_id)
        row = db_update(db, sql)
        logging.debug("update group notice rows:%s", row.rowcount)

    @staticmethod
    def update_group_super(db, group_id, is_super):
        s = 1 if is_super else 0
        sql = "UPDATE `group` SET super=%s WHERE id=%s" % (s, group_id)
        row = db_update(db, sql)
        logging.debug("update group super:%s", row.rowcount)

    @staticmethod
    def disband_group(db, group_id):
        sql = "DELETE FROM `group` WHERE id=%s" % group_id
        row = db_delete(db, sql)
        logging.debug("rows:%s", row)

        sql = "DELETE FROM group_member WHERE group_id=%s" % group_id
        row = db_delete(db, sql)
        logging.debug("delete group rows:%s", row)

    @staticmethod
    def add_group_member(db, group_id, member_id):
        sql = "INSERT INTO group_member(group_id, uid) VALUES(%s, %s)" % (group_id, member_id)
        r = db_insert(db, sql)
        logging.debug("insert rows:%s", r)

    @staticmethod
    def delete_group_member(db, group_id, member_id):
        sql = "DELETE FROM group_member WHERE group_id=%s AND uid=%s" % (group_id, member_id)
        r = db_delete(db, sql)
        logging.debug("delete group member rows:%s", r)

    @staticmethod
    def get_group_members(db, group_id):
        sql = "SELECT uid, nickname FROM group_member WHERE group_id=%s" % group_id
        rows = db_fetchall(db, sql)
        return list(rows)

    @staticmethod
    def update_nickname(db, group_id, member_id, nickname):
        sql = "UPDATE `group_member` SET nickname=%s WHERE group_id=%s AND uid=%s" % (nickname, group_id, member_id)
        # r = db.execute(sql, (nickname, group_id, member_id))
        r = db_update(db, sql)
        logging.debug("update nickname rows:%s", r.rowcount)

    @staticmethod
    def get_group_master(db, group_id):
        sql = "SELECT master FROM `group` WHERE id=%s" % group_id
        r = db_fetchone(db, sql)
        return r["master"]

    @staticmethod
    def get_group(db, group_id):
        sql = "SELECT id, appid, master, super, name, COALESCE(notice, '') as notice FROM `group` WHERE id=%s" % group_id
        r = db_fetchone(db, sql)
        return r

    # 获取用户所在的所有群
    @staticmethod
    def get_groups(db, appid, uid):
        sql = "SELECT g.id, g.appid, g.master, g.super, g.name, COALESCE(g.notice, '') as notice FROM `group_member`, `group` as g WHERE group_member.uid=%s AND group_member.group_id=g.id AND g.appid=%s"
        sql = sql % (uid, appid)
        cursor = db_fetchall(db, sql)
        return list(cursor)

    # groups_actions_id 每个操作的序号，自增
    # groups_actions 记录之前的action ID 和当前的action ID 格式："prev_id:id"
    @staticmethod
    def publish_message(rds, channel, msg):
        with rds.pipeline() as pipe:
            while True:
                try:
                    pipe.watch("groups_actions_id")
                    pipe.watch("groups_actions")
                    action_id = pipe.get("groups_actions_id")
                    action_id = int(action_id) if action_id else 0
                    action_id = action_id + 1

                    group_actions = pipe.get("groups_actions").decode()
                    prev_id = 0

                    if group_actions:
                        _, prev_id = group_actions.split(":")

                    pipe.multi()
                    pipe.set("groups_actions_id", action_id)

                    group_actions = "%s:%s" % (prev_id, action_id)
                    pipe.set("groups_actions", group_actions)

                    m = "%s:%s" % (group_actions, msg)
                    pipe.publish(channel, m)

                    pipe.execute()
                    logging.info("publish msg:%s actions:%s", msg, group_actions)
                    break
                except redis.WatchError as e:
                    logging.info("watch err:%s", e)
