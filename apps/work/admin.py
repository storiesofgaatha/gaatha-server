from django.contrib import admin

from .models import Work, WorkImage, People
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


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'designation',
        'email',
        'is_current_employee',
    ]
