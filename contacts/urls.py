from django.urls import path
from . import views


urlpatterns = [
    path('', views.contact_list, name='post_list'),
    path('contact/<int:pk>/', views.contact_detail, name='contact_detail'),
]
