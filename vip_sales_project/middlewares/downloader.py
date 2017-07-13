# -*- coding: utf-8 -*-
import time
from scrapy.exceptions import IgnoreRequest
from scrapy.http import HtmlResponse, Response
from selenium import webdriver
import selenium.webdriver.support.ui as ui


class CustomDownloader(object):
    def __init__(self):
        
        #PATH = "/Users/tanishindaira/Desktop/spider/ClassifiedSearch/phantomjs-2.1.1-macosx/bin/phantomjs"

        # self.driver = webdriver.PhantomJS(executable_path='/Users/yituwangpeng/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
        self.driver = webdriver.PhantomJS()
        wait = ui.WebDriverWait(self.driver, 10)

    def VisitPersonPage(self, url):
        print('visitperspage function started.....')
        self.driver.get(url)
        time.sleep(1)
        
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        time.sleep(5)
        content = self.driver.page_source.encode('utf-8')
        print('endinf function vistipersonpage.....')
        return content

    def __del__(self):
        self.driver.quit()