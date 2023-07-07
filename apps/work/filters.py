import strawberry
from typing import Optional

from .models import Work
from .enums import WorkTypeEnum


@strawberry.django.filters.filter(Work)
class WorkFilter:
    category: Optional[strawberry.ID]
    work_type: Optional[WorkTypeEnum]
