from django.shortcuts import redirect
from django.shortcuts import render



from .forms import CourseForm

from .models import Course

from django.http import HttpResponse

def add_course(request):
	# form = CourseForm()
	# return render(request,"add_course.html",{"form":form})


	if request.method == "POST":
		form = CourseForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("list_courses")


		else:
			return HttpResponse("invalid data", status=400)

	else:
		form = CourseForm()

	return render(request,"add_course.html",{"form":form})



def list_courses(request):
	courses = Course.objects.all()

	return render(request,"all_courses.html",{"courses": courses})


def courses_details(request,pk):
	course = Course.objects.get(pk=pk)
	return render(request,"courses_details.html",{"course":course})


def edit_course(request,pk):
	course= Course.objects.get(pk=pk)
	if request.method == "POST":
		form = CourseForm(request.POST,instance = course)
		if form.is_valid:
			form.save()
			return redirect("list_courses")
	else:
		form = CourseForm(instance = course)

	return render(request,"edit_course.html",{"form":form})






 



