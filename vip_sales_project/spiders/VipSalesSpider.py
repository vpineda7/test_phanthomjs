# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.loader import ItemLoader
from vip_sales_project.items import VipSalesProjectItem
import re
import time

class MySpider(scrapy.Spider):
    name = 'VipSalesSpider'
    allowed_domains = ['cinepolis.com.sv']
    start_urls = [
        'https://cinepolis.com.sv/cartelera/san-salvador-el-salvador/cinepolis-galerias-san-salvador'
    ]

    def parse(self, response):
        
        
        self.log('A response from just arrived!')#%s just arrived!') #% response.body)

        bodystr = response.xpath('//*[@id="carteleraCiudad"]/section[2]/div[5]/div/article[1]/div/header/h3/a/text()').extract()


        print "bodystr = %s" % (bodystr)
        print "len bodystr = %d" % (len(bodystr))
        print "len bodystr = %d" % (len(u''))
        

        for deal in response.xpath('//*[@id="carteleraCiudad"]/section[2]/div[5]/div/article'):    
            print u'película: %s' % deal.xpath('./div/header/h3/a/text()').extract()+' DSFAD'
            











        #-----------------------------  ----------------------------
        # if len(bodystr)==0:
        #     print 'response.body is Noneresponse.body is Noneresponse.body is Noneresponse.body is None'

        #     time.sleep(1)

        #     r = scrapy.Request(response.url, callback=self.parse, dont_filter=True)
        #     yield r
        #     return

        
        # for sel in response.xpath('//div[@class="result"]'):
        #     print "find the key word!"

        #     item = VipSalesProjectItem()

        #     titles = sel.xpath('h3[@class="c-title"]/a')
        #     item['title'] = titles[0].xpath('string(.)').extract()
        #     item['url'] = sel.xpath('h3[@class="c-title"]/a/@href').extract()
        #     dess = sel.xpath('div')
        #     item['des'] = dess[0].xpath('string(.)').extract()

        #     sites = sel.xpath('div/p[@class="c-author"]/text()').extract()
        #     if len(sites) > 0:
        #         print 11
        #     else:
        #         sites = sel.xpath('div/div[last()]/p[@class="c-author"]/text()').extract()

        #     strlist = sites[0].split() 
            
        #     item['site'] = strlist[0]

        #     strlistLen = len(strlist)
        #     if strlistLen==2:
        #         item['time'] = time.strftime('%Y年%m月%d日',time.localtime(time.time()))
        #     elif strlistLen==3:
        #         item['time'] = strlist[1]

        #     yield item

        # #下一页 递归
        # next_url = response.xpath('//p[@id="page"]/a[last()]/@href').extract_first()
        # next_str = response.xpath('//p[@id="page"]/a[last()]/text()').extract_first()

        # print "next_url = %s %s" % (next_url,next_str)

        # pos = next_str.find(u'下一页')
        # if pos!=-1 and len(next_url) > 0:
        #    new_url = "http://news.baidu.com" + next_url

        #    print "[parse]new_url = %s" % (new_url)
           
        #    r = scrapy.Request(new_url, callback=self.parse, dont_filter=True)
        #    yield r


