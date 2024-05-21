from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy import Request
import time


class RbcSpider(CrawlSpider):
    name = "rbc_crawler"
    allowed_domains = ["rbc.ru"]
    start_urls = ["https://www.rbc.ru/search/?query=ендовицкий"]

    rules = (
        Rule(LinkExtractor(restrict_css='.search-item')),
    )

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, callback=self.parse_with_delay, dont_filter=True)

    def parse_with_delay(self, response):
        for link in LinkExtractor(allow=()).extract_links(response):
            yield Request(link.url)
        time.sleep(5)
