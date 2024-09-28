from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path
from . import views
from .views import feedback, reservation_view, success_view 



urlpatterns = [
    path("", views.home),
    path('product-detail/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),    
    path("about/", views.aboutview.as_view(),name="about"),
    path("home/", views.homeview.as_view(),name="home"),
    path("contact/", views.contactview.as_view(),name="contact"),
    path("blog/", views.blogview.as_view(),name="blog"),
    path("shop/", views.shopview.as_view(),name="shop"),
    path('feedback/', feedback, name='feedback'),
    path('reservation/', views.reservation_view.as_view(), name='reservation'),
    path('success/', success_view, name='success'),  # Ensure this points to your success view
    path("cart/", views.cartview.as_view(),name="cart"),
    path("wishlist/", views.wishlistview.as_view(),name="wishlist"),
    path('profile/', views.ProfileView.as_view(),name="profile"),
    path('search/', views.search, name="search"), 
]
