import strawberry
from typing import List, Optional
from strawberry import auto
from strawberry.types import Info

from utils import build_url
from .models import Work, WorkImage
from gaatha.types import FileFieldType
from .filters import WorkFilter


@strawberry.django.type(WorkImage)
class WorkImageType:
    id: auto

    @strawberry.field
    async def image(self, info: Info) -> Optional[FileFieldType]:
        return build_url(self.image, info.context['request'])


@strawberry.django.type(Work)
class WorkType:
    id: auto
    title: auto
    description: auto
    area: auto
    category: auto
    status: auto
    tag: auto
    duration: auto
    location: auto

    @strawberry.field
    async def art_work(self, info: Info) -> Optional[FileFieldType]:
        result = await info.context["work_art_work_loader"].load(self.id)
        return build_url(result, info.context['request'])

    @strawberry.field
    async def cover_image(self, info: Info) -> Optional[FileFieldType]:
        result = await info.context["work_cover_image_loader"].load(self.id)
        return build_url(result, info.context['request'])

    @strawberry.field
    async def images(self, info: Info) -> List[WorkImageType]:
        return await info.context["work_image_loader"].load(self.id)


@strawberry.django.type(Work, pagination=True, filters=WorkFilter)
class WorkListType(WorkType):
    pass
