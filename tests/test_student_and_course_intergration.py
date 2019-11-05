from django.test import TestCase

from student.models import Student

from course.models import Course

import datetime

class StudentCourseTestCase(TestCase):
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

        self.student_b = Student.objects.create(
            first_name = "Peter",
            last_name = "Kamau",
            date_of_birth = datetime.date(2007,4,7),
            gender = "male",
            registration_no  = "901",
            email = "kamaupeter@gmail.com",
            phone_number = "0720830673",
            date_joined = datetime.date.today(),
            )

        self.python = Course.objects.create(
            name="Python",
            duration_of_course=9,
            start_date=datetime.date.today(),
            end_date=datetime.date.today(),
            Description="backeneddeveloper",
            )

        self.javascript = Course.objects.create(
            name="JavaScript",
            duration_of_course=7,
            start_date=datetime.date.today(),
            end_date=datetime.date.today(),
            Description="fronteddeveloper",
            )

        self.design = Course.objects.create(
            name="Design",
            duration_of_course=5,
            start_date=datetime.date.today(),
            end_date=datetime.date.today(),
            Description="fronteddeveloper",
            )
        
    def test_student_can_join_a_course(self):
        self.student_a.courses.add(self.python)
        self.assertEqual(self.student_a.courses.count(),1)
        self.student_a.courses.add(self.javascript)
        self.assertEqual(self.student_a.courses.count(),2)
        self.student_a.courses.add(self.design)
        self.assertEqual(self.student_a.courses.count(),3)

    def test_student_can_join_many_courses(self):
        self.student_b.courses.add(self.python,self.javascript,self.design)
        self.assertEqual(self.student_b.courses.count(),3)
		