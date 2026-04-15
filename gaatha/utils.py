from strawberry.enum import EnumType
from django.db.models.fields.files import FileField, ImageField
from uuid import uuid4


def get_enum_label(
    enum_type: EnumType,
    value: str,
    default_description='',
) -> str:
    if value:
        return enum_type(value).label
    return default_description


class SecureFileField(FileField):
    def generate_filename(self, instance, filename):
        """
        Overwrites https://github.com/django/django/blob/main/django/db/models/fields/files.py#L345
        """
        # Append uuid4 path to the filename
        filename = f"{uuid4().hex}/{filename}"
        return super().generate_filename(instance, filename)


class SecureImageField(ImageField):
    def generate_filename(self, instance, filename):
        filename = f"{uuid4().hex}/{filename}"
        return super().generate_filename(instance, filename)