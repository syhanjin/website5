# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-6-9 22:56                                                    =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : models.py                                                         =
#    @Program: website5                                                        =
# ==============================================================================
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill

from account.utils import create_uuid


class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        """
        创建用户
        """
        if not email:
            raise ValueError('用户必须拥有邮件地址')
        if not name:
            raise ValueError('用户必须拥有用户名')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """
        创建并保存超级用户
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.admin = 1
        user.save(using=self._db)
        return user


class AdminChoices(models.IntegerChoices):
    USER = 0, '普通用户'
    NORMAL = 1, '管理员'

    SUPER = 5, '超级管理员'
    DEVELOPER = 10, '开发者'


class User(AbstractBaseUser, PermissionsMixin, models.Model):
    class Meta:
        db_table = "account"
        indexes = [
            models.Index(fields=['uuid', 'name', '-created']),
        ]

    email = models.EmailField(
        verbose_name='邮箱',
        max_length=255,
        unique=True,
    )
    uuid = models.CharField("用户id", primary_key=True, default=create_uuid, editable=False, max_length=8)
    created = models.DateTimeField("创建时间", auto_now_add=True, editable=False)
    name = models.CharField("用户名", max_length=32, unique=True)
    signature = models.CharField("个性签名", max_length=256, default="")
    is_active = models.BooleanField("是否激活", default=True)
    admin = models.PositiveSmallIntegerField(
        "管理员级别", choices=AdminChoices.choices, default=AdminChoices.USER
    )
    avatar = ProcessedImageField(
        verbose_name="头像", default='avatar/default.jpg', upload_to='avatar',
        processors=[ResizeToFill(128, 128)], format='JPEG',
        options={'quality': 80}
    )

    objects = UserProfileManager()
    DESCRIPTION_FIELDS = ["uuid", "name", "admin"]
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email']
    PUBLIC_FIELDS = ['uuid', 'name', 'avatar', 'signature', 'admin']
    PRIVATE_FIELDS = ['email', 'created']
    ALL_FIELDS = PUBLIC_FIELDS + PRIVATE_FIELDS

    def __str__(self):
        return self.name

    def get_avatar_url(self):
        return settings.MEDIA_URL + str(self.avatar)
