<template>
    <div class="container-fluid Detail">

        <div class="row">
            <div class="col-md-6">
                <h3 class="ms-5">{{book.title}}</h3>
                <p class="ms-5">{{book.content}}</p>
            </div>
            <div class="col-md-6">
                <img :src="`http://127.0.0.1:8000${book.image}`" class="w-100 img-fluid" width="600px">
            </div>
            <div class="col-lg-3 mt-5">
                <div class="card sticky-lg-top shop-card">
                    <div class="card-body">
                        <h5 class="card-title">{{book.title}}</h5>
                        <p class="card-text">Price: ${{book.price}}</p>
                        <button v-if="showAddToShopCard && $store.state.isAuthenticated" @click="addToCardShop()" class="btn btn-primary card-link">Add to your shop card</button>
                        <button v-if="!$store.state.isAuthenticated" class="btn btn-warning card-link">Please login</button>
                        <button v-if="!showAddToShopCard" class="btn btn-info card-link">Already in your shop card</button>
                    </div>
                </div>
            </div>
            <div class="col-lg-8 text-center mt-5">
                <p>{{book.about_book}}</p>
            </div>
            <div class="col-lg-1"></div>
        </div>

        <h3 class="ms-5">Related <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-arrow-right-circle-fill" viewBox="0 0 16 16"><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0zM4.5 7.5a.5.5 0 0 0 0 1h5.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5H4.5z"/></svg></h3>

    </div>
</template>


<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRoute } from 'vue-router'

export default {
    name: "Detail",
    setup() {
        const route = useRoute();
		let book = ref("")
        let slug = ref("")
        slug.value = route.params.slug
        let showAddToShopCard = ref(true)





        function addToCardShop(){
            axios
                .post('AddToShopcard/', {
                    slug: slug.value
                })
                .then(response => {
                    if(response.status == 200){
                        showAddToShopCard.value = false
                    }
                })
                .catch(error => {
                    showAddToShopCard.value = true
                    console.log(error.response)
                })
        }

        
  	    onMounted(() => {
            axios
                .post('ShowDetailBook/', {
                    slug: slug.value
                })
                .then(response => {
                    book.value = response.data.data[0]
                    
                    document.documentElement.scrollTop = 0;
                })
                .catch(error => {
                    console.log(error.response)
                })

            axios
                .post('ShowShopcard/')
                .then(response => {
                    for (let i = 0; i < response.data.data.length; i++) {
                        if(response.data.data[i].slug == slug.value){
                            showAddToShopCard.value = false
                        }
                    }
                })
                .catch(error => {
                    console.log(error.response)
                })
        })

        
    
  	    return {
			book,
            addToCardShop,
            showAddToShopCard,
  	    }
    }
  
};
</script>


<style scoped>
.Detail {
    margin-top: 7rem;
}

.shop-card{
    top: 75px;
}

a {
	text-decoration: none;
}

</style>