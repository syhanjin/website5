# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-5-21 10:16                                                   =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : apps.py                                                           =
#    @Program: website5                                                        =
# ==============================================================================
"""
account
用户系统，继承AbstractUser
统一表名：`Account`
统一模型
"""
from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'
