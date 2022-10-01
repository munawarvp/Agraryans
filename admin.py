from django.contrib import admin
from . models import reg_table,add_reservation_form,add_equipment_table,add_package_table,add_category_table,add_user_table,contact_form

# Register your models here.

admin.site.register(reg_table)
admin.site.register(add_reservation_form)
admin.site.register(add_equipment_table)
admin.site.register(add_package_table)
admin.site.register(add_category_table)
admin.site.register(add_user_table)
admin.site.register(contact_form)