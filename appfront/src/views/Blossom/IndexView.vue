<!--===========================================================================
  = Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                     =
  =                                                                           =
  =   @Time : 2023-6-8 13:23                                                  =
  =   @Author : hanjin                                                        =
  =   @Email : 2819469337@qq.com                                              =
  =   @File : IndexView.vue                                                   =
  =   @Program: website5                                                      =
  ===========================================================================-->

<script setup lang="ts">
import {useAccountStore} from "@/stores/account";
import {useBlossomStore} from "@/stores/Blossom";
import {onMounted} from "vue";

const account = useAccountStore()
const Blossom = useBlossomStore()


onMounted(async () => {
  await Blossom.fetchPersonInfo()
})

</script>

<template>
  <div>
    <router-view v-if="Blossom.has_permission"></router-view>
    <div v-else>
      <span>您没有访问该页面的权限</span>
    </div>
  </div>
</template>

<style scoped>
</style>