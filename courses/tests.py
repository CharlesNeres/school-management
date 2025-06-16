from django.test import TestCase
from datetime import date

from users.models import Teacher
from .models import Course
# Create your tests here.
class CourseModelTest(TestCase):
    def test_create_course(self):
        teacher = Teacher.objects.create(
            first_name="Alice",
            last_name="Smith",
            email="alice@example.com",
            hire_date=date(2025, 9, 30)
        )

        course = Course.objects.create(
            name="Introduction to Python",
            description="Learn the basics of Python programming.",
            start_date=date(2025, 7, 1),
            end_date=date(2025, 9, 30),
            teacher=teacher
        )

        self.assertEqual(course.name, "Introduction to Python")
        self.assertEqual(course.description, "Learn the basics of Python programming.")
        self.assertEqual(course.start_date, date(2025, 7, 1))
        self.assertEqual(course.end_date, date(2025, 9, 30))
        self.assertEqual(course.teacher, teacher)