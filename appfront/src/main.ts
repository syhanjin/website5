/*=============================================================================
 = Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                      =
 =                                                                            =
 =   @Time : 2023-6-20 13:53                                                  =
 =   @Author : hanjin                                                         =
 =   @Email : 2819469337@qq.com                                               =
 =   @File : main.ts                                                          =
 =   @Program: website5                                                       =
 =============================================================================*/

import './assets/main.css'
import {createApp} from 'vue'

import App from './App.vue'
import router from './router'
import axios from "axios";
import {pinia} from "@/pinia";
import VueWechatTitle from 'vue-wechat-title'

const app = createApp(App)

axios.defaults.baseURL = import.meta.env.VITE_BASE_API_URL
// app.config.globalProperties.$http = axios
app.use(VueWechatTitle)
app.use(pinia)
app.use(router)


app.mount('#app')
