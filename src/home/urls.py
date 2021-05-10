from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .product_controller import ProductViewSet
from .homework import *

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

    path('new', new),

    path('group/<int:group_id>/students', students_by_group, name='students_by_group'),
    path('products', product_list, name='product_list'),
    path('product_name/<int:product_id>', product_name, name='product_name'),
    path('product/create', create_product, name='create_product'),
    path('productss', APIProducts.as_view()),
    path('productss/<int:pk>', APIProductsdetail.as_view()),
    path('projects', projects),
    path('project/<int:project_id>', project),
    path('comments/', api_comments),
    path('api_comment_detail/<int:pk>', api_comment_detail),
    path('projectss', APIProject.as_view()),
    path('projectss/<int:pk>', APIProjectDetail.as_view()),
    path('proj', api_projects)
]
#
# router = DefaultRouter()
# router.register(r'products', ProductViewSet, basename='product')
#
# urlpatterns = [
#     path('api/', include(router.urls))
# ]