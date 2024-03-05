<template>
    <div class="home-page">
      <nav class="navbar">
        <div class="title">TITLE</div>
        <div class="nav-links">
          <router-link to="/login">LOGIN</router-link>
          <router-link to="/about">ABOUT US</router-link>
          <router-link to="/contact">CONTACT</router-link>
        </div>
      </nav>
      
      <div class="main-content">
        <h1 class="main-title">TITLE TITLE TITLE</h1>
        <p class="slogan">THIS IS A SLOGAN AND RESUMES THE WEBPAGE</p>
        <router-link to="/register">
          <button class="create-account-btn">CREATE AN ACCOUNT!</button>
        </router-link>
      </div>
      
      <div class="side-content">
        <p>THIS WILL BE AN IMG.THIS WILL BE AN IMG.THIS WILL BE AN IMG...</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'HomePage'
    // Your script part
  }
  </script>
  
  <style scoped>
  .home-page {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
  }
  
  .navbar {
    display: flex;
    justify-content: space-between;
    padding: 1rem;
    width: 100%;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }
  
  .nav-links a {
    margin: 0 1rem;
    text-decoration: none;
    color: #333;
  }
  
  .main-content {
    margin: 2rem 0;
  }
  
  .main-title {
    font-size: 3rem;
    margin-bottom: 1rem;
  }
  
  .slogan {
    margin-bottom: 2rem;
  }
  
  .create-account-btn {
    padding: 0.5rem 1rem;
    background-color: yellow;
    border: none;
    cursor: pointer;
    font-size: 1rem;
  }
  
  .side-content {
    background-color: #000;
    color: #fff;
    padding: 2rem;
    width: 50%;
    /* Adjust the size accordingly */
    margin: auto;
    text-align: left;
  }
  </style>