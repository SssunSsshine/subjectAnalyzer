from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy import Request
import time


class RbcSpider(CrawlSpider):
    name = "sudact_crawler"
    allowed_domains = ["sudact.ru"]
    start_urls = ["https://sudact.ru/regular/doc/?regular-txt=гусев&regular-case_doc=&regular-lawchunkinfo=&regular"
                  "-date_from=&regular-date_to=&regular-workflow_stage=&regular-area=&regular-court=&regular-judge"
                  "=#searchResult"]

    rules = (
        Rule(LinkExtractor(allow="regular/doc")),
    )

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, callback=self.parse_with_delay, dont_filter=True)

    def parse_with_delay(self, response):
        for link in LinkExtractor(allow=()).extract_links(response):
            yield Request(link.url)
        time.sleep(5)
