from django.contrib import admin

# Register your models here.
from .models import Teacher, Student


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth')
    fields = ['first_name', 'last_name', ('date_of_birth')]
#admin.site.register(Teacher)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student)