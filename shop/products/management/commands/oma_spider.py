import requests
from django.core.management.base import BaseCommand
from products.models import Product
from products.spider import OmaSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.signalmanager import dispatcher
from scrapy import signals
from shop import settings
from django_rq import job


@job
def run_spider():
    Product.objects.all().delete()

    def crawler_results(signal, sender, item, response, spider):
        image_name = item["image_name"].split("/")[-1]
        response = requests.get(item["image_name"])
        open(settings.MEDIA_ROOT / "products" / image_name, "wb").write(
            response.content
        )
        Product.objects.update_or_create(
            external_id=item["external_id"],
            defaults={
                "title": item["name"],
                "price": item["price"],
                "image": f"products/{image_name}",
                "excerpt": item["category"],
                "description": item["link"],
            },
        )

    dispatcher.connect(crawler_results, signal=signals.item_scraped)

    scrapy_settings = get_project_settings()
    scrapy_settings[
        "USER_AGENT"
    ] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0"

    process = CrawlerProcess(get_project_settings())
    process.crawl(OmaSpider)
    process.start()


class Command(BaseCommand):
    help = "Crawl OMA catalog"

    def handle(self, *args, **options):
        run_spider()
