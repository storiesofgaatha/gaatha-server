import strawberry
from strawberry import auto
from strawberry.types import Info
import strawberry_django

from .models import Work, WorkImage, WorkCategory
from gaatha.types import FileFieldType
from .filters import WorkFilter


@strawberry_django.ordering.order(Work)
class WorkOrderType:
    order: auto


@strawberry.django.type(WorkCategory)
class WorkCategoryType:
    id: auto
    name: auto


@strawberry.django.type(WorkImage)
class WorkImageType:
    id: auto

    @strawberry.field
    async def image(self, info: Info) -> FileFieldType | None:
        return FileFieldType.resolve(self.image, info)


@strawberry.django.type(Work)
class WorkType:
    id: auto
    title: auto
    sub_title: auto
    description: auto
    area: auto
    status: auto
    duration: auto
    location: auto
    category: WorkCategoryType
    is_cover_image_dark: auto
    order: auto

    @strawberry.field
    async def art_work(self, info: Info) -> FileFieldType | None:
        return FileFieldType.resolve(self.art_work, info)

    @strawberry.field
    async def cover_image(self, info: Info) -> FileFieldType | None:
        return FileFieldType.resolve(self.cover_image, info)

    @strawberry.field
    async def images(self, info: Info) -> list[WorkImageType]:
        return await info.context["work_image_loader"].load(self.id)


@strawberry.django.type(Work, pagination=True, filters=WorkFilter)
class WorkListType(WorkType):
    pass


@strawberry.type
class FilterChoiceType:
    work_category: list[WorkCategoryType] | None
