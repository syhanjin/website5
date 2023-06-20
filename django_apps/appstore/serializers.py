# -*- coding: utf-8 -*-

# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-5-21 12:36                                                   =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : serializers.py                                                    =
#    @Program: website5                                                        =
# ==============================================================================

from rest_framework import serializers

from appstore.models import App, AppVersion


class AppVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppVersion
        fields = '__all__'

    author = serializers.SerializerMethodField(read_only=True)
    apk = serializers.FileField(source="installer")

    def get_author(self, obj):
        return {
            'name': obj.author.name,
            'uuid': obj.author.uuid
        }


class AppCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('name', 'description')


class AppVersionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppVersion
        fields = AppVersion.REQUIRED_FIELDS + ['app_id']

    app_id = serializers.UUIDField()
    is_force = serializers.ChoiceField(choices=['true', 'false'])
    installer = serializers.FileField()

    def validate(self, attrs):
        if not App.objects.filter(id=attrs["app_id"]).exists():
            raise serializers.ValidationError("app不存在")
        app = App.objects.get(id=attrs["app_id"])
        if app.versions.filter(version_name=attrs['version_name']).exists():
            raise serializers.ValidationError("版本名已存在")
        if app.versions.filter(version_code=attrs['version_code']).exists():
            raise serializers.ValidationError("版本号已存在")
        return attrs
    # def validate_app_id(self, attr):
    #     if App.objects.filter(id=attr).exists():
    #         return attr
    #     else:
    #         raise serializers.ValidationError("app不存在")
    # def validate_version_name(self, attr):
    #     if App.objects.get(id)
    #         return attr
    #     else:
    #         raise serializers.ValidationError("app不存在")


class AppSerializer(serializers.ModelSerializer):
    versions = AppVersionSerializer(many=True)

    class Meta:
        model = App
        fields = '__all__'
