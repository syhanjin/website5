<!--===========================================================================
  = Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                     =
  =                                                                           =
  =   @Time : 2023-6-8 12:32                                                  =
  =   @Author : hanjin                                                        =
  =   @Email : 2819469337@qq.com                                              =
  =   @File : ActivationView.vue                                              =
  =   @Program: website5                                                      =
  ===========================================================================-->

<script setup lang="ts">
import {onMounted, ref} from "vue";
import axios from "axios";
import {useRoute, useRouter} from "vue-router";

const route = useRoute()
const router = useRouter()

const submitting = ref(false), text = ref('正在激活'), errors = ref([])
onMounted(async () => {
  submitting.value = true
  // console.log({
  //   uid: route.params.uid,
  //   token: route.params.token
  // })
  await axios.post('/users/activation/', {
    uid: route.params.uid,
    token: route.params.token
  }).then((rel) => {
    submitting.value = false
    text.value = '激活成功'
    setTimeout(() => {
      router.push('/login')
    }, 3000)
  }).catch((err) => {
    const data = err.response.data
    errors.value = []
    if (typeof (data) === 'string') {
      errors.value.push(data)
    } else {
      for (const key in data) {
        errors.value = errors.value.concat(data[key])
      }
    }
    // console.log(errors)
    submitting.value = false
    text.value = '激活失败'
  })
})
</script>

<template>
  <el-card v-loading="submitting" class="activate" shadow="hover">
    <!-- div slot="header" class="title">
      <span>用户激活</span>
    </div -->
    <div v-if="errors.length" class="errors">
      <span v-for="error in errors" v-html="error"></span>
    </div>
    <!-- div class="item">
      <span>用户编号</span>
      <span>{{ $route.params.uid }}</span>
    </div>
    <div class="item">
      <el-button plain @click="activate" :disabled="disabled" class="submit">{{ submitText }}</el-button>
    </div -->
    <p :class="{error: errors.length}">{{ text }}</p>
  </el-card>
</template>

<style scoped>
@media screen and (min-width: 750px) {
  .activate {
    width: 50%;
    padding: 50px 50px 30px;
    margin: 15px auto;
  }
}

@media screen and (max-width: 450px) {
  .activate {
    width: 98%;
    padding: 20px 10px;
    margin: 15px auto;
  }
}

.activate {
  border-radius: 5px;
  border: 3px solid #b4bccc;
  max-width: 450px;
  height: fit-content;
}

.errors {
  width: 100%;
  margin-bottom: 22px;
  padding: 5px 5%;
  /*background-color: #ba3131;*/
  /*color: #fff;*/
  color: #ba3131;
}

.activate p {
  width: 100%;
  margin-bottom: 22px;
  padding: 5px 5%;
  font-size: 24px;
  font-weight: 400;
  text-align: center;
}

.activate p.error {
  color: #ba3131;
}

.errors > span {
  display: block;
  margin-bottom: 10px;
  text-align: center;
  font-size: 14px;
}

.errors > span:last-child {
  margin-bottom: 0;
}

.item > span {
  display: inline-block;
}

.item > span:first-child {
  width: 80px;
  color: gray;
}

.item > span:last-child {
  flex: 1;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
</style>