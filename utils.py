from gaatha.types import FileFieldType


def build_url(file, request) -> FileFieldType | None:
    if file:
        url = request.build_absolute_uri(file.url)
        return FileFieldType(name=file.name, url=url).resolve_file()
    return None
