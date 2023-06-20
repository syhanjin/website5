# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-6-18 22:6                                                    =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : name.py                                                           =
#    @Program: website5                                                        =
# ==============================================================================

# -*- coding: utf-8 -*-
from rest_framework import serializers

from Blossom.conf import settings


class ClassNameSerializer(serializers.ModelSerializer):
    """
    为了解决循环引入的奇怪问题，这里单独拿出一个序列化器
    """

    class Meta:
        model = settings.models.class_
        fields = ["id", "created", "year", "name", "type"]

    id = serializers.CharField()
    created = serializers.IntegerField()
    year = serializers.IntegerField()
    name = serializers.CharField()
    type = serializers.CharField()
