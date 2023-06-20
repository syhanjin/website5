# -*- coding: utf-8 -*-
# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-6-18 20:51                                                   =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : person.py                                                         =
#    @Program: website5                                                        =
# ==============================================================================
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from Blossom.conf import settings
from Blossom.mixins import SetMixin


class PersonPagination(PageNumberPagination):
    # 默认的大小
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 30


class PersonViewSet(viewsets.ModelViewSet, SetMixin):
    serializer_class = settings.serializers.person_detail
    queryset = settings.models.person.objects.all()
    permission_classes = settings.permissions.blossom
    pagination_class = PersonPagination
    lookup_field = "id"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_serializer_class(self):
        if self.action == "set_user":
            return settings.serializers.person_set_user
        elif self.action == "me":
            return settings.serializers.person_all
        elif self.action == "list":
            return settings.serializers.person_description
        elif self.action == "create":
            return settings.serializers.person_create
        elif self.action == "set":
            obj = self.get_object()
            if obj.role == settings.choices.role.student:
                return settings.serializers.person_set_student
            if obj.role == settings.choices.role.teacher:
                return settings.serializers.person_set_teacher
        return super(PersonViewSet, self).get_serializer_class()

    def get_permissions(self):
        if self.action == "me":
            self.permission_classes = settings.permissions.current
        return super(PersonViewSet, self).get_permissions()

    def perform_create(self, serializer):
        # print(serializer.__dir__())
        # obj = serializer.save()
        getattr(
            settings.models,
            f"person_{serializer.data['role'].lower()}"
        ).objects.create(**serializer.data)

    @action(methods=["post"], detail=True)
    def set_user(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        obj = self.get_object()
        obj.user = user
        obj.save()
        return Response(
            data={
                "id": obj.id,
                "user": obj.user.uuid
            }
        )

    @action(methods=["get", "post"], detail=False)
    def me(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(instance=user.blossom_person)
        return Response(data=serializer.data)
