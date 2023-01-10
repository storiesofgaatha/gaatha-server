from django.contrib import admin

from .models import Work, WorkImage
# Register your models here.


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'status',
        'duration',
    ]


@admin.register(WorkImage)
class WorkImageAdmin(admin.ModelAdmin):
    list_display = [
        'id',
    ]
