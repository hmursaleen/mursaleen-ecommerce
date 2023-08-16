from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name = 'home'),
	path('login/', views.login_view, name='login'),
	path('signup/', views.signup, name='signup'),
	path('search/', views.search, name='search'),
	path('product/<slug:slug>/', views.category_detail, name='category_detail'),
	path('product/<slug:category_slug>/<slug:slug>/', views.product_detail, name='product_detail'),
	path('vendor/<int:pk>/', views.vendor_detail, name='vendor_detail'),
	path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
	path('change-quantity/<str:product_id>/', views.change_quantity, name='change_quantity'),
	path('remove-from-cart/<str:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart_view, name='cart_view'),
	path('cart/checkout/', views.checkout, name='checkout'),
	path('cart/success/', views.success, name='success'),
	path('logout/', views.logout_view, name='logout'),
]
