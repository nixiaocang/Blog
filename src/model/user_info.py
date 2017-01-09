#!/usr/bin/env python
# -*- coding:utf-8 -*-

from lib.db_helper import Blog
import json


class UserInfo():

    _table_name = 'user_info'

    def __init__(self):
        self.db = Blog()

    def get_one(self, user_id):
        sql = 'select * from user_info where user_id="%s" and is_del=0' % user_id
        res = self.db.query_one(sql)
        if res:
            return res.as_dict()
        return res

if __name__ =='__main__':
    res = UserInfo().get_one("jiaogf1234")
    print res
