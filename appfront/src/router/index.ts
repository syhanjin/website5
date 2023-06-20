/*=============================================================================
 = Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                      =
 =                                                                            =
 =   @Time : 2023-6-20 13:1                                                   =
 =   @Author : hanjin                                                         =
 =   @Email : 2819469337@qq.com                                               =
 =   @File : index.ts                                                         =
 =   @Program: website5                                                       =
 =============================================================================*/

import {createRouter, createWebHistory} from 'vue-router'
import {useAccountStore} from "@/stores/account";
import {pinia} from "@/pinia";

const BlossomInfoPersonRoutes = {
    path: "person/:id",
    component: () => import("@/views/Blossom/info/person/IndexView.vue"),
    children: [
        {
            path: "",
            component: () => import("@/views/Blossom/info/person/HomeView.vue")
        }, {
            path: "edit",
            component: () => import("@/views/Blossom/info/person/InfoEditorView.vue")
        }
    ]
}

const BlossomInfoRoutes = {
    path: "info",
    component: () => import("@/views/Blossom/info/IndexView.vue"),
    children: [
        {
            path: "",
            component: () => import("@/views/Blossom/info/HomeView.vue")
        },
        BlossomInfoPersonRoutes
    ]
}


const BlossomRoutes = {
    path: "/blossom",
    component: () => import("@/views/Blossom/IndexView.vue"),
    meta: {
        requireLogin: true
    },
    children: [
        {
            path: "",
            component: () => import("@/views/Blossom/HomeView.vue"),
            meta: {
                title: "朝华Blossom"
            }
        },
        BlossomInfoRoutes
    ]
}

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {path: "/", component: () => import('@/views/HomeView.vue')},
        BlossomRoutes,
        {
            path: "/signup",
            component: () => import("@/views/account/SignupView.vue"),
            meta: {
                title: "注册"
            }
        }, {
            path: "/login",
            component: () => import("@/views/account/LoginView.vue"),
            meta: {
                title: "登录"
            }
        }, {
            path: "/activation/:uid/:token",
            component: () => import("@/views/account/ActivationView.vue"),
            meta: {
                title: "账户激活"
            }
        },

        // 404 页面
        {
            path: '/:catchAll(.*)',
            name: 'NotFound',
            component: () => import('@/views/NotFound.vue'),
            meta: {
                title: '404 Not Found'
            }
        }
    ]
})

function requireLogin(meta) {
    return meta.requireLogin || meta.admin > 0
}

router.beforeEach((to, from, next) => {

    const account = useAccountStore(pinia)
    // if (to.meta.requiresAuth && !main.isLoggedIn) return '/login'

    if (to.matched.some(record => requireLogin(record.meta)) && !account.isAuthenticated) {
        next({
            path: '/login',
            query: {'redirect': to.fullPath}
        })
        return
    }
    next()
})

export default router
