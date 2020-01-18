from django.db import models


# Create your models here.
# 产品表
class Order(models.Model):
    amazon_order_id = models.CharField(max_length=108, verbose_name="AMZ订单ID")
    merchant_order_id = models.CharField(max_length=108, blank=True, null=True, verbose_name="MER订单ID")
    purchase_date = models.CharField(max_length=108, blank=True, null=True, verbose_name="下单时间")
    last_updated_date = models.CharField(max_length=108, blank=True, null=True, verbose_name="最近更新时间时间")
    order_status = models.CharField(max_length=32, blank=True, null=True, verbose_name="订单状态")
    fulfillment_channel = models.CharField(max_length=32, blank=True, null=True, verbose_name="配送渠道")
    sales_channel = models.CharField(max_length=50, blank=True, null=True, verbose_name="销售渠道")
    order_channel = models.CharField(max_length=50, blank=True, null=True, verbose_name="下单渠道")
    url = models.CharField(max_length=50, blank=True, null=True, verbose_name="链接")
    ship_service_level = models.CharField(max_length=50, blank=True, null=True, verbose_name="配送方式")
    product_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="产品名称")
    sku = models.CharField(max_length=50, blank=True, null=True, verbose_name="SKU")
    asin = models.CharField(max_length=50, blank=True, null=True, verbose_name="ASIN")
    item_status = models.CharField(max_length=32, blank=True, null=True, verbose_name="配送状态")
    quantity = models.CharField(max_length=32, blank=True, null=True, verbose_name="数量")
    currency = models.CharField(max_length=32, blank=True, null=True, verbose_name="货币")
    item_price = models.CharField(max_length=32, blank=True, null=True, verbose_name="总价")
    item_tax = models.CharField(max_length=32, blank=True, null=True, verbose_name="税")
    shipping_price = models.CharField(max_length=32, blank=True, null=True, verbose_name="运输费")
    shipping_tax = models.CharField(max_length=32, blank=True, null=True, verbose_name="运输税")
    gift_wrap_price = models.CharField(max_length=32, blank=True, null=True, verbose_name="礼品包装价格")
    gift_wrap_tax = models.CharField(max_length=32, blank=True, null=True, verbose_name="礼品包装税")
    item_promotion_discount = models.CharField(max_length=32, blank=True, null=True, verbose_name="订单优惠折扣")
    ship_promotion_discount = models.CharField(max_length=32, blank=True, null=True, verbose_name="运输优惠折扣")
    ship_city = models.CharField(max_length=32, blank=True, null=True, verbose_name="城市")
    ship_state = models.CharField(max_length=32, blank=True, null=True, verbose_name="州")
    ship_postal_code = models.CharField(max_length=32, blank=True, null=True, verbose_name="邮政编码")
    ship_country = models.CharField(max_length=32, blank=True, null=True, verbose_name="国家")
    promotion_ids = models.CharField(max_length=32, blank=True, null=True, verbose_name="促销ID")
    is_business_order = models.CharField(max_length=32, blank=True, null=True, verbose_name="是否企业买家")
    purchase_order_number = models.CharField(max_length=32, blank=True, null=True, verbose_name="采购订单号")
    price_designation = models.CharField(max_length=32, blank=True, null=True, verbose_name="定价类型")

    def __str__(self):
        return self.amazon_order_id

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = "订单"
