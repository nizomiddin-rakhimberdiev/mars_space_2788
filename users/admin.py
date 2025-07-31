from django.contrib import admin
from .models import Teacher, Group, Student, Course
# Register your models here.
admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Course)
