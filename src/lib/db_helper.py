#!/usr/bin/env python
# -*- coding:utf-8 -*-

import records

from util.config import Configuration
from util.logger import api_logger
from util.tools import print_stack


class MySQLHelper:

    def __init__(self, database_url):
        self.logger = api_logger()
        try:
            self.db = records.Database(database_url)
        except Exception, e:
            self.logger.error(e.message)
            raise e

    def query(self, sql):
        rows = self.db.query(sql)
        res = [row.as_dict() for row in rows]
        return res

    def query_one(self, sql):
        rows = self.db.query(sql)
        result = [item for item in rows.all()]
        return result[0] if result else {}

    def un_query(self, sql):
        res = self.db.query(sql)
        return res

def Blog():
    _db = 'blog'
    conf = Configuration().get_section(_db)
    database_url = conf.get('url')
    try:
        return MySQLHelper(database_url)
    except Exception, e:
        print e.message

        print_stack()
        return None

if __name__=='__main__':
    sql = 'select * from user_info'
    res = Blog().query(sql)
    print res
