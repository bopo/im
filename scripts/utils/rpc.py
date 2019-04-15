# -*- coding: utf-8 -*-
import json
import logging
from urllib.parse import urlencode

import requests

import config

im_url = config.IM_RPC_URL


def post_message(appid, sender, receiver, cls, content):
    params = {
        "appid": appid,
        "class": cls,
        "sender": sender
    }

    payload = {
        "receiver": receiver,
        "content": content,
    }

    url = im_url + "/post_im_message?" + urlencode(params)

    logging.debug("url:%s", url)

    return requests.post(url, json=payload)


def send_group_notification_s(appid, gid, notification, members):
    url = im_url + "/post_group_notification"

    payload = {
        "appid": appid,
        "group_id": gid,
        "notification": json.dumps(notification)
    }

    if members:
        payload["members"] = members

    resp = requests.post(url, json=payload)

    if resp.status_code != 200:
        logging.warning("send group notification error:%s", resp.content)
    else:
        logging.debug("send group notification success:%s", payload)

    print('content:', resp.content)
    print('status_code:', resp.status_code)

    return resp


def send_group_notification(appid, gid, op, members):
    try:
        return send_group_notification_s(appid, gid, op, members)
    except Exception as e:
        logging.warning("send group notification err:%s", e)
        return None


def init_message_queue(appid, uid, platform_id, device_id):
    payload = {
        "appid": appid,
        "uid": uid,
        "device_id": device_id,
        "platform_id": platform_id
    }

    url = im_url + "/init_message_queue"
    logging.debug("url:%s", url)

    res = requests.post(url, json=payload)
    return res.status_code == 200


def get_offline_count(appid, uid, platform_id, device_id):
    params = {
        "appid": appid,
        "uid": uid,
        "device_id": device_id,
        "platform_id": platform_id
    }

    url = im_url + "/get_offline_count"
    logging.debug("url:%s", url)
    headers = {"Content-Type": "application/json"}

    res = requests.get(url, params=params, headers=headers)

    if res.status_code != 200:
        return 0
    else:
        r = res.json()
        return r["data"]["count"]


def dequeue_message(appid, uid, msgid):
    payload = {
        "appid": appid,
        "uid": uid,
        "msgid": msgid
    }

    url = im_url + "/dequeue_message"
    res = requests.post(url, json=payload)
    return res.status_code == 200
