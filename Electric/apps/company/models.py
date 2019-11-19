from datetime import datetime
from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.


class CompanyCategory(models.Model):

    CATEGORY_RANK = (
        (1, "一级类别"),
        (2, "二级类别"),
    )

    CATEGORY_TYPE = (
        ("general", "概况"),
        ("consult", "企业咨询"),
        ("science", "企业科技"),
        ("product", "企业产品"),
        ("relation", "企业联系"),
        ("forum", "企业论坛"),
    )

    name = models.CharField(max_length=30,verbose_name="名称")
    name_code = models.CharField(default="",max_length=30,verbose_name="英文名")
    category_rank = models.IntegerField(choices=CATEGORY_RANK,default=1,verbose_name="类别级别")
    category_type = models.CharField("支付类型", choices=CATEGORY_TYPE, default="general", max_length=25)
    # 一个父级分类对应多个子分类
    parent_category = models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE,verbose_name="当前类别的父级", related_name="sub_cat")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间",help_text="添加时间")

    class Meta:
        verbose_name = "企业类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CompanyForum(models.Model):
    '''一个类别有多个论坛'''
    category = models.ForeignKey(CompanyCategory,on_delete=models.CASCADE,null=True,blank=True,verbose_name="类别", related_name='forums')
    title = models.CharField(max_length=66, verbose_name="论坛题目", null=True,blank=True)
    title_code = models.CharField(max_length=66, verbose_name="论坛题目英文", null=True, blank=True)
    author = models.CharField(max_length=66, verbose_name="作者姓名", null=True,blank=True)
    author_code = models.CharField(max_length=66, verbose_name="作者姓名英文", null=True, blank=True)
    author_unit = models.CharField(max_length=66, verbose_name="作者单位", null=True,blank=True)
    author_unit_code = models.CharField(max_length=66, verbose_name="作者单位英文", null=True, blank=True)
    add_time = models.DateTimeField("发表时间", default=datetime.now)

    class Meta:
        verbose_name = "论坛"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Company(models.Model):
    category = models.ForeignKey(CompanyCategory,on_delete=models.CASCADE,null=True,blank=True,verbose_name="类别", related_name='company')

    name = models.CharField( max_length=100, verbose_name="名称", null=True,blank=True)
    name_code = models.CharField(max_length=30,verbose_name="英文名", null=True,blank=True)

    brief = models.TextField("简短描述", max_length=300,default="")
    brief_code = models.TextField("简短英文描述", max_length=300,default="")

    desc = UEditorField(verbose_name=u"内容", imagePath="company/images/", width=1000, height=300,
                                  filePath="company/files/", default='')
    desc_code = UEditorField(verbose_name=u"英文内容", imagePath="company/images/", width=1000, height=300,
                        filePath="company/files/", default='')

    # 封面图
    company_front_image = models.ImageField(upload_to="company/images/", null=True, blank=True, verbose_name="封面图")
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = "企业"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CompanyImage(models.Model):
    """
    一个企业有多个照片
    """
    # related_name：通过related_name把所有对应图片传递给goods
    category = models.ForeignKey(CompanyCategory,on_delete=models.CASCADE,related_name="category_image",verbose_name="企业类别",default="")
    image = models.ImageField(upload_to="company/images/",max_length=200,null=True,blank=True,verbose_name="图片")
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = '企业类别图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.category.name
