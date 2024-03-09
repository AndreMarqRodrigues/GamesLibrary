<template>
  <div class="home-page">
    <navBarVue/>
    <div class="home-page content">
    <div class="content-wrapper">
      <div class="text-content">
        <h1 class="main-title">GAMINGLIB</h1>
        <p class="slogan">Get all your gaming history together. Fuse all your libraries!</p>
        <router-link to="/register">
          <button class="create-account-btn">CREATE AN ACCOUNT!</button>
        </router-link>
      </div>
      <div class="image-content">
        <img src="../assets/HomePageImg.png">
      </div>
    </div>
  </div>
  </div>
</template>
  
<script>
import navBarVue from './navBarNotLogged.vue';
export default {
  name: 'Home',
  components:{
    navBarVue
  }
}
</script>

  
<style scoped>
.home-page {
  background-image: url('@/assets/HomePageBG.png');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  height: 100vh;
  width: 100%;
  display: flex;
}
.home-page-content{
  align-items: center;
  justify-content: center;
  text-align: center;
  margin: 0;
  padding: 0;

}

img, svg {
    vertical-align: middle;
    border-radius: 25rem;
}

.content-wrapper {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%; 
}

.text-content {
  flex: 1;
  margin-right: 10rem;
  margin-left: 10rem;
  background-color: rgba(66,72,79,0.8);
  border-radius: 25px; 
}

.image-content {
  flex: 1;
}


.main-title {
  font-weight: 700;
  color: yellow;
  font-size: 7.5rem;
  margin-bottom: 1rem;
  margin-left: 10rem;
}

.slogan {
  font-weight: 700;
  color:white;
  font-size: 1.3rem;
  margin-bottom: 2rem;
  margin-left: 10rem;
}

.create-account-btn {
  padding: 0.5rem 1rem;
  background-color: yellow;
  border: none;
  cursor: pointer;
  font-size: 1rem;
  font-weight: bold;
  margin-bottom: 2rem;
  margin-left: 25rem;
}
</style>