# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-6-8 12:28                                                    =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : models.py                                                         =
#    @Program: website5                                                        =
# ==============================================================================
import uuid

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class AppManager(models.Manager): pass


class AppVersionManager(models.Manager): pass


class App(models.Model):
    class Meta:
        db_table = "app"
        indexes = [
            models.Index(fields=["name"]),
            # models.Index(fields=["description"])
        ]

    id = models.UUIDField("编号", primary_key=True, default=uuid.uuid4, editable=False, max_length=64)
    name = models.CharField("应用名称", max_length=64, unique=True)
    description = models.TextField("应用描述", max_length=5000)

    objects = AppManager()

    def __unicode__(self):
        return self.name


class AppVersion(models.Model):
    class Meta:
        db_table = "app_version"
        ordering = ['-released']

    id = models.UUIDField("编号", primary_key=True, default=uuid.uuid4, editable=False, max_length=64)
    app = models.ForeignKey(to=App, related_name='versions', on_delete=models.CASCADE)

    version_name = models.CharField("版本名称", max_length=64)
    version_code = models.PositiveIntegerField("版本号")
    updates = models.CharField("更新内容", max_length=5000)
    author = models.ForeignKey(User, verbose_name='发布者', null=True, on_delete=models.SET_NULL)
    released = models.DateTimeField("发布时间", auto_now_add=True, editable=False)
    installer = models.FileField("安装程序", upload_to="apps/")
    is_force = models.BooleanField("是否强制更新", default=False)

    REQUIRED_FIELDS = ['version_name', 'version_code', 'updates', 'installer', 'is_force']

    objects = AppVersionManager()

    def __unicode__(self):
        return self.version_name
