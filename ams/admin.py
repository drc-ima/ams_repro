from django.contrib import admin

# Register your models here.
from easy_select2 import select2_modelform

from ams import models

admin.site.register(models.Hardware)
admin.site.register(models.Software)
admin.site.register(models.Information)
admin.site.register(models.Infrastructure)
admin.site.register(models.Staff)
admin.site.register(models.DepartmentLead)
admin.site.register(models.Department)
admin.site.register(models.Assign)
admin.site.register(models.Owner)

AssignForm = select2_modelform(models.Assign, attrs={'width': '250px'})


class AssignAdmin(admin.ModelAdmin):
    form = AssignForm
