from django.db import models
from django.contrib.auth.models import AbstractUser # abstractuser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Name")) # language pov va mov fayl ochishi uchun
    sub_title = models.CharField(max_length=200, null=True, blank=True, verbose_name=_("sub_title"))
    author = models.CharField(max_length=100, verbose_name=_("author"))
    publication_date = models.DateField(null=True, blank=True, verbose_name=_("publication_date"))
    description = models.TextField(null=True, blank=True, verbose_name=_("description"))

    def __str__(self):
        return self.title