"""django2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from django.views.static import serve
from django2 import settings
from utils.upload_image import upload_image
from migrations import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 管理后台home方法
    path('home/', include(('home.urls', 'home'), namespace='home')),
    # 商品模块
    path('goods/', include(('goods.urls', 'goods'), namespace='goods')),
    # 商品模块
    path('order/', include(('order.urls', 'order'), namespace='order')),
    # kindeditor编辑器上传图片地址
    re_path(r'^util/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),

    # 配置media路径
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]