<!--===========================================================================
  = Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                     =
  =                                                                           =
  =   @Time : 2023-6-20 17:32                                                 =
  =   @Author : hanjin                                                        =
  =   @Email : 2819469337@qq.com                                              =
  =   @File : InfoEditorView.vue                                              =
  =   @Program: website5                                                      =
  ===========================================================================-->

<script setup lang="ts">
import {computed, defineProps, reactive} from "vue";
import type {PersonInfo} from "@/stores/Blossom";
import {useBlossomStore} from "@/stores/Blossom";
import {useAccountStore} from "@/stores/account";

const Blossom = useBlossomStore()
const account = useAccountStore()

const props = defineProps<{
  info: PersonInfo
}>()
const has_permission = computed(() => Blossom.id === props.info.id || account.me.admin >= 10)
const form = reactive<PersonInfo>(props.info)

function phoneNumberFormatter(attr: string) {
  let temp = attr.replaceAll(/\D/g, "")
  const slt = [3, 7, 11]
  let res = temp.slice(0, 3)
  for (let i = 0; i < slt.length - 1; i++) {
    if (temp.length > slt[i]) {
      res += " " + temp.slice(slt[i], slt[i + 1])
    }
  }
  return res
}
</script>

<template>
  <div v-if="has_permission">
    <el-form class="form" :model="form">
      <el-form-item prop="photo" label="照片">
        <el-image :src="form.photo"></el-image>
      </el-form-item>
      <el-form-item prop="birthday" label="生日">
        <el-date-picker v-model="form.birthday"></el-date-picker>
      </el-form-item>
      <el-form-item prop="phone" label="手机号">
        <el-input v-model="form.phone" :formatter="phoneNumberFormatter"></el-input>
      </el-form-item>
      <el-form-item prop="email" label="邮箱">
        <el-input v-model="form.email"></el-input>
      </el-form-item>
      <el-form-item prop="QQ" label="QQ">
        <el-input v-model="form.QQ"></el-input>
      </el-form-item>
      <el-form-item prop="WeChat" label="微信">
        <el-input v-model="form.WeChat"></el-input>
      </el-form-item>
    </el-form>
  </div>
  <div v-else>
    您没有编辑该页面的权限
  </div>
</template>

<style scoped>
.form {
  width: 500px;
  margin: 15px auto;
}
</style>