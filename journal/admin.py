from django.contrib import admin
from .models import Student, Subjects, Class

# Register your models here.
admin.site.register(Student)
admin.site.register(Subjects)
admin.site.register(Class)
