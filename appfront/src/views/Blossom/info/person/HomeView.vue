<!--===========================================================================
  = Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                     =
  =                                                                           =
  =   @Time : 2023-6-20 12:47                                                 =
  =   @Author : hanjin                                                        =
  =   @Email : 2819469337@qq.com                                              =
  =   @File : HomeView.vue                                                    =
  =   @Program: website5                                                      =
  ===========================================================================-->

<script setup lang="ts">

import {computed, defineProps, ref} from "vue";
import type {PersonInfo} from "@/stores/Blossom";
import ClassName from "@/components/Blossom/class_/ClassName.vue";
import {gender} from "@/constants/Blossom";
import {Iphone, Message} from "@element-plus/icons-vue";
import moment from "moment";

const props = defineProps<{
  info: PersonInfo
}>()
// console.log(info)

const is_teacher = computed(() => props.info.role === 'teacher'),
    is_student = computed(() => props.info.role === 'student');

const baseInfoLabels = ref<Array<{
  label: string,
  key: string,
  icon?: any,
  iconClass?: string,
  translater?: Function
}>>([
  // {label: "姓名", key: "name", icon: markRaw(User)},
  // {label: "性别", key: "gender", iconClass: "icon-gender", translater: (gender) => ({male: "男", female: "女"}[gender])},
  // {
  //   label: "生日", key: "birthday", iconClass: "icon-shengri", translater: (attr) => {
  //     return attr ? moment(attr, "%mm月%dd日") : "未设置"
  //   }
  // },
  // {label: "", key: "", iconClass: ""},
  // {label: "", key: "", iconClass: ""},
  // {label: "手机号", key: "phone", icon: markRaw(Phone)},
  // {label: "邮箱", key: "email", icon: markRaw(Message)},
  // {label: "QQ", key: "QQ", iconClass: "icon-QQ"},
  // {label: "微信", key: "WeChat", iconClass: "icon-weixin"},
])

function infoFilter(attr) {
  return attr || "未设置"
}

</script>

<template>
  <div>
    <div class="info-box">
      <div class="box1">
        <div class="left-box">
          <el-image :src="info.photo"></el-image>
        </div>
        <div class="right-box">
          <p class="name-box">
            <el-tag v-if="is_teacher" type="info">{{ info.extra.subject }}</el-tag>
            <span class="name">{{ info.name }} </span>

            <el-icon size="14">
              <component :is="gender[info.gender]"/>
            </el-icon>
          </p>
          <p></p>
          <el-row>
            生日：{{ info.birthday ? moment(info.birthday).format("Y年M月D日") : "未设置" }}
          </el-row>
          <el-row>
            <!-- @formatter:off -->
            <el-col :span="6"><el-icon><Iphone/></el-icon>{{ infoFilter(info.phone)}}</el-col>
            <el-col :span="6"><el-icon><Message/></el-icon>{{ infoFilter(info.email) }}</el-col>
            <el-col :span="6"><i class="iconfont icon-QQ"/>{{ infoFilter(info.QQ) }}</el-col>
            <el-col :span="6"><i class="iconfont icon-weixin"/>{{ infoFilter(info.WeChat) }}</el-col>
            <!-- @formatter:on -->
          </el-row>
          <div>
            <span class="info-title" v-if="is_teacher">管理班级</span>
            <span class="info-title" v-if="is_student">所在班级</span>
            <template v-for="i in info.CLASS">
              <ClassName :info="i" is-link/>
              <span v-if="i < info.CLASS.length - 1">，</span>
            </template>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.info-box {
  display: flex;
  align-items: center;
}

.info-box > div {
  flex: 1
}

.box1 {
  display: flex;
  flex-direction: row;

}

.box1 > .left-box {
  padding: 0 30px;

}

.box1 > .left-box .el-image {
  height: 256px;
  width: 192px;
  border: #6c757d solid 1px;
}

.box1 > .right-box {
  flex: 1;
  display: flex;
  align-items: start;
  flex-direction: column;
  justify-content: stretch;
}

.box1 > .right-box > * {
  width: 100%;
}

.name-box {
  font-size: 24px;
  height: 32px;
  margin-bottom: 12px;
}

.name {
  margin-left: 5px;
}

.info-title {
  display: block;
  color: #4f4f4f;
}

</style>