from django.http import HttpRequest, JsonResponse
from django.shortcuts import render

from apps.core.utils import create_context
from apps.market.models import Category as ProductCategory, Product


def base(request: HttpRequest):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()

    return render(
        request,
        'site/market/base.html',
        create_context('market', data={
            "categories": categories,
            "products": products
        })
    )
