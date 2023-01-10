from django.contrib import admin

from .models import Work, WorkImage
from .forms import WorkForm


class WorkImageInline(admin.TabularInline):
    model = WorkImage
    extra = 1


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    form = WorkForm
    list_display = [
        'title',
        'status',
        'duration',
    ]

    inlines = [
        WorkImageInline,
    ]
