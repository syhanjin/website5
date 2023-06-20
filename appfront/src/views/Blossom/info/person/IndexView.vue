<!--===========================================================================
  = Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                     =
  =                                                                           =
  =   @Time : 2023-6-18 14:4                                                  =
  =   @Author : hanjin                                                        =
  =   @Email : 2819469337@qq.com                                              =
  =   @File : IndexView.vue                                                   =
  =   @Program: website5                                                      =
  ===========================================================================-->

<script setup lang="ts">

import {onBeforeMount, ref} from "vue";
import type {PersonInfo} from "@/stores/Blossom";
import axios from "axios";
import {useRoute} from "vue-router";

const route = useRoute()

const info = ref<PersonInfo>()
const dataFetched = ref(false)
onBeforeMount(async () => {
  await axios.get(`/blossom/person/${route.params.id}`)
      .then(resp => {
        info.value = resp.data
      })
  dataFetched.value = true
})
</script>

<template>
  <div v-if="dataFetched">
    <router-view :info="info"></router-view>
  </div>
</template>

<style scoped>

</style>