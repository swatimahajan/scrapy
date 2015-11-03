import scrapy
#from scrapy.spider import BaseSpider
#from ..items import GiftItem
#from ..items import *	
from scrapy.selector import HtmlXPathSelector
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir) 
from tutorial.items import GiftItem
#from .. import items
import items
class GiftSpider(scrapy.Spider):
    name = "gifts"
    allowed_domains = ["gifts.com"]
    start_urls = [
            "https://www.gifts.com/birthday/man/NwxRkV?navContent=T%3aBirthday%3a%26nbsp%3b%26nbsp%3bMen&navLocation=T%3a1-5%3a2-13&productgroup=glpfbir"]
    def parse(self, response):
    	hxs = HtmlXPathSelector(response)
    	titles = hxs.xpath("//a")
    	items = []
    	for i in titles:
    		item = GiftItem()
    		item['title'] = i.xpath("img").extract()
    		item['link'] = i.xpath("@href").extract()
    		items.append(item)
    	return items
#	 	with open('outputfile','wb') as f:
#	 		print "hello"
#	 		for i in response.xpath("//img"):
#	 			print "message"
#	 			f.write(str(i))
#	 			print "\n"
#
#		print "hiiii"
#def parse(self, response):
	#filename = response.url.split("/")[-2] + '.html'
	#with open(filename, 'wb') as f:
		#f.write(response.body)'''
def parse(self, response):
    with open('newfile','wb') as f:
        x = response.xpath("//a/img").extract()
        for i in x:
            y = i.encode("utf8")
        			#f.write(str(i)
            f.write(y.split()[1][9:-8])
            print "\n"

#print "hiiii"
            	
	    
