<template>
    <div class="container Profile">
        <p class="mx-auto w-25 alert alert-success p-4 text-center fw-bolder fs-3">Profile</p>
        <div class="row g-3">
            <div class="col-md-6">
                <label for="inputUserName" class="form-label">Username</label>
                <input type="text" class="form-control" id="inputUserName" disabled :value="`${username}`">
            </div>

            <div class="col-md-6">
                <label for="inputFullName" class="form-label">Full name</label>
                <input type="text" class="form-control" disabled :value="`${fullName}`" id="inputFullName" >
            </div>

            <div class="col-md-6">
                <label for="inputAddress" class="form-label">Address</label>
                <input type="text" class="form-control" disabled :value="`${address}`" id="inputAddress">
            </div>

            <div class="col-md-6">
                <label for="inputPhoneNumber" class="form-label">PhoneNumber</label>
                <input type="text" class="form-control" disabled :value="`${phoneNumber}`" id="inputPhoneNumber">
            </div>

            <div class="col-md-6">
                <label for="inputEmail" class="form-label">Email</label>
                <input type="text" class="form-control" disabled :value="`${email}`" id="inputEmail" >
            </div>

            <div class="col md-6"></div>

            <div class="col-md-6">
                <button class="btn fw-bold bg-danger" @click="doLogout">Logout</button>

                <button type="button" class="btn btn-primary mx-3" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
                    Change information
                </button>
                
                <button type="button" class="btn btn-dark" data-bs-toggle="modal" data-bs-target="#changepasswordBackdrop">
                    Change password
                </button>
            </div>
    
        </div>


        <div class="modal fade" id="changepasswordBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="changepasswordBackdropLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="changepasswordBackdropLabel">Change password</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">


                        <div class="row g-3">
                            <div class="col-md-6">
                                <label for="password1Name" class="form-label">Password</label>
                                <input v-model="changePassword1" type="text" class="form-control" id="password1Name">
                            </div>

                            <div class="col-md-6">
                                <label for="password2Name" class="form-label">Confirm password</label>
                                <input v-model="changePassword2" type="text" class="form-control" id="password2Name" >
                            </div>
                            
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button @click="changePassword()" class="btn fw-bold bg-success">Submit</button>
                    </div>
                </div>
            </div>
        </div>

        

        <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="staticBackdropLabel">Change information</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">


                        <div class="row g-3">
                            <div class="col-md-6">
                                <label for="inputUserName" class="form-label">Username</label>
                                <input type="text" class="form-control" id="inputUserName" disabled :value="`${username}`">
                            </div>

                            <div class="col-md-6">
                                <label for="inputFirstName" class="form-label">First name</label>
                                <input v-model="updateFirstName" type="text" class="form-control" id="inputFirstName" >
                            </div>

                            <div class="col-md-6">
                                <label for="inputLastName" class="form-label">Last name</label>
                                <input v-model="updateLastName" type="text" class="form-control" id="inputLastName" >
                            </div>

                            <div class="col-md-6">
                                <label for="inputAddress" class="form-label">Address</label>
                                <input v-model="updateAddress" type="text" class="form-control" id="inputAddress">
                            </div>

                            <div class="col-md-6">
                                <label for="inputPhoneNumber" class="form-label">PhoneNumber</label>
                                <input v-model="updatePhoneNumber" type="text" class="form-control" id="inputPhoneNumber">
                            </div>

                            <div class="col-md-6">
                                <label for="inputEmail" class="form-label">Email</label>
                                <input v-model="updateEmail" type="text" class="form-control" id="inputEmail" >
                            </div>

                            
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button @click="updateInfo" class="btn fw-bold bg-success">Submit</button>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>


<script>
import { ref, onMounted } from 'vue'
import { useStore } from 'vuex'
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios'
import Swal from 'sweetalert2'


export default {
	setup() {
        const store = useStore()
        const route = useRoute();
        const router = useRouter();

        let username = ref('')
        let fullName = ref('')
        let address = ref('')
        let phoneNumber = ref('')
        let email = ref('')


        let updateFirstName = ref('')
        let updateLastName = ref('')
        let updateAddress = ref('')
        let updatePhoneNumber = ref()
        let updateEmail = ref('')


        let changePassword1 = ref()
        let changePassword2 = ref()

        onMounted(() => {
            axios
                .get('ShowProfile/')
                .then(response => {
                    username.value = response.data[0].username
                    fullName.value = response.data[0].first_name + ' ' + response.data[0].last_name
                    address.value = response.data[0].address
                    phoneNumber.value = response.data[0].phone_number
                    email.value = response.data[0].email
                })
                .catch(error => {
                    console.log(error.response)
                    store.commit('logout')
                    router.push('/login')
                })
        })
        

        function doLogout() {
            axios
                .post('dj-rest-auth/logout/')
                .then(response => {
                    store.commit('logout')
                    router.push('/login')
                })
                .catch(error => {
                    console.log(error.response)
                })
        }


        function updateInfo(){
            axios
                .put('GetProfileInformation/', {
                    first_name: updateFirstName.value,
                    last_name: updateLastName.value,
                    email: updateEmail.value,
                    address: updateAddress.value,
                    phone_number: updatePhoneNumber.value
                })
                .then(response => {
                    console.log(response.data)
                    Swal.fire({
                        title: 'YEEY',
                        text:   "Your information changed successfully",
                        icon: 'success',
                    });
                    location.reload()
                })
                .catch(error => {
                    console.log(error.response)
                    Swal.fire({
                        title: 'OPPS',
                        text:   "Please enter your information corrently",
                        icon: 'warning',
                    });
                })

        }


        function changePassword(){
            axios
                .post('dj-rest-auth/password/change/', {
                    new_password1: changePassword1.value,
                    new_password2: changePassword2.value,
                })
                .then(response => {
                    console.log(response.data)
                    Swal.fire({
                        title: 'YEEY',
                        text:   "Your password changed successfully",
                        icon: 'success',
                    });
                    location.reload()
                })
                .catch(error => {
                    Swal.fire({
                        title: 'OPPS',
                        text:   "Please enter a valid password",
                        icon: 'warning',
                    });
                })
        }


		return {
			doLogout,
            username,
            fullName,
            address,
            phoneNumber,
            email,

            updateInfo,
            updateFirstName,
            updateLastName,
            updateAddress,
            updatePhoneNumber,
            updateEmail,

            changePassword,
            changePassword1,
            changePassword2,
		}
    
	},

}

</script>



<style scoped>
.Profile{
    margin-top: 7rem;
}
</style>