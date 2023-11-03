from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from core import views as core_views

urlpatterns = [
    path('', core_views.home, name='home'),
    path('p1', core_views.productone, name='links'),
    path('posts', core_views.postdata, name='posts'),
]