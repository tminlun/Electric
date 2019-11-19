from django.shortcuts import render,redirect,reverse
from django.views import View
from django.contrib.auth import authenticate,login,logout

from .models import Banner
from .forms import LoginForm

from company.models import CompanyCategory

# Create your views here.


class IndexView(View):
    def get(self, request):
        banners = Banner.objects.all()
        company_categorys = CompanyCategory.objects.filter(category_rank=1)[:3]

        # 获取语言，英语
        language = request.GET.get("language", "")
        if language == "en":
            return render(request, 'index_en.html', {
                "language": language,
                "banners": banners,
                "company_categorys": company_categorys
            })
        # 中文
        else:
            return render(request,'index.html', {
                "language": language,
                "banners": banners,
                "company_categorys": company_categorys
            })


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()

        language = request.GET.get("language", "")
        if language == "en":
            return render(request, 'login_en.html',{
                "language": language,
                "login_form": login_form,
            })
        else:
            return render(request, 'login.html', {
                "language": language,
                "login_form": login_form,
            })

    def post(self, request):
        language = request.GET.get("language", "")

        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 获取值
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('index'))
            else:
                # 账号密码不匹配
                if language == "en":
                    return render(request, 'login_en.html',{
                        "language": language,
                        'login_form': login_form,
                        'msg': 'Wrong account or password',
                    })
                else:
                    return render(request, 'login.html', {
                        "language": language,
                        'login_form': login_form,
                        'msg': '账号或者密码错误',
                    })

        else:
            # 验证错误
            if language == "en":
                return render(request, 'login_en.html', {
                    "language": language,
                    "login_form": login_form,  # 错误
                })

            else:
                return render(request, 'login.html', {
                    "language": language,
                    "login_form": login_form,  # 错误
                })


class LogoutView(View):
    """注销"""
    def get(self,request):
        logout(request)
        return redirect(request.GET.get('from', reverse('index')))
