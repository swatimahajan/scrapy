import scrapy
from scrapy.spider import BaseSpider
from tutorial.items import GiftItem

class GiftSpider(BaseSpider):
    name = "gifts"
    allowed_domains = ["gifts.com"]
    start_urls = [
            "https://www.gifts.com/birthday/man/NwxRkV?navContent=T%3aBirthday%3a%26nbsp%3b%26nbsp%3bMen&navLocation=T%3a1-5%3a2-13&productgroup=glpfbir",
        ]
def parse(self, response):
	filename = response.url.split("/")[-2] + '.html'
	with open(filename, 'wb') as f:
		f.write(response.body)


 	with open('scrapedoutput','wb') as f:
 		for i in response.xpath("//img"):
 			f.write(i.encode('utf8'))
 			print "\n"


            	#filename1 = "scrapdata"
		#with open('scrapdata','wb') as fo:
		#	fo.write(response.xpath("//img").extract())
		#for sel in response.xpath('//a'):
		#	link = sel.xpath('img').extract()
		#	print link'''
		#fo = open("foo", "wb")
		#fo.write( "Python is a great language.\nYeah its great!!\n");

		# Close opend file
		#fo.close()
	 #def parse(self, response):
	    