from django.contrib import admin
from .models import Enrollment

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrollment_date', 'active')
    search_fields = ('student__first_name', 'student__last_name', 'course__name')
    list_filter = ('active', 'enrollment_date')