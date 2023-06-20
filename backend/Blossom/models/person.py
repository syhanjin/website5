# -*- coding: utf-8 -*-

# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-6-18 22:6                                                    =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : person.py                                                         =
#    @Program: website5                                                        =
# ==============================================================================
from django.contrib.auth import get_user_model
from django.db import models
from imagekit.models import ProcessedImageField
from phonenumber_field.modelfields import PhoneNumberField
from pilkit.processors import SmartResize

from account.utils import create_uuid

User = get_user_model()


class GenderChoices(models.TextChoices):
    male = "male", "男"
    female = "female", "女"


class RoleChoices(models.TextChoices):
    student = "student", "学生"
    teacher = "teacher", "老师"


class Person(models.Model):
    """
    为了处理老师与学生模型的异同，打算采用继承
    模型基本不发生变化，但是在子类中拥有特别内容
    """
    # class Meta:
    #     abstract = True

    id = models.CharField("id", primary_key=True, default=create_uuid, editable=False, max_length=8)
    user = models.OneToOneField(User, related_name="blossom_person", on_delete=models.SET_NULL, null=True)
    name = models.CharField("姓名", max_length=256)
    gender = models.CharField("性别", max_length=16, choices=GenderChoices.choices)
    birthday = models.DateField("生日", null=True)
    role = models.CharField("角色", max_length=16, choices=RoleChoices.choices)

    # 联系方式
    phone = PhoneNumberField(verbose_name="手机号码", region="CN", null=True)
    email = models.EmailField(verbose_name="邮箱", null=True)
    QQ = models.CharField("QQ", max_length=12, null=True)
    WeChat = models.CharField("微信", max_length=64, null=True)

    # 图片和视频
    # 图片封面
    photo = ProcessedImageField(
        [SmartResize(192, 256)], format="JPEG", upload_to="blossom/photo", default="blossom/photo/default.jpg"
    )
    # 相册 > 图片向相册绑定 > 相册绑定资源 > Media模型

    # 班级
    CLASS = models.ManyToManyField(
        "Blossom.Class",
        through="Blossom.ClassMembership",
        through_fields=("PERSON", "CLASS")
    )

    CONTACTS = ["phone", "email", "QQ", "WeChat"]
    INFO = ["name", "gender", "birthday", "role", "photo"]

    DESCRIPTION_FIELDS = [
        "id", "name", "role", "gender", "user"
    ]

    PUBLIC_FIELDS = ["id", "user", "CLASS"] + CONTACTS + INFO

    REQUIRED_FIELDS = [
        "name", "role", "gender"
    ]
    EDITABLE_FIELDS = [
        "phone", "email", "QQ", "WeChat", "photo"
    ]

    ALL_FIELDS = "__all__"


class PersonStudent(Person):
    DESCRIPTION_FIELDS = []
    PUBLIC_FIELDS = []
    EDITABLE_FIELDS = []


class PersonTeacher(Person):
    subject = models.CharField("科目", max_length=16)
    DESCRIPTION_FIELDS = ["subject"]
    PUBLIC_FIELDS = ["subject"]
    EDITABLE_FIELDS = ["subject"]
