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

                    <div class="form-group my-4">
                        <label for="exampleInputPassword2">Repeat password</label>
                        <input 
                            type="password" 
                            class="form-control" 
                            id="exampleInputPassword2" 
                            placeholder="Repeat password" 
                            v-model="password2"
                            :class="{'is-invalid':password2E===true, 'is-valid':password2E===false}"
                        >
                        <div class="invalid-feedback">
                            {{ password2EM }}
                        </div>
                    </div>


                    <button type="submit" class="btn btn-success">Sign in</button>

                    <p class="mt-3"><router-link to="/register" class="text-decoration-none">I haven't any account</router-link></p>
                </div>
            </form>
        </div>
    </div>
</template>


<script>
import { useStore } from 'vuex'
import { useRoute, useRouter } from 'vue-router'
import { ref } from "vue";
import axios from 'axios'

export default {
	setup() {
        const store = useStore()
        const route = useRoute()
        const router = useRouter()

        let username = ref('')
        let password = ref('')
        let password2 = ref('')
        let usernameE = ref()
        let usernameEM = ref('')
        let passwordE = ref()
        let password2E = ref()
        let passwordEM = ref('')
        let password2EM = ref('')


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

            if(password2.value.length < 8){
                password2E.value = true
                access = false
                if(password2.value.length == 0){
                    password2EM.value = 'Repeat password required.'
                } else {
                    password2EM.value = 'Repeat password must be more than 7 charactors.'
                }
            } else {
                password2E.value = false
                password2EM.value = ''
            }

            if(password.value != password2.value){
                access = false
                passwordE.value = true
                password2E.value = true
                passwordEM.value = 'Password and repeat password are not same'
            } else {
                if(!passwordE.value && password2E.value) {
                    access = true
                }
            }

            if(access){

                axios
                    .post('dj-rest-auth/registration/', {
                        username: username.value,
                        password1: password.value,
                        password2: password2.value,
                    })
                    .then(response => {
                        router.push('/login')
                    })
                    .catch(error => {
                        console.log(error.response)
                        if(error.response.data.username) {
                            usernameE.value = true
                            usernameEM.value = error.response.data.username.join(" ")
                        } else if(error.response.data.password1){
                            passwordE.value = true
                            password2E.value = true
                            passwordEM.value = error.response.data.password1.join(" ")
                        }
                    })

            }
            
        }


        return {
            doLogin,
            username,
            password,
            password2,
            usernameE,
            usernameEM,
            passwordE,
            password2E,
            passwordEM,
            password2EM,
        }
	},
}

</script>


<style scoped>
#register-card{
    margin-top: 7rem;
}
</style>