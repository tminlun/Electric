from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from DjangoUeditor.models import UEditorField

# Create your models here.


class UserProfile(AbstractUser):
    """ 用户扩展 """
    name = models.CharField(max_length=15,null=True,blank=True,verbose_name="姓名")  # 可以用手机号码和密码登录，不用名字
    birthday = models.DateField(null=True,blank=True,verbose_name="生日")
    gender = models.CharField(max_length=6,default='male', choices=(('male','男'), ('female','女')), verbose_name="性别")
    mobile = models.CharField(null=True,blank=True,max_length=11,verbose_name="手机号码")
    email = models.EmailField(max_length=100,null=True,blank=True,verbose_name="邮箱")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.username  # 父类AbstractUser原本的属性


#轮播图
class Banner(models.Model):
    title = models.CharField('标题', max_length=100,null=True,blank=True)
    image = models.ImageField('轮播图', upload_to="banner/%Y%m",null=True,blank=True,max_length=100,default='banner/default.png')
    url = models.URLField('访问地址',max_length=200,null=True,blank=True)#url是图片的路径
    index = models.IntegerField('顺序',default=100)# index控制轮播图的播放顺序
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class About(models.Model):
    telephone = models.CharField(max_length=30, verbose_name="电话",null=True,blank=True)
    address = models.CharField(max_length=100, verbose_name="地址")
    address_code = models.CharField(max_length=100, verbose_name="英文地址",default="")
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '关于公司'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.telephone
