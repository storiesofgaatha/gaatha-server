from factory import fuzzy
from factory.django import DjangoModelFactory
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import (
    Project
)


class ProjectFactory(DjangoModelFactory):
    title = fuzzy.FuzzyText(length=15)
    location = fuzzy.FuzzyText(length=50)
    image = SimpleUploadedFile('test.jpg', b'whatevercontentsyouwant')

    class Meta:
        model = Project
