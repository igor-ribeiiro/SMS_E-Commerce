import Vue from 'vue'
import Vuex from 'vuex'

import { fetchOrders, finishOrder } from "@/api/orders"
import { fetchStore } from '@/api/store';
import { IOrder, IStoreItem, IOrders } from "@/api/types";

Vue.use(Vuex)

export interface IRootState {
  orders: IOrders;
  store: IStoreItem[];
}

export interface ILoginForm {
  username: string,
  password: string,
}

export default new Vuex.Store<IRootState>({
  state: {
    orders: {
      delivery: [],
      stored: []
    },
    store: []
  },

  actions: {
    async fetchStore({ dispatch, commit }) {
      const store = fetchStore();

      setTimeout(() => dispatch('fetchStore'), 10 * 1000);

      commit('setStore', await store);
    },

    async fetchOrders({ dispatch, commit }) {
      const orders = fetchOrders();

      setTimeout(() => dispatch('fetchOrders'), 5 * 1000);

      commit('setOrders', await orders);

    },

    async finishOrder({ commit }, order: IOrder) {
      if (order.enviado) return;

      const finish = finishOrder(order);
      commit('setFinishedOrder', order);

      await finish;
    }
  },

  getters: {
    deliveryOrders(state) {
      return state.orders.delivery;
    },
    storedOrders(state) {
      return state.orders.stored;
    },
  },

  mutations: {
    setFinishedOrder(state, order: IOrder) {
      const update = (o: IOrder) => o.id === order.id ? { ...order, enviado: true } : o;

      if (order.endereco) {
        const delivery = state.orders.delivery.map(update);
        state.orders = { ...state.orders, delivery };
      } else {
        const stored = state.orders.stored.map(update);
        state.orders = { ...state.orders, stored };
      }
    },

    setOrders(state, orders: IOrders) {
      state.orders = orders;
    },

    setStore(state, items: IStoreItem[]) {
      state.store = items;
    }
  }
})
