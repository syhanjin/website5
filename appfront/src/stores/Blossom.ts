/*=============================================================================
 = Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                      =
 =                                                                            =
 =   @Time : 2023-6-20 13:36                                                  =
 =   @Author : hanjin                                                         =
 =   @Email : 2819469337@qq.com                                               =
 =   @File : Blossom.ts                                                       =
 =   @Program: website5                                                       =
 =============================================================================*/

import {defineStore} from "pinia";
import type {UserInfo} from "./account"
import axios from "axios";

interface State {
    id: string,
    has_permission: boolean,
    info: PersonInfo | {}
}

export interface PersonStudentExtra {

}

export interface PersonTeacherExtra {
    subject: string
}

export interface PersonInfo {
    id: string,
    user: UserInfo | null,
    name: string,
    role: string,
    gender: string,
    birthday: string | null,
    photo: string,
    phone: string,
    email: string,
    QQ: string,
    WeChat: string
    extra: PersonStudentExtra | PersonTeacherExtra | null,
    CLASS: Array<ClassInfo>
}

// export interface PersonStudentEditableInfo {
//     birthday?: string | null,
//     photo?: string,
//     phone?: string,
//     email?: string,
//     QQ?: string,
//     WeChat?: string
// }
//
// export interface PersonTeacherEditableInfo {
//     birthday: string | null,
//     photo: string,
//     phone: string,
//     email: string,
//     QQ: string,
//     WeChat: string,
//     subject: string
// }

export interface ClassInfo {
    id: string,
    created: number,
    name: string,
    year: number,
    type: string,
    headteacher: PersonInfo | null,
    member_count: number
}

export const useBlossomStore = defineStore("Blossom", {
    state: (): State => {
        return {
            has_permission: true,
            id: "",
            info: {}
        }
    },
    getters: {},
    actions: {
        async fetchPersonInfo() {
            if (this.info.id) return
            await axios.get("/blossom/person/me")
                .then(resp => {
                    this.id = resp.data.id
                    this.info = resp.data
                })
                .catch(err => {
                    if (err.response.status == 403) {
                        this.has_permission = false
                    }
                })
        }
    }
})