import strawberry
from strawberry import auto

from .models import Project
from gaatha.types import FileFieldType


@strawberry.django.type(Project)
class ProjectType:
    id: auto
    title: auto
    location: auto
    image: FileFieldType


@strawberry.django.type(Project, pagination=True)
class ProjectListType(ProjectType):
    pass
