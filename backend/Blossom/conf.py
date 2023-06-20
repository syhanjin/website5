# -*- coding: utf-8 -*-

# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-6-18 22:5                                                    =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : conf.py                                                           =
#    @Program: website5                                                        =
# ==============================================================================

from conf import ObjDict, create_lazy_settings

SETTINGS_NAMESPACE = "APPSTORE"


def SERIALIZER(name):
    return f"Blossom.serializers.{name}"


def MODEL(name):
    return f"Blossom.models.{name}"


def PERMISSION(name):
    return f"Blossom.permissions.{name}"


default_settings = {
    "permissions": ObjDict(
        {
            "blossom": [PERMISSION("Blossom")],
            "student": [PERMISSION("BlossomStudent")],
            "teacher": [PERMISSION("BlossomTeacher")],
            "current": [PERMISSION("CurrentBlossom")]
        }
    ),
    "models": ObjDict(
        {
            "person": MODEL("person.Person"),
            "person_student": MODEL("person.PersonStudent"),
            "person_teacher": MODEL("person.PersonTeacher"),
            "class_": MODEL("class_.Class"),
            "class_membership": MODEL("class_.ClassMembership"),
            "class_membership_student": MODEL("class_.ClassMembershipStudent"),
            "class_membership_teacher": MODEL("class_.ClassMembershipTeacher"),
        }
    ),
    "serializers": ObjDict(
        {
            "person_description": SERIALIZER("person.PersonDescriptionSerializer"),
            "person_detail": SERIALIZER("person.PersonDetailSerializer"),
            "class_detail": SERIALIZER("class_.ClassDetailSerializer"),
            "class_description": SERIALIZER("class_.ClassDescriptionSerializer"),
            "class_name": SERIALIZER("name.ClassNameSerializer"),
            "person_all": SERIALIZER("person.PersonAllSerializer"),
            "person_create": SERIALIZER("person.PersonCreateSerializer"),
            "person_set_user": SERIALIZER("person.PersonSetUserSerializer"),
            "class_create": SERIALIZER("class_.ClassCreateSerializer"),
            "class_set": SERIALIZER("class_.ClassSetSerializer"),
            "person_set_student": SERIALIZER("person.PersonSetStudentSerializer"),
            "person_set_teacher": SERIALIZER("person.PersonSetTeacherSerializer"),
            # Class-Person 关系序列化器（区分student和teacher）
            "class_membership_description": SERIALIZER("class_.ClassMembershipDescriptionSerializer"),
            "class_membership_detail": SERIALIZER("class_.ClassMembershipDetailSerializer"),
            "class_membership_set_student": SERIALIZER("class_.ClassMembershipSetStudentSerializer"),
            "class_membership_set_teacher": SERIALIZER("class_.ClassMembershipSetTeacherSerializer"),
            "class_membership_create": SERIALIZER("class_.ClassMembershipCreateSerializer"),
        }
    ),
    "choices": ObjDict(
        {
            "role": MODEL("person.RoleChoices")
        }
    )
}

settings = create_lazy_settings(default_settings, SETTINGS_NAMESPACE, [])
