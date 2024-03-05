<template>
    <section class="vh-100" style="background-color: rgba(39,43,48,255)">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/slate/bootstrap.min.css" integrity="sha384-8iuq0iaMHpnH2vSyvZMSIqQuUnQA7QM+f6srIdlgBrTSEyd//AWNMyEaSF2yPzNQ" crossorigin="anonymous">
  <div class="container h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col-lg-12 col-xl-11">
        <div class="card text-black" style="border-radius: 25px;">
          <div class="card-body p-md-5">
            <div class="row justify-content-center">
              <div class="col-md-10 col-lg-6 col-xl-5 order-2 order-lg-1">
                <p class="text-center h1 fw-bold mb-5 mx-1 mx-md-4 mt-4" style="color: #eee;">Sign up</p>
                <form class="mx-1 mx-md-4">
                  <div class="d-flex flex-row align-items-center mb-4">
                    <i class="fas fa-user fa-lg me-3 fa-fw"></i>
                    <div class="form-outline flex-fill mb-0">
                        <label class="form-label" for="form3Example1c" style="color: #eee;">Your Name:</label>
                      <input type="text" id="form3Example1c" class="form-control"  v-model="user.name"  />
                    </div>
                  </div>
                  <div class="d-flex flex-row align-items-center mb-4">
                    <i class="fas fa-envelope fa-lg me-3 fa-fw"></i>
                    <div class="form-outline flex-fill mb-0">
                      <label class="form-label" for="form3Example3c" style="color: #eee;">Your Email:</label>
                      <input type="email" id="form3Example3c" class="form-control" v-model="user.email" />
                    </div>
                  </div>
                  <div class="d-flex flex-row align-items-center mb-4">
                    <i class="fas fa-lock fa-lg me-3 fa-fw"></i>
                    <div class="form-outline flex-fill mb-0">
                        <label class="form-label" for="form3Example4c" style="color: #eee;">Password:</label>
                      <input type="password" id="form3Example4c" class="form-control" v-model="user.password"/>
                    </div>
                  </div>
                  <div class="d-flex flex-row align-items-center mb-4">
                    <i class="fas fa-key fa-lg me-3 fa-fw"></i>
                    <div class="form-outline flex-fill mb-0">
                      <label class="form-label" for="form3Example4cd" style="color: #eee;">Repeat your password</label>
                      <input type="password" id="form3Example4cd" class="form-control" v-model="user.confirmPassword" />
                    </div>
                  </div>
                  <div class="d-flex justify-content-center mx-4 mb-3 mb-lg-4">
                    <button type="button" class="btn btn-primary btn-lg" @click="register">Register</button>
                  </div>
                </form>
              </div>
              <div class="col-md-10 col-lg-6 col-xl-7 d-flex align-items-center order-1 order-lg-2">
                <img src="../assets/LogoForRegisterVue.png" class="img-fluid" style="border-radius: 25rem;">
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            user: {
                name: '',
                email: '',
                password: '',
                confirmPassword: ''
            },
            errors:{
              email: '',
              password: ''
            }
        };
    },
    methods: {
    validateEmail(email) {
      const re = /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/;
      return re.test(email);
    },
    async register() {
      // Reset error messages
      this.errors.email = '';
      this.errors.password = '';

      // Validate email
      if (!this.validateEmail(this.user.email)) {
        this.errors.email = 'Invalid email format';
      }

      // Validate password length
      if (this.user.password.length < 8) {
        this.errors.password = 'Password must be at least 8 characters long';
      }

      // Check for any validation errors
      if (this.errors.email || this.errors.password) {
        return; // Stop the registration process
      }
      if (this.user.password !== this.user.confirmPassword) {
        alert("Passwords do not match!");
        return;
      }
    try {
        console.log("Attempting to register...");
        await axios.post('http://localhost:5000/register', {
            name: this.user.name,
            email: this.user.email,
            password: this.user.password,
        });
        // Handle success (e.g., redirect to login page)
        console.log("Registration successful, redirecting to login...");
        this.$router.push({ name: 'login' });
    } catch (error) {
        // Improved error handling
        if (error.response && error.response.data && error.response.data.msg) {
            console.error("Error during registration:", error.response.data.msg);
            alert(error.response.data.msg); // Show the error message to the user
        } else {
            console.error("An unexpected error occurred:", error);
            alert("An unexpected error occurred. Please try again later.");
        }
    }
}
}
}
</script>

<style>

</style>