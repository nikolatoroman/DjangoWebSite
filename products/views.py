from django.shortcuts import render, get_object_or_404
from .models import Product


def home(request):
    products = Product.objects.filter(is_available=True)[:8]

    return render(request, 'index.html', {
        'products': products
    })

def games(request):

    products = Product.objects.filter(is_available=True)

    query = request.GET.get('q')
    platform = request.GET.get('platform')
    sort = request.GET.get('sort')

    if query:
        products = products.filter(title__icontains=query)

    if platform:
        products = products.filter(platform=platform)

    if sort == 'newest':
        products = products.order_by('-release_date')

    elif sort == 'price_asc':
        products = products.order_by('price')

    elif sort == 'price_desc':
        products = products.order_by('-price')

    elif sort == 'name':
        products = products.order_by('title')

    return render(request, 'games.html', {
        'products': products,
        'query': query,
        'selected_platform': platform,
        'selected_sort': sort,
    })


def psplus(request):
    return render(request, 'psplus.html')

def contact(request):
    return render(request, 'contact.html')

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_available=True)

    return render(request, 'product_detail.html', {
        'product': product
    })