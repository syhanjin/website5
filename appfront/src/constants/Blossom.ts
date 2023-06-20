/*=============================================================================
 = Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                      =
 =                                                                            =
 =   @Time : 2023-6-19 13:37                                                  =
 =   @Author : hanjin                                                         =
 =   @Email : 2819469337@qq.com                                               =
 =   @File : Blossom.ts                                                       =
 =   @Program: website5                                                       =
 =============================================================================*/

import {markRaw} from "vue";
import {Female, Male} from "@element-plus/icons-vue"

export const ClassTypeChoices = {
    administrative: "行政班级",
    walking: "走班班级"
}

export const PersonRoleChoices = {
    student: "学生",
    teacher: "老师"
}

export const gender = {
    male: markRaw(Male),
    female: markRaw(Female)
}