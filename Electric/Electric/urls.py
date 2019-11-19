"""Electric URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
import xadmin
from django.urls import path,include,re_path
from django.conf import settings #上传图片
from django.conf.urls.static import static #上传图片

from users.views import IndexView, LoginView, LogoutView
from company.views import CompanyView, CompanyDetailView


urlpatterns = [
    path('xadmin/', xadmin.site.urls, name="xadmin"),
    path('captcha/',include('captcha.urls')), #验证码
    path('ueditor/', include('DjangoUeditor.urls')),
    path("", IndexView.as_view(), name="index"),  # 首页
    path("company/", CompanyView.as_view(), name="company"),  # 企业列表
    path("company_detail/<int:pk>", CompanyDetailView.as_view(), name="company_detail"),  # 企业详情
    path('login/', LoginView.as_view(), name="login"),  # 登录
    path('logout/',LogoutView.as_view(),name="logout"), #注销

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
