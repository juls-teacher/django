import logging
import os
from django.db.models import Sum, F
from django.http import HttpResponse
from django.conf import settings
from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render, redirect
from products.forms import AddProductForm
from products.models import Product
from django.core.cache import cache

logger = logging.getLogger(__name__)


def index(request):

    # if int(os.getenv(key='FIRST_PARAM')) :
    #     logger.info(f'second variable  {os.getenv(key="SECOND_PARAM")}')
    # else:
    #     logger.info(f'third variable {os.getenv(key="THIRD_PARAM")}')
    # return HttpResponse("Shop index view")

    # title = request.GET.get("title")
    # purchases__count = request.GET.get("purchases__count")
    #
    # result = cache.get(f"products-view-{title}-{purchases__count}")
    # if result is not None:
    #     return result

    products1 = Product.objects.all()
    # if request.GET.get("title"):
    #     products1 = products1.get(title=request.GET.get("title"))
    #     consumers = products1.purchases.all().distinct("user_id")
    #     return render(request, 'product_info.html', {"products1": products1, "consumers": consumers})

    # if title is not None:
    #     products1 = products1.filter(title__icontains = title)
    #
    # if purchases__count is not None:
    #     products1 = products1.filter(purchases__count=purchases__count)
    #
    # # string = "<br>".join([str(p) for p in products1])
    # # return HttpResponse(string)0


    if request.GET.get("sort") == 'price':
        products1 = products1.order_by('price')
        string = '<br>'.join([f'Product - {data.title}. Price - {data.price}' for data in products1])
        return HttpResponse(f'Sorted by price <br> {string}')
    if request.GET.get("sort") == 'popular':
        products1 = products1.annotate(count_sum = Sum("purchases__count")).order_by('count_sum')
        string = '<br>'.join([f'Product- {data.title}. Sold - {data.count_sum}' for data in products1])
        return HttpResponse(f'popular sale <br> {string}')
    if request.GET.get("sort") == 'purchased_money':
        products1 = products1.annotate(purchased_money=Sum(F('price')*F('purchases__count'))).order_by('-purchased_money')
        string = '<br>'.join([f'Product - {data.title}. Earned - {data.purchased_money}' for data in products1])
        return HttpResponse(f'Products sorted by earned money <br> {string}')

    products = Product.objects.all()
    response = render(request, 'index.html', {"products": products})
    #cache.set(f"products-view-{title}-{purchases__count}", response, 60 * 60)
    return response

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

def add_product(request):
    if request.method == "POST":
        form = AddProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(title=form.cleaned_data["title"],
                                   price=form.cleaned_data["price"],
                                   color=form.cleaned_data["color"],
                                   description=form.cleaned_data["description"])
            return redirect("index")
    else:
        form = AddProductForm()
    return render(request,'add_product.html', {"form": form})