# _*_coding:utf-8_*_
__author__ = 'LCG'

from ymx01 import models
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def load_product_detail(column_name,obj):
    '''用于显示product详情页中的信息'''
    label_name = models.Product._meta.get_field(column_name).verbose_name
    field_obj=obj._meta.get_field(column_name)#通过列名获取列对象

    if field_obj.choices:  # choices type
        column_data = getattr(obj, "get_%s_display" % column_name)()
    else:
        column_data = getattr(obj, column_name)
    if 'ManyToManyField' in field_obj.__repr__():
        column_data = getattr(obj, column_name).select_related()
        column_datas = ""
        for item in column_data:
            column_datas += '%s,' % item
        column_data=column_datas


    ele = '''<div class="col-md-4" style="margin-bottom: 8px"><label><strong>%s:</strong></label><label>%s</label></div>'''\
          % (label_name, column_data)

    return mark_safe(ele)


@register.simple_tag
def load_product_accessories(obj):
    '''用于显示product辅料的信息,obj是相应辅料对象'''

    accessorie_type = obj.get_Accessories_type_display()
    accessorie_name=obj.name
    accessorie_pic=obj.image
    picture_str="<a href='#' class='thumbnail'>" \
                "<img src='/static/img/accessories/%s.jpg'></a>"%(accessorie_name)
    ele='''<div class="col-md-2 img-acc-print">
                <div class='col-md-12'>%s</div>
                <div class='col-md-12'>%s</div>
                </div>'''%(accessorie_name,picture_str)

    return mark_safe(ele)

@register.simple_tag
def load_main_img(obj_product):
    '''用于生成图片标签'''
    sellerSku=obj_product.sellerSku
    image_url=obj_product.image
    ele='''<img src="/static/img/swimwear/%s/%s(1).jpg" alt="缩略图">
                </a>'''%(sellerSku,image_url)

    return mark_safe(ele)

@register.simple_tag
def load_img(obj_product, i='1'):
    '''用于生成图片标签'''
    i=to_string(i)
    sellerSku=obj_product.sellerSku
    image_url=obj_product.image
    ele='''<a href="#" class="thumbnail">
                    <img src="/static/img/swimwear/%s/%s(%s).jpg"
                         alt="缩略图">
                </a>'''%(sellerSku,image_url,i)

    return mark_safe(ele)

@register.simple_tag
def load_description(description):
    '''显示不分行描述'''
    ele=''''''
    # feature=obj_product.features
    description=description.split('\r\n')
    for item in description:
        ele += "<p>%s</p>"%item
    return mark_safe(ele)


@register.simple_tag
def load_features(feature):
    '''显示描述，根据换行符分行'''
    ele=''''''
    # feature=obj_product.features
    features=feature.split('\r\n')
    for item in features:
        ele += "<tr><td>%s</td></tr>"%item
    return mark_safe(ele)



@register.simple_tag
def load_Periods(pro_periods,column_name):
    '''用于生成图片标签'''
    ele=''''''
    for obj in pro_periods:
        column_data = getattr(obj, column_name)
        ele+="<td>%s</td>"%column_data
    return mark_safe(ele)

@register.simple_tag
def get_detail_path(table_obj):
    '''路径调整'''
    path=table_obj.request.path
    # request_path=path.split('?')[0]#去掉查询过滤的条件
    # request_path=request_path.remove()
    request_path='/ymx01/product/'
    return mark_safe(request_path)


@register.filter
def to_string(value):
    return '%s' % value