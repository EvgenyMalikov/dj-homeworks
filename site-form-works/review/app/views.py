from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic.base import View
from django.views.generic.list import ListView

from .models import Product, Review
from .forms import ReviewForm


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'


class ProductView(View):
    template_name = 'app/product_detail.html'
    form_class = ReviewForm

    def get(self, request, pk, *args, **kwargs):
        form = self.form_class
        product = get_object_or_404(Product, id=pk)
        context = {
            'product': product,
        }
        list_review = request.session.get('list_review', [])
        if pk in list_review:
            context['reviews'] = Review.objects.filter(product_id=pk)
            context['is_review_exist'] = True
        else:
            context['form'] = form
            context['is_review_exist'] = False
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            Review.objects.create(
                text=form.cleaned_data.get('text'),
                product_id=pk
            )
            list_review = request.session.get('list_review', [])
            list_review.append(pk)
            request.session['list_review'] = list_review
        return redirect('product_detail', pk=pk)


# def product_list_view(request):
#     template = 'app/product_list.html'
#     products = Product.objects.all()
#
#     context = {
#         'product_list': products,
#     }
#
#     return render(request, template, context)


# def product_view(request, pk):
#     template = 'app/product_detail.html'
#     product = get_object_or_404(Product, id=pk)
#
#     form = ReviewForm
#     if request.method == 'POST':
#         # логика для добавления отзыва
#         pass
#
#     context = {
#         'form': form,
#         'product': product
#     }
#
#     return render(request, template, context)