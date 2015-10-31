import scrapy
#from scrapy.spider import BaseSpider
#from ..items import GiftItem
#from ..items import *	
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir) 
import items
#from .. import items
class GiftSpider(scrapy.Spider):
    name = "gifts"
    allowed_domains = ["gifts.com"]
    start_urls = [
            "https://www.gifts.com/birthday/man/NwxRkV?navContent=T%3aBirthday%3a%26nbsp%3b%26nbsp%3bMen&navLocation=T%3a1-5%3a2-13&productgroup=glpfbir",
            "http://www.gifts.com/birthday/woman/NwxyuP?navContent=T%3aBirthday%3a%26nbsp%3b%26nbsp%3bWomen&navLocation=T%3a1-5%3a3-13&productgroup=glpfbir",
            "https://www.gifts.com/birthday/child/NwxhwX?navContent=T%3aBirthday%3a%26nbsp%3b%26nbsp%3bKids&navLocation=T%3a1-5%3a4-13&productgroup=gbirhnr"
        ]
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
            	
	    