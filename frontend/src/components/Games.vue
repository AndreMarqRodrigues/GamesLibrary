<template>
  <div class="jumbotron vertical-center">
    <div class="container">

      <!--bootswatch CDN-->
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/slate/bootstrap.min.css" integrity="sha384-8iuq0iaMHpnH2vSyvZMSIqQuUnQA7QM+f6srIdlgBrTSEyd//AWNMyEaSF2yPzNQ" crossorigin="anonymous">
      <div class="row">
        <div class="col-sm-12">
          <hr><br><h1 class="text-center bg-primary text-white" style="border-radius: 10px;">Games Library🕹️</h1>
          <!--Alert Message-->
          <div class="alert alert-success" role="alert" v-if="showMessage">{{ message }}</div>
          <!--Button to trigger modal-->
          <button type="button" class="btn btn-success" @click="showAddModal">
          Add Game
          </button>
          
          <br><br>
          <table class="table table-hover">
            <!--Table Head -->
            <thead>
              <tr>
                <!--Table header cells-->
                <th scope="col">Title</th>
                <th scope="col">Genre</th>
                <th scope="col">Played?</th>
                <th scope="col">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(game, index) in games" :key="index">
                <td>{{ game.title }}</td>
                <td>{{ game.genre }}</td>
                <td>{{ game.played ? 'Yes' : 'No' }}</td>
                <td>
                  <div class="btn-group" role="group">
                    <button type="button" class="btn btn-info btn-sm" @click="showEditModal(game)">Update</button>
                    <button type="button" class="btn btn-danger btn-sm" @click="deleteGame(game)">Delete</button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
          <footer class="bg-primary text-white text-center" style="border-radius: 10px;">Copyright &copy; All Rights Reserved 2024.</footer>
        </div>
      </div>
      <!-- Add Game Modal -->
      <div class="modal fade" id="addGameModal" tabindex="-1" aria-labelledby="addGameModalLabel" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="addGameModalLabel">Add a new game</h5>
              <button type="button" class="btn-close" @click="closeModal"></button>
            </div>
            <div class="modal-body">
              <form @submit.prevent="onSubmit">
                <!-- Title input -->
                <div class="mb-3">
                  <label for="add-title" class="form-label">Title:</label>
                  <input type="text" class="form-control" id="add-title" v-model="addGameForm.title" required>
                </div>
                <!-- Genre input -->
                <div class="mb-3">
                  <label for="add-genre" class="form-label">Genre:</label>
                  <input type="text" class="form-control" id="add-genre" v-model="addGameForm.genre" required>
                </div>
                <!-- Played checkbox -->
                <div class="mb-3 form-check">
                  <input type="checkbox" class="form-check-input" id="add-played" v-model="addGameForm.played">
                  <label class="form-check-label" for="add-played">Played?</label>
                </div>
                <!-- Submit and Reset buttons -->
                <button type="submit" class="btn btn-primary">Submit</button>
                <button type="button" class="btn btn-secondary" @click="closeModal">Cancel</button>
              </form>
            </div>
          </div>
        </div>
      </div>
      <!-- End of Add Game Modal -->

      <!-- Edit Game Modal -->
      <div class="modal fade" id="editGameModal" tabindex="-1" aria-labelledby="editGameModalLabel" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="editGameModalLabel">Update game</h5>
              <button type="button" class="btn-close" @click="closeEditModal"></button>
            </div>
            <div class="modal-body">
              <form @submit.prevent="onSubmitUpdate">
                <!-- Title input -->
                <div class="mb-3">
                  <label for="edit-title" class="form-label">Title:</label>
                  <input type="text" class="form-control" id="edit-title" v-model="editGameForm.title" required>
                </div>
                <!-- Genre input -->
                <div class="mb-3">
                  <label for="edit-genre" class="form-label">Genre:</label>
                  <input type="text" class="form-control" id="edit-genre" v-model="editGameForm.genre" required>
                </div>
                <!-- Played checkbox -->
                <div class="mb-3 form-check">
                  <input type="checkbox" class="form-check-input" id="edit-played" v-model="editGameForm.played">
                  <label for="edit-played" class="form-check-label">Played?</label>
                </div>
                <!-- Submit and Reset buttons -->
                <button type="submit" class="btn btn-info">Update</button>
                <button type="button" class="btn btn-secondary" @click="closeEditModal">Cancel</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { nextTick } from 'vue';
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle.min.js';

export default {
  data() {
    return {
      games: [],
      showModal: false, //This is now used only for reactivity, not direct display control 
      addGameForm: {
        id: "",
        title: "",
        genre: "",
        played: false,
      },
      editGameForm: {
        id: "",
        title: "",
        genre: "",
        played: false,
      },
      showMessage: false,
      message: "",
    };
  },
  methods: {
    getGames() {
      const path = 'http://127.0.0.1:5000/games';
      axios.get(path).then(res => {
        this.games = res.data.games;
      }).catch(err => {
        console.error(err);
      });
    },
    showAddModal() {
      this.showModalMethod('addGameModal');
    },
    showEditModal(game) {
      console.log(game)
      this.editGameForm = { ...game };
      this.showModalMethod('editGameModal');
    },
    showModalMethod(modalId) {
      nextTick(() => {
        const myModal = new bootstrap.Modal(document.getElementById(modalId));
        myModal.show();
      });
    },
    closeModal() {
      // This function hides the modal 
      nextTick(() => {
        var myModalEl = document.getElementById('addGameModal');
        var modal = bootstrap.Modal.getInstance(myModalEl);
        if (modal){
          modal.hide();
        }
      })
    },
    closeEditModal() {
      // This function hides the modal 
      nextTick(() => {
        var myModalEl = document.getElementById('editGameModal');
        var modal = bootstrap.Modal.getInstance(myModalEl);
        if (modal){
          modal.hide();
        }
      })
    },
    addGame() {
      axios.post('http://127.0.0.1:5000/games', this.addGameForm)
        .then(() => {
          this.getGames();
          this.showMessage = true;
          this.message = "Game added successfully!";
          setTimeout(() => this.showMessage = false, 5000);
        }).catch(error => {
          console.error(error);
        });
    },
    updateGame() {
      const id = this.editGameForm.id;
      axios.put(`http://127.0.0.1:5000/games/${id}`, this.editGameForm)
        .then(() => {
          this.getGames();
          this.showMessage = true;
          this.message = "Game updated successfully!";
          setTimeout(() => this.showMessage = false, 5000);
        }).catch(error => {
          console.error(error);
        });
    },
    onSubmit() {
      this.addGame();
      this.closeModal();
    },
    onSubmitUpdate() {
      this.updateGame();
      this.closeEditModal();
    },
    //Delete Individual Game
    removeGame(gameID){
      console.log(gameID)
      const path = `http://127.0.0.1:5000/games/${gameID}`
      axios.delete(path).then(() => {
        this.getGames();
        this.message = "Game removed !";
        this.showMessage = true
        setTimeout(() => this.showMessage = false, 5000);
      })
      .catch((err) =>{
        console.log(err);
        this.getGames();
      })
    },
    // Handle delete button
    deleteGame(game){
      this.removeGame(game.id);
    }
  },
  created() {
    this.getGames();
  },
}
</script>