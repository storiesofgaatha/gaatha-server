import strawberry
from .models import Work

CategoryEnum = strawberry.enum(Work.Category, name="CategoryEnum")
TagEnum = strawberry.enum(Work.Tag, name="TagEnum")
