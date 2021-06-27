import scrapy


class IHOPScraper(scrapy.Spider):
    name = 'ihop_scraper'
    start_urls = ['https://restaurants.ihop.com/']

    def parse(self, response, **kwargs):
        for subdivision in response.css('div.map-list-item').css('a.ga-link'):
            subdivision_page = subdivision.attrib['href']
            subdivision_name = subdivision.root.text
            yield {
                'subdivision': subdivision_name,
                'page': subdivision_page
            }
