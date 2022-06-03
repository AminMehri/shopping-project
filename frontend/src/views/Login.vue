<template>
    <div class="container" id="register-card">
        <div class="card mx-auto mw-100 shadow-lg" style="width: 40rem;">
            <div class="card-title">
                <div class="d-flex justify-content-center">
					<h2 class="font-weight-bold mr-2 px-3" style="color:#16151a; background-color:#957bda" > P </h2>
					<h2 style="color: #957bda">HILOSOPHY</h2>
				</div>
            </div>
            <form @submit.prevent="doLogin">
                <div class="card-body">
                    <div class="form-group">
                        <label for="exampleUsername">Username</label>
                        <input 
                            type="text" 
                            class="form-control" 
                            id="exampleUsername" 
                            placeholder="Enter username" 
                            v-model="username"
                            :class="{'is-invalid':usernameE===true, 'is-valid':usernameE===false}"
                        >
                        <div class="invalid-feedback">
                            {{ usernameEM }}
                        </div>
                    </div>

                    <div class="form-group my-4">
                        <label for="exampleInputPassword1">Password</label>
                        <input 
                            type="password" 
                            class="form-control" 
                            id="exampleInputPassword1" 
                            placeholder="Password" 
                            v-model="password"
                            :class="{'is-invalid':passwordE===true, 'is-valid':passwordE===false}"
                        >
                        <div class="invalid-feedback">
                            {{ passwordEM }}
                        </div>
                    </div>


                    <button type="submit" class="btn btn-success">Sign in</button>

                    <p class="mt-3"><router-link to="/register" class="text-decoration-none">I haven't any account</router-link></p>
                    <p class="mt-3"><a href="#" class="text-decoration-none" data-bs-toggle="modal" data-bs-target="#resetBackdrop">I forgot my password</a></p>
                </div>
            </form>

            <div class="modal fade" id="resetBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="resetBackdropLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="resetBackdropLabel">Reset password</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">


                            <div class="row g-3">

                            <div class="col-md-12">
                                <label for="inputResetPasswordEmail" class="form-label">Email</label>
                                <input v-model="resetPasswordEmail" type="text" class="form-control" id="inputResetPasswordEmail" >
                            </div>
                                
                            </div>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            <button @click="resetPassword()" class="btn fw-bold bg-success">Submit</button>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>

<script>
import { useStore } from 'vuex'
import { useRoute, useRouter } from 'vue-router'
import { onMounted, ref } from "vue";
import axios from 'axios'
import Swal from 'sweetalert2'


export default {
	setup() {
        const store = useStore()
        const route = useRoute()
        const router = useRouter()

        let username = ref('')
        let password = ref('')
        let usernameE = ref()
        let usernameEM = ref('')
        let passwordE = ref()
        let passwordEM = ref('')


        let resetPasswordEmail = ref()

        onMounted(() => {
            console.log(store.state.isAuthenticated)
            if(store.state.isAuthenticated){
                router.push('/profile')
            }
        })


        function doLogin() {
            let access = true
            if(username.value.length < 5){
                usernameE.value = true
                access = false
                if(username.value.length == 0){
                    usernameEM.value = 'Username required.'
                } else {
                    usernameEM.value = 'Username must be more than 4 charactors.'
                }
            } else {
                usernameE.value = false
                usernameEM.value = ''
            }

            if(password.value.length < 8){
                passwordE.value = true
                access = false
                if(password.value.length == 0){
                    passwordEM.value = 'Password required.'
                } else {
                    passwordEM.value = 'Password must be more than 7 charactors.'
                }
            } else {
                passwordE.value = false
                passwordEM.value = ''
            }

            if(access){

                axios
                    .post('dj-rest-auth/login/', {
                        username: username.value,
                        password: password.value
                    })
                    .then(response => {
                        store.commit('login', response.data.access_token)
                        router.push('/profile')
                    })
                    .catch(error => {
                        usernameEM.value = error.response.data.non_field_errors.join(" ")
                        usernameE.value = true
                        passwordE.value = true
                    })

            }
            
        }


        function resetPassword() {
            axios
                .post('dj-rest-auth/password/reset/', {
                    email: resetPasswordEmail.value
                })
                .then(response => {
                    Swal.fire({
                        title: 'YEEY',
                        text:   "We sent you an email. Please check!",
                        icon: 'success',
                    });
                })
                .catch(error => {
                    console.log(error.response)
                })
        }


        return {
            doLogin,
            username,
            password,
            usernameE,
            usernameEM,
            passwordE,
            passwordEM,
            resetPassword,
            resetPasswordEmail,

        }
	},
}

</script>




<style scoped>
#register-card{
    margin-top: 7rem;
}
</style>