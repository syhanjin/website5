<!--===========================================================================
  = Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                     =
  =                                                                           =
  =   @Time : 2023-6-7 13:47                                                  =
  =   @Author : hanjin                                                        =
  =   @Email : 2819469337@qq.com                                              =
  =   @File : SignupView.vue                                                  =
  =   @Program: website5                                                      =
  ===========================================================================-->

<script setup lang="ts">

import {reactive, ref} from "vue";
import type {FormInstance, FormRules} from "element-plus";
import axios from "axios";
import {useRoute, useRouter} from "vue-router";
import {Lock, Message, User} from "@element-plus/icons-vue"

const formRef = ref<FormInstance>()
const router = useRouter()
const route = useRoute()


const checkName = (rule, value, callback) => {
  if (!value) {
    callback(new Error('请输入用户名'))
  }
  callback()
}
const checkPwd1 = (rule, value, callback) => {
  if (value && form.pwd2) {
    formRef.value.validateField('pwd2')
  }
  if (!value || value.length < 8) {
    callback(new Error('密码太短'))
  } else {
    callback()
  }
}
const checkPwd2 = (rule, value, callback) => {
  if (!value) {
    callback(new Error('确认密码不可为空'))
    return
  }
  if (value !== form.pwd1) {
    callback(new Error('密码不匹配'))
  } else {
    callback()
  }
}
const checkEmail = (rule, value, callback) => {
  if (!value) callback(new Error('邮箱不可为空'))
  const reg = /^\w+((-\w+)|(\.\w+))*@[A-Za-z\d]+((\.|-)[A-Za-z\d]+)*\.[A-Za-z\d]+$/
  if (!reg.test(value)) {
    callback(new Error('这不是一个邮箱'))
  }
  callback()
}

const form = reactive({
  name: '',
  pwd1: '',
  pwd2: '',
  email: ''
})
const errors = ref([])
const creating = ref(false), codeDisabled = ref(false), submitDisabled = ref(false),
    submitText = ref('创建账户')
const rules = reactive<FormRules>({
  name: {validator: checkName, trigger: 'blur'},
  pwd1: {validator: checkPwd1, trigger: 'blur'},
  pwd2: {validator: checkPwd2, trigger: 'blur'},
  email: {validator: checkEmail, trigger: 'blur'}
})

const querySearchEmail = (queryString, callback) => {
  const emailList = [
    {value: '@qq.com'},
    {value: '@126.com'},
    {value: '@163.com'},
    {value: '@sina.com'},
    {value: '@21cn.com'},
    {value: '@sohu.com'},
    {value: '@yahoo.com.cn'},
    {value: '@tom.com'},
    {value: '@etang.com'},
    {value: '@eyou.com'},
    {value: '@56.com'},
    {value: '@x.cn'},
    {value: '@chinaren.comsogou.com'},
    {value: '@citiz.com'}
  ]
  let results = []
  const queryList = []
  emailList.forEach((item) => {
    queryList.push({value: queryString.split('@')[0] + item.value})
  })
  results = queryString
      ? queryList.filter(createFilter(queryString))
      : queryList
  callback(results)
}

function createFilter(queryString) {
  return (item) => {
    return item.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0
  }
}

function submitForm() {
  formRef.value.validate((valid) => {
    // console.log(valid)
    if (valid) {
      creating.value = true
      submitText.value = '正在创建'
      axios.post('/users/', {
        name: form.name,
        email: form.email,
        password: form.pwd2
      })
          .then((rel) => {
            creating.value = false
            const data = rel.data
            if (Object.prototype.hasOwnProperty.call(data, 'uuid')) {
              submitText.value = '创建成功，正在跳转登录...'
              setTimeout(() => {
                router.push('/login' + (route.query.redirect || ''))
              }, 3000)
            }
          })
          .catch((error) => {
            const data = error.response.data
            errors.value = []
            if (typeof (data) === 'string') {
              errors.value.push(data)
            } else {
              for (const key in data) {
                errors.value = errors.value.concat(data[key])
              }
            }
            creating.value = false
            console.log(errors)
            submitText.value = '创建失败'
            submitDisabled.value = true
            setTimeout(() => {
              submitText.value = '重新创建'
              submitDisabled.value = false
            }, 3000)
          })
    } else {
      return false
    }
  })
}

function resetForm() {
  formRef.value.resetFields()
}

</script>

<template>
  <el-form
      ref="formRef"
      :model="form"
      :rules="rules"
      class="signup"
      label-width="80px"
  >
    <el-form-item>
      <h3>注册用户</h3>
    </el-form-item>
    <div v-if="errors.length" class="errors">
      <span v-for="error in errors">{{ error }}</span>
    </div>
    <el-form-item label="用户名" prop="name">
      <el-input v-model="form.name" :prefix-icon="User"/>
    </el-form-item>
    <el-form-item label="密码" prop="pwd1">
      <el-input v-model="form.pwd1" :prefix-icon="Lock" show-password/>
    </el-form-item>
    <el-form-item label="确认密码" prop="pwd2">
      <el-input v-model="form.pwd2" :prefix-icon="Lock" show-password/>
    </el-form-item>
    <el-form-item label="电子邮件" prop="email">
      <el-autocomplete
          v-model="form.email"
          :fetch-suggestions="querySearchEmail"
          :trigger-on-focus="false"
          class="email"
          :prefix-icon="Message"
      />
    </el-form-item>
    <el-form-item>
      <el-button v-loading="creating" :disabled="submitDisabled" type="primary" @click="submitForm">
        {{ submitText }}
      </el-button>
      <el-button @click="resetForm">重置</el-button>
    </el-form-item>
  </el-form>
</template>

<style scoped>

@media screen and (min-width: 750px) {
  .signup {
    width: 50%;
    padding: 50px 50px 30px;
    margin: 15px auto;
  }
}

@media screen and (max-width: 450px) {
  .signup {
    width: 98%;
    padding: 20px 10px;
    margin: 15px auto;
  }
}

.signup {
  border-radius: 5px;
  border: 3px solid #b4bccc;
  max-width: 450px;
}

.email {
  width: 100%;
}

.errors {
  width: 100%;
  color: #ba3131;
}

.errors > span {
  display: block;
  margin-bottom: 10px;
  text-align: center;
  font-size: 14px;
}

.errors > span:last-child {
  margin-bottom: 0;
}
</style>