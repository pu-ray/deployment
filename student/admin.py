from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
	list_display = ("registration_no","first_name","last_name","date_of_birth","email","image")
	search_fields = ("registration_no","first_name","last_name","email","image")

admin.site.register(Student,StudentAdmin)

# Register your models here.
