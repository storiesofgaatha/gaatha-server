from django.contrib import admin

from .models import Work, WorkImage, WorkCategory
from .forms import WorkForm


class WorkImageInline(admin.TabularInline):
    model = WorkImage
    extra = 1


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    form = WorkForm
    list_display = [
        'title',
        'work_type',
        'status',
        'category',
        'status',
        'duration',
        'order',
    ]

    inlines = [
        WorkImageInline,
    ]


@admin.register(WorkCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]
