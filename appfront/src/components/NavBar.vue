<!--===========================================================================
  = Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                     =
  =                                                                           =
  =   @Time : 2023-6-7 14:33                                                  =
  =   @Author : hanjin                                                        =
  =   @Email : 2819469337@qq.com                                              =
  =   @File : NavBar.vue                                                      =
  =   @Program: website5                                                      =
  ===========================================================================-->

<script lang="ts" setup>
import {ref} from 'vue'
import {useAccountStore} from "@/stores/account";
import UserMenu from "@/components/account/UserMenu.vue";
import {useRoute} from "vue-router";

const account = useAccountStore()
const route = useRoute()

const links = ref([
  {text: '首页', url: '/'},
  {text: '关于', url: '/about'},
  {text: '朝华', url: '/blossom'}
])

function url(to) {
  return to + (to !== route.path ? ('?redirect=' + route.path) : '')
}

</script>

<template>
  <el-header class="nav">
    <!--    <img id="icon" :src="icon" onclick="window.location.href='/';"/>-->
    <div class="bar">
      <template v-for="link in links">
        <div>
          <router-link :to="link.url">{{ link.text }}</router-link>
          <!-- <a :href="link.url">{{ link.text }}</a> -->
        </div>
      </template>
    </div>
    <div class="user">
      <div v-if="!account.isAuthenticated" class="ops">
        <div>
          <router-link :to="url('/signup')">注册</router-link>
          <!-- <a href="/signup">注册</a> -->
          <el-divider direction="vertical"></el-divider>
          <router-link :to="url('/login')">登录</router-link>
          <!-- <a href="/login">登录</a> -->
        </div>
      </div>
      <el-avatar v-if="account.isAuthenticated" :size="64" :src="account.me.avatar"
                 class="avatar"></el-avatar>
      <user-menu/>
    </div>
  </el-header>
</template>


<style scoped>
.nav {
  position: relative;
  top: 0;
  left: 0;
  height: 80px;
  width: 100%;
  background-color: #e5e7e3;
  box-shadow: 2px 2px 2px 2px #d5d7d3;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.nav #icon {
  width: 72px;
  height: 72px;
  cursor: pointer;
  border-radius: 50%;
  top: 0;
  bottom: 0;
  margin: auto 10px;
  left: 15px;
  position: relative;
}

.nav .bar {
  margin: auto 0;
  bottom: 0;
  top: 0;
  position: relative;
  min-width: 100px;
  /* width: 600px; */
  height: 45px;
  line-height: 45px;
  cursor: default;
  text-align: left;
}

.nav .bar div {
  /*text-align: center;*/
  position: relative;
  font-size: 20px;
  display: inline-block;
  margin: 2.5px 20px;
  height: 40px;
  width: 80px;
  cursor: default;
}

.nav .bar div:before {
  content: '';
  position: absolute;
  display: block;
  width: 0;
  margin: 0 auto;
  bottom: 0;
  left: 0;
  right: 0;
  border-bottom: 2.5px solid red;
  transition: width 0.3s ease-in;
}

.nav .bar div:hover:before {
  width: 80px;
}

.nav .bar div a {
  width: 100%;
  height: 100%;
  text-align: center;
  display: inline-block;
  position: relative;
}

.avatar:hover + >>> .user-menu, >>> .user-menu:hover {
  display: block;
  opacity: 1;
  z-index: 999;
}

.user {
  margin: auto 0;
  bottom: 0;
  top: 0;
  position: relative;
  right: 125px;
  height: 70px;
  text-align: center;
  line-height: 45px;
  cursor: default;
  display: flex;
  align-items: center;
}

.user .ops {
  position: relative;
  width: 100px;
  display: inline-block;
}

.user .ops a {
  cursor: pointer;
  font-size: 16px;
  display: inline-block;
}

.user .avatar {
  /*margin-right: 150px;*/
}

</style>