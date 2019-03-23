<template>
  <div class="sms">
    <BaseView>
      <el-container>
        <el-header>
          <h1>Estoque</h1>
        </el-header>
        <el-main>
          <el-container>
            <el-col :span="20" :offset="2">
              <el-table
                :data="storeItems"
                :row-class-name="isBroken"
                empty-text="Nenhum Item no Carrinho"
                highlight-current-row
              >
                <el-table-column prop="descricao" label="Descricao"></el-table-column>
                <el-table-column prop="quantidade" label="Quantidade"></el-table-column>
                <el-table-column prop="preco" label="Preço (R$)"></el-table-column>
              </el-table>
            </el-col>
          </el-container>
        </el-main>
      </el-container>
    </BaseView>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";

import BaseView from "@/views/BaseView.vue";

import { IStoreItem } from "@/api/types";

@Component({ components: { BaseView } })
export default class Estoque extends Vue {
  mounted() {
    this.$store.dispatch("fetchStore");
  }

  get storeItems() {
    return this.$store.state.store;
  }

  isBroken({ row, index }: { row: IStoreItem; index: number }) {
    return row.quantidade > 0 ? "" : "broken-row";
  }
}
</script>

<style>
.broken-row {
  background-color: rgb(253, 226, 226) !important;
}
</style>
