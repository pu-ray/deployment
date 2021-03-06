from django.urls import path,include

from .views import add_course,list_courses,courses_details,edit_course

urlpatterns = [path("add/",add_course, name = "add_course"),

               path("list/",list_courses, name ="list_courses"),

               path("view/<int:pk>/",  courses_details, name="courses_details"),

			   path("edit/<int:pk>/",  edit_course, name="edit_course"),

			   ]