import strawberry
from strawberry import auto
from strawberry.types import Info
import strawberry_django

from .models import People
from gaatha.types import FileFieldType


@strawberry_django.ordering.order(People)
class PeopleOrderType:
    order: auto


@strawberry.django.type(People)
class PeopleType:
    id: auto
    name: auto
    email: auto
    designation: auto
    qualification: auto
    is_current_employee: auto
    is_founder: auto
    linkedin_url: auto
    instagram_url: auto
    order: auto

    @strawberry.field
    async def profile_picture(self, info: Info) -> FileFieldType | None:
        return FileFieldType.resolve(self.profile_picture, info)

    @strawberry.field
    async def art_work(self, info: Info) -> FileFieldType | None:
        return FileFieldType.resolve(self.art_work, info)


@strawberry.django.type(People, pagination=True)
class PeopleListType(PeopleType):
    pass
