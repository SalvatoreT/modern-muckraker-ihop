import scrapy


class IHOPScraper(scrapy.Spider):
    name = 'ihop_scraper'
    start_urls = ['https://restaurants.ihop.com/']
    allowed_domains = ['restaurants.ihop.com']

    def parse(self, response, **kwargs):
        yield from response.follow_all(css='div.map-list-item a.ga-link', callback=self.parse_subdivision)

    def parse_subdivision(self, response):
        yield from response.follow_all(css='div.map-list-item a.ga-link', callback=self.parse_city)

    def parse_city(self, response):
        yield from response.follow_all(css='div.map-list-item a.ga-link', callback=self.parse_store)

    @staticmethod
    def parse_store(response):
        hours = list(map(lambda row: {
            'day': row.xpath(".//span/@data-daypart").get(),
            'open': row.css("span.time-open::text").get(),
            'close': row.css("span.time-close::text").get()
        }, list(response.css('div.hide-mobile div.day-hour-row'))))
        subdivision_abbr, subdivision = response.xpath('//meta[@name="state"]/@content').get().split(", ")
        yield {
            'store_id': response.css('div.js-favorite a.ga-link').xpath('@data-fid').get(),
            'subdivision': subdivision,
            'subdivision_abbr': subdivision_abbr,
            'city': response.xpath('//meta[@name="city"]/@content').get(),
            'zip': response.xpath('//meta[@name="zip"]/@content').get(),
            'address': response.xpath('//meta[@name="address"]/@content').get(),
            'url': response.url,
            'hours': hours
        }
