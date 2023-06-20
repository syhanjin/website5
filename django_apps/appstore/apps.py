# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-5-21 10:34                                                   =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : apps.py                                                           =
#    @Program: website5                                                        =
# ==============================================================================

from django.apps import AppConfig

"""
应用商店服务，提供应用下载，和更新服务
"""


class AppstoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appstore'
