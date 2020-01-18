from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe


from django.utils.timezone import now

# Create your models here.


class UserProfile(AbstractUser):
    """用户信息表"""

    # role = models.ForeignKey("Role",verbose_name="权限角色")
    role = models.ManyToManyField('Role', "on_delete", blank=True)
    memo = models.TextField('备注', blank=True, null=True, default=None)
    date_joined = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def __str__(self):  # __str__ on Python 2
        return self.username

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = u"用户信息"

class Role(models.Model):
    """角色表"""
    name = models.CharField(max_length=64, unique=True)
    menus = models.ManyToManyField("FirstLayerMenu", "on_delete", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "角色"
        verbose_name_plural = "角色"


class FirstLayerMenu(models.Model):
    '''第一层侧边栏菜单'''
    name = models.CharField('菜单名', max_length=64)
    url_type_choices = ((0, 'related_name'), (1, 'absolute_url'))
    url_type = models.SmallIntegerField(choices=url_type_choices, default=0)
    url_name = models.CharField(max_length=64)
    order = models.SmallIntegerField(default=0, verbose_name='菜单排序')
    sub_menus = models.ManyToManyField('SubMenu', "on_delete", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "第一层菜单"
        verbose_name_plural = "第一层菜单"


class SubMenu(models.Model):
    '''第二层侧边栏菜单'''

    name = models.CharField('二层菜单名', max_length=64)
    url_type_choices = ((0, 'related_name'), (1, 'absolute_url'))
    url_type = models.SmallIntegerField(choices=url_type_choices, default=0)
    url_name = models.CharField(max_length=64)
    order = models.SmallIntegerField(default=0, verbose_name='菜单排序')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "第二层菜单"
        verbose_name_plural = "第二层菜单"


# 产品品牌
class Brand(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name="品牌名称")
    detail = models.CharField(max_length=100,blank=True, null=True, verbose_name="品牌描述")
    isDelete = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "品牌"
        verbose_name_plural = "品牌"

# 产品系列
class Series(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name="系列名称")
    detail = models.CharField(max_length=100,blank=True, null=True, verbose_name="系列描述")
    isDelete = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "系列"
        verbose_name_plural = "系列"

# 目标人群
class Target_audience(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name="目标人群")
    detail = models.CharField(max_length=100,blank=True, null=True, verbose_name="目标人群描述")
    isDelete = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "目标人群"
        verbose_name_plural = "目标人群"

# 使用场景
class Scene(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name="使用场景")
    detail = models.CharField(max_length=100, blank=True, null=True, verbose_name="使用场景描述")
    isDelete = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "使用场景"
        verbose_name_plural = "使用场景"


# 开发人
class Designer(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name="设计人")
    isDelete = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "开发人"
        verbose_name_plural = "开发人"


# 里衬
class Lining(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name="里衬")
    detail = models.CharField(max_length=100, blank=True, null=True,  verbose_name="里衬描述")
    isDelete = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "里衬"
        verbose_name_plural = "里衬"

# 辅料
class Accessories(models.Model):
    Accessories_type_choices = ((0, '育苗袋'), (1, '标签'), (2, '培育土'), (3, '育苗杯'),(4, '其他辅料'))
    Accessories_type = models.SmallIntegerField(choices=Accessories_type_choices, default=0, verbose_name="辅料类型")
    name = models.CharField(max_length=20, unique=True, verbose_name="辅料名称")
    image = models.CharField(max_length=100, blank=True, null=True, verbose_name="图片路径")
    inventory = models.IntegerField(default=0,verbose_name="库存")
    detail = models.CharField(max_length=100, blank=True, null=True,  verbose_name="辅料描述")
    isDelete = models.IntegerField(default=0)

    def __str__(self):
        return '%s~%s'%(self.get_Accessories_type_display(),self.name)
        # return self.name

    class Meta:
        verbose_name = "辅料"
        verbose_name_plural = "辅料"


# 设计阶段
class Periods(models.Model):
    name = models.ForeignKey("Product", "on_delete", blank=True, null=True,verbose_name="产品")
    period_choices = ((0, '阶段一'), (1, '阶段二'), (2, '阶段三'), (3, '阶段四'), (4, '阶段五'))
    period = models.SmallIntegerField(choices=period_choices, default=0, verbose_name="设计阶段")
    date = models.DateField(default=now,verbose_name="创建日期")
    detail = models.TextField(blank=True, null=True, verbose_name="解决方案")
    finish_date = models.DateField(default=now,verbose_name="完结日期")
    isDelete = models.IntegerField(default=0)

    def __str__(self):
        return '%s-%s'%(self.name,self.get_period_display())

    class Meta:
        verbose_name = "设计阶段"
        verbose_name_plural = "设计阶段"

# 产品表
class Product(models.Model):
    productName = models.CharField(max_length=108, verbose_name="产品名称")
    status_choices = ((0, '设计'), (1, '完成'))
    status = models.SmallIntegerField(choices=status_choices, default=0, verbose_name="产品状态")
    title = models.CharField(max_length=512,blank=True, null=True, verbose_name="产品标题")
    sellerSku = models.CharField(max_length=32,blank=True, null=True, verbose_name="SKU名称")
    image = models.CharField(max_length=50,blank=True, null=True, verbose_name="产品图片")
    brand = models.ForeignKey("Brand", "on_delete", blank=True, null=True,verbose_name="品牌")
    series = models.ForeignKey("Series", "on_delete", blank=True, null=True,verbose_name="系列")
    number = models.CharField(max_length=108,blank=True, null=True, verbose_name="数量")
    target_audience = models.ManyToManyField("Target_audience", "on_delete", blank=True, null=True,verbose_name="人群")
    scene = models.ForeignKey("Scene", "on_delete", blank=True, null=True,verbose_name="使用场景")
    weight = models.CharField(max_length=32,blank=True, null=True,  verbose_name="重量")
    offer = models.CharField(max_length=32, blank=True, null=True, verbose_name="报价")
    designer = models.ForeignKey("Designer", "on_delete", blank=True, null=True,verbose_name="设计人")
    accessories = models.ManyToManyField("Accessories", "on_delete", blank=True, null=True,verbose_name="辅料")
    inf_more = models.TextField(blank=True, null=True, verbose_name="其他信息")
    slogan = models.TextField(blank=True, null=True, verbose_name="Slogan")
    features = models.TextField(blank=True, null=True, verbose_name="产品特点")
    a_description = models.TextField(blank=True, null=True, verbose_name="A+描述")
    date_created = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.productName

    class Meta:
        verbose_name = "产品"
        verbose_name_plural = "产品"



