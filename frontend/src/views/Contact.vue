<template>
    <div class="container Contact">
        <section class="mb-4">

            <div class="row">

                <div class="col-md-9 mb-md-0 mb-5">
                    <form id="contact-form">

                        <div class="row">

                            <div class="col-md-6">
                                <div class="form-floating mb-3">
                                    <input type="name" class="form-control" id="nameInput" placeholder="example">
                                    <label for="nameInput">Your name</label>
                                </div>
                            </div>

                            <div class="col-md-6">
                                <div class="form-floating mb-3">
                                    <input type="email" class="form-control" id="emailInput" placeholder="name@example.com">
                                    <label for="emailInput">Email address</label>
                                </div>
                            </div>

                        </div>

                        <div class="row">
                            <div class="col-md-12">
                                <div class="form-floating mb-3">
                                    <input type="text" class="form-control" id="subjectInput" placeholder="example">
                                    <label for="subjectInput">Subject</label>
                                </div>
                            </div>
                        </div>

                        <div class="row">

                            <div class="col-md-12">

                                <div class="form-floating mb-3">
                                    <textarea class="form-control" placeholder="Leave a message here" id="textareaInput" style="height: 100px"></textarea>
                                    <label for="textareaInput">Your message</label>
                                </div>

                            </div>
                        </div>

                    </form>

                    <div class="text-center text-md-left">
                        <a @click="sendMessage()" class="btn btn-primary">Send</a>
                    </div>
                    <div class="status"></div>
                </div>
                <!--Grid column-->

                <!--Grid column-->
                <div class="col-md-3 text-center">
                    <ul class="list-unstyled mb-0">
                        <li><svg xmlns="http://www.w3.org/2000/svg" width="45" height="45" fill="currentColor" class="bi bi-geo-alt-fill" viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
                            <p>Mashhad, IR</p>
                        </li>

                        <li><svg xmlns="http://www.w3.org/2000/svg" width="45" height="45" fill="currentColor" class="bi bi-telephone-fill" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1.885.511a1.745 1.745 0 0 1 2.61.163L6.29 2.98c.329.423.445.974.315 1.494l-.547 2.19a.678.678 0 0 0 .178.643l2.457 2.457a.678.678 0 0 0 .644.178l2.189-.547a1.745 1.745 0 0 1 1.494.315l2.306 1.794c.829.645.905 1.87.163 2.611l-1.034 1.034c-.74.74-1.846 1.065-2.877.702a18.634 18.634 0 0 1-7.01-4.42 18.634 18.634 0 0 1-4.42-7.009c-.362-1.03-.037-2.137.703-2.877L1.885.511z"/></svg>
                            <p>+ 98 915 231 44**</p>
                        </li>

                        <li><svg xmlns="http://www.w3.org/2000/svg" width="45" height="45" fill="currentColor" class="bi bi-envelope-fill" viewBox="0 0 16 16"><path d="M.05 3.555A2 2 0 0 1 2 2h12a2 2 0 0 1 1.95 1.555L8 8.414.05 3.555ZM0 4.697v7.104l5.803-3.558L0 4.697ZM6.761 8.83l-6.57 4.027A2 2 0 0 0 2 14h12a2 2 0 0 0 1.808-1.144l-6.57-4.027L8 9.586l-1.239-.757Zm3.436-.586L16 11.801V4.697l-5.803 3.546Z"/></svg>
                            <p>aminmehri45@gmail.com</p>
                        </li>
                    </ul>
                </div>
                <!--Grid column-->

            </div>

        </section>
    </div>
</template>


<script>
import Swal from 'sweetalert2'
import { ref } from "vue";


export default{
    setup() {
        function sendMessage() {
            if(document.getElementById('nameInput').value.length != 0 && document.getElementById('emailInput').value.length != 0 && document.getElementById('subjectInput').value.length != 0 && document.getElementById('textareaInput').value.length != 0){
                Swal.fire({
                    title: 'YEEY',
                    text:   "Your message sent to us successfuly. Thanks. Be in touch!",
                    icon: 'success',
                });

                location.reload()
            }else {
                Swal.fire({
                    title: 'SHIIIT!',
                    text:   "Please enter your information correctly!",
                    icon: 'warning',
                });
            }
            
        }


        return{
            sendMessage,
        }
    },
}
</script>




<style scoped>
.Contact {
    margin-top: 8rem;
}

</style>
