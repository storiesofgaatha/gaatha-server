import strawberry
from strawberry import auto

from .models import People
from gaatha.types import FileFieldType


@strawberry.django.type(People)
class PeopleType:
    id: auto
    name: auto
    email: auto
    designation: auto
    qualification: auto
    is_current_employee: auto
    linkedin_url: auto
    instagram_url: auto
    profile_picture: FileFieldType
    art_work: FileFieldType


@strawberry.django.type(People, pagination=True)
class PeopleListType(PeopleType):
    pass
