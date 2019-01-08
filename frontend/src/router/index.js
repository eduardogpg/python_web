import Vue from 'vue'
import Router from 'vue-router'

import Main from '@/components/Main'
import Books from '@/components/Books'
import Home from '@/components/Home'
import About from '@/components/About'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'main',
      component: Main
    },
    {
      path: '/home',
      name: 'home',
      component: Home,
    },
    {
      path: 'about',
      name: 'about',
      component: About,
    },
    {
      path: '/books',
      name: 'books',
      component: Books
    }
  ],
  mode: 'history'
})
