# -*- coding: utf-8 -*-
# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-6-2 22:30                                                    =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : serializers.py                                                    =
#    @Program: website5                                                        =
# ==============================================================================
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = User.ALL_FIELDS


class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = User.PUBLIC_FIELDS


class UserDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = User.DESCRIPTION_FIELDS


class UserAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('avatar',)

    avatar = serializers.ImageField()

    # avatar = Base64ImageField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.avatar_field = 'avatar'
        self.fields["new_{}".format(self.avatar_field)] = self.fields.pop(
            self.avatar_field
        )


class UserSetAvatarSerializer(UserAvatarSerializer):
    class Meta:
        model = User
        fields = ('avatar',)


class UserSignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('signature',)

    signature = serializers.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.signature_field = 'signature'
        self.fields["new_{}".format(self.signature_field)] = self.fields.pop(
            self.signature_field
        )


class UserSetSignatureSerializer(UserSignatureSerializer):
    class Meta:
        model = User
        fields = ('signature',)

    pass
