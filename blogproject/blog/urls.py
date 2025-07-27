from django.urls import path
from blog.views import *

urlpatterns = [
    path('',home_view, name='home'),
    path('register/',register_view, name='register'),
    path('login/',login_view, name='login'),
    path('logout/',logout_view, name='logout'),
    path('create/',post_create, name='post_create'),
    path('update/<int:pk>/',post_update, name='post_update'),
    path('delete/<int:pk>/',post_delete, name='post_delete'),
]
