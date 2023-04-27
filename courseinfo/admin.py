from django.contrib import admin
from .models import Section, Student, Semester, Course, Instructor, Registration, Year, Period


admin.site.register(Period)
admin.site.register(Section)
admin.site.register(Student)
admin.site.register(Semester)
admin.site.register(Instructor)
admin.site.register(Registration)
admin.site.register(Year)
admin.site.register(Course)
