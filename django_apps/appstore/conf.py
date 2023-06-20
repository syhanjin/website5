# -*- coding: utf-8 -*-

# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-6-16 23:36                                                   =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : conf.py                                                           =
#    @Program: website5                                                        =
# ==============================================================================

from conf import ObjDict, create_lazy_settings

SETTINGS_NAMESPACE = "APPSTORE"

default_settings = {
    "permissions": ObjDict(
        {
            "app": ["rest_framework.permissions.AllowAny"],
            "app_create": ["account.permissions.AdminSuper"],
            "app_version_create": ["account.permissions.AdminSuper"]
        }
    )
}

settings = create_lazy_settings(default_settings, SETTINGS_NAMESPACE, [])
