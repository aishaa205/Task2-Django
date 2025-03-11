from django.contrib import admin
from .models import Classroom, Course, School, Exam

admin.site.register(Classroom)
admin.site.register(School)
admin.site.register(Course)
admin.site.register(Exam)