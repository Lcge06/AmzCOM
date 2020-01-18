from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

import datetime
import json
import glob

from ymx01 import models
from ymx01 import tables
from ymx01.ymxcore.sysinis import sysini

import os

# Create your views here.

# 主页
@login_required
def app_index(request):
    pass

@login_required
def product_display(request):
    if not sysini.sysdata:
        sysini.init_discover(request.user)  # 第一次登录首页时初始化系统数据
    errors = []
    admin_class = sysini.sysdata['product']
    querysets = tables.table_filter(request, admin_class, admin_class.model)
    acc_list = tables.get_accessories_list(request, admin_class.model)#获取辅料

    if request.method == 'POST':#这里对辅料过滤进行判断
        if '_accessories_filter' in request.POST:
            querysets=tables.accessories_filter(request,querysets,acc_list)

    searched_querysets = tables.search_by(request, querysets, admin_class)
    order_res = tables.get_orderby(request, searched_querysets, admin_class)

    paginator = Paginator(order_res[0], admin_class.list_per_page)

    page = request.GET.get('page')
    try:
        table_obj_list = paginator.page(page)
    except PageNotAnInteger:
        table_obj_list = paginator.page(1)
    except EmptyPage:
        table_obj_list = paginator.page(paginator.num_pages)

    table_obj = tables.TableHandler(request,
                                    admin_class.model,
                                    admin_class,
                                    table_obj_list,
                                    order_res)

    # accessories_tpye = models.Accessories.Accessories_type_choices
    # accessories_list=admin_class.model._meta.get_field('accessories').get_choices()


    page_inf = {
        'title': '产品',
        'home': '首页',
        'table': '产品',
        'url': {'home': 'product_list', 'table': 'product_list'},
    }

    return render(request, 'ymx01/product_view_list.html',
                  {'sys': sysini,
                   'table_obj': table_obj,
                   'app_name': 'ymx01',
                   'active_url': '/ymx01/',
                   'acc_list': acc_list,
                   'paginator': paginator,
                   'page_inf': page_inf,
                   'errors': errors})

@login_required
def product_detail(request,table_name,obj_id):

    admin_class=sysini.sysdata[table_name]

    obj_product = models.Product.objects.get(id=obj_id)#通过ID获取产品
    obj_accessories=obj_product.accessories.select_related()#产品对应的辅料
    obj_period=models.Periods.objects.filter(name=obj_product)#产品对应的阶段

    pic_str="static/img/swimwear/%s" % (obj_product.sellerSku)
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    pic_path=os.path.join(base_dir,pic_str)
    pic_list=os.listdir(pic_path)#获取产品图片文件夹下的图片数量
    admin_class.picture_num=range(1,len(pic_list))

    page_inf = {
        'title': '产品详情',
        'home':'首页',
        'table': '产品',
        'url':{'home':'product_list','table':'product_list'},
        'detail':obj_product.productName,
    }
    return render(request,'ymx01/product_detail.html',{'sys':sysini,
                                                       'admin_class':admin_class,
                                                       'product':obj_product,
                                                       'pro_periods':obj_period,
                                                       'page_inf':page_inf,
                                                       'accessories':obj_accessories})

@login_required
def product_filter(request,table_name, table_attr, attr_value):
    errors = []
    admin_class = sysini.sysdata[table_name]

    querysets=tables.table_filter(request,admin_class,admin_class.model,table_attr,attr_value)
    searched_querysets = tables.search_by(request, querysets, admin_class)
    order_res = tables.get_orderby(request, searched_querysets, admin_class)

    paginator = Paginator(order_res[0], admin_class.list_per_page)

    page = request.GET.get('page')
    try:
        table_obj_list = paginator.page(page)
    except PageNotAnInteger:
        table_obj_list = paginator.page(1)
    except EmptyPage:
        table_obj_list = paginator.page(paginator.num_pages)

    table_obj = tables.TableHandler(request,
                                    admin_class.model,
                                    admin_class,
                                    table_obj_list,
                                    order_res)

    # accessories_tpye = models.Accessories.Accessories_type_choices
    # accessories_list = admin_class.model._meta.get_field('accessories').get_choices()
    acc_list = tables.get_accessories_list(request, admin_class.model)

    page_inf = {
        'title': '产品',
        'home': '首页',
        'table': '产品',
        'url': {'home': 'product_list', 'table': 'product_list'},
    }

    return render(request, 'ymx01/product_view_list.html',
                  {'sys': sysini,
                   'table_obj': table_obj,
                   'app_name': 'ymx01',
                   'active_url': '/ymx01/',
                   'acc_list': acc_list,
                   'page_inf': page_inf,
                   'paginator': paginator,
                   'errors': errors})


