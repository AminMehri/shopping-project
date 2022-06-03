<template>
    <div class="container Password-Reset-Confirm">
        <p>you are a wancki, basterd!</p>
        <p>you fucking idiot forgot your password</p>
        <p>what a dick!!!</p>
        <p>hey asshole!</p>
        <p>click below button</p>
        <button class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#resetPasswordBackdrop">I forgot my password</button>

        <div class="modal fade" id="resetPasswordBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="resetPasswordBackdropLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="resetPasswordBackdropLabel">Reset password</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">


                            <div class="row g-3">

                            <div class="col-md-12">
                                <label for="inputResetPassword1" class="form-label">New password</label>
                                <input v-model="resetPassword1" type="text" class="form-control" id="inputResetPassword1" >
                            </div>

                            <div class="col-md-12">
                                <label for="inputResetPassword2" class="form-label">New password confirm</label>
                                <input v-model="resetPassword2" type="text" class="form-control" id="inputResetPassword2" >
                            </div>
                                
                            </div>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" id="close_modal">Close</button>
                            <button @click="resetPasswordConfirm()" class="btn fw-bold bg-success">Submit</button>
                        </div>
                    </div>
                </div>
            </div>
    </div>
</template>

<script>
import { useRoute, useRouter } from 'vue-router'
import { ref } from "vue";
import axios from 'axios'
import Swal from 'sweetalert2'


export default {
	setup() {
        const route = useRoute()
        const router = useRouter()

        let resetPassword1 = ref()
        let resetPassword2 = ref()

        let uid = ref(route.params.uid)
        let token = ref(route.params.token)


        function resetPasswordConfirm(){
            axios
                .post(`dj-rest-auth/password/reset/confirm/${uid.value}/${token.value}/`, {
                    new_password1: resetPassword1.value,
                    new_password2: resetPassword2.value,
                    uid: uid.value,
                    token: token.value
                })
                .then(response => {
                    document.getElementById('close_modal').click()
                    Swal.fire({
                        title: 'YEEY',
                        text:   "Your password has been reset. Please login!",
                        icon: 'success',
                    });
                    router.push('/login')
                })
                .catch(error => {
                    Swal.fire({
                        title: 'OPPS',
                        text:   "Please enter your information corrently",
                        icon: 'warning',
                    });
                })
        }


        return {
            resetPasswordConfirm,
            resetPassword1,
            resetPassword2,
        }
	},
}

</script>




<style scoped>
.Password-Reset-Confirm{
    margin-top: 7rem;
}
</style>