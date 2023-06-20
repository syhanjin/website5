# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-6-18 15:44                                                   =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : models.py                                                         =
#    @Program: website5                                                        =
# ==============================================================================
from django.core.validators import FileExtensionValidator
from django.db import models


class MediaTypeChoices(models.TextChoices):
    image = 'mediaimage', '图片',
    video = 'mediavideo', '视频'


class Media(models.Model):
    class Meta:
        db_table = "media"
        ordering = ['-created']

    created = models.DateTimeField(auto_now_add=True, editable=False)
    type = models.CharField("类型", max_length=16)

    def __unicode__(self):
        return str(self.created)


class MediaImage(Media):
    class Meta:
        db_table = "media_image"

    image = models.ImageField(upload_to="images")

    @property
    def url(self):
        return self.image.url


class MediaVideo(Media):
    class Meta:
        db_table = "media_video"

    video = models.FileField(upload_to="videos", validators=[FileExtensionValidator(allowed_extensions=['video/*'])])

    @property
    def url(self):
        return self.video.url
