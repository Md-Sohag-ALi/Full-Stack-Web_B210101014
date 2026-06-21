from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/',views.ecom_dashboard , name = 'dashboard' ),
    path('setting-dashboard/',views.setting_dashboard , name = 'setting-dashboard' ),
    path('product-main-category-list/', views.product_main_category_list_view, name = 'product-main-category-list'),
    path('add-product-main-category/', views.add_product_main_category, name = 'add-product-main-category'),
    path('product-main-category/<int:pk>/', views.product_main_category_details, name = 'product-main-category-details')
    ] 