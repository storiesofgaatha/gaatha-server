import strawberry
from asgiref.sync import sync_to_async

from apps.work.types import WorkType, WorkListType
from apps.work.models import (
    WorkCategory,
    WorkTag
)
from apps.work.types import (
    FilterChoiceType,
    WorkCategoryType,
    WorkTagType,
)
from apps.people.types import PeopleListType


@sync_to_async
def get_work_filter_options() -> FilterChoiceType:
    return FilterChoiceType(
        work_category=[
            WorkCategoryType(
                id=id,
                name=name
            ) for id, name in WorkCategory.objects.values_list('id', 'name')
        ],
        work_tag=[
            WorkTagType(
                id=id,
                name=name
            ) for id, name in WorkTag.objects.values_list('id', 'name')
        ]
    )


@strawberry.type
class Query():
    works: list[WorkListType] = strawberry.django.field()
    work: WorkType = strawberry.django.field()
    people: list[PeopleListType] = strawberry.django.field()

    @strawberry.field
    async def filter_choices(self) -> FilterChoiceType:
        return await get_work_filter_options()


schema = strawberry.Schema(query=Query)
