from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/',views.ecom_dashboard , name = 'dashboard' ),
    path('setting-dashboard/',views.setting_dashboard , name = 'setting-dashboard' ),
    path('product-main-category-list/', views.product_main_category_list_view, name = 'product-main-category-list'),
    path('add-product-main-category/', views.add_product_main_category, name = 'add-product-main-category'),
    path('product-main-category/<int:pk>/', views.product_main_category_details, name = 'product-main-category-details'),
    path('product-list/', views.product_list, name = 'product-list'),
    path('product-detail/<int:pk>/', views.product_detail, name = 'product-detail'),
    path('product/edit/<int:pk>/', views.product_edit, name = 'product-edit'),
    path('add-new-product/', views.add_new_product, name = 'add-new-product'),
    path('products/<slug:product_slug>/', views.products_details, name = 'products-details'),
    path('', views.home, name = 'home'),
   
    #Authintication
    path('login/', views.login_view, name='user_login'),
    path('register/', views.register_view, name='user_register'),
    path('logout/', views.logout_view, name='user_logout'),
]  