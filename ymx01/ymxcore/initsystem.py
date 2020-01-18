from ymx01 import models
from ymx01.ymxcore.sysinis import sysini,BaseMyAdmin

# Register your models here.
class ProductAdmin(BaseMyAdmin):
    model = models.Product
    list_display = ['productName','title','brand','status']
    fk_fields = ('brand','series','scene','designer')
    choice_fields = ('status',)
    list_filter = ('date_created',)
    search_fields = ('productName','sellerSku')
    colored_fields = {
        'status':{'设计':"rgba(145, 255, 0, 0.78)",
                  '完成':"#ddd"},

    }
    basic_fields = ('productName', 'status','brand', 'sellerSku','series','target_audience','scene','weight','offer', 'designer')
    mtm_fields = ('accessories', 'inf_more', 'features', 'a_description')
    picture_num=range(1, 7)

sysini.init_sysdata(models.Product,ProductAdmin)

