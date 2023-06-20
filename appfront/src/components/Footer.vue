<!--===========================================================================
  = Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                     =
  =                                                                           =
  =   @Time : 2023-6-7 13:35                                                  =
  =   @Author : hanjin                                                        =
  =   @Email : 2819469337@qq.com                                              =
  =   @File : Footer.vue                                                      =
  =   @Program: website5                                                      =
  ===========================================================================-->

<script setup lang="ts">
import {ref} from "vue";

interface Link {
  title: string,
  url: string
}

const links = ref<Array<Link>>([])
</script>

<template>
  <el-footer class="tail">
    <div class="links" v-if="links.length">
      <p>友情链接</p>
      <div>
        <a v-for="link in links" :href="link.url" target="_Blank">{{ link.title }}</a>
      </div>
    </div>
    <div class="">
      <a href="/contactus" target="_blank">联系我们</a>
    </div>
    ©2020-2021 sakuyark.com 版权所有
    <a href="http://www.beian.miit.gov.cn">湘ICP备2021010731号</a>
  </el-footer>
</template>

<style scoped>
.tail {
  min-height: 30px;
  margin-bottom: 10px;
  background-color: white;
  padding-top: 15px;
  width: 100%;
  position: relative;
  font-size: 12px;
  top: 0;
  left: 0;
  text-align: center;
  color: black;
}

.tail .links {
  position: relative;
  width: 200px;
  height: 84px;
  margin: 15px 0 15px 100px;
  text-align: left;
  padding-left: 10px;
}

.tail .links p {
  font-weight: bold;
  font-size: 14px;
  margin-left: -10px;
}

.tail .links div a {
  display: block;
  width: 100%;
  height: 14px;
  line-height: 14px;
}

.tail .links div {
  position: relative;
  display: inline-block;
  width: 100px;
  height: 84px;
  vertical-align: top;
}
</style>