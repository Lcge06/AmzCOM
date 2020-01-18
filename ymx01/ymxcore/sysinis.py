from django.contrib import admin

class BaseMyAdmin(object):
    list_display = []
    list_filters = []
    search_fields = []
    list_per_page = 18
    ordering = None
    filter_horizontal = []
    list_editable = []
    readonly_fields = []
    actions = ["delete_selected_objs", ]
    readonly_table = False
    modelform_exclude_fields = []
    add_form = None

    mtm_fields=[]
    choice_fields=[]
    basic_fields=[]

    # def delete_selected_objs(self, request, querysets):
    #     app_name = self.model._meta.app_label
    #     model_name = self.model._meta.model_name
    #     if self.readonly_table:
    #         errors = {"readonly_table": "This table is readonly ,cannot be deleted or modified!"}
    #     else:
    #         errors = {}
    #     if request.POST.get("_delete_confirm") == "yes":
    #         if not self.readonly_table:
    #             querysets.delete()
    #         return redirect("/myadmin/%s/%s/" % (app_name, model_name))
    #     selected_ids = ','.join([str(i.id) for i in querysets])
    #     return render(request, "myadmin/table_objs_delete.html", {"objs": querysets,
    #                                                               "admin_class": self,
    #                                                               "app_name": app_name,
    #                                                               "model_name": model_name,
    #                                                               "model_verbose_name": self.model._meta.verbose_name,
    #                                                               "selected_ids": selected_ids,
    #                                                               "admin_action": request._admin_action,
    #                                                               "errors": errors
    #                                                               })

    def default_form_validation(self):
        '''用户可以在此进行自定义的表单验证，相当于django form的clean方法'''
        pass


class AdminAlreadyRegistered(Exception):
    def __init__(self, msg):
        self.message = msg


class SysInitial(object):
    """通过该类对各模块进行初始化"""
    def __init__(self):
        self.sysdata={}
        self.menus={}

    def init_discover(self,user):
        self.int_menu(user)
        self.mod_import()#通过反射的方法导入initsystem模块

    def init_sysdata(self, model_class, admin_class=None):
         """初始化系统,在initsysytem中调用此函数，可以对需要初始化的数据进行统一注册
         model_class是在models中建的模型类，或者其他需要显示的模型类
         admin_class是对model_class的自定义设置
         sysdata中以model_class的名称存储了class_admin这个类，
         而将model_class这个类存储在admin_class下的model属性里"""
         model_name=model_class._meta.model_name
         if not admin_class:  # no custom admin class , use BaseAdmin
             admin_class = BaseMyAdmin()
         else:
             admin_class = admin_class()
         admin_class.model = model_class  # 绑定model 对象和admin 类

         self.sysdata[model_name]=admin_class

    def int_menu(self,user):
        '''初始化用户菜单'''
        if user:
            for role in user.role.select_related():#通过user获取角色
                for menu in role.menus.select_related():#通过角色获取权限
                    self.menus[menu.name]=menu

    def mod_import(self):
        try:
            mod = __import__("ymx01.ymxcore.initsystem")  # 反射导入initsystem模块
        except ImportError:
            print(ImportError)


sysini=SysInitial() #实例化该类，每个app下的myadmin模块调用该实例，不会对该类进行重复实例化