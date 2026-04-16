import strawberry

from .enums import WorkTypeEnum
from .models import Work


@strawberry.django.filters.filter(Work)
class WorkFilter:
    category: strawberry.ID | None
    work_type: WorkTypeEnum | None
