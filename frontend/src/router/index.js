import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import Contact from '../views/Contact.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Profile from '../views/Profile.vue'
import ShopCard from '../views/ShopCard.vue'
import Detail from '../views/Detail.vue'
import All_Categories from '../views/All_Categories.vue'
import Single_Category from '../views/Single_Category.vue'
import All_Authors from '../views/All_Authors.vue'
import Single_Author from '../views/Single_Author.vue'
import Password_Reset_Confirm from '../views/Password_Reset_Confirm.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/product/:slug',
    name: 'detail',
    component: Detail,
  },
  {
    path: '/about',
    name: 'about',
    component: About
  },
  {
    path: '/contact',
    name: 'contact',
    component: Contact
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
    meta: { loginRedirect: true }
  },
  {
    path: '/register',
    name: 'register',
    component: Register,
    meta: { loginRedirect: true }
  },
  {
    path: '/profile',
    name: 'profile',
    component: Profile,
    meta: { loginRequired: true }
  },
  {
    path: '/shopcard',
    name: 'shopcard',
    component: ShopCard,
    meta: { loginRequired: true }
  },
  {
    path: '/categories',
    name: 'all_categories',
    component: All_Categories,
  },
  {
    path: '/category/:slug',
    name: 'single_category',
    component: Single_Category,
  },
  {
    path: '/authors',
    name: 'all_authors',
    component: All_Authors,
  },
  {
    path: '/author/:slug',
    name: 'single_author',
    component: Single_Author,
  },
  {
    path: '/dj-rest-auth/password/reset/confirm/:uid/:token',
    name: 'password_reset_confirm',
    component: Password_Reset_Confirm,
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.loginRequired)) {
    if (store.state.isAuthenticated) {
      next()
    } else {
      next("/login")
    }
  }else if (to.matched.some(record => record.meta.loginRedirect)) {
    if (store.state.isAuthenticated) {
      next("/profile")
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router
