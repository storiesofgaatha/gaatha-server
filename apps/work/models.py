
from django.utils.translation import gettext_lazy as _
from django.db import models


# Create your models here.
class Work(models.Model):
    class Category(models.TextChoices):
        RESIDENTAL = 'residental', _('Residental')
        CIVIC = 'civic', _('Civic')
        LANDSCAPE = 'landscape', _('Landscape')
        RESEARCH = 'research', _('Research')

    class Tag(models.TextChoices):
        ARCHITECTURE = 'architecture', _('Architecture')
        INTERIOR = 'interior', _('Interior')
        GRAPHICS = 'graphics', _('Graphics')
        VISUALIZATION = 'visualization', _('Visualization')
        EXIBITION = 'exibition', _('Exibition')

    title = models.CharField(max_length=255)
    description = models.TextField(
        blank=True,
        verbose_name=_('Description')
    )
    art_work = models.FileField(null=True, blank=True, upload_to="art_works")
    cover_image = models.ImageField(
        null=True,
        blank=True,
        upload_to="cover_images",
        verbose_name=_('Cover image')
    )
    area = models.CharField(max_length=50, blank=True)
    category = models.CharField(
        max_length=50, verbose_name=_('Category'), choices=Category.choices
    )
    status = models.CharField(max_length=250, verbose_name=_('Status'))
    tag = models.CharField(
        max_length=50, verbose_name=_('Tag'), choices=Tag.choices
    )
    duration = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=500, blank=True)

    class Meta:
        verbose_name = "Work"
        verbose_name_plural = "Works"

    def __str__(self):
        return str(self.id)


class WorkImage(models.Model):
    work = models.ForeignKey(
        Work,
        on_delete=models.CASCADE,
        related_name='workimage_work',
        verbose_name=_('Work'),
        null=True,
        blank=True,
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to="workimage_image",
        verbose_name=_('Image')
    )

    def __str__(self):
        return str(self.work.id)


class People(models.Model):
    name = models.CharField(max_length=250, verbose_name=_('Name'))
    profile_picture = models.ImageField(
        null=True,
        blank=True,
        upload_to="profile_pictures",
        verbose_name=_("Profile Picture")
    )
    art_work = models.FileField(
        null=True,
        blank=True,
        upload_to="art_works",
        verbose_name=_("Art Work")
    )
    email = models.EmailField(max_length=250, verbose_name=_('Email'))
    designation = models.CharField(
        max_length=100, blank=True, verbose_name=_("Designation")
    )
    qualification = models.CharField(
        max_length=250, blank=True, verbose_name=_("Qualification")
    )
    is_current_employee = models.BooleanField(default=True)
    linked_in_url = models.CharField(
        max_length=500, verbose_name=_("LinkedIn"), blank=True
    )
    instagram_url = models.CharField(
        max_length=500, verbose_name=_('Instagram'), blank=True
    )

    class Meta:
        verbose_name = _("People")
        verbose_name_plural = _("People")

    def __str__(self):
        return str(self.name)
