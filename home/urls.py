from django.contrib.auth.decorators import login_required
from django.urls import path


from home import views

urlpatterns = [
    # 办理后台首页
    path('index/', login_required(views.Index.as_view()), name='index'),
    # 登录
    path('login/', views.Login.as_view(), name='login'),
    # 退出
    path('logout/', login_required(views.Logout.as_view()), name='logout'),
]
