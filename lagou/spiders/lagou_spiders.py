# coding=utf8
from scrapy import log
from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import Request, FormRequest
import json
import time

from lagou.items import LagouItem
from lagou.config import _config_time, _upconfig
path = _upconfig("path_files") + "/"

class LagouSpider(CrawlSpider):
    name = "lagou"
    log.start(logfile=_upconfig("path_log") + "/log.txt")

    def start_requests(self, page_num=1):
        return [Request("http://www.lagou.com/jobs/positionAjax.json?px=new",
                        body="first=true&kd=&pn={0}".format(page_num),
                        meta={"first": True, "kd": "", "pn": page_num},
                        method="POST",
                        headers={"Content-Type": "application/x-www-form-urlencoded"},
                        callback=self.parse
                        )]

    def parse(self, response):
        # 得到当前页数、响应结果
        page_num = response.meta["pn"]
        content = response.body

        try:
            sites = json.loads(content)
            results = sites["content"]["result"]
        except Exception, error:
            log.msg("JSON : {0}<#>{1}<#>{2}<#>{3}".format(time.time(), page_num, error, content), level=log.CRITICAL)
            return
        
        # 解析结果 保存到LagouItem 异步存储
        min_timesort = None
        for res in results:
            try:
                item = LagouItem()
                for key, value in res.items():
                    # 比较当页最小时间
                    if (key == "createTimeSort") and (value < min_timesort or min_timesort is None):
                        min_timesort = value
                    try:
                        item[key] = value
                    except:
                        pass
                yield item
            except Exception, error:
                log.msg("ITEM : {0}<#>{1}<#>{2}".format(time.time(), res, error), level=log.ERROR)
        
        # 单独封装的比较两个时间戳的方法 若1>2 则返回True 反之False
        def compare_time(timea, timeb):
            print "timea's {0} ! timeb's {1}".format(type(timea), type(timeb))
            if len(str(timea)) > len(str(timeb)):   timea = int(str(timea)[:len(str(timeb))])
            else:   timeb = int(str(timeb)[:len(str(timea))])
            if timea > timeb:   return True
            else:   return False
        
        log.msg("** num:{0},  min:{1}".format(page_num, min_timesort), level=log.INFO)
        
        # 指定爬取的时间(库中最晚数据时间) 晚于 已经爬取的时间 则停止爬取
        if compare_time(_config_time("crawl_min_time"), min_timesort) or \
            compare_time(_config_time("db_max_time"), min_timesort):
            log.msg("####### False", level=log.DEBUG)
#         elif page_num > 200:
#             log.msg("####### False", level=log.DEBUG)
        else:
            log.msg("####### True", level=log.DEBUG)
            yield Request("http://www.lagou.com/jobs/positionAjax.json?px=new",
                          body="first=false&kd=&pn={0}".format(page_num + 1),
                          meta={"first": False, "kd": "", "pn": page_num + 1,},
                          method="POST",
                          headers={"Content-Type": "application/x-www-form-urlencoded"},
                          callback=self.parse
                          )
