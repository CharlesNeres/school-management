from django.contrib import admin
from .models import Course
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'teacher')
    search_fields = ('name',)
    list_filter = ('start_date', 'end_date', 'teacher')
