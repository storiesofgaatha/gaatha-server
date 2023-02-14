import factory
from factory import fuzzy
from factory.django import DjangoModelFactory
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import (
    Work,
    WorkTag,
    WorkCategory,
    WorkImage,
)


class WorkCategoryFactory(DjangoModelFactory):
    name = fuzzy.FuzzyText(length=15)

    class Meta:
        model = WorkCategory


class WorkTagFactory(DjangoModelFactory):
    name = fuzzy.FuzzyText(length=15)

    class Meta:
        model = WorkTag


class WorkFactory(DjangoModelFactory):
    category = factory.SubFactory(WorkCategoryFactory)
    tag = factory.SubFactory(WorkTagFactory)
    cover_image = SimpleUploadedFile('test.jpg', b'whatevercontentsyouwant')
    art_work = SimpleUploadedFile('test.jpg', b'whatevercontentsyouwant')
    title = fuzzy.FuzzyText(length=15)
    description = fuzzy.FuzzyText(length=50)
    area = fuzzy.FuzzyText(length=50)
    status = fuzzy.FuzzyText(length=50)
    duration = fuzzy.FuzzyText(length=50)
    location = fuzzy.FuzzyText(length=50)
    is_cover_image_dark = True

    class Meta:
        model = Work


class WorkImageFactory(DjangoModelFactory):
    work = factory.SubFactory(WorkFactory)
    image = SimpleUploadedFile('test.jpg', b'whatevercontentsyouwant')

    class Meta:
        model = WorkImage
