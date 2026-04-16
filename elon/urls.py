from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('elon/<int:id>/', views.elon_detail, name='detail'),
    path('create/', views.create_elon, name='create'),
    path('update/<int:id>/', views.update_elon, name='update'),
    path('delete/<int:id>/', views.delete_elon, name='delete'),
]