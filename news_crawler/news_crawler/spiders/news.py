import scrapy

class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["theguardian.com"]
    start_urls = ["https://www.theguardian.com/world"]

    def parse(self, response):
        articles = response.css('li.dcr-39s4cb')
        if not articles:
            self.log("Nenhum artigo encontrado")

        for article in articles:
            title = article.css('h3.card-headline span.show-underline::text').get()
            url = article.css('a::attr(href)').get()
            date = article.css('time::attr(datetime)').get()

            if title and url and date:
                yield {
                    'title': title,
                    'url': response.urljoin(url),
                    'date': date,
                }

        next_page = response.css('a[rel="next"]::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
