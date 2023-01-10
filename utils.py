from gaatha.types import FileFieldType


def build_url(file, request):
    if type(file) == list:
        file = file[0]
    file_name = file.name
    url = ''
    if file_name:
        url = request.build_absolute_uri(file.url)
        return FileFieldType(name=file_name, url=url).resolve_file()
    return None
