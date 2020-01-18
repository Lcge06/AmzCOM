# _*_coding:utf-8_*_
__author__ = 'LCG'
from ymx01.ymxcore.sysinis import sysini
from ymx01 import models
from django import template
from django.utils.safestring import mark_safe
from django.core.exceptions import FieldDoesNotExist
import re

register = template.Library()


@register.simple_tag
def render_page_num(request, paginator_obj, loop_counter):
    abs_full_url = request.get_full_path()

    if "?page=" in abs_full_url:
        url = re.sub("page=\d+", "page=%s" % loop_counter, request.get_full_path())
    elif "?" in abs_full_url:
        url = "%s&page=%s" % (request.get_full_path(), loop_counter)
    else:
        url = "%s?page=%s" % (request.get_full_path(), loop_counter)

    if loop_counter == paginator_obj.number:  # current page
        return mark_safe('''<li class='active'><a href="{abs_url}">{page_num}</a></li>''' \
                         .format(abs_url=url, page_num=loop_counter))

    if abs(loop_counter - paginator_obj.number) < 2 or \
            loop_counter == 1 or loop_counter == paginator_obj.paginator.num_pages:  # the first page or last

        return mark_safe('''<li><a href="{abs_url}">{page_num}</a></li>''' \
                         .format(abs_url=url, page_num=loop_counter))
    elif abs(loop_counter - paginator_obj.number) < 3:
        return mark_safe('''<li><a href="{abs_url}">...</a></li>''' \
                         .format(abs_url=url, page_num=loop_counter))
    else:
        return ''


@register.simple_tag
def display_orderby_arrow(table_obj, loop_counter):
    if table_obj.orderby_col_index == loop_counter:
        if table_obj.orderby_field.startswith('-'):  # 降序
            orderby_icon = '''<i class="fa fa-caret-up" aria-hidden="true"></i>'''
        else:
            orderby_icon = '''<i class="fa fa-caret-down" aria-hidden="true"></i>'''
        return mark_safe(orderby_icon)
    return ''

@register.simple_tag
def build_table_row(row_obj, table_obj,onclick_column=None,target_link=None):
    row_ele = "<tr>"
    # print("lsit editab",table_obj.list_editable)
    row_ele += "<td><input type='checkbox' tag='row-check' value='%s' > </td>" % row_obj.id
    if table_obj.list_display:
        for index, column_name in enumerate(table_obj.list_display):
            if hasattr(row_obj, column_name):
                field_obj = row_obj._meta.get_field(column_name)
                # column_data = field_obj._get_val_from_obj(row_obj)
                if field_obj.choices:  # choices type
                    column_data = getattr(row_obj, "get_%s_display" % column_name)()
                else:
                    column_data = getattr(row_obj, column_name)

                if 'DateTimeField' in field_obj.__repr__():
                    column_data = getattr(row_obj, column_name).strftime("%Y-%m-%d %H:%M:%S") \
                        if getattr(row_obj, column_name) else None
                if 'ManyToManyField' in field_obj.__repr__():
                    column_data = getattr(row_obj, column_name).select_related().count()

                # if onclick_column == column_name:
                #     column = ''' <td><a class='btn-link' href=%s>%s</a></td> '''% (url_reverse(target_link,args=(column_data, )),column_data)

                if index == 0:  # 首列可点击进入更改页
                    column = '''<td><a class='btn-link'  href='%sdetail/%s/' >%s</a> </td> ''' % (
                    table_obj.request.path,
                    row_obj.id,
                    column_data)
                elif column_name in table_obj.colored_fields:  # 特定字段需要显示color
                    color_dic = table_obj.colored_fields[column_name]
                    if column_data in color_dic:
                        column = "<td style='background-color:%s'>%s</td>" % (color_dic[column_data],
                                                                              column_data)
                    else:
                        column = "<td>%s</td>" % column_data
                else:
                    column = "<td>%s</td>" % column_data

            elif hasattr(table_obj.admin_class, column_name):  # customized field
                field_func = getattr(table_obj.admin_class, column_name)
                print(field_func)
                table_obj.admin_class.instance = row_obj
                column = "<td>%s</td>" % field_func(table_obj.admin_class)

            row_ele += column
    else:
        base_path=table_obj.request.path.split('?')[0]
        row_ele += "<td><a class='btn-link'  href='{request_path}detail/{obj_id}/' >{column}</a></td>". \
            format(request_path=base_path, column=row_obj, obj_id=row_obj.id)

    # for dynamic display
    if table_obj.dynamic_fk:
        if hasattr(row_obj, table_obj.dynamic_fk):
            ##print("----dynamic:",getattr(row_obj,table_obj.dynamic_fk), row_obj)
            ##print(row_obj.networkdevice)
            dy_fk = getattr(row_obj, table_obj.dynamic_fk)  # 拿到的是asset_type的值
            if hasattr(row_obj, dy_fk):
                dy_fk_obj = getattr(row_obj, dy_fk)
                # print("-->type",type(dy_fk_obj), dy_fk_obj )
                for index, column_name in enumerate(table_obj.dynamic_list_display):
                    if column_name in table_obj.dynamic_choice_fields:
                        column_data = getattr(dy_fk_obj, 'get_%s_display' % column_name)()
                    else:
                        column_data = dy_fk_obj._meta.get_field(column_name)._get_val_from_obj(dy_fk_obj)
                    # print("dynamic column data", column_data)

                    column = "<td>%s</td>" % column_data
                    row_ele += column
            else:
                # 这个关联的表还没创建呢
                pass
    row_ele += "</tr>"
    return mark_safe(row_ele)


@register.simple_tag
def load_search_element(table_obj):
    #print("search:",table_obj.search_fields)
    if table_obj.search_fields:
        already_exist_ars = ''
        for k,v in table_obj.request.GET.items():
            if k != 'q':#igonore old search text
                already_exist_ars += "<input type='hidden' name='%s' value='%s' >" % (k,v)
        # placeholder = "通过 %s" % "".join(table_obj.search_fields)
        # placeholder = placeholder+"查询"
        placeholder = "搜索 产品"
        ele = '''
            <div class="searchbox">
               <form class="navbar-form navbar-left" method="get">
                    <div class="input-group search-group">
                        <div class="form-control"><input type="text" name="q" value='%s' class="form-control" placeholder="%s"></div>
                        %s
                        <span class="input-group-btn">
                            <button class="btn btn-primary" type="submit"><i class="fa fa-search"></i></button>
                        </span>
                    </div>
               </form>
            </div>

        '''% (table_obj.request.GET.get('q') if table_obj.request.GET.get('q') else '',
              placeholder,already_exist_ars)
        return mark_safe(ele)
    return ''

@register.simple_tag
def get_table_column(column, table_obj):
    if hasattr(table_obj.model_class,column):
        return  table_obj.model_class._meta.get_field(column).verbose_name
    else:
        return column

    # else:#might be customized field,which is not exist in model class
    #     #check if this field exist in admin class
    #     if hasattr(table_obj.admin_class, column):
    #         field_func = getattr(table_obj.admin_class,column)
    #         if hasattr(field_func,'display_name'):
    #             return field_func.display_name
    #         return field_func.__name__


@register.simple_tag
def char_addslashes(sku):
    return "/"+sku+"/"


@register.filter
def to_string(value):
    return '%s' % value


@register.simple_tag
def load_menus(request):
    menus = []
    for menu_name in sysini.menus:
        menus.append(sysini.menus[menu_name])
    # for role in request.user.role.select_related():
    #     menus.extend(role.menus.select_related())
    return sorted(set(menus), key=lambda x: x.order)
