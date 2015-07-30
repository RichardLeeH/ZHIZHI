# -*- coding: utf-8 -*-
# encoding: utf-8
from types import NoneType

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import os 
import time
import glob
import shutil
import pymongo
from pymongo import Connection

class DBConn:
    conn = None
    servers = "mongodb://localhost:27017"

    def connect(self):
        self.conn = pymongo.Connection(host='127.0.0.1',port=27017)

    def close(self):
        return self.conn.disconnect()

    def getConn(self):
        return self.conn
    
if __name__ == "__main__":
    
    BASE_USR = "http://zhidao.baidu.com/question/%s.html"
    "http://zhidao.baidu.com/question/%s.html" % s for s in range(353477925, 393070082)
    
    con = Connection("mongodb://localhost:27017")
    db = con.zhidao #连接zhidao数据库
    orgin = db.QuestionItem #连接test中的post集合，相当于MySQL中的表
    posts = orgin.find()
    count = posts.count()
    print ("共有数据：" + str(count))
    desZhidao = db.ZDQuestionItem
    for post in posts:
        print post
        desZhidao.insert(post)
    
