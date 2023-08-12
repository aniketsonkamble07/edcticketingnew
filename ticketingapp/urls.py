from django.contrib import admin
from django.urls import path, include
from . import views

    

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event/<int:event_id>/book/', views.book_ticket, name='book_ticket'),
    path('register/', views.register, name='register'),
    path('profile/', views.user_profile, name='user_profile'),
    path('accounts/profile/', views.user_profile, name='user_pprofile'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
    path('participants_list/', views.participants_list, name='participants_list'),
    path('event_participants/<int:event_id>/', views.event_participants_list, name='event_participants_list'),



    # Add any additional URL patterns here, such as admin views if applicable
]


