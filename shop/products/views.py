import logging
import os
from django.http import HttpResponse
from django.conf import settings
from datetime import timedelta
from django.utils import timezone

from products.models import Product

logger = logging.getLogger(__name__)


def index(request):
    # if request.GET.get("param"):
    #     logger.info(f' My custom var= {settings.MY_CUSTOM_VARIABLE}')
    #     logger.info(f' My env var= {settings.MY_ENV_VARIABLE}')
    #     logger.info(f' My param = {request.GET.get("param")}')
    #
    # if int(os.getenv(key='FIRST_PARAM')) :
    #     logger.info(f'second variable  {os.getenv(key="SECOND_PARAM")}')
    # else:
    #     logger.info(f'third variable {os.getenv(key="THIRD_PARAM")}')
    # return HttpResponse("Shop index view")

    products1 = Product.objects.all()
    title = request.GET.get("title")
    if title is not None:
        products1 = products1.filter(title__icontains = title)

    purchases__count= request.GET.get("purchases__count")
    if purchases__count is not None:
        products1 = products1.filter(purchases__count=purchases__count)

    string = "<br>".join([str(p) for p in products1])
    return HttpResponse(string)

def products(request):
    if request.GET.get("product"):
        product = Product.objects.filter(title=f"{request.GET.get('product')}").first()
        return HttpResponse(f"""Title: {product.title},price: {product.price}""")

    get_all_products = Product.objects.all()
    prod_for_view = " "
    for data in get_all_products:
        get_data = f'<br>Product name - {data.title}. Price - {data.price}.'
        prod_for_view += get_data
    return HttpResponse(prod_for_view)


