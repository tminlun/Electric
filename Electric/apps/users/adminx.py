import xadmin
from xadmin import views

from .models import Banner


class BannerAdmin(object):
    list_display = ('title', 'index', 'url', 'image','add_time')
    search_fields = ['title', 'image', 'index','url']
    list_filter = ['title', 'image', 'index', 'url', 'add_time']


xadmin.site.register(Banner, BannerAdmin)



# 配置
# 创建xadmin的最基本管理器配置，并与view绑定
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    #修改左上角的title
    site_title = '后台管理界面'
    #修改footer
    site_footer = '智能电网门户网站'
    #收起菜单
    menu_style = 'accordion'


# 将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView,BaseSetting)
# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView, GlobalSettings)#views.(点)