# -*- coding: utf-8 -*-

# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-6-18 20:8                                                    =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : mixins.py                                                         =
#    @Program: website5                                                        =
# ==============================================================================

from rest_framework.decorators import action
from rest_framework.response import Response


class SetMixin:
    @action(methods=["post"], detail=True)
    def set(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(
            instance=self.get_object(),
            validated_data=serializer.validated_data
        )
        return Response(data=serializer.data)
