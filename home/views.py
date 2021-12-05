from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from django.views import View

from home.forms import UserLoginForm


class Index(View):
    def get(self, request, *args, **kwargs):
        # 判断如果是get请求，则返回管理后台首页
        return render(request, 'backweb/index.html')


class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'backweb/login.html')

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            # 使用auth，验证用户名和密码是否正确
            user = auth.authenticate(request,
                                     username=request.POST.get('username'),
                                     password=request.POST.get('password'))
            if user:
                # 如果验证用户成功，则获取到user对象，并使用Djnaog自带的auth的login方法实现登录
                auth.login(request, user)
                return redirect('home:index')
            else:
                return redirect('home:login')
        else:
            return render(request, 'backweb/login.html', {'form': form})


class Logout(View):
    def get(self, request, *args, **kwargs):
        # 使用django自带的auth的logout方法，实现退出操作
        auth.logout(request)
        return redirect('home:login')
