from django.contrib.auth.decorators import login_required
from django.urls import path


from order import views

urlpatterns = [
    # 订单列表页面
    path('order_list/', login_required(views.OrderList.as_view()), name='order_list'),
]
