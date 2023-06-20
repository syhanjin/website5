<!--===========================================================================
  = Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                     =
  =                                                                           =
  =   @Time : 2023-6-19 8:43                                                  =
  =   @Author : hanjin                                                        =
  =   @Email : 2819469337@qq.com                                              =
  =   @File : HomeView.vue                                                    =
  =   @Program: website5                                                      =
  ===========================================================================-->

<script setup lang="ts">

import axios from "axios";
import {markRaw, reactive, ref} from "vue";
import {Search} from "@element-plus/icons-vue";
import type {ClassInfo} from "@/stores/Blossom";
import PersonName from "@/components/Blossom/person/PersonName.vue";
import ClassName from "@/components/Blossom/class_/ClassName.vue";

const classes = ref<Array<ClassInfo>>([])
const class_page = ref(1)
const class_next = ref(true)
const tab_name = ref("class")

const s = ref("")
const searching = ref(false)
const class_desc = reactive([
  {label: "id", text_key: "id", component: null},
  {label: "建班年份", text_key: "created", component: null},
  {label: "班主任", text_key: "headteacher", component: markRaw(PersonName), props: {}},
  {label: "人数", text_key: "member_count", component: null}
])

async function getClassePages(page: number | null = null, search = "") {
  if (!class_next.value && !page) return
  class_page.value = page || class_page.value
  await axios.get(`/blossom/class?page=${class_page.value}&search=${search}`)
      .then(resp => {
        classes.value = classes.value.concat(resp.data.results)
        class_next.value = Boolean(resp.data.next)
        class_page.value++;
      })
}

async function search() {
  if (tab_name.value === "class") {
    classes.value = []
    searching.value = true
    await getClassePages(1, s.value)
    searching.value = false
  }
}
</script>

<template>
  <div>
    <el-tabs v-model="tab_name" class="search-main">
      <!-- 查找班级 -->
      <el-tab-pane label="按班级" name="class">
        <el-input v-model="s" placeholder="输入关键字查询，不可有错别字" @change="search">
          <template #append>
            <el-button :icon="Search" @click="search" :loading="searching"/>
          </template>
        </el-input>
        <div v-infinite-scroll="getClassePages">
          <el-collapse>
            <template v-for="i in classes">
              <el-collapse-item>
                <template #title>
                  <ClassName :info="i"/>
                </template>
                <div class="class-desc">
                  <template v-for="item in class_desc">
                    <el-row>
                      <el-col :span="4" class="class-desc__label"><span>{{ item.label }}</span></el-col>
                      <el-col :span="20" class="class-desc__text">
                        <span v-if="!item.component">{{ i[item.text_key] }}</span>
                        <component v-else :is="item.component" :info="i[item.text_key]" v-bind="item.props"></component>
                      </el-col>
                    </el-row>
                  </template>
                </div>
              </el-collapse-item>
            </template>
          </el-collapse>
        </div>
      </el-tab-pane>
      <!-- 查找人 -->
      <el-tab-pane label="按人" name="person">

      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<style scoped>
.search-main {
  max-width: 500px;
  margin-left: 100px;
}

.class-title, .class-desc {
  padding: 0 15px;
}

.class-title > * {
  margin: 0 .2em;
}

.class-desc__label {
  color: #6c757d;
}
</style>