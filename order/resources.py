# resources.py
from import_export import resources
from .models import Order


class OrderResource(resources.ModelResource):
    class Meta:
        model = Order
        # skip_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        # report_skipped = True
        # 在导入预览页面中显示跳过的记录

        # import_id_fields   = ('id',)
        # exclude = ('id',)
        # 对象标识的默认字段是id，您可以选择在导入时设置哪些字段用作id

        fields = ('id',
                  'amazon_order_id',
                  'merchant_order_id',
                  'purchase_date',
                  'last_updated_date',
                  'order_status',
                  'fulfillment_channel',
                  'sales_channel',
                  'order_channel',
                  'url',
                  'ship_service_level',
                  'product_name',
                  'sku',
                  'asin',
                  'item_status ',
                  'quantity',
                  'currency',
                  'item_price',
                  'item_tax',
                  'shipping_price',
                  'shipping_tax',
                  'gift_wrap_price',
                  'gift_wrap_tax ',
                  'item_promotion_discount',
                  'ship_promotion_discount',
                  'ship_city',
                  'ship_state ',
                  'ship_postal_code',
                  'ship_country',
                  'promotion_ids',
                  'is_business_order',
                  'purchase_order_number',
                  'price_designation')
