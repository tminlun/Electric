# _*_ encoding:utf-8 _*_
__date__: '2019/11/7 0007 20:15'

import xadmin

from .models import CompanyCategory,Company,CompanyForum,CompanyImage


class CompanyCategoryAdmin(object):
    list_display = ('name', 'name_code', 'category_rank', 'category_type','parent_category', 'add_time')


class CompanyForumAdmin(object):
    list_display = ('category', 'title', 'title_code','author','author_code',
                    'author_unit','author_unit_code','add_time')


class CompanyAdmin(object):
    list_display = ('category', 'name', 'name_code',
                    'desc', 'desc_code', 'company_front_image', 'add_time')


class CompanyImageAdmin(object):
    list_display = ('category', 'image', 'add_time')


xadmin.site.register(CompanyCategory, CompanyCategoryAdmin)
xadmin.site.register(CompanyForum, CompanyForumAdmin)
xadmin.site.register(Company, CompanyAdmin)
xadmin.site.register(CompanyImage, CompanyImageAdmin)
