#!/usr/bin/env python
#-*- coding:utf-8 -*-
#import redis
#r = redis.StrictRedis(host='172.16.34.125', port=6379)
#print r.llen('sdsds')

from pymongo import MongoClient
conn = MongoClient('172.16.34.125', 27017)
db = conn['jiaogf']
vtable = 'vdata_20160507'
content = db[vtable].find()[0]
print content

