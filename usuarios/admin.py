from django.contrib import admin
from usuarios.models import Usuario
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#Register your models here.

# class AdminInline(admin.StackedInline):
#     model = Admin
#     can_delete = False
#     verbose_name_plural = 'Admins'

# class ClientesInline(admin.StackedInline):
#     model = Clientes
#     can_delete = False
#     verbose_name_plural = 'Clientes'

# class UserAdmin(BaseUserAdmin):
#     inlines = (AdminInline, ClientesInline)
#     list_display = ('username', 'email')
#     def get_form(self, request, obj=None, **kwargs):
#         form = super().get_form(request, obj, **kwargs)
#         is_superuser = request.user.is_superuser
#         disabled_fields = set()  # type: Set[str]

#         # Prevent non-superusers from editing their own permissions
#         if not is_superuser:
#             disabled_fields |= {
#                 'username',
#                 'is_staff',
#                 'is_superuser',
#                 'user_permissions',
#                 'groups',
#                 'last_login',
#                 'date_joined',
#             }

#         for f in disabled_fields:
#             if f in form.base_fields:
#                 form.base_fields[f].disabled = True

#         return form

admin.site.register(Usuario)

