from ymx01.models import Accessories
from ymx01.tables import table_filter,TableHandler,search_by,get_orderby

class ProductHandler(TableHandler):
    def get_accessories_filter_list(self):
        accessories_tpye_choices = Accessories.Accessories_type_choices
        for i in accessories_tpye_choices:
            pass