# coding=utf8
from lagou.config import _update_dbmaxtime, _upconfig
import os

if not os.path.exists(_upconfig("path_log")):
    os.mkdir(_upconfig("path_log"))
if not os.path.exists(_upconfig("path_files")):
    os.mkdir(_upconfig("path_files"))

# 指定要往前爬取到几点
_upconfig("MsutParam", "crawl_min_time", "2016/5/4 08:00:00")
_update_dbmaxtime()

os.system("scrapy crawl lagou")