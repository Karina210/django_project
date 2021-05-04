from django.urls import path

from home.views import *

urlpatterns = [
    path(r'', index, name='index'),
    path(r'query/', query),
    path(r'name/', name),
    path(r'age/', age),
    path(r'date/', date1),
    path(r'com/', com),
    path(r'comm/', comm),
    path(r'index1', index1),
    # path(r'feedback/', feedback, name='feedback_url'),
    # path('customers', customers, name='customers_list_url'),
    path('customers', list_customers, name='customers_list_url'),
    path('customer/<customerId>/delete', delete_customer, name='delete_customer_url'),

    path('customer/form/create', create_customer_form, name='create_customer_form'),
    path('customer/create', create_customer, name='create_customer'),

    path('customer/<int:customer_id>', find, name='find_customer'),

    path('customer/<int:customer_id>/update', update, name='update_customer'),

    path('new', new)
]
