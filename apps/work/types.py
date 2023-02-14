import strawberry
from strawberry import auto
from strawberry.types import Info

from .models import Work, WorkImage, WorkTag, WorkCategory
from gaatha.types import FileFieldType
from .filters import WorkFilter


@strawberry.django.type(WorkTag)
class WorkTagType:
    id: auto
    name: auto


@strawberry.django.type(WorkCategory)
class WorkCategoryType:
    id: auto
    name: auto


@strawberry.django.type(WorkImage)
class WorkImageType:
    id: auto
    image: FileFieldType


@strawberry.django.type(Work)
class WorkType:
    id: auto
    title: auto
    description: auto
    area: auto
    status: auto
    duration: auto
    location: auto
    category: WorkCategoryType
    tag: WorkTagType
    is_cover_image_dark: auto

    art_work: FileFieldType
    cover_image: FileFieldType

    @strawberry.field
    async def images(self, info: Info) -> list[WorkImageType]:
        return await info.context["work_image_loader"].load(self.id)


@strawberry.django.type(Work, pagination=True, filters=WorkFilter)
class WorkListType(WorkType):
    pass


@strawberry.type
class FilterChoiceType:
    work_category: list[WorkCategoryType] | None
    work_tag: list[WorkTagType] | None
