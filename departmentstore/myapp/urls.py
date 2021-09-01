from django.urls import path
from . import views
app_name = 'dashboard'



urlpatterns = [
    path('',views.index, name='index'),
    path('staff/',views.staff, name='staff'),
    path('product/',views.product, name='product'),
    path('order/',views.order, name='order'),
    path('product_delete/<int:id>/',views.product_delete,name="product_delete"),
    path('product_update/<int:id>/',views.product_update,name="product_update"),
    path('staff_detail/<int:id>/',views.staff_detail,name="staff_detail"),
]