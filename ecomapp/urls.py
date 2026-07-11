from django.urls import path

from . import views_payment
from . import views
urlpatterns = [
    path('dashboard/',views.ecom_dashboard , name = 'dashboard' ),
    path('setting-dashboard/',views.setting_dashboard , name = 'setting-dashboard' ),
    path('product-main-category-list/', views.product_main_category_list_view, name = 'product-main-category-list'),
    path('add-product-main-category-details/', views.add_product_main_category, name = 'add-product-main-category'),
    path(
    "backend/product-main-category-edit/<int:pk>/",views.product_main_category_edit,name="product-main-category-edit"),
    path('product-main-category/<int:pk>/', views.product_main_category_details, name = 'product-main-category-details'),
    path('product-list/', views.product_list, name = 'product-list'),
    path('product-detail/<int:pk>/', views.product_detail, name = 'product-detail'),
    path('product/edit/<int:pk>/', views.product_edit, name = 'product-edit'),
    path('add-new-product/', views.add_new_product, name = 'add-new-product'),
    path('products/<slug:product_slug>/', views.products_details, name = 'products-details'),
    path('', views.home, name = 'home'),
   
    #User Authintication
    path('login/', views.user_login_view, name='user_login'),
    path('register/', views.user_register_view, name='user_register'),
    path('logout/', views.user_logout_view, name='user_logout'),
    path('request-otp/', views.request_otp_view, name='request_otp'),
    path('verify-otp/', views.verify_otp_view, name='verify_otp'),
    
    #Admin Authintication
     path('admin-logout/', views.admin_logout_view, name='admin-logout'),
    path('admin-login/', views.admin_login_view, name='admin-login'),
    
    
    #ajax
     path('add-or-update-cart/', views.add_or_update_cart, name='add-or-update-cart'),
     
     path('cart/', views.cart, name='cart'),
     path('checkout/', views.checkout, name='checkout'),
     
     
     #payment
     
     path('payment/success/<str:str_data>/', views_payment.payment_complete, name='payment-complete'),
     path('payment/cancel/<str:str_data>/', views_payment.payment_cancel, name='payment-cancel'),
     path('payment/failed/<str:str_data>/', views_payment.payment_failed, name='payment_FAILED'),
     path('payment/check/<str:str_data>/', views_payment.payment_check, name="payment_check"),
     path('profile/', views.profile, name='profile'),
     path("profile/edit/", views.edit_profile, name="edit_profile"),
     path("backend/change-password/",views.change_password,name="change-password"),
]   