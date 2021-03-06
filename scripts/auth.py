# -*- coding: utf-8 -*-
import hashlib
import random
import sys

import redis

import config
from models.user import User

rds = redis.StrictRedis(host=config.REDIS_HOST, password=config.REDIS_PASSWORD, port=config.REDIS_PORT,
                        db=config.REDIS_DB)

UNICODE_ASCII_CHARACTER_SET = ('abcdefghijklmnopqrstuvwxyz'
                               'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                               '0123456789')


def random_token_generator(length=30, chars=UNICODE_ASCII_CHARACTER_SET):
    rand = random.SystemRandom()
    return ''.join(rand.choice(chars) for _ in range(length))


def create_access_token():
    return random_token_generator()


def saslprep(string):
    return string if type(string) is str else string.decode()


def ha1(username, realm, password):
    text = ':'.join((username, realm, saslprep(password)))
    return hashlib.md5(bytes(text, encoding='utf-8')).hexdigest()


def hmac(username, realm, password):
    return ha1(username, realm, password)


APPID = config.APPID


def grant_auth_token(uid, name):
    appid = APPID
    token = User.get_user_access_token(rds, appid, uid)

    if not token:
        token = create_access_token()
        User.add_user_count(rds, appid, uid)

    User.save_user_access_token(rds, appid, uid, name, token)

    u = "{}_{}".format(appid, uid)
    realm = "com.beetle.face"
    key = hmac(u, realm, token)

    User.set_turn_key(rds, appid, uid, key)
    User.set_turn_password(rds, appid, uid, token)

    return token


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("auth uid name")
        sys.exit(1)

    uid = int(sys.argv[1])
    name = sys.argv[2] if len(sys.argv) > 2 else ""
    print('token:', grant_auth_token(uid, name).decode())
