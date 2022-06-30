from django.db import models

from client.models import User
from gag.helpers import UploadTo
from gag.mixins import TranslateMixin
from django.utils.translation import gettext_lazy as _


class Category(TranslateMixin, models.Model):
    translate_fields = ['name']

    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)
    image = models.ImageField(upload_to=UploadTo('category'))


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, verbose_name=_('Kategoriya'))
    comment = models.TextField(verbose_name=_("Izoh"))
    file = models.FileField(verbose_name=_("Rasm/Video"), upload_to=UploadTo('post'))
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.RESTRICT)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    comment = models.TextField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', null=True, default=None, on_delete=models.CASCADE)

