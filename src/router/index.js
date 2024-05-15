import { createRouter, createWebHistory } from 'vue-router'
import LoginView from "../components/LoginView.vue"
import ListeEmployes from "../views/EmployeeList.vue"

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'Login',
      component: LoginView
    },
    {
      path: '/employeelist',
      name: 'EmployeeList',
      component: ListeEmployes
    }
  ]
})

export default router
