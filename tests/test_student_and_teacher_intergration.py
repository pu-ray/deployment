from django.test import TestCase

from student.models import Student

from teacher.models import Teacher

import datetime

class StudentTeacherTestCase(TestCase):
    def setUp(self):
        self.student_a = Student.objects.create(
            id="34678900",
            first_name = "Emmah",
            last_name = "Wanjiru",
            date_of_birth = datetime.date(1998,6,9),
            gender = "female",
            registration_no  = "9893",
            email = "emmahmbugua@gmail.com",
            phone_number = "0790773408",
            date_joined = datetime.date.today(),
            )

        self.teacher_a = Teacher.objects.create(
            first_name = "Jeff",
            last_name = "Mwangi",
            gender = "male",
            e_mail = "mwangijeff@gmail.com",
            phone_number = "0745890760",
            proffessional="Web designer",
            subject="Web design",
            id_number="756890435",
            date_joined = datetime.date.today(),
            )

        self.teacher_b = Teacher.objects.create(
            first_name = "James",
            last_name = "Mwai",
            gender = "male",
            e_mail = "mwaijames@gmail.com",
            phone_number = "0734567098",
            proffessional="Developer",
            subject="Python",
            id_number="756890435",
            date_joined = datetime.date.today(),
            )

    