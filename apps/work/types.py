import strawberry
from strawberry import auto
from strawberry.types import Info

from utils import build_url
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

    @strawberry.field
    async def image(self, info: Info) -> FileFieldType | None:
        return build_url(self.image, info.context['request'])


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

    @strawberry.field
    async def art_work(self, info: Info) -> FileFieldType | None:
        return build_url(self.art_work, info.context['request'])

    @strawberry.field
    async def cover_image(self, info: Info) -> FileFieldType | None:
        return build_url(self.cover_image, info.context['request'])

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
