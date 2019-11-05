from django.test import TestCase

from .models import Teacher

from teacher.forms import TeacherForm

from django.core.validators import BaseValidator

import datetime

from django.test import Client

from django.urls import reverse

class AddTeacherTestCase(TestCase):

    def setUp(self):

        self.data = {"first_name": "Purity",
                     "last_name": "Mbugua",
                     "gender": "Female",
                     "registration_no":  "1234",
                     "email" : "mbuguapurity1@mail.com",
                     "phone_number" :'254723736296',
                     "date_joined" : datetime.date.today(), 

                     
                     }

        self.bad_data = {"first_name": "Purity",
                         "last_name": "Mbugua",
                         "gender": "Female",
                         "registration_no":  "1234",
                         "email" : "mbuguapurity",
                         "phone_number" :'254723736296',
                         "date_joined" : datetime.date.today(), 
                     
                    }

    def test_teacher_form_accepts_valid_data(self):
        form = TeacherForm(self.data)
        self.assertFalse(form.is_valid())

    def test_teacher_from_rejects_invalid_data(self):
        form = TeacherForm(self.bad_data)
        self.assertFalse(form.is_valid())


    def test_add_teacher_view_invalid_data(self):
        client = Client()
        url = reverse ("add_teacher")
        response = client.post(url,self.data)
        self.assertTrue(response.status_code,200)


    def test_add_teacher_view(self):
        client = Client()
        url = reverse ("add_teacher")
        response = client.post(url,self.bad_data)
        self.assertEqual(response.status_code,400)

 
