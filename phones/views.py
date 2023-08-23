from django.shortcuts import render, redirect, get_object_or_404

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_option = request.GET.get('sort', 'name')  # По умолчанию сортировка по имени
    if sort_option == 'name':
        phones = Phone.objects.order_by('name')
    elif sort_option == 'min_price':
        phones = Phone.objects.order_by('price')
    elif sort_option == 'max_price':
        phones = Phone.objects.order_by('-price')
    else:
        phones = Phone.objects.all()
    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
