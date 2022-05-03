from django.db import models
from django.utils.html import mark_safe
from django.core.files.storage import get_storage_class
from django_extensions.db.models import TimeStampedModel

media_storage = get_storage_class()()


class Record(TimeStampedModel):
    photo = models.ImageField(upload_to="docs")

    def photo_tag(self):
        return mark_safe(
            '<img src="%s" width="600" />'
            % (media_storage.url(name=self.photo.file.name))
        )

    photo_tag.short_description = "My uploaded photo"
