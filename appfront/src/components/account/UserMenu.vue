<!--===========================================================================
  = Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                     =
  =                                                                           =
  =   @Time : 2023-6-7 14:31                                                  =
  =   @Author : hanjin                                                        =
  =   @Email : 2819469337@qq.com                                              =
  =   @File : UserMenu.vue                                                    =
  =   @Program: website5                                                      =
  ===========================================================================-->

<script setup lang="ts">

import {useAccountStore} from "@/stores/account";
import {Lock, SwitchButton} from '@element-plus/icons-vue'
import {ref} from "vue";
import axios from "axios";
import {ElMessage} from "element-plus";

const account = useAccountStore()

const showLogoutDialog = ref(false)

async function logout(logout_all) {
  if (logout_all) {
    await axios.post('/token/logout/')
        .then(resp => {
          account.removeToken()
          localStorage.removeItem("token")
        }).catch(err => {
          try {
            const data = err.response.data
            let errors = '<p>登出失败</p>'
            for (const key in data) {
              errors += '<p>' + data[key] + '</p>'
            }
            ElMessage({
              dangerouslyUseHTMLString: true,
              message: errors,
              type: 'error'
            })
          } catch (e) {
            ElMessage({
              dangerouslyUseHTMLString: true,
              message: '<p>登出失败</p><p>' + err + '</p>',
              type: 'error'
            })
          }
        })
  } else {
    account.removeToken()
    localStorage.removeItem("token")
  }
  showLogoutDialog.value = false
}
</script>


<template>
  <el-card v-if="account.isAuthenticated" :body-style="{padding: '5px 20px 20px'}" class="user-menu"
           shadow="hover">
    <el-row class="name-box">
      <el-col :span="24">
        <el-link :href="'/user/'+account.me.uuid" :underline="false" class="name">
          {{ account.me.name }}
        </el-link>
      </el-col>
    </el-row>
    <el-row class="options">
      <el-link class="options-button" :underline="false" icon="el-icon-setting" href="/settings">
        个人设置
      </el-link>
    </el-row>
    <el-row class="footer">
      <el-col :span="12">
        <el-button disabled :icon="Lock" plain size="small" type="primary">锁定</el-button>
      </el-col>
      <el-col :span="12">
        <el-button :icon="SwitchButton" plain size="small" type="danger" @click="showLogoutDialog=true">登出</el-button>
      </el-col>
    </el-row>
  </el-card>
  <el-dialog v-model="showLogoutDialog" title="登出" width="70%">
    <span>确认要登出您的账号吗</span>
    <template #footer>
      <el-button type="primary" @click="logout(false)">登出此设备</el-button>
      <el-button @click="logout(true)">登出所有设备</el-button>
      <el-button @click="showLogoutDialog=false">我想继续保持登录状态</el-button>
    </template>
  </el-dialog>
</template>
<style scoped>

.user-menu {
  /*display: none;*/
  opacity: 0;
  position: absolute;
  width: 300px;
  min-height: 100px;
  top: 80px;
  right: -115px;
  overflow: hidden;
  z-index: -1;
  text-align: center;
  color: #6c757d;
  background: #fff;
  border: 1px solid #ccc;
  border-radius: 5px;
  transition: all .2s;
}

.options {
  /*border-bottom: rgba(216, 216, 216, 32) solid 1px;*/
  /*width: 100%;*/
  height: 34px;
  line-height: 24px;
  /*display: flex;*/
}

.options-button {
  width: 100%;
  /*height: 100%;*/
  height: 34px;
  border: 0;
  border-radius: 5px;
  text-align: left;
  transition: 0.8s;
  display: block;
  font-size: 14px;
  padding: 5px 10px;
}

.options-button:hover {
  background-color: #E3E5E7;
}

.options-button:after {
  content: '>';
  float: right;
}

.name {
  font-weight: 400;
  font-size: 24px;
}

.name-box {
  line-height: 30px;
  height: 30px;
  margin-bottom: 15px;
}

.footer {
  margin-top: 30px;
}
</style>