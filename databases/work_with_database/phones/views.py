from django.shortcuts import render
from .models import Phone


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort_dict = {
        'name': 'name',
        'cost_from_low': 'price',
        'cost_from_high': '-price'
    }
    sort_key = request.GET.get('sort')

    if sort_key:
        phones = phones.order_by(sort_dict.get(sort_key, 'name'))
    return render(
        request,
        template,
        context={
            'phones': phones
        }
    )


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug).first()
    context = {
        'phone': phone
    }
    return render(request, template, context)
