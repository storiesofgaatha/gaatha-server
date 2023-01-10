import strawberry
from typing import Optional, List

from .models import Work
from .enums import CategoryEnum, TagEnum


@strawberry.django.filters.filter(Work)
class WorkFilter:
    status: Optional[str]
    category: List[CategoryEnum] | None
    tag: List[TagEnum] | None

    def filter_category(self, queryset):
        if not self.category:
            return queryset
        return queryset.filter(category__in=self.category)

    def filter_tag(self, queryset):
        if not self.tag:
            return queryset
        return queryset.filter(tag__in=self.tag)
