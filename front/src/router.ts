import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)


export default new Router({
  scrollBehavior: (to, from, savedPosition) => {
    if (savedPosition) {
      return savedPosition
    } else {
      return { x: 0, y: 0 }
    }
  },
  routes: [
    {
      path: "/",
      redirect: "/sms",
    },
    {
      path: "/sms",
      component: () => import(/* webpackChunkName: "sms" */ "@/views/SMS.vue"),
    },
    {
      path: "/estoque",
      component: () => import(/* webpackChunkName; "estoque: */ "@/views/Estoque.vue")
    }
  ]
})
