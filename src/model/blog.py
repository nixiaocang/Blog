#!/usr/bin/env python
# -*- coding:utf-8 -*-

from lib.db_helper import Blog
import json


class BlogModel():

    _table_name = 'blog'

    def __init__(self):
        self.db = Blog()

    def get_one(self, text_id):
        sql = 'select * from blog where text_id="%s" and is_del=0' % text_id
        res = self.db.query_one(sql)
        if res:
            return res.as_dict()
        return res

    def get(self, user_id):
        sql = 'select * from blog where user_id="%s" and is_del=0' % user_id
        res = self.db.query(sql)
        return res

if __name__ =='__main__':
    res = BlogModel().get("jiaogf123")
    print res
