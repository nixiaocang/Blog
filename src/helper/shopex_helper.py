#!/usr/bin/env python
# -*- coding:utf-8 -*-

import uuid
import requests
import json
from model.gabrin import Gabrin
from model.leviathan import Leviathan
from util.config import Configuration

OVERLORD_URL = Configuration().get('service', 'OVERLORD_URL')


class Shopex:
    def __init__(self, kwargs):
        self.kwargs = {}
        self.domain = kwargs.get('domain')
        self.contact = kwargs.get('contact', 'admin')
        self.username = kwargs.get('username', 'admin')
        self.password = kwargs.get('username', 'admin')
        self.shopex_id = kwargs.get('shopex_id', '131109009276')
        self.kwargs['domain'] = self.domain
        self.kwargs['contact'] = self.contact
        self.kwargs['username'] = self.username
        self.kwargs['password'] = self.password

    def gen_account(self):
        res = requests.post(OVERLORD_URL, data=self.kwargs)
        res = json.loads(res.content)
        status = res.get('status')
        bag = {'status': int(status)}
        if status == '0':
            result = res.get('result')
            enterprise_id = result.get('enterprise_id')
            user_id = result.get('root_user_id')
            self.modify_db_log(enterprise_id, user_id)
            bag['domain'] = self.domain
            bag['username'] = self.username
            bag['password'] = self.password
            bag['ent_id'] = enterprise_id
            bag['user_id'] = user_id

        else:
            print "生成商派账号出错:%s" % res.get('errstr')
            bag['errstr'] = res.get('errstr')
        return bag

    def modify_db_log(self, enterprise_id, user_id):
        Leviathan().update_ent_type(enterprise_id)
        Gabrin().modify_shopex(user_id, self.shopex_id)


if __name__ == '__main__':
    print '请输入domain, 如果不输入,将会随机生成'
    domain = raw_input("domain: ")
    if domain == '':
        domain = str(uuid.uuid1())[:4]
    print '请输入用户名, 如果不输入, 默认为admin'
    username = raw_input("username: ")
    if username == '':
        username = 'admin'
    print '请输入密码, 如果不输入, 默认为admin'
    password = raw_input("password: ")
    if password == '':
        password = 'admin'

    kwargs = {
        "domain": domain,
        "username": username,
        "contact": "admin",
        "password": password,
    }
    Shopex(kwargs).gen_account()
