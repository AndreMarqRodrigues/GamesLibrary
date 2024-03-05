<template>
    <section class="vh-100">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/slate/bootstrap.min.css" integrity="sha384-8iuq0iaMHpnH2vSyvZMSIqQuUnQA7QM+f6srIdlgBrTSEyd//AWNMyEaSF2yPzNQ" crossorigin="anonymous">
  <div class="container-fluid h-custom">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col-md-9 col-lg-6 col-xl-5">
        <img src="../assets/LogoForHomeVue.png" class="img-fluid" style="border-radius: 25rem;">
      </div>
      <div class="col-md-8 col-lg-6 col-xl-4 offset-xl-1">
        <form>
            <p class="lead fw-normal mb-0 me-3" style="padding-bottom: 10px;">Sign in:</p>

          <!-- Email input -->
          <div class="form-outline mb-4">
            <input type="email" id="form3Example3" class="form-control form-control-lg"
              placeholder="Enter a valid email address" v-model="user.email"/>
            <label class="form-label" for="form3Example3">Email address</label>
          </div>

          <!-- Password input -->
          <div class="form-outline mb-3">
            <input type="password" id="form3Example4" class="form-control form-control-lg"
              placeholder="Enter password" v-model="user.password"/>
            <label class="form-label" for="form3Example4">Password</label>
          </div>

          <div class="d-flex justify-content-between align-items-center">
            <!-- Checkbox -->
            <div class="form-check mb-0">
              <input class="form-check-input me-2" type="checkbox" value="" id="form2Example3" />
              <label class="form-check-label" for="form2Example3">
                Remember me
              </label>
            </div>
            <a href="#!" class="text-body">Forgot password?</a>
          </div>

          <div class="text-center text-lg-start mt-4 pt-2">
            <button type="button" class="btn btn-primary btn-lg"
              style="padding-left: 2.5rem; padding-right: 2.5rem;"
              @click="login">Login</button>
            <p class="small fw-bold mt-2 pt-1 mb-0">Don't have an account?
              <router-link to="/register" class="link-danger">Register</router-link>
            </p>
          </div>

        </form>
      </div>
    </div>
  </div>
  <div
    class="d-flex flex-column flex-md-row text-center text-md-start justify-content-between py-4 px-4 px-xl-5 bg-primary">
    <!-- Copyright -->
    <div class="text-white mb-3 mb-md-0">
      Copyright © 2020. All rights reserved.
    </div>
    <!-- Copyright -->

    <!-- Right -->
    <div>
      <a href="#!" class="text-white me-4">
        <i class="fab fa-facebook-f"></i>
      </a>
      <a href="#!" class="text-white me-4">
        <i class="fab fa-twitter"></i>
      </a>
      <a href="#!" class="text-white me-4">
        <i class="fab fa-google"></i>
      </a>
      <a href="#!" class="text-white">
        <i class="fab fa-linkedin-in"></i>
      </a>
    </div>
    <!-- Right -->
  </div>
</section>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            user: {
                email: '',
                password: ''
            }
        };
    },
    methods: {
        async login() {
            try {
                const response = await axios.post('http://localhost:5000/login', this.user);
                // Store the access token in the browser's localStorage.
                localStorage.setItem('access_token', response.data.access_token);
                console.log('access_token', response.data.access_token);
                // Use Vue Router for redirection
                this.$router.push({ name: 'Games' });
                // Setting it globally
axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('access_token')}`;
            } catch (error) {
                // Handle error (e.g., show error message)
            }
        }
    }, goToRegister(){
      console.log("This button is working")
      this.$router.push({ name: 'Register' });
    }
}
</script>

<style>
.divider:after,
.divider:before {
content: "";
flex: 1;
height: 1px;
background: #eee;
}
.h-custom {
height: calc(100% - 73px);
}
@media (max-width: 450px) {
.h-custom {
height: 100%;
}
}
</style>