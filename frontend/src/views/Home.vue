<template>
	<div class="container-md Home">
		<div class="row">
			<div v-if="books.length" v-for="book in books" class="card-sl border-end border-start col-lg-4 col-md-6 col-sm-12">
				<div class="card-image">
					<img src="https://picsum.photos/400/200" width="400" height="200" />
				</div>

				<button class="card-action btn" id="shopcard">
					<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-cart-plus" viewBox="0 0 16 16"><path d="M9 5.5a.5.5 0 0 0-1 0V7H6.5a.5.5 0 0 0 0 1H8v1.5a.5.5 0 0 0 1 0V8h1.5a.5.5 0 0 0 0-1H9V5.5z"/><path d="M.5 1a.5.5 0 0 0 0 1h1.11l.401 1.607 1.498 7.985A.5.5 0 0 0 4 12h1a2 2 0 1 0 0 4 2 2 0 0 0 0-4h7a2 2 0 1 0 0 4 2 2 0 0 0 0-4h1a.5.5 0 0 0 .491-.408l1.5-8A.5.5 0 0 0 14.5 3H2.89l-.405-1.621A.5.5 0 0 0 2 1H.5zm3.915 10L3.102 4h10.796l-1.313 7h-8.17zM6 14a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm7 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0z"/></svg>
				</button>

				<div class="card-heading fs-5">
					{{book.title}}
					<span class="d-block text-muted fs-6">
						<span v-for="i in book.category">{{i}}&nbsp;&nbsp;&nbsp;</span>
					</span>
					<span v-for="i in book.author" class="d-block text-muted fs-6">{{i}}&nbsp;&nbsp;&nbsp;</span>
				</div>
				<div class="card-text">
					{{book.description}}
				</div>
				<div class="card-text">
					${{book.price}}
				</div>
				<router-link :to="`/product/${book.slug}`" class="card-button py-3">See more</router-link>
			</div>
			<div v-if="!books.length" class="alert alert-warning">No Books For Show</div>

		</div>


		<nav class="">
			<ul class="pagination justify-content-center">
				<router-link v-if="previousPage" @click="getPreviousPage()" type="button" class="btn rounded-circle pagination-button" to="/"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-caret-left" viewBox="0 0 16 16"><path d="M10 12.796V3.204L4.519 8 10 12.796zm-.659.753-5.48-4.796a1 1 0 0 1 0-1.506l5.48-4.796A1 1 0 0 1 11 3.204v9.592a1 1 0 0 1-1.659.753z"/></svg></router-link>
				<router-link v-if="nextPage" @click="getNextPage()" type="button" class="btn rounded-circle pagination-button" to="/"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-caret-right" viewBox="0 0 16 16"><path d="M6 12.796V3.204L11.481 8 6 12.796zm.659.753 5.48-4.796a1 1 0 0 0 0-1.506L6.66 2.451C6.011 1.885 5 2.345 5 3.204v9.592a1 1 0 0 0 1.659.753z"/></svg></router-link>
			</ul>
		</nav>  
 
	</div>
</template>

<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'

export default {
    name: "Home",

    setup() {

		let books = ref("")
		let nextPage = ref('')
		let previousPage = ref('')
		
    
  	    onMounted(() => {
            axios
                .get('ShowBooks/')
                .then(response => {
                    books.value = response.data.results
					nextPage.value = response.data.next
					nextPage.value = nextPage.value.slice(22,nextPage.value.length)
					previousPage.value = response.data.previous
					previousPage.value = previousPage.value.slice(22,previousPage.value.length)

                })
                .catch(error => {
                    console.log(error.response)
                })
        })



		function getNextPage(){
			axios
                .get(`${nextPage.value}`)
                .then(response => {
                    books.value = response.data.results

					nextPage.value = response.data.next
					previousPage.value = response.data.previous

					if(nextPage.value){
						nextPage.value = nextPage.value.slice(22,nextPage.value.length)
					}

					if(previousPage.value){
						previousPage.value = previousPage.value.slice(22,previousPage.value.length)
					}

					document.documentElement.scrollTop = 0;
                })
                .catch(error => {
                    console.log(error.response)
                })
		}


		function getPreviousPage(){
			axios
                .get(`${previousPage.value}`)
                .then(response => {
                    books.value = response.data.results

					nextPage.value = response.data.next
					previousPage.value = response.data.previous

					if(nextPage.value){
						nextPage.value = nextPage.value.slice(22,nextPage.value.length)
					}

					if(previousPage.value){
						previousPage.value = previousPage.value.slice(22,previousPage.value.length)
					}

					document.documentElement.scrollTop = 0;
                })
                .catch(error => {
                    console.log(error.response)
                })
		}
    

  	    return {
			books,
			nextPage,
			previousPage,
			getNextPage,
			getPreviousPage,
  	    }
    }
  
};
</script>


<style scoped>
body {
	font-family: Varela Round;
	background: #f1f1f1;
}

.Home {
	margin-top: 7rem;
}

a {
	text-decoration: none;
}

.card-sl {
	border-radius: 8px;
}

.card-sl:hover{
	box-shadow: 6px 6px 6px 0 rgba(0, 0, 0, 0.2), 6px 6px 6px 0 rgba(0, 0, 0, 0.19);
}

.card-image img {
	max-height: 100%;
	max-width: 100%;
	border-radius: 8px 8px 0px 0;
}

.card-action {
	position: relative;
	float: right;
	margin-top: -25px;
	margin-right: 20px;
	z-index: 2;
	color: #c9351e;
	background: #fff;
	border-radius: 100%;
	padding: 15px;
	font-size: 15px;
	box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.2), 0 1px 2px 0 rgba(0, 0, 0, 0.19);
}

.card-heading {
	font-size: 18px;
	font-weight: bold;
	background: #fff;
	padding: 10px 15px;
}

.card-text {
	padding: 10px 15px;
	background: #fff;
	font-size: 14px;
	color: #636262;
}

.card-button {
	display: flex;
	justify-content: center;
	padding: 10px 0;
	width: 100%;
	background-color: #000000;
	color: #fff;
	border-radius: 0 0 8px 8px;
}

.card-button:hover {
	text-decoration: none;
	background-color: #1D3461;
	color: #fff;
	transition-duration: 0.4s;

}

.pagination-button {
	background-color: #957bda;
}
</style>