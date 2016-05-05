# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class LagouItem(scrapy.Item):
    companyId = scrapy.Field()
    positionId = scrapy.Field()
    createTimeSort = scrapy.Field()

    positionName = scrapy.Field()
    positionType = scrapy.Field()
    createTime = scrapy.Field()
    companyShortName = scrapy.Field()
    city = scrapy.Field()
    companyName = scrapy.Field()
    companyLogo = scrapy.Field()

    # workYear = scrapy.Field()
    # education = scrapy.Field()
    # jobNature = scrapy.Field()
    # positionFirstType = scrapy.Field()
    # salary = scrapy.Field()
    # positionAdvantage = scrapy.Field()
    # industryField = scrapy.Field()
    # financeStage = scrapy.Field()
    # companyLabelList = scrapy.Field()
    # leaderName = scrapy.Field()
    # companySize = scrapy.Field()
    # deliverCount = scrapy.Field()
    # score = scrapy.Field()
    # adjustScore = scrapy.Field()
    # relScore = scrapy.Field()
    # formatCreateTime = scrapy.Field()
    # randomScore = scrapy.Field()
    # countAdjusted = scrapy.Field()
    # calcScore = scrapy.Field()
    # orderBy = scrapy.Field()
    # showOrder = scrapy.Field()
    # haveDeliver = scrapy.Field()
    # adWord = scrapy.Field()
    # positonTypesMap = scrapy.Field()
    # hrScore = scrapy.Field()
    # flowScore = scrapy.Field()
    # showCount = scrapy.Field()
    # pvScore = scrapy.Field()
    # plus = scrapy.Field()
    # imstate = scrapy.Field()
    # totalCount = scrapy.Field()
    # searchScore = scrapy.Field()