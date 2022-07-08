from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views import View
from django.core.paginator import Paginator
from .models  import Product
from datetime import datetime
class ProductsList(ListView):
    model = Product

    ordering = 'name'

    template_name = 'products.html'

    context_object_name = 'products'

    def get_context_date(self,**kwargs):
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['next_sale'] = None
        return context



class ProductDetail(DetailView):
    model = Product

    template_name = 'product.html'

    context_object_name = 'product'


class Products(View):

    def get(self, request):
        products = Product.objects.order_by('-price')
        p = Paginator(products,
                      1)  # создаём объект класса пагинатор, передаём ему список наших товаров и их количество для одной страницы

        products = p.get_page(request.GET.get('page',
                                              1))  # берём номер страницы из get-запроса. Если ничего не передали, будем показывать первую страницу.
        # теперь вместо всех объектов в списке товаров хранится только нужная нам страница с товарами

        data = {
            'products': products,
        }
        return render(request, 'product_list.html', data)
