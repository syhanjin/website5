# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-6-18 20:8                                                    =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : class_.py                                                         =
#    @Program: website5                                                        =
# ==============================================================================

# -*- coding: utf-8 -*-
from django.db.models import Count
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

from Blossom.conf import settings
from Blossom.mixins import SetMixin


class ClassPagination(PageNumberPagination):
    # 默认的大小
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 30


class ClassViewSet(viewsets.ModelViewSet, SetMixin):
    serializer_class = settings.serializers.class_detail
    queryset = settings.models.class_.objects.all()
    permission_classes = settings.permissions.blossom
    pagination_class = ClassPagination
    filter_backends = [SearchFilter]
    search_fields = ["name"]
    lookup_field = "id"

    def get_queryset(self):
        queryset = super().get_queryset().annotate(member_count=Count("membership"))
        if self.action == 'list':
            queryset = queryset.order_by("-created", "name")
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return settings.serializers.class_detail
        elif self.action == "create":
            return settings.serializers.class_create
        elif self.action == "set":
            return settings.serializers.class_set
        return super().get_serializer_class()

    def get_permissions(self):
        return super().get_permissions()


class ClassMemberViewSet(viewsets.ModelViewSet, SetMixin):
    serializer_class = settings.serializers.class_membership_detail
    queryset = settings.models.class_membership_student.objects.all()
    permission_classes = settings.permissions.blossom
    lookup_field = "id"

    def get_queryset(self):
        queryset = self.get_class().membership.all()
        return queryset

    def get_class(self):
        return settings.models.class_.objects.get(pk=self.kwargs['class_id'])

    def get_serializer_class(self):
        if self.action == "set":
            if self.request.user.blossom_person.role == settings.choices.role.student:
                return settings.serializers.class_membership_set_student
            elif self.request.user.blossom_person.role == settings.choices.role.teacher:
                return settings.serializers.class_membership_set_teacher
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action == "create":
            pass
        elif self.action == "set":
            self.permission_classes = settings.permissions.current
        return super().get_permissions()


class ClassMembershipViewSet(viewsets.ModelViewSet):
    """用于创建关联"""
    serializer_class = settings.serializers.class_membership_description
    queryset = settings.models.class_membership.objects.all()
    permission_classes = settings.permissions.blossom
    lookup_field = "id"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_serializer_class(self):
        if self.action == "create":
            return settings.serializers.class_membership_create
        return super(ClassMembershipViewSet, self).get_serializer_class()

    def get_permissions(self):
        if self.action == "create":
            pass
        return super(ClassMembershipViewSet, self).get_permissions()
