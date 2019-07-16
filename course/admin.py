from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
	list_display = ("start_date","name","end_date","Description")
	search_fields = ("start_date","name","end_date")

admin.site.register(Course,CourseAdmin)
