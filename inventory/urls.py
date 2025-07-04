from django.urls import path
from . import views

urlpatterns = [
    path('', views.public_view, name='public_view'),
    path('login/', views.login_view, name='login'),
    path('user/', views.user_view, name='user_view'),
    path('logout/', views.logout_view, name='logout'),
    path('about/', views.about_view, name='about'),
    path('goods/', views.goods_view, name='goods'),

]
