import scrapy
from ..items import BsaaItem


class ProjSpider(scrapy.Spider):
    name = 'proj'
    allowed_domains = ['www.bhhsamb.com']
    start_urls = ['https://www.bhhsamb.com/agents']
    page_num = 2

    def parse(self, response):
        items = BsaaItem()
        Agent_name = response.css('.agent-name a::text').extract()
        items['Agent_name'] = Agent_name
        yield items
        # headers = {
        #     'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
        # yield headers

        next_page = 'https://www.bhhsamb.com/agents?page=' + str(ProjSpider.page_num) + ''
        if ProjSpider.page_num <= 42:
            ProjSpider.page_num += 1

            yield response.follow(next_page, callback=self.parse)
