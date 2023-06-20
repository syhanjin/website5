# -*- coding: utf-8 -*-


# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-6-2 22:3                                                     =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : utils.py                                                          =
#    @Program: website5                                                        =
# ==============================================================================
import shortuuid


def create_uuid(): return shortuuid.ShortUUID(alphabet="0123456789").random(8)
