# -*- coding: utf-8 -*-
# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-6-17 18:2                                                    =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : class_.py                                                         =
#    @Program: website5                                                        =
# ==============================================================================

from django.db import models

from account.utils import create_uuid


class ClassTypeChoices(models.TextChoices):
    administrative = "administrative", "行政班级"
    walking = "walking", "走班班级"


class Class(models.Model):
    class Meta:
        ordering = ['-created', 'name']

    id = models.CharField("班级编号", default=create_uuid, primary_key=True, max_length=8)
    created = models.PositiveIntegerField("建班年份")
    year = models.PositiveIntegerField("")
    name = models.CharField("班级名称", max_length=256)
    type = models.CharField("班级类型", max_length=128, choices=ClassTypeChoices.choices)
    headteacher = models.ForeignKey(
        "Blossom.PersonTeacher", on_delete=models.SET_NULL, null=True, related_name="managed_classes",
        verbose_name="班主任"
    )
    description = models.TextField("班级描述")

    # 注意 count Field 需要在get_queryset中添加聚合
    PUBLIC_FIELDS = ["id", "created", "name", "type", "headteacher", "year", "member_count"]
    DESCRIPTION_FIELDS = ["id", "created", "name", "type", "headteacher", "year", "member_count"]
    REQUIRED_FIELDS = ["created", "name", "type"]
    EDITABLE_FIELDS = ["headteacher", "description"]


# 中间表

class ClassMembership(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['CLASS', 'PERSON'], name='class_membership')
        ]

    id = models.CharField("id", primary_key=True, default=create_uuid, editable=False, max_length=8)
    CLASS = models.ForeignKey(Class, related_name="membership", on_delete=models.CASCADE)
    PERSON = models.ForeignKey("Blossom.Person", related_name="membership", on_delete=models.CASCADE)
    REQUIRED_FIELDS = ["CLASS", "PERSON"]


class ClassMembershipStudent(ClassMembership):
    """
    Class-Person 学生中间表
    """
    membership_ptr = models.OneToOneField(
        ClassMembership, on_delete=models.CASCADE,
        related_name="membership_student",
        parent_link=True, primary_key=True,
    )
    nickname = models.TextField("外号", max_length=2048)
    position = models.TextField("职位", max_length=1024)
    number = models.PositiveIntegerField("学号", null=True)

    joined = models.DateTimeField("加入时间", null=True, default=None)
    exited = models.DateTimeField("离开时间", null=True, default=None)

    EDITABLE_FIELDS = ["nickname", "position", "number"]


class ClassMembershipTeacher(ClassMembership):
    """
    Class-Person 老师中间表
    """
    membership_ptr = models.OneToOneField(
        ClassMembership, on_delete=models.CASCADE,
        related_name="membership_teacher",
        parent_link=True, primary_key=True,
    )

    EDITABLE_FIELDS = []
