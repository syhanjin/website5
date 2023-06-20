# -*- coding: utf-8 -*-

# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-6-18 17:8                                                    =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : serializers.py                                                    =
#    @Program: website5                                                        =
# ==============================================================================

from rest_framework import serializers

from .models import Media, MediaImage, MediaVideo


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['created', 'url', 'pk']

    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return getattr(obj, obj.type).url


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaImage
        fields = ['created', 'url', 'pk']

    url = serializers.ImageField(use_url=True, source='image')


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaVideo
        fields = ['created', 'url', 'pk']

    url = serializers.FileField(use_url=True, source='video')
