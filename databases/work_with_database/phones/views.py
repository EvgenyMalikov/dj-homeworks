from django.shortcuts import render
from .models import Phone


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    if request.GET.get('sort') == 'min_price':
        return render(request, template, {'phones': phones.order_by('price')})
    if request.GET.get('sort') == 'name':
        return render(request, template, {'phones': phones.order_by('name')})
    if request.GET.get('sort') == 'max_price':
        return render(request, template, {'phones': phones.order_by('-price')})
    return render(request, template, {'phones': phones})


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug).first()
    context = {'phone': phone}
    return render(request, template, context)
