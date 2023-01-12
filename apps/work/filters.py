import strawberry
from typing import Optional

from .models import Work


@strawberry.django.filters.filter(Work)
class WorkFilter:
    category: Optional[strawberry.ID]
    tag: Optional[strawberry.ID]
