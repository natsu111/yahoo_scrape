# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from yahoo_japan.items import YahooJapanItem


class NewsCrawlContentSpider(CrawlSpider):
    name = 'news_crawl_content'
    allowed_domains = ['yahoo.co.jp']
    start_urls = ['http://news.yahoo.co.jp/']

    rules = (
        Rule(
            LinkExtractor(restrict_css='ul.yjnHeader_sub_cat'),
        ),
        Rule(
            LinkExtractor(restrict_css='ul.topicsList_main li'),
        ),
        Rule(
            LinkExtractor(
                restrict_css='div.tpcNews_body > p.tpcNews_detailLink'),
            callback='parse_item'
        ),
    )

    def parse_item(self, response):
        item = YahooJapanItem()
        item['title'] = response.css(
            '#ym_newsarticle > div.hd > h1::text').extract_first()
        item['content'] = response.xpath(
            '//*[@id="ym_newsarticle"]/div[2]/div[1]/p/text()').extract()
        item['category'] = response.css(
            'ul#gnSec li.current a::text').extract_first()
        return item
