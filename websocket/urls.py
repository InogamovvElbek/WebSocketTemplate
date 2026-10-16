from django.contrib import admin
from django.urls import path
from apps import views

urlpatterns = [
    path('', views.chat, name='chat'),
    path('categories/', views.category_list, name='category_list'),
    path('scores/', views.score_list, name='score_list'),
    path('admin/', admin.site.urls),
]
