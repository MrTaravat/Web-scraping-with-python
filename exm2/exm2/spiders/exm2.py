import scrapy
class Exm2Spider(scrapy.Spider):
    name = 'exm2'
    start_urls = ['http://quotes.toscrape.com/']
    def parse(self, response):
        print('#'*100)
        for data in response.css('div.quote'):
            yield {'title': data.css('span.text::text').get(),
            'author': data.css('small.author::text').get(),
            'tags': data.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield  response.follow(next_page,callback=self.parse)
        # if next_page:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(url=next_page, callback=self.parse)
            