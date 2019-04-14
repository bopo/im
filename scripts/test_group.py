# -*- coding: utf-8 -*-
import json
import logging
import pprint
import sys
import time
from urllib.parse import urlencode
from user import User

import redis
import requests

import config
import pymysql
import pytest

from group import Group
# from mysql import Mysql

from rpc import send_group_notification

publish_message = Group.publish_message

rds = redis.StrictRedis(host=config.REDIS_HOST, port=config.REDIS_PORT, password=config.REDIS_PASSWORD, db=config.REDIS_DB)

db = pymysql.connect(*config.MYSQL)
# db = Mysql(*config.MYSQL)

APPID = config.APPID

def create_group(master, name, is_super, members):
    appid = APPID
    
    gid = Group.create_group(db, appid, master, name, is_super, members)
    s = 1 if is_super else 0
    content = "%d,%d,%d"%(gid, appid, s)

    publish_message(rds, "group_create", content)
    
    for mem in members:
        content = "%d,%d"%(gid, mem)
        publish_message(rds, "group_member_add", content)
    
    v = {
        "group_id":gid, 
        "master":master, 
        "name":name, 
        "members":members,
        "timestamp":int(time.time())
    }

    op = {"create":v}
    send_group_notification(appid, gid, op, members)
    
    return gid



def delete_group(gid):
    appid = APPID
    Group.disband_group(db, gid)

    v = {
        "group_id":gid,
        "timestamp":int(time.time())
    }

    op = {"disband":v}
    send_group_notification(appid, gid, op, None)

    content = "%d"%gid
    publish_message(rds, "group_disband", content)


def upgrade_group(gid):
    """从普通群升级为超级群"""
    appid = APPID
    group = Group.get_group(db, gid)

    members = Group.get_group_members(db, gid)

    if not group:
        raise ResponseMeta(400, "group non exists")

    Group.update_group_super(db, gid, 1)

    content = "%d,%d,%d"%(gid, appid, 1)
    publish_message(rds, "group_upgrade", content)

    v = {
        "group_id":gid,
        "timestamp":int(time.time()),
        "super":1
    }

    op = {"upgrade":v}
    send_group_notification(appid, gid, op, None)


def update_group(gid):
    """更新群组名称"""
    appid = request.appid
    obj = json.loads(request.data)
    name = obj["name"]
    Group.update_group_name(db, gid, name)

    v = {
        "group_id":gid,
        "timestamp":int(time.time()),
        "name":name
    }

    op = {"update_name":v}
    
    send_group_notification(appid, gid, op, None)
    
def add_group_member(gid, members):
    appid = APPID
    if len(members) == 0:
        return

    db.begin()
    for member_id in members:
        try:
            Group.add_group_member(db, gid, member_id)
        except umysql.SQLError as e:
            #1062 duplicate member
            if e[0] != 1062:
                raise

    db.commit()

    for member_id in members:
        v = {
            "group_id":gid,
            "member_id":member_id,
            "timestamp":int(time.time())
        }
        op = {"add_member":v}
        send_group_notification(appid, gid, op, [member_id])
         
        content = "%d,%d"%(gid, member_id)
        publish_message(rds, "group_member_add", content)



def remove_group_member(gid, memberid):
    appid = APPID
    Group.delete_group_member(db, gid, memberid)
         
    v = {
        "group_id":gid,
        "member_id":memberid,
        "timestamp":int(time.time())
    }
    op = {"quit_group":v}
    send_group_notification(appid, gid, op, [memberid])
     
    content = "%d,%d"%(gid,memberid)
    publish_message(rds, "group_member_remove", content)
    


def get_groups(uid):
    """获取个人的群组列表"""
    appid = APPID
    groups = Group.get_groups(db, appid, uid)
    return groups

@pytest.fixture(scope='function')
def test_create():
    master = int(sys.argv[2])
    name = sys.argv[3]
    is_super = int(sys.argv[4])
    members = []

    for m in sys.argv[5:]:
        assert members.append(int(m))

    gid = create_group(master, name, is_super, members)
    assert gid

@pytest.fixture(scope='function')
def test_delete():
    gid = int(sys.argv[2])
    assert delete_group(gid)

@pytest.fixture(scope='function')
def test_upgrade():        
    gid = int(sys.argv[2])
    assert upgrade_group(gid)

@pytest.fixture(scope='function')
def test_add_member():        
    gid = int(sys.argv[2])
    members = []        
    for m in sys.argv[3:]:
        members.append(int(m))
        assert add_group_member(gid, members)

@pytest.fixture(scope='function')
def test_remove_member():
    gid = int(sys.argv[2])
    for m in sys.argv[3:]:
        assert remove_group_member(gid, int(m))

@pytest.fixture(scope='function')
def test_get():            
    uid = 1
    groups = get_groups(uid)
    assert groups
