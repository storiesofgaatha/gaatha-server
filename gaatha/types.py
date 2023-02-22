from __future__ import annotations
import strawberry
from strawberry.types import Info

from django.db import models


@strawberry.type
class FileFieldType:
    name: str
    url: str

    @staticmethod
    def resolve(file: models.FileField, info: Info) -> FileFieldType | None:
        if file:
            return FileFieldType(
                name=file.name,
                url=info.context['request'].build_absolute_uri(file.url),
            )
