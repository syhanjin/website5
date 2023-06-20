<!--===========================================================================
  = Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                     =
  =                                                                           =
  =   @Time : 2023-6-20 13:58                                                 =
  =   @Author : hanjin                                                        =
  =   @Email : 2819469337@qq.com                                              =
  =   @File : App.vue                                                         =
  =   @Program: website5                                                      =
  ===========================================================================-->

<script setup lang="ts">
import {RouterView, useRoute} from 'vue-router'
import NavBar from "@/components/NavBar.vue";
import {useAccountStore} from "@/stores/account";
import {onBeforeMount, onMounted} from "vue";
import Footer from "@/components/Footer.vue";
import zhCn from "element-plus/es/locale/lang/zh-cn";

const account = useAccountStore()
const route = useRoute()
const locale = zhCn

onBeforeMount(async () => {
  account.initializeStore()
})
onMounted(async () => {
  await account.fetchUserInfo()
})
</script>

<template>
  <el-config-provider :locale="locale">
    <NavBar/>
    <el-main class="container">
      <RouterView v-wechat-title="route.meta.title"/>
    </el-main>
    <Footer/>
  </el-config-provider>
</template>


<style scoped>

</style>
