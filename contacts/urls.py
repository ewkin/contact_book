from django.contrib import admin
from django.urls import path, include
from . import views
from .views import register
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('', views.contact_list, name='post_list'),
    path('contact/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('contact/new/', views.contact_new, name='contact_new'),
    path('contact/<int:pk>/edit/', views.contact_edit, name='contact_edit'),
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logedout'),
    path('register/', register, name="register"),
    path('admin/', admin.site.urls),
]
