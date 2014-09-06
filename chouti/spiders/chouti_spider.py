import re
import json



from scrapy.selector import Selector

try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider

from scrapy.selector import HtmlXPathSelector
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc  
from scrapy.contrib.spiders import CrawlSpider, Rule  
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle 
from chouti.items import *  


class ChoutiSpider(CrawlSpider):
    name = "chouti"

    allowed_domains = ["chouti.com"]

    start_urls = []

    for i in range(1,100):
        start_urls.append("http://dig.chouti.com/all/hot/recent/%d" % i)
        print start_urls[i-1]

    def parse(self, response):
        items = []
        sel = Selector(response)
        #hxs = HtmlXPathSelector(response)
        #hxs.select('//div[@class="news-content"]//a[1]//text()')
       
        news = sel.xpath('//div[@class="news-content"]//a[1]')

        for new in news:
            item = ChoutiItem();
            title = new.xpath(".//text()").extract()[0];
            item['title'] = title.replace("\r\n","").strip().encode('utf-8')
            if not item['title']:
                continue
            url = new.xpath(".//@href").extract()[0];
            item['url'] = url.encode('utf-8')
            print item['title']
            print item['url']
            items.append(item)
        return items

    def _process_request(self, request):
        info('process ' + str(request))
        return request
