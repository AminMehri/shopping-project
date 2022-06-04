<template>
	<div class="container mt-5 Single_Category">
        <h1 class="alert alert-success text-center">NOVEL</h1>
		<div class="row">
			<div v-for="book in books" class="card-sl border-end border-start col-lg-4 col-md-6 col-sm-12">
				<div class="card-image">
					<img src="https://picsum.photos/400/200" width="400" height="200" />
				</div>

				<button class="card-action btn" id="shopcardbutton">
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

		</div>
 
	</div>
</template>

<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRoute } from 'vue-router'

export default {
  name: "Home",

    setup() {
		let books = ref("")
        const route = useRoute();
        let slug = ref("")
        slug.value = route.params.slug
        
  	    onMounted(() => {
            axios
                .post('ShowSingleCategory/', {
                    slug: slug.value
                })
                .then(response => {
                    books.value = response.data.data
					document.documentElement.scrollTop = 0;
                })
                .catch(error => {
                    console.log(error.response)
                })
        })
    
  	    return {
			books,
  	    }
    }

};
</script>


<style scoped>
body {
	font-family: Varela Round;
	background: #f1f1f1;
}

.Single_Category {
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