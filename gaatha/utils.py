from strawberry.enum import EnumType


def get_enum_label(
    enum_type: EnumType,
    value: str,
    default_description="",
) -> str:
    if value:
        return enum_type(value).label
    return default_description
