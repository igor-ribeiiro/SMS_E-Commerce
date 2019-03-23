<template>
  <div>
    <NavBar></NavBar>
    <slot></slot>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";

import NavBar from "@/components/NavBar.vue";

@Component({ components: { NavBar } })
export default class BaseView extends Vue {}
</script>

<style>
</style>
