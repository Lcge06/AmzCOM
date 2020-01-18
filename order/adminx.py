import xadmin

from order import models
from .resources import OrderResource

# Register your models here.
#通过该类可以对admin中表进行自定义设置
@xadmin.sites.register(models.Order)
class OrderAdmin(object):

    list_display = ['amazon_order_id','purchase_date','sku','quantity','item_price']
    list_display_links = ['amazon_order_id']

    list_filter = ('sku','order_status','item_status')

    search_fields = ('amazon_order_id','sku')
    show_detail_fields=['amazon_order_id']


    #设置导出的列
    list_per_page = 15
    import_export_args = {
        'import_resource_class': OrderResource,
        # 'export_resource_class': ProductInfoResource,
    }


