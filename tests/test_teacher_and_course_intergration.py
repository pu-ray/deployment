from django.test import TestCase

from teacher.models import Teacher

from course.models import Course

import datetime

class TeacherCourseTestCase(TestCase):
    def setUp(self):
            self.teacher_a = Teacher.objects.create(
            first_name = "James",
            last_name = "Mwai",
            gender = "male",
            phone_number = "0745890760",
            proffessional="Software Developer",
            subject="Python",
            id_number="756890435",
            date_joined = datetime.date.today(),
            )
            
            self.teacher_b = Teacher.objects.create(
            first_name = "Jeff",
            last_name = "Mwangi",
            gender = "male",
            phone_number = "0745890760",
            proffessional="Designer",
            subject="Python",
            id_number="756890435",
            date_joined = datetime.date.today(),
            )

            self.python = Course.objects.create(
            name="Python",
            duration_of_course=9,
            start_date=datetime.date.today(),
            end_date=datetime.date.today(),
            Description="backeneddevelopement",
            )

            self.java = Course.objects.create(
            name="Java",
            duration_of_course=7,
            start_date=datetime.date.today(),
            end_date=datetime.date.today(),
            Description="backeneddevelopement",
            )


            self.javascript = Course.objects.create(
            name="JavaScript",
            duration_of_course=7,
            start_date=datetime.date.today(),
            end_date=datetime.date.today(),
            Description="fronteddevelopement",
            )

            self.design = Course.objects.create(
            name="Design",
            duration_of_course=5,
            start_date=datetime.date.today(),
            end_date=datetime.date.today(),
            Description="fronteddevelopement",
            )

    def test_course_can_be_trained_by_a_teacher(self):
       self.python.teacher = self.teacher_a
       self.assertEqual(self.python.teacher, self.teacher_a)

    def test_many_courses_can_be_trained_by_one_teacher(self):
       self.python.teacher = self.teacher_b
       self.javascript.teacher = self.teacher_b
       self.assertEqual(self.javascript.teacher,self.python.teacher)
