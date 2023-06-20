<!--===========================================================================
  = Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                     =
  =                                                                           =
  =   @Time : 2023-6-7 14:10                                                  =
  =   @Author : hanjin                                                        =
  =   @Email : 2819469337@qq.com                                              =
  =   @File : LoginView.vue                                                   =
  =   @Program: website5                                                      =
  ===========================================================================-->

<script setup lang="ts">

import {onBeforeMount, reactive, ref} from "vue";
import {useAccountStore} from "@/stores/account";
import {useRoute, useRouter} from "vue-router";
import type {FormInstance} from "element-plus";
import axios from "axios";
import {Lock, User} from "@element-plus/icons-vue"

const account = useAccountStore()
const router = useRouter()
const route = useRoute()

const formRef = ref<FormInstance>()

const form = reactive({
  name: '',
  password: ''
})
const errors = ref([]),
    submitting = ref(false),
    submitDisabled = ref(false),
    submitText = ref('登录')
const rules = reactive({
  name: {
    validator: (rule, value, callback) => {
      if (!value) {
        callback(new Error('用户名不可为空'))
      } else {
        callback()
      }
    },
    trigger: 'blur'
  },
  password: {
    validator: (rule, value, callback) => {
      if (!value) {
        callback(new Error('密码不可为空'))
      } else {
        callback()
      }
    },
    trigger: 'blur'
  }
})
onBeforeMount(() => {
      if (account.isAuthenticated) {
        router.push(route.query.redirect || '/')
      }
    }
)

function submitForm() {
  formRef.value.validate((valid) => {
    if (valid) {
      submitting.value = true
      submitText.value = '登录中...'
      axios.defaults.headers.common.Authorization = ''
      localStorage.removeItem('token')
      axios.post('/token/login/', form)
          .then((resp) => {
            submitting.value = false
            const token = resp.data.auth_token
            account.setToken(token)
            localStorage.setItem('token', token)
            submitText.value = '登录成功'
            router.push(route.query.redirect || '/')
          })
          .catch((error) => {
            submitting.value = false
            const data = error.response.data
            if (Object.prototype.hasOwnProperty.call(data, 'non_field_errors')) {
              errors.value = ['用户名或密码错误']
              submitText.value = '再次尝试'
            } else {
              errors.value = []
              if (typeof (data) === 'string') {
                errors.value.push(data)
              } else {
                for (const key in data) {
                  errors.value = errors.value.concat(data[key])
                }
              }
              submitText.value = '登录失败'
              submitDisabled.value = true
              setTimeout(() => {
                submitText.value = '再次尝试'
                submitDisabled.value = false
              }, 3000)
            }
          })
    } else {
      return false
    }
  })
}

const qqLoginUrl = ref(
    'https://graph.qq.com/oauth2.0/authorize' +
    '?response_type=code&client_id=101978697' +
    '&redirect_uri=https%3A%2F%2Fsakuyark.com%2Faccount%2Flogin%2Fqq&state=login'
)

</script>

<template>
  <div class="login">
    <h3 class="title">登录</h3>
    <el-form ref="formRef" :model="form" :rules="rules">
      <el-form-item prop="name">
        <el-input
            v-model="form.name"
            placeholder="用户名"
            :prefix-icon="User"
        />
      </el-form-item>
      <el-form-item prop="password">
        <el-input
            v-model="form.password"
            placeholder="密码"
            :prefix-icon="Lock"
            show-password
        />
      </el-form-item>
      <div v-if="errors.length" class="errors">
        <span v-for="(error, index) in errors" :key="index">{{ error }}</span>
      </div>
      <el-form-item>
        <el-button v-loading="submitting" :disabled="submitDisabled" class="loginBtn" plain @click="submitForm()">
          {{ submitText }}
        </el-button>
      </el-form-item>
    </el-form>

    <div class="other">
      <div class="login-ways">
        <span>其他</span>
        <div class="login-qq">
          <a id="qqLoginBtn" :href="qqLoginUrl"></a>
        </div>
      </div>
      <div class="retrieve">
        <span>忘记密码？</span>
        <a :href="route.path + '/retrieve'">找回密码</a>
      </div>
      <div class="clear"></div>
    </div>
  </div>

</template>

<style scoped>
@media screen and (min-width: 750px) {
  .login {
    width: 50%;
    padding: 50px 50px 30px;
    margin: 15px auto;
    height: 500px;
  }
}

@media screen and (max-width: 450px) {
  .login {
    width: 98%;
    height: 400px;
    padding: 20px 10px;
    margin: 15px auto;
  }
}

.login {
  max-width: 450px;
  border-radius: 5px;
  border: 3px solid #b4bccc;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.loginBtn {
  width: 100%;
}

.errors {
  width: 100%;
  /*margin-bottom: 22px;*/
  /*padding: 5px 5%;*/
  /*background-color: #ba3131;*/
  /*color: #fff;*/
  color: #ba3131;
}

.errors > span {
  display: block;
  margin-bottom: 10px;
  text-align: center;
  font-size: 14px;
}

form {
  flex: 1;
}

.retrieve {
  display: inline-block;
  font-size: 12px;
  float: right;
}

.retrieve span {
  margin: 5px 7px;
}

.retrieve a {
  color: blue;
}

.title {
  font-size: 24px;
  text-align: center;
  margin-bottom: 35px;
}

.login *:focus {
  outline: 0;
}

#qqloginBtn {
  background: url(/static/images/QQ.png) center/cover;
  display: inline-block;
  width: 24px;
  height: 24px;
  border-radius: 50% 50%;
  cursor: pointer;
}

.login-ways > span {
  height: 24px;
  line-height: 24px;
  font-size: 12px;
  color: #555666;
}

.other .login-ways {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  line-height: 24px;
  height: 24px;
}

.other .login-ways > div {
  margin-left: 0.2em;
  line-height: 24px;
  height: 24px;
}
</style>