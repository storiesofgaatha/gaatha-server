import strawberry
from strawberry import auto
from strawberry.types import Info

from utils import build_url
from .models import Project
from gaatha.types import FileFieldType


@strawberry.django.type(Project)
class ProjectType:
    id: auto
    title: auto
    location: auto

    @strawberry.field
    async def image(self, info: Info) -> FileFieldType | None:
        return build_url(self.image, info.context['request'])


@strawberry.django.type(Project, pagination=True)
class ProjectListType(ProjectType):
    pass
