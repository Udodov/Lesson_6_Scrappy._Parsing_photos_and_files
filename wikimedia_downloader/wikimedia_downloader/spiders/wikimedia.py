import scrapy
import os

class WikimediaSpider(scrapy.Spider):
    name = "wikimedia"
    start_urls = ["https://commons.wikimedia.org/wiki/Category:Featured_pictures_on_Wikimedia_Commons"]

    def parse(self, response):
        for image_page in response.xpath("//*[@id='mw-category-media']/ul/li/div/a/@href").extract():
            yield scrapy.Request(response.urljoin(image_page), callback=self.parse_image_page)
                    
    def parse_image_page(self, response):
        full_image_url = response.xpath("//*[contains(@class, 'fullImageLink')]/a/@href").extract_first()
        if full_image_url:
            yield scrapy.Request(response.urljoin(full_image_url), callback=self.save_image)
                    
    def save_image(self, response):
        filename = response.url.split("/")[-1]
        if not os.path.exists('image'):
            os.makedirs('image')
        with open(f'image/{filename}', 'wb') as f:
            f.write(response.body)
