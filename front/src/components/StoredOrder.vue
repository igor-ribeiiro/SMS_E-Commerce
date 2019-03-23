<template>
  <div class="message-delivery">
    <el-row>
      <el-col :span="18">
        <div class="msg-name">{{ order.name }} ({{ order.telefone }})</div>
        <el-tree
          :data="orderTree"
          :props="{children: 'children', label: 'label'}"
          default-expand-all
        ></el-tree>
      </el-col>
      <el-col :span="6" v-if="!order.enviado">
        <el-button circle type="success" icon="el-icon-check" @click="finishOrder(order)"></el-button>
      </el-col>
    </el-row>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";

import { IOrder, IOrders } from "@/api/types";

@Component
export default class StoredOrder extends Vue {
  @Prop() order?: IOrder;

  finishOrder(order: IOrder) {
    this.$store.dispatch("finishOrder", order);
  }

  get orderTree() {
    return [
      {
        label: "Produtos selecionados",
        children: this.order!.items.map(i => ({
          label: `${i.quantidade} - ${i.descricao}`
        }))
      }
    ];
  }
}
</script>

<style>
.message-delivery {
  padding-bottom: 8px;
}

.msg-name {
  font-size: 1rem;
  margin-bottom: 16px;
}
</style>
