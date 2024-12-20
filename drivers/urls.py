from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_drivers, name='list_drivers'),
    path('create_driver/', views.create_driver, name='create_driver'),
    path('update_driver/<int:driver_id>/', views.update_driver, name='update_driver'),
    path('delete_driver/<int:driver_id>/', views.delete_driver, name='delete_driver'),
]
