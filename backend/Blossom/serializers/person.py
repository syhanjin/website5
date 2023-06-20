# -*- coding: utf-8 -*-

# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-6-20 12:47                                                   =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : person.py                                                         =
#    @Program: website5                                                        =
# ==============================================================================
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from Blossom.conf import settings
from Blossom.models.person import Person, PersonStudent, PersonTeacher
from account.serializers import UserDescriptionSerializer


class PersonAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = Person.ALL_FIELDS

    # user = UserDescriptionSerializer()


class PersonDetailStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonStudent
        fields = PersonStudent.PUBLIC_FIELDS


class PersonDetailTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonTeacher
        fields = PersonTeacher.PUBLIC_FIELDS


class PersonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = Person.PUBLIC_FIELDS + ['extra']

    phone = PhoneNumberField()
    user = UserDescriptionSerializer(allow_null=True)
    extra = serializers.SerializerMethodField()
    CLASS = settings.serializers.class_name(many=True)

    def get_extra(self, obj):
        if obj.role == settings.choices.role.student:
            return PersonDetailStudentSerializer(obj.personstudent).data
        if obj.role == settings.choices.role.teacher:
            return PersonDetailTeacherSerializer(obj.personteacher).data


class PersonDescriptionStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonStudent
        fields = PersonStudent.DESCRIPTION_FIELDS


class PersonDescriptionTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonTeacher
        fields = PersonTeacher.DESCRIPTION_FIELDS


class PersonDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = Person.DESCRIPTION_FIELDS + ['extra']

    extra = serializers.SerializerMethodField()

    def get_extra(self, obj):
        if obj.role == settings.choices.role.student:
            return PersonDescriptionStudentSerializer(obj.personstudent).data
        if obj.role == settings.choices.role.teacher:
            return PersonDescriptionTeacherSerializer(obj.personteacher).data


class PersonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = Person.REQUIRED_FIELDS


class PersonSetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["user"]

    # user = serializers.CharField()
    # def validate_user(self, attr):


class PersonSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = Person.EDITABLE_FIELDS

    phone = PhoneNumberField(required=False)
    email = serializers.EmailField(required=False)
    QQ = serializers.CharField(required=False)
    WeChat = serializers.CharField(required=False)
    photo = serializers.ImageField(required=False)


class PersonSetStudentSerializer(PersonSetSerializer):
    class Meta:
        model = PersonStudent
        fields = Person.EDITABLE_FIELDS + PersonStudent.EDITABLE_FIELDS


class PersonSetTeacherSerializer(PersonSetSerializer):
    class Meta:
        model = PersonTeacher
        fields = Person.EDITABLE_FIELDS + PersonTeacher.EDITABLE_FIELDS

    subject = serializers.CharField(required=False)
