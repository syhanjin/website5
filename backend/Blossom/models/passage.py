# -*- coding: utf-8 -*-

# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-6-9 23:7                                                     =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : passage.py                                                        =
#    @Program: website5                                                        =
# ==============================================================================

from django.db import models


class Passage(models.Model):
    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=["title"])
        ]

    # id = models.UUIDField("文章编号", primary_key=True, default=uuid.uuid4, editable=False, max_length=64)
    title = models.CharField("标题", max_length=512)
    content = models.TextField("内容", max_length=50000)
    created = models.DateTimeField("发布时间", auto_now_add=True)
    updated = models.DateTimeField("更新时间", auto_now=True)
    author = models.ForeignKey("Blossom.Person", related_name="passages", on_delete=models.CASCADE)


class PassageToPerson(Passage):
    to = models.ManyToManyField("Blossom.Person")


class PassageToClass(Passage):
    to = models.ManyToManyField("Blossom.Class")
