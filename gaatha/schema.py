# schema.py
import strawberry
from typing import List
from asgiref.sync import sync_to_async
from apps.work.types import WorkType, WorkListType
from apps.work.models import Work
from gaatha.enums import GenericEnumValue
from apps.work.types import WorkFilterChoiceType


@sync_to_async
def get_work_filter_options() -> WorkFilterChoiceType:
    return WorkFilterChoiceType(
        category=[
            GenericEnumValue(
                name=Work.Category(category).name,
                label=Work.Category(category).label
            ) for category in Work.Category
        ],
        tag=[
            GenericEnumValue(
                name=Work.Tag(tag).name,
                label=Work.Tag(tag).label
            ) for tag in Work.Tag
        ],
    )


@strawberry.type
class Query():
    works: List[WorkListType] = strawberry.django.field()
    work: WorkType = strawberry.django.field()

    @strawberry.field
    async def work_filter_choices(self) -> WorkFilterChoiceType:
        options = await get_work_filter_options()
        return options


schema = strawberry.Schema(query=Query)
