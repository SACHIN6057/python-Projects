
from django.urls import path

from . import views




urlpatterns = [
    path('',views.Index),
    path('home', views.Index),
    path('login',views.login),
    path('signup',views.signup),
    path('content',views.content),
    path('content/create',views.create),
    path('login/delete',views.delete),
    path('delete/<int:post_id>/',views.delete1),
]