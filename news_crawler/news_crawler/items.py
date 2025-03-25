import scrapy

class NewsCrawlerItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    published_date = scrapy.Field()
    