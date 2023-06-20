/*=============================================================================
 = Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                      =
 =                                                                            =
 =   @Time : 2023-6-7 14:3                                                    =
 =   @Author : hanjin                                                         =
 =   @Email : 2819469337@qq.com                                               =
 =   @File : account.ts                                                       =
 =   @Program: website5                                                       =
 =============================================================================*/

import {defineStore} from 'pinia'
import axios from "axios";

interface State {
    isAuthenticated: boolean,
    token: string,
    me: UserInfo | {}
}

interface UserInfo {
    uuid: string,
    name: string,
    email: string | null,
    avatar: string,
    signature: string,
    admin: number,
    created: string
}

export const useAccountStore = defineStore('account', {
    state: (): State => {
        return {
            isAuthenticated: false,
            token: "",
            me: {}
        }
    },
    getters: {},
    actions: {
        initializeStore() {
            const token = localStorage.getItem('token')
            if (token) {
                this.setToken(token)
            } else {
                this.removeToken()
            }
        },
        async fetchUserInfo(is_force = false) {
            if (!this.isAuthenticated) return
            if (is_force || !this.me.uuid) {
                await axios.get(`/users/me`)
                    .then((resp) => {
                        this.me = resp.data
                    })
                return this.me
            }

        },
        setToken(token) {
            // localStorage.setItem("token", token)
            this.token = token
            this.isAuthenticated = true
            axios.defaults.headers.common.Authorization = 'Token ' + this.token
        },
        removeToken() {
            // localStorage.setItem("token", "")
            this.token = ''
            this.isAuthenticated = false
            axios.defaults.headers.common.Authorization = ''
        }
    }
})
