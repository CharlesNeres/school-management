from django.urls import path
from . import views

urlpatterns = [
    path('', views.enrollment_list, name='enrollment_list'),
    path('create/', views.enrollment_create, name='enrollment_create'),
    path('<int:pk>/edit/', views.enrollment_update, name='enrollment_update'),
    path('<int:pk>/delete/', views.enrollment_delete, name='enrollment_delete'),
    path('<int:pk>/', views.enrollment_detail, name='enrollment_detail'),

]