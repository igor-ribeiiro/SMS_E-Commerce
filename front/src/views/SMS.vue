<template>
  <div class="sms">
    <BaseView>
      <el-container>
        <el-header>
          <h1>Compras por SMS</h1>
        </el-header>
        <el-main>
          <el-row>
            <el-col>
              <p>Visualize as compras realizadas por celular</p>
            </el-col>
          </el-row>
          <el-row>
            <el-col :span="12">
              <el-container>
                <el-header>
                  <el-row>
                    <el-col :span="18">
                      <div class="sms-header">
                        <h2>Para Entregar</h2>
                      </div>
                    </el-col>
                  </el-row>
                </el-header>
                <el-main>
                  <el-timeline reverse>
                    <el-timeline-item
                      v-for="(order, index) in $store.getters.deliveryOrders"
                      :key="index"
                      :color="order.enviado ? '#67C23A' : '#F56C6C'"
                      :timestamp="new Date(order.timestamp).toLocaleString()"
                    >
                      <DeliveryOrder :order="order"/>
                    </el-timeline-item>
                  </el-timeline>
                </el-main>
              </el-container>
            </el-col>
            <el-col :span="12">
              <el-container>
                <el-header>
                  <el-row>
                    <el-col :span="18">
                      <div class="sms-header">
                        <h2>Para Deixar Separado</h2>
                      </div>
                    </el-col>
                  </el-row>
                </el-header>
                <el-main>
                  <el-timeline reverse>
                    <el-timeline-item
                      v-for="(order, index) in $store.getters.storedOrders"
                      :key="index"
                      :color="order.enviado ? '#67C23A' : '#F56C6C'"
                      :timestamp="new Date(order.timestamp).toLocaleString()"
                    >
                      <StoredOrder :order="order"/>
                    </el-timeline-item>
                  </el-timeline>
                </el-main>
              </el-container>
            </el-col>
          </el-row>
        </el-main>
      </el-container>
    </BaseView>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";

import BaseView from "@/views/BaseView.vue";
import DeliveryOrder from "@/components/DeliveryOrder.vue";
import StoredOrder from "@/components/StoredOrder.vue";

import { IOrder, IOrders } from "@/api/types";

@Component({ components: { BaseView, DeliveryOrder, StoredOrder } })
export default class Mensagens extends Vue {
  mounted() {
    this.$store.dispatch("fetchOrders");
  }
}
</script>

<style>
.sms-header {
  border-bottom: 1px solid rgb(160, 207, 255);
}

.sms-header h2 {
  color: #303133;
}
</style>
