/*=============================================================================
 = Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                      =
 =                                                                            =
 =   @Time : 2023-6-20 13:48                                                  =
 =   @Author : hanjin                                                         =
 =   @Email : 2819469337@qq.com                                               =
 =   @File : vite.config.ts                                                   =
 =   @Program: website5                                                       =
 =============================================================================*/

import {fileURLToPath, URL} from 'node:url'

import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import {ElementPlusResolver} from 'unplugin-vue-components/resolvers'

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        vue(),
        AutoImport({
            resolvers: [ElementPlusResolver()],
        }),
        Components({
            resolvers: [ElementPlusResolver()],
        }),
    ],
    resolve: {
        alias: {
            '@': fileURLToPath(new URL('./src', import.meta.url))
        }
    }
})
