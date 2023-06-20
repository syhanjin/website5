# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-6-18 22:5                                                    =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : class_.py                                                         =
#    @Program: website5                                                        =
# ==============================================================================

# -*- coding: utf-8 -*-
from django.db import models
from rest_framework import serializers

from Blossom.conf import settings
from Blossom.models.class_ import Class, ClassMembership, ClassMembershipStudent, ClassMembershipTeacher


class ClassDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = Class.PUBLIC_FIELDS

    member_count = serializers.IntegerField(required=False)
    headteacher = settings.serializers.person_description()


class ClassDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = Class.DESCRIPTION_FIELDS

    member_count = serializers.IntegerField(required=False)
    headteacher = settings.serializers.person_description()


class ClassCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = Class.REQUIRED_FIELDS

    created = serializers.IntegerField(min_value=2000, max_value=2050)


# print(settings.models.person_teacher.objects.all())


class ClassSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = Class.EDITABLE_FIELDS

    headteacher = serializers.PrimaryKeyRelatedField(
        queryset=settings.models.person_teacher.objects, required=False, allow_null=True
    )
    description = serializers.CharField(required=False, allow_null=True, allow_blank=True)


# ClassMembership
class ClassMembershipDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassMembership
        fields = ["PERSON", "CLASS"]

    PERSON = settings.serializers.person_description()
    CLASS = settings.serializers.class_description()


class ClassMembershipDetailStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassMembershipStudent
        exclude = ["PERSON", "CLASS"]


class ClassMembershipDetailTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassMembershipTeacher
        exclude = ["PERSON", "CLASS"]


class ClassMembershipDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassMembership
        fields = "__all__"

    PERSON = settings.serializers.person_description()
    membership = serializers.SerializerMethodField()

    def get_membership(self, obj):
        role = obj.PERSON.role
        if role == settings.choices.role.student:
            return ClassMembershipDetailStudentSerializer(obj.membership_student).data
        if role == settings.choices.role.teacher:
            return ClassMembershipDetailTeacherSerializer(obj.membership_teacher).data


class ClassMembershipSetStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassMembershipStudent
        fields = ClassMembershipStudent.EDITABLE_FIELDS

    nickname = serializers.CharField(required=False, allow_null=False, allow_blank=True)
    position = serializers.CharField(required=False, allow_null=False, allow_blank=True)
    number = serializers.IntegerField(required=False, allow_null=True)


class ClassMembershipSetTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassMembershipTeacher
        fields = ClassMembershipTeacher.EDITABLE_FIELDS

    subject = serializers.CharField(required=False, allow_null=False, allow_blank=True)


class ClassMembershipCreateSerializer(serializers.Serializer):
    CLASS = serializers.PrimaryKeyRelatedField(queryset=settings.models.class_.objects)
    PERSON = serializers.PrimaryKeyRelatedField(queryset=settings.models.person.objects)

    def create(self, validated_data):
        model: models.Model = getattr(settings.models, f"class_membership_{validated_data['PERSON'].role.lower()}")
        obj = model.objects.create(**validated_data)
        return obj

    def update(self, instance, validated_data):
        pass
