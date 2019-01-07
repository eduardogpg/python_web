import Vue from 'vue'
import Router from 'vue-router'

import Main from '@/components/Main'
import Books from '@/components/Books'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'main',
      component: Main
    },
    {
      path: '/books',
      name: 'books',
      component: Books
    }
  ],
  mode: 'history'
})
