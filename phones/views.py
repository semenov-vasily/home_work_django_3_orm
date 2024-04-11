from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from phones.models import Phone


def home(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    all_phones = Phone.objects.all()
    if sort == 'name':
        all_phones = Phone.objects.order_by('name')
    elif sort == 'min_price':
        all_phones = Phone.objects.order_by('price')
    elif sort == 'max_price':
        all_phones = Phone.objects.order_by('-price')
    all_phones_list = [{
            'name': phone.name,
            'price': phone.price,
            'image': phone.image,
            'release_date': phone.release_date,
            'lte_exists': phone.lte_exists,
            'slug': phone.slug,
        } for phone in all_phones]
    data = {
        'phones': all_phones_list
    }
    return render(request, template, context=data)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    phone_data = {
        'name': phone.name,
        'price': phone.price,
        'image': phone.image,
        'release_date': phone.release_date,
        'lte_exists': phone.lte_exists,
        'slug': phone.slug,
    }
    data = {
        'phone': phone_data
    }
    return render(request, template, context=data)
