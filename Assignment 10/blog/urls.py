from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog_home'),
    path('create/', views.create_blog, name='create_blog'),
    path('my/', views.my_blogs, name='my_blogs'),
    path('edit/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),
]
