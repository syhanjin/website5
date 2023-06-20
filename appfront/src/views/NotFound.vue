<!--===========================================================================
  = Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                     =
  =                                                                           =
  =   @Time : 2023-6-7 13:0                                                   =
  =   @Author : hanjin                                                        =
  =   @Email : 2819469337@qq.com                                              =
  =   @File : NotFound.vue                                                    =
  =   @Program: website5                                                      =
  ===========================================================================-->

<script setup lang="ts">
import {useRouter} from "vue-router";

const router = useRouter()
</script>

<template>
  <div class="NotFound">
    <h2>页面走丢了</h2>
    <a href="#" @click="router.back(-1)">返回上一页</a>
  </div>
</template>

<style scoped>

.NotFound {
  text-align: center;
}

h2 {
  font-size: 64px;
  letter-spacing: .2em;
}
</style>