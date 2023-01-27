<template>
    <div class="row container-fluid">

        <div class="col-lg-9">
            <div class="container shopcard">

                <div v-if="books.length" v-for="book in books" class="card mx-auto mb-3" style="max-width: 840px;">
                    <div class="row g-0">
                        <div class="col-md-4">
                            <img :src="`http://127.0.0.1:8000${book.cover}`" class="w-100 img-fluid rounded-start" width="500px">
                        </div>
                        <router-link :to="`/product/${book.slug}`" class="col-md-8 text-muted">
                            <div class="card-body">
                                <h5 class="card-title">{{book.title}}</h5>
                                <p class="card-text">{{book.description}}</p>
                                <p class="card-text"><small>${{book.price}}</small></p>
                            </div>
                        </router-link>
                        <button @click="removeFromShopCard(book.slug)" class="btn btn-danger mt-4" id="removeShopCardButton">Remove from shop card</button>
                    </div>
                </div>  

                <div v-if="!books.length" class="alert alert-warning">No Books For Show</div>       

            </div>  
        </div>

        <div class="col-lg-3 mt-5">
            <div class="card sticky-lg-top shop-card">
                <div class="card-body">
                    <h5 class="card-title">Total price: ${{total_price}}</h5>
                    <button @click="payMent()" class="btn btn-primary card-link w-100">PAY</button>
                </div>
            </div>
        </div>

    </div>
      
</template>


<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import Swal from 'sweetalert2'


export default {
    name: "ShopCard",
    setup() {
		let books = ref("")
		let total_price = ref("")
        let i = ref()

        function getShopCard(){
            axios
                .post('ShowShopcard/')
                .then(response => {
                    books.value = response.data.data
                    total_price.value = response.data.total_price
                })
                .catch(error => {
                    console.log(error.response)
                })
        }
    
  	    onMounted(() => {
            getShopCard()
        })

        function removeFromShopCard(slug){
            axios
            .put('RemoveFromShopcard/', {
                slug: slug
            })
            .then(response => {
                getShopCard()
            })
            .catch(error => {
                console.log(error.response)
            })

        }


        function payMent(){
            if(total_price.value == 0){
                Swal.fire({
                    title: 'OOOPPPSSS!',
                    text:   "Your shop card is empty",
                    icon: 'warning',
                });
            }else {
                Swal.fire({
                    title: 'YEYY!',
                    text:   "Your books will send to you soon.",
                    icon: 'success',
                });
                for (let i = 0; i < books.value.length; i++) {
                    let slg = books.value[i].slug
                    removeFromShopCard(slg)
                }
            }
        }    
  	    return {
			books,
            total_price,
            removeFromShopCard,
            payMent,
  	    }
    }
  
};
</script>



<style scoped>
.shopcard{
    margin-top: 7rem;
}

a {
    text-decoration: none;
}

.text-muted:hover {
    color: blueviolet !important;
}

.shop-card{
    top: 75px;
}
</style>