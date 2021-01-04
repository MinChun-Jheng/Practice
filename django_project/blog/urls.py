from django.urls import path
from . import views

urlpatterns = [
    # 2. package.func
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
