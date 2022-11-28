from django.shortcuts import render, redirect

from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort_by = request.GET.get('sort')
    if sort_by == None:
        context = {'phones': phones}
    else: 
        if sort_by == 'name':
            phones = phones.order_by('name')
        elif sort_by == 'min_price':
            phones = phones.order_by('price')
        elif sort_by == 'max_price':
            phones = phones.order_by('price').reverse()
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)