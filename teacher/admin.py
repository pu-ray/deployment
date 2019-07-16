from django.contrib import admin
from .models import Teacher

class TeacherAdmin(admin.ModelAdmin):
	list_display = ("phone_number","first_name","last_name","date_joined","e_mail","image")
	search_fields = ("phone_number","first_name","last_name","e_mail","image")

admin.site.register (Teacher,TeacherAdmin)
