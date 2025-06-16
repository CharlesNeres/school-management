from django.contrib import admin
from .models import Student, Teacher
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'birth_date')
    search_field = ('first_name', 'last_name', 'email')
    list_filter = ('birth_date',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'hire_date')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('hire_date',)