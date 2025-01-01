import scrapy
from ..items import EntertainmentcrawlerItem

# class EntertainmentSpider(scrapy.Spider):
#     name = "entertainment"
#     start_urls = [
#         'https://variety.com/'
#     ]
#
#     def parse(self, response):
#         # Loop through the list of articles found in the response
#         for article in response.xpath("//div[@class='l-river__content']/ul/li/article"):
#             item = EntertainmentcrawlerItem()
#
#             # Extracting data with error handling
#             title = article.xpath("header/h3/a/text()").get()
#             link = article.xpath("figure/a/@href").get()
#             img = article.xpath("figure/a/img/@data-src").get()
#
#             # Handle cases where any of the required fields are missing
#             if title and link and img:
#                 item['title'] = title
#                 item['image'] = img
#                 item['url'] = link
#                 item['source'] = 'Variety'
#                 yield item

class EntertainmentSpider(scrapy.Spider):
    name = "entertainment_in"
    start_urls = [
        'https://indianexpress.com/section/entertainment/'
    ]

    def parse(self, response):
        # Loop through the articles found in the response
        for article in response.xpath("//div[@class='nation']/div[@class='articles']"):
            item = EntertainmentcrawlerItem()

            # Extracting data with error handling
            title = article.xpath(".//div[@class='title']/a/text()").get()
            link = article.xpath(".//div[@class='snaps']/a/@href").get()

            # Handling image extraction and error handling
            s = article.xpath(".//div[@class='snaps']/a/noscript").get()
            if s:
                img = s.split('"')[5]  # Make sure to validate the index in the split
            else:
                img = None

            if title and link and img:
                item['title'] = title
                item['image'] = img
                item['url'] = link
                item['source'] = 'Indian Express'
                yield item
