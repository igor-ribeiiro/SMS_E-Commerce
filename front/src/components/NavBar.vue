<template>
  <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" router>
    <el-menu-item index="/sms">Compras SMS</el-menu-item>
    <el-menu-item index="/estoque">Estoque</el-menu-item>
  </el-menu>
</template>

<script>
export default {
  computed: {
    activeIndex() {
      return this.$router.currentRoute.path;
    }
  }
};
</script>

<style>
</style>
