# -*- coding: utf-8 -*-
import scrapy
from douyu.items import DouyuItem


class DouyuyzSpider(scrapy.Spider):
	name = 'douyuyz'
	allowed_domains = ['douyu.com']
	start_urls = ["https://www.douyu.com/g_yz"]

	def parse(self, response):
		for each in response.xpath("//div[@class='DyListCover HeaderCell is-href']/a"):
			item = DouyuItem()
			item['image_link']= each.xpath("./div/div/img/@src").extract()[0]
			item['nick_name']= each.xpath("./div/div/h2/text()").extract()[0]
			item['fans_num']= each.xpath("./div/div/span[@class ='DyListCover-hot']/text()").extract()[0]
			yield item

	#	item = DouyuItem()
	#	for each in response.xpath("//div[@class= 'box-bd']/ul/li"):
	#		item['image_link']= each.xpath("./a/img/@data-original").extract()[0]
	#		item['nick_name']= each.xpath("./span/span/i/text()").extract()[0]
	#		print(item)
	#		yield item
