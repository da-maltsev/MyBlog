from django.db import models

from core.models import BaseModel


class Tag(BaseModel):
    ...


class Post(BaseModel):
    slug = models.SlugField(max_length=20, unique=True,
                            db_index=True, verbose_name='URL')
    body = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='posts', through='TagPost')


class TagPost(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
