<!--===========================================================================
  = Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                     =
  =                                                                           =
  =   @Time : 2023-6-19 9:23                                                  =
  =   @Author : hanjin                                                        =
  =   @Email : 2819469337@qq.com                                              =
  =   @File : ClassName.vue                                                   =
  =   @Program: website5                                                      =
  ===========================================================================-->

<script setup lang="ts">

import {defineProps, withDefaults} from "vue";
import type {ClassInfo} from "@/stores/Blossom";
import {ClassTypeChoices} from "@/constants/Blossom";

interface PropsType {
  info: ClassInfo | null,
  isLink?: boolean
}

withDefaults(defineProps<PropsType>(), {
  info: null,
  isLink: false
})
</script>

<template>
  <div class="class-name">
    <router-link v-if="isLink" :to="`/blossom/info/class/${info.id}`">{{ info.name }}</router-link>
    <span v-else>{{ info.name }}</span>
    <el-tag size="small">{{ info.created }}年{{ info.year }}届</el-tag>
    <el-tag size="small">{{ ClassTypeChoices[info.type] }}</el-tag>
  </div>
</template>

<style scoped>
.class-name {
  margin-right: 1em;
}

.class-name > * {
  margin-right: 0.5em;
}

.class-name > *:last-child {
  margin-right: 0;
}
</style>