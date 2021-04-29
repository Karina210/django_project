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
    path(r'feedback/', feedback, name='feedback_url'),
    path('customers', customers, name='customers_list_url')
]