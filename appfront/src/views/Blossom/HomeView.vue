<!--===========================================================================
  = Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                     =
  =                                                                           =
  =   @Time : 2023-6-17 11:3                                                  =
  =   @Author : hanjin                                                        =
  =   @Email : 2819469337@qq.com                                              =
  =   @File : HomeView.vue                                                    =
  =   @Program: website5                                                      =
  ===========================================================================-->

<script setup lang="ts">

import {ref} from "vue"

const modules = ref([
  {
    url: "/blossom/info",
    title: "基本信息"
  }, {
    url: "/blossom/toast",
    title: "拾花录"
  }
])
</script>

<template>
  <div>
    <div class="modules">
      <template v-for="module in modules">
        <el-card class="module-item" shadow="hover">
          <template #header>
            <router-link :to="module.url" class="title">{{ module.title }}</router-link>
          </template>
        </el-card>
      </template>
    </div>
  </div>
</template>

<style scoped>
.modules {
  /*height: 100px;*/
  display: flex;
}

.module-item >>> .el-card__header {
  padding: 0;
}

.module-item >>> .el-card__header > .title {
  display: block;
  padding: calc(var(--el-card-padding) - 2px) var(--el-card-padding);
}

.modules > .module-item {
  /*text-align: center;*/
  flex: 1;
  margin: 15px 30px;
}
</style>