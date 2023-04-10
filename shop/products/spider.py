import scrapy


class OmaSpider(scrapy.Spider):
    name = "oma.by"
    allowed_domains = ["https://www.oma.by"]
    start_urls = ["https://www.oma.by/elektroinstrument-c?"]
    page_count = 69
    def parse(self, response, **kwargs):
        for product in response.css(".catalog-grid .product-item"):
            data = {
                "external_id": int(product.attrib.get("data-ga-product-id")),
                "name": product.attrib.get("data-ga-product-name").strip(),
                "price": product.attrib.get("data-ga-product-price").strip(),
                "category": product.attrib.get("data-ga-category-last").strip(),
                "link": f"{self.allowed_domains[0]}{product.css('a.area-link::attr(href)').get()}",
            }

            # main_img_url = response.urljoin(response.xpath('//div[@class="pictureSlider"]//a/img/@src').get())
            # data['image_urls'] = [main_img_url, ]


            yield data



        next_page = response.css(".page-nav_box .btn__nav-right::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
