#!/usr/bin/env python
# -*- coding:utf-8 -*-

from lib.db_helper import Blog
import json
from util.tools import uniq_id


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

    def insert(self, bag):
        text_id = uniq_id('text')
        title = bag.get('title')
        description = bag.get('description')
        content = bag.get('content')
        content = json.dumps(content, encoding="UTF-8", ensure_ascii=False)
        sql = 'INSERT INTO `blog` (`user_id`, `text_id`, `title`, `description`, `content`, `is_del`) VALUES ("jiaogf", "%s", "%s", "%s", %s, 0)' % (text_id, title, description, content)
        self.db.un_query(sql)

    def delete(self, text_id):
        sql = 'update blog set is_del=1 where text_id="%s"' % text_id
        self.db.un_query(sql)

if __name__ =='__main__':
    res = BlogModel().get_one('text_a062069282b6436ea7bf0371115969e6')
    print res
