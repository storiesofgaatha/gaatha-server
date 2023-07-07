from __future__ import annotations
import strawberry
from strawberry.types import Info
from typing import Optional

from django.db import models


@strawberry.type
class FileFieldType:
    name: str
    url: str
    width: Optional[int]
    height: Optional[int]

    @staticmethod
    def resolve(file: models.FileField, info: Info) -> FileFieldType | None:
        width = None
        height = None
# TODO file width, height calculation is a heavy operation so it should be saved in the database in future.
        if hasattr(file, 'width'):
            width = file.width
        if hasattr(file, 'height'):
            height = file.height
        if file:
            return FileFieldType(
                name=file.name,
                url=info.context['request'].build_absolute_uri(file.url),
                # TODO file width ,height calculation is a heavy operation so it should be saved in database in furute.
                width=width,
                height=height
            )
