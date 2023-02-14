from django.db import models
from django.utils.translation import gettext_lazy as _


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    location = models.CharField(max_length=500, verbose_name=_('Location'))
    image = models.FileField(null=True, blank=True, upload_to="project/images")

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self):
        return self.title
