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
from django.contrib import admin
from extra_apps import xadmin
from django.urls import path,include
from ymx01.views import views,website
from AmzCOM import views as main_views

import ymx01.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls,name='x_admin'),
    path('', main_views.PortalView.as_view()),
    path('ymx01/', include(ymx01.urls)),
    path('account/login/', website.acc_login, name='ymx01_login'),
    path('account/logout/', website.acc_logout, name='ymx01_logout'),
]
