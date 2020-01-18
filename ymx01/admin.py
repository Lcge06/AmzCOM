from django.contrib import admin
from ymx01 import models
from django import forms

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# class UserCreationForm(forms.ModelForm):
#     """A form for creating new users. Includes all the required
#     fields, plus a repeated password."""
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
#
#     class Meta:
#         model = models.UserProfile
#         fields = ('email','name')
#
#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2
#
#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super(UserCreationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user
#
#
# class UserChangeForm(forms.ModelForm):
#     """A form for updating users. Includes all the fields on
#     the user, but replaces the password field with admin's
#     password hash display field.
#     """
#     password = ReadOnlyPasswordHashField(label="Password",
#         help_text=("Raw passwords are not stored, so there is no way to see "
#                     "this user's password, but you can change the password "
#                     "using <a href=\"password/\">this form</a>."))
#
#     class Meta:
#         model = models.UserProfile
#         fields = ('email','password','is_active', 'is_admin')
#
#     def clean_password(self):
#         # Regardless of what the user provides, return the initial value.
#         # This is done here, rather than on the field, because the
#         # field does not have access to the initial value
#         return self.initial["password"]
#
#
# class UserProfileAdmin(UserAdmin):
#     # The forms to add and change user instances
#     form = UserChangeForm
#     add_form = UserCreationForm
#
#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = ('id','email','is_admin','is_active')
#     list_filter = ('is_admin',)
#     list_editable = ['is_admin']
#
#     fieldsets = (
#         (None, {'fields': ('email','name', 'password')}),
#         ('Personal info', {'fields': ('memo',)}),
#
#         ('用户权限', {'fields': ('is_active','is_staff','is_admin','role','user_permissions','groups')}),
#
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email',  'password1', 'password2','is_active','is_admin')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ('user_permissions','groups')


# Register your models here.
#通过该类可以对admin中表进行自定义设置
class ProductAdmin(admin.ModelAdmin):
    model = models.Product
    list_display = ['productName','title','brand','status']

    fk_fields = ('brand','series')
    choice_fields = ('material','status')
    # list_filter = ('factory','designer','technology','material')

    mtm_fields=('target_audience','size','material','lining_material','technology','accessories')

    search_fields = ('productName','title')
    colored_fields = {
        'status':{'设计':"rgba(145, 255, 0, 0.78)",
                  '完成':"#ddd"},
    }

admin.site.register(models.UserProfile)
admin.site.register(models.Role)
admin.site.register(models.Product)
admin.site.register(models.Periods)
admin.site.register(models.Brand)
admin.site.register(models.Series)
admin.site.register(models.Target_audience)
admin.site.register(models.Scene)
admin.site.register(models.Designer)
admin.site.register(models.Lining)
admin.site.register(models.Accessories)
admin.site.register(models.FirstLayerMenu)
admin.site.register(models.SubMenu)
