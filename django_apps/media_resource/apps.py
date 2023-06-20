# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-5-21 14:13                                                   =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : apps.py                                                           =
#    @Program: website5                                                        =
# ==============================================================================

from django.apps import AppConfig

"""
媒体资源
"""


class MediaResourceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'media_resource'
