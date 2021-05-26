import scrapy


class SingledataSpider(scrapy.Spider):
    name = 'singledata'
    allowed_domains = ['www.bhhsamb.com']
    start_urls = ['https://www.bhhsamb.com/agents/51039-didi-pache']

    def parse(self, response):

       Agent_name=response.xpath("(//div/h1)/text()").get()
       job_title=response.xpath("//div[1]/div/div[4]/div/div[1]/div/div/span[1]/text()").get()
       image_url=response.xpath("//img[@class='agent-photo']/@src").get()
       address=response.xpath("(//div/br)/text()").extract()
       contact_details=response.xpath("//span[@class='agent-contact-full-prefix']/text()").extract()
      # contact_details=response.xpath("//a[@class='non-link']/text()").extract()
       social_accounts=response.xpath("//div[@class='agent-social-icons social']/a").get()
       offices=response.xpath("//div[@id='team_offices']/a/text()").get()
       languages=response.xpath("//div[1]/div/div[5]/div/div/div[3]/ul/li/text()").get()
       description=response.xpath("//div[@class='col-sm-24']/p").extract()

       yield {
           'agent_name': Agent_name,
           'job_title':job_title,
           'image_url':image_url,
           'address':address,
          'contact_details':contact_details,
           #'contact_details':contact_details,
           'social_accounts':social_accounts,
           'office':offices,
           'languages':languages,
           'description':description
       }





        # headers = {
        #     'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
        # yield headers




