<!--===========================================================================
  = Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                     =
  =                                                                           =
  =   @Time : 2023-6-17 21:12                                                 =
  =   @Author : hanjin                                                        =
  =   @Email : 2819469337@qq.com                                              =
  =   @File : PersonName.vue                                                  =
  =   @Program: website5                                                      =
  ===========================================================================-->

<script setup lang="ts">
import type {PersonInfo} from "@/stores/Blossom";
import {computed, defineProps} from "vue";

const props = defineProps<{
  info: PersonInfo | null
}>()

const is_student = computed(() => (props.info.role === 'student')),
    is_teacher = computed(() => (props.info.role === 'teacher'))
</script>

<template>
  <div v-if="info">
    <router-link :to="`/blossom/info/person/${info.id}`">
      <template v-if="is_teacher">
        <el-tag size="small" type="info">{{ info.extra.subject }}</el-tag>
      </template>
      <span>{{ props.info.name }}</span>

    </router-link>
  </div>
  <div v-else>
    未提供
  </div>
</template>

<style scoped>

</style>