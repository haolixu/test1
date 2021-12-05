from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from django2.settings import PAGE_NUMBER
from order.models import OrderInfo


class OrderList(View):

    def get(self, request, *args, **kwargs):
        try:
            page = request.GET.get('page', 1)
        except:
            page = 1
        order_infos = OrderInfo.objects.all()
        paginator = Paginator(order_infos, PAGE_NUMBER)
        page = paginator.page(page)
        return render(request, 'backweb/order_list.html', {'order_infos': order_infos, 'page': page})
