from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns=[
    path('',views.index1,name='index1'),
    path('add_contact_form',views.add_contact_form,name='add_contact_form'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('index',views.index,name='index'),
    path('reg_form_submission',views.reg_form_submission,name='reg_form_submission'),
    path('login_form_submission',views.login_form_submission,name='login_form_submission'),

    path('reservation',views.reservation,name='reservation'),
    path('add_new_reservation',views.add_new_reservation,name='add_new_reservation'),
    path('add_reservation',views.add_reservation,name='add_reservation'),
    path('update_reservation/<int:id>',views.update_reservation,name='update_reservation'),
    path('update_reservation_form/<int:id>',views.update_reservation_form,name='update_reservation_form'),
    path('delete_reservation_list/<int:id>',views.delete_reservation_list,name='delete_reservation_list'),
    path('invoice',views.invoice,name='invoice'),

    path('equipments',views.equipments,name='equipments'),
    path('add_equipments',views.add_equipments,name='add_equipments'),
    path('add_equipment_form',views.add_equipment_form,name='add_equipment_form'),
    path('edit_equipment/<int:id>',views.edit_equipment,name='edit_equipment'),
    path('edit_equipment_form/<int:id>',views.edit_equipment_form,name='edit_equipment_form'),
    path('delete_equipment_list/<int:id>',views.delete_equipment_list,name='delete_equipment_list'),

    path('view_package',views.view_package,name='view_package'),
    path('create_package',views.create_package,name='create_package'),
    path('create_package_form',views.create_package_form,name='create_package_form'),
    path('delete_package_list/<int:id>',views.delete_package_list,name='delete_package_list'),
    path('edit_package/<int:id>',views.edit_package,name='edit_package'),
    path('edit_package_form/<int:id>',views.edit_package_form,name='edit_package_form'),

    path('view_categories',views.view_categories,name='view_categories'),
    path('add_categories',views.add_categories,name='add_categories'),
    path('add_category_form',views.add_category_form,name='add_category_form'),
    path('edit_categories/<int:id>',views.edit_categories,name='edit_categories'),
    path('edit_category_form/<int:id>',views.edit_category_form,name='edit_category_form'),
    path('delete_category_list/<int:id>',views.delete_category_list,name='delete_category_list'),

    path('userlst',views.userlst,name='userlst'),
    path('add_user',views.add_user,name='add_user'),
    path('add_user_form',views.add_user_form,name='add_user_form'),
    path('edit_user/<int:id>',views.edit_user,name='edit_user'),
    path('edit_user_form/<int:id>',views.edit_user_form,name='edit_user_form'),
    path('delete_user_list/<int:id>',views.delete_user_list,name='delete_user_list'),

    path('forgot_password',views.forgot_password,name='forgot_password'),
    path('faqs',views.faqs,name='faqs'),
    path('logout',views.logout,name='logout'),


]