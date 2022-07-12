from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('<int:post_id>/', views.detail, name="post_detail"),
]