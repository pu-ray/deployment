from django.test import TestCase

from .models import Course

from course.forms import CourseForm

from django.core.validators import BaseValidator

import datetime

from .models import Course

from django.test import Client


from django.urls import reverse




class AddCourseTestCase(TestCase):

    def setUp(self):

        self.data = {"name": "Hospitality",
                     "duration_of_course" : datetime.date.today(),
                     "start_date" : datetime.date.today(),
                     "end_date": datetime.date.today(),
                     "Description": "In this course we offer full time and part time courses",
                     
                     }

        self.bad_data = {"name": "Hospitality",
                         "duration_of_course" : datetime.date.today(),
                         "start_date" : datetime.date.today(),
                         "end_date": "datetime.date.today()",
                          "Description": "In this course we offer full time and part time courses",

                     }

    def test_course_form_accepts_valid_data(self):
        form = CourseForm(self.data)
        self.assertFalse(form.is_valid())

    def test_course_from_rejects_invalid_data(self):
        form = CourseForm(self.bad_data)
        self.assertFalse(form.is_valid())

    def test_add_course_view(self):
        client = Client()
        url = reverse ("add_course")
        response = client.post(url,self.data)
        self.assertTrue(response.status_code,200)


    def test_add_course_view_invalid_data(self):
        client = Client()
        url = reverse ("add_course")
        response = client.post(url,self.bad_data)
        self.assertEqual(response.status_code,400)

 

