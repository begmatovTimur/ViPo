from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('posts/<int:pk>', views.post_detail, name='post_detail'),
    path('register',views.register, name='register'),
    path('log_in', views.log_in, name='log_in'),
    path('account', views.account, name='account'),
]