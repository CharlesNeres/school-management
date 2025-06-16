from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/<int:pk>/edit/', views.student_update, name='student_update'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/create/', views.teacher_create, name='teacher_create'),
    path('teachers/<int:pk>/edit/', views.teacher_update, name='teacher_update'),
    path('teachers/<int:pk>/delete/', views.teacher_delete, name='teacher_delete'),
    path('teachers/<int:pk>/', views.teacher_detail, name='teacher_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='account_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='account_logout'),
]