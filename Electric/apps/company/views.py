from pure_pagination import Paginator, EmptyPage, PageNotAnInteger #分页
from django.shortcuts import render
from django.views import View

from .models import Company, CompanyCategory
# Create your views here.


# 企业列表
class CompanyView(View):
    def get(self, request):
        categorys = CompanyCategory.objects.all()
        language = request.GET.get("language", "")

        # 分类
        category2_pk = request.GET.get("category2", 1)
        if category2_pk:
            try:
                # 企业
                category = categorys.get(pk=category2_pk)
                companys = Company.objects.filter(category=category)
            except:
                if language == "en":
                    return render(request, 'zx-list_en.html', {
                        "categorys": categorys,
                        "language": language,
                    })

                else:
                    return render(request, 'zx-list.html', {
                        "categorys": categorys,
                        "language": language,

                    })
            # 分页功能
            try:
                page = request.GET.get('page', 1)  # 获取n（page=n）,默认显示第一页
            except PageNotAnInteger:
                page = 1  # 出现异常显示第一页
            p = Paginator(companys, 2, request=request)  # 进行分页，每5个作为一页
            companys = p.page(page)  # 获取当前页面

        # 获取语言，英语
        if language == "en":
            return render(request, 'zx-list_en.html', {
                "categorys": categorys,
                "language": language,
                "companys": companys,
                "category": category,
            })

        else:
            return render(request, 'zx-list.html',{
                "categorys": categorys,
                "language": language,
                "companys": companys,
                "category": category,

            })


# 企业详情
class CompanyDetailView(View):
    def get(self, request, pk):
        language = request.GET.get("language", "")

        # 分类
        try:
            # 详情
            company = Company.objects.get(pk=pk)
        except:
            return render(request, 'zx-detail.html', {
            })
        category = company.category

        # 获取语言，英语
        if language == "en":
            return render(request, 'zx-detail_en.html',{
                "category": category,
                "company": company,
            })
        else:
            return render(request, 'zx-detail.html', {
                "category": category,
                "company": company,
            })


