import scrapy
from unsplash_scraper.items import UnsplashImage

class UnsplashSpider(scrapy.Spider):
    # Название паука
    name = 'unsplash_spider'
    # Ограничиваем домены, которые может посещать паук
    allowed_domains = ['unsplash.com']
    # Начальная страница для сканирования
    start_urls = ['https://unsplash.com/s/photos/nature']

    def parse(self, response):
        """
        Основной метод для обработки ответа страницы.
        Извлекает ссылки на страницы фотографий и ссылки на следующую страницу.
        """
        # Извлекаем ссылки на страницы фотографий
        photo_links = response.css('a[href*="/photos/"]::attr(href)').getall()
        for link in photo_links:
            # Переходим по каждой ссылке и вызываем метод parse_photo для обработки
            yield response.follow(link, self.parse_photo)

        # Переходим на следующую страницу
        next_page = response.css('a[rel="next"]::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_photo(self, response):
        """
        Метод для обработки страницы фотографии.
        Извлекает URL изображения, заголовок и категорию.
        """
        item = UnsplashImage()
        
        # Извлекаем URL изображения из мета-тега
        item['image_urls'] = [response.css('meta[property="og:image"]::attr(content)').get()]
        
        # Извлекаем заголовок из мета-тега
        item['title'] = response.css('meta[property="og:title"]::attr(content)').get()
        
        # Здесь можно добавить логику для определения категории
        item['category'] = 'nature'
        
        yield item
