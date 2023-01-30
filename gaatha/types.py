import strawberry


@strawberry.type
class FileFieldType:
    name: str
    url: str

    def resolve_file(self):
        return FileFieldType(name=self.name, url=self.url)
