# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import base64
from scrapy import log
from lagou.config import _upconfig
path = _upconfig("path_files") + "/"

class LagouPipeline(object):
    def __init__(self):
        self.db = MySQLdb.connect(host="127.0.0.1", user="jss", passwd="123456",
                                  port=3306, db="lagou", charset="utf8"
                                  )
        self.cursor = self.db.cursor()
        log.msg("db connection success !", log.INFO)

    def process_item(self, item, spider):
        try:
            resultId = base64.encodestring("{0}-{1}-{2}".format(item["companyId"],
                                                                item["positionId"],
                                                                item["createTimeSort"]
                                                                ))
            params = (resultId, item["companyId"], item["positionId"], item["createTimeSort"], item["positionName"],
                      item["positionType"], item["createTime"], item["companyShortName"], item["city"], item["companyName"],
                      item["companyLogo"]
                      )
            sql = "insert into result(ResultId, CompanyId, PositionId, CreateTimeSort, PositionName," + \
                "PositionType, CreateTime, CompanyShortName, City, CompanyName, CompanyLogo " + \
                ") values (%s, %d, %d, %d, %s, %s, %s, %s, %s, %s, %s);"
            
            log.msg("++ {0}:{1}".format(resultId, base64.decodestring(resultId)), log.DEBUG)
            self.cursor.execute(sql, params)
        except Exception, error:
            log.msg("insert error : {0}  {1}".format(error, item), log.WARNING)
        #return item
    
    def get_maxtime(self):
        try:
            self.cursor.execute("select Max(createTimeSort) from result;")
            return self.cursor.fetchall()
        except Exception, error:
            log.msg("select error : {0}  {1}".format(error), log.WARNING)
