# -*- coding: utf-8 -*-

import scrapy
from  ..items import TutorialItem

class princesmall(scrapy.Spider):
    name = "lezhi"
    allowed_domains = ["lezhi.com"]
    start_urls = [
        "http://www.lezhi.com/Resume/hefei?perpage/10/companyname_type/1/keywords/%CB%E3%B7%A8%B9%A4%B3%CC%CA%A6/degreem/0/page/1=",
    ]

    def parse(self, response):
        allfill = response.css(".right.fll").xpath("label/div[1]/text()").extract()
        item = TutorialItem()
        for a in allfill:
            print a, "---"

        info = response.css(".fl.talents_sort_text").xpath("span/text()").extract()
        item['info'] = info

        for m in info:
            print m, "----"

        name = response.xpath('//a/div/label/div[1]/text()').extract()

        for n in name:
            item['name'] = name
            print n, "----"

        experience = response.xpath('//a/div/div[1]/text()').extract()
        for e in  experience:
            item['company'] = experience
            print e, "----"

        return item