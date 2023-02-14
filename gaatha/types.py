import strawberry
from strawberry.types import Info

from django.db import models


@strawberry.type
class FileFieldType:

    @strawberry.field
    async def name(self: models.FileField | None) -> str | None:
        if self:
            return self.name

    @strawberry.field
    async def url(self: models.FileField | None, info: Info) -> str | None:
        if self:
            return info.context['request'].build_absolute_uri(self.url)

    @strawberry.field
    async def exists(self: models.FileField | None) -> bool:
        return not not self
