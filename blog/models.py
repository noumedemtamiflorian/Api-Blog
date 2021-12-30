from django.db.models import *
from django.utils.text import slugify


class Category(Model):
    name = CharField(max_length=255, unique=True)
    slug = SlugField(max_length=255, unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
