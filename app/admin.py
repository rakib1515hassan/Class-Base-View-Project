from django.contrib import admin
from .models import *

# Register your models here.
#admin.site.register(Student)
@admin.register(Student)
class student_admin(admin.ModelAdmin):
    list_display = ("name", "roll", "course")


@admin.register(Teacher)
class Teacher_admin(admin.ModelAdmin):
    list_display = ("name", "teaching")
