<template>
  <div class="container">
    <div class="row">
      <div class="col-3 offset-3">
        <span class="mdi mdi-book-open-variant"></span>
        <h1 class="main-title">LEAVE MANAGEMENT</h1>
      </div>
      <div class="col-9 offset-9">
        <div class="content">
          <h1 class="title">Login</h1>
          <div class="form-group">
            <label for="username">username</label>
            <input type="text" placeholder="username" id="username" v-model="username" autofocus required />
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input type="password" placeholder="Password" id="password" v-model="password" required />
          </div>
          <div class="split">
            <button class="btn btn-primary" @click="login">
              Connection
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  import axios from 'axios';
    data() {
    return {
      username: "",
      password: "",
    }
  },
  methods: {
    login() {
      let data = {
        "username": this.username,
        "password": this.password
      };
      axios.post("/login", data)
        .then((response) => {
          localStorage.setItem('user', JSON.stringify(response.data));
          this.$router.push({ name: 'EmployeeList' });
        })
        .catch((error) => {
          console.log(error);
        })
        .finally(() => {
          console.log("Always executed")
        })
      // localStorage.setItem("user", JSON.stringify(data))
    }
  }

};
</script>

<style scoped>
.row {
  display: flex;
}

.row>div {
  min-height: 100vh;
}

.col-3 {
  width: 25%;
  background: var(--color-primary);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.col-3 .mdi {
  font-size: 6em;
  color: var(--color-white);
}

.col-3 .main-title {
  color: var(--color-white);
  font-size: 2.5rem;
  text-transform: uppercase;
}

.col-9 {
  flex: 1 1;
  background: var(--color-background);
  display: flex;
  justify-content: center;
  align-items: center;
}

.col-9 .content {
  background: var(--color-white);
  padding: 3em;
  width: 26em;
  box-shadow: 0px 0px 15px 5px var(--color-grey),
    0 20px 20px var(--color-grey);
}

.col-9 .content .title {
  color: var(--color-primary);
  font-weight: 600;
  margin-bottom: 1.3em;
}

.col-9 .content .form-group,
.col-9 .content .form-check {
  margin-bottom: 1.5em;
}

.split {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
}

small {
  cursor: pointer;
}

@media (max-width: 40em) {
  .col-3 {
    display: none;
  }

  .col-9 .content {
    width: 23em;
  }
}
</style>