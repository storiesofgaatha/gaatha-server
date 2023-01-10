# schema.py
import strawberry
from typing import List
from apps.work.types import WorkType, WorkListType


@strawberry.type
class Query():
    works: List[WorkListType] = strawberry.django.field()
    work: WorkType = strawberry.django.field()


schema = strawberry.Schema(query=Query)
