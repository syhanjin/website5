# -*- coding: utf-8 -*-

# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-6-17 10:58                                                   =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : permissions.py                                                    =
#    @Program: website5                                                        =
# ==============================================================================

from rest_framework import permissions

from Blossom.models.person import RoleChoices as PersonRoleChoices
from account.permissions import AdminDeveloper, CurrentUser


class _Blossom(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return (
                super().has_permission(request, view)
                and bool(self.get_blossom_person(request))
        )

    def get_blossom_person(self, request):
        return getattr(request.user, "blossom_person", None)


class _BlossomStudent(_Blossom):
    def has_permission(self, request, view):
        return (
                super().has_permission(request, view)
                and self.get_blossom_person(request).role == PersonRoleChoices.student
        )


class _BlossomTeacher(_Blossom):
    def has_permission(self, request, view):
        return (
                super().has_permission(request, view)
                and self.get_blossom_person(request).role == PersonRoleChoices.teacher
        )


# 同一个行政班，同一个年级

Blossom = _Blossom | AdminDeveloper
BlossomStudent = _BlossomStudent | AdminDeveloper
BlossomTeacher = _BlossomTeacher | AdminDeveloper

_CurrentBlossom = _Blossom & CurrentUser
CurrentBlossom = _CurrentBlossom | AdminDeveloper
CurrentBlossomStudent = (_BlossomStudent & _CurrentBlossom) | AdminDeveloper
CurrentBlossomTeacher = (_BlossomTeacher & _CurrentBlossom) | AdminDeveloper
