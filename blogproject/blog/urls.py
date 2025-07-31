from django.urls import path, include
from blog.views import *
from blog.api import api_register, api_login, api_logout, PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('',home_view, name='home'),
    path('register/',register_view, name='register'),
    path('login/',login_view, name='login'),
    path('logout/',logout_view, name='logout'),
    path('create/',post_create, name='post_create'),
    path('update/<int:pk>/',post_update, name='post_update'),
    path('delete/<int:pk>/',post_delete, name='post_delete'),
    path('api/register/', api_register, name='api_register'),
    path('api/login/', api_login, name='api_login'),
    path('api/logout/', api_logout, name='api_logout'),
    path('api/', include(router.urls)),
]
