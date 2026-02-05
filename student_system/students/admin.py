from django.contrib import admin
from .models import Students

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'mobile')
    search_fields = ('full_name', 'email', 'mobile')

