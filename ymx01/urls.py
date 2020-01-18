"""AmzCOM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from ymx01.views import views

urlpatterns = [
    # url(r'^$', views.product_display, name="product_list"),
    # url(r'^(\w+)/$', views.display_inventory, name="inventory_now"),  # 显示每个表的数据
    url(r'^product/$', views.product_display, name='product_list'),
    url(r'^(\w+)/detail/(\d+)/$', views.product_detail, name="product_detail"),
    url(r'^(\w+)/(\w+)/(\w+)/$', views.product_filter, name="product_filter"),
    # url(r'^order_now/$', views.index_display, name='order_now'),
    # url(r'^(\w+)/(\w+)/$', views.display_table_list, name="table_list"),  # 显示每个表的数据
]
