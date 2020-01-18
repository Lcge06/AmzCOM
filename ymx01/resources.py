# resources.py
from import_export import resources
from .models import Product

class PustomerResource(resources.ModelResource):

    class Meta:
        model = Product
        fields = ('id', 'productName', 'status', 'title')
