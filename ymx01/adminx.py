import xadmin

from ymx01 import models
from ymx01.models import Product,Accessories,Periods
from xadmin import views
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline
from .resources import PustomerResource


@xadmin.sites.register(views.website.IndexView)
class MainDashboard(object):
    widgets = [
        [
            {"type": "html", "title": "AXESEA",
             "content": "<h3> 欢迎使用LeeGu产品管理软件! "},
            {"type": "list", "model": "ymx01.periods", "params": {"o": "-finish_date"}},
        ],
        [
            {"type": "qbutton", "title": "Quick Start",
             "btns": [{"model": Periods}, {"title": "AXESEA", "url": "http://www.axesea.com"}]},
            {"type": "addform", "model": Periods},
        ]
    ]

@xadmin.sites.register(views.BaseAdminView)
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


@xadmin.sites.register(views.CommAdminView)
class GlobalSetting(object):
    # 设置base_site.html的Title
    site_title = 'AmazonGo'
    # 设置base_site.html的Footer
    site_footer = 'lcg2019'
    # 折叠菜单
    menu_style = "accordion" #'default'
    # global_search_models = [models.Product,models.Designer]
    # global_models_icon = {
    #     models.Product: "fa fa-laptop", models.Accessories: "fa fa-cloud"
    # }




# Register your models here.
#通过该类可以对admin中表进行自定义设置
@xadmin.sites.register(models.Product)
class ProductAdmin(object):

    list_display = ['productName','image','sellerSku','brand','status']
    list_display_links = ['productName']

    list_filter = ('brand','series','status')

    search_fields = ('productName','sellerSku')
    show_detail_fields=['productName']

    style_fields = {"accessories": "checkbox-inline"}

    form_layout = (
        Main(
            TabHolder(
                Tab(
                    "Product Inf",
                    Fieldset(
                        "Basic Inf",
                        "productName", 'title', "status", 'sellerSku', 'image',
                        # Row(
                        #     AppendedText("weight", "G"),
                        #     AppendedText("offer", "$")
                        # ),
                        AppendedText("weight", "G"),
                        AppendedText("offer", "$"),
                        'brand', 'series', 'number', 'target_audience', 'scene',
                       'designer', 'inf_more','slogan', 'features', 'a_description',

                        # description="产品的一些基本信息",
                    )
                ),
                Tab(
                    "More Inf",
                    Fieldset(
                        "More Inf",
                        'accessories',
                    ),

                )
            ),

        ),
        # Side(
        #     Fieldset("什么都没有"),
        # )
    )
    #设置导出的列
    list_export_fields = ("productName", 'title', "status", 'sellerSku')
    list_per_page = 15
    import_export_args = {
        'import_resource_class': PustomerResource,
        # 'export_resource_class': ProductInfoResource,
    }

class BrandAdmin(object):
    import_excel=True



# xadmin.site.register(models.Product,ProductAdmin)
xadmin.site.register(models.Accessories)
xadmin.site.register(models.Periods)
xadmin.site.register(models.Brand)
xadmin.site.register(models.Series)
xadmin.site.register(models.Target_audience)
xadmin.site.register(models.Scene)
xadmin.site.register(models.Designer)
xadmin.site.register(models.Lining)
xadmin.site.register(models.FirstLayerMenu)
xadmin.site.register(models.SubMenu)
xadmin.site.register(models.UserProfile)
xadmin.site.register(models.Role)

