from django.contrib import admin

# Register your models here.

from .models import *


@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'department', 'attendance_status')
    list_filter = ('department', 'attendance_status')
    search_fields = ('name', 'department')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(AttendanceStatus)
class AttendanceStatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
