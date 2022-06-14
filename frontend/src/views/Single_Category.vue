<template>
	<div class="container mt-5 Single_Category">
        <h1 class="alert alert-success text-center">{{category_title}}</h1>
		<div class="row">
			<div v-for="book in books" class="card-sl position-relative border-end border-start col-lg-4 col-md-6 col-sm-12">
				<div class="card-image">
					<img class="w-100" :src="`http://127.0.0.1:8000${book.cover}`" width="400"/>
				</div>

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
				<div class="card-text mb-5">
					${{book.price}}
				</div>
				<router-link :to="`/product/${book.slug}`" class="card-button py-3 position-absolute" style="left: 0px; bottom: 0px;">See more</router-link>
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
		let category_title = ref("")
        slug.value = route.params.slug
        
  	    onMounted(() => {
            axios
                .post('ShowSingleCategory/', {
                    slug: slug.value
                })
                .then(response => {
                    books.value = response.data.data
					category_title.value = response.data.category_title.toUpperCase()
					document.documentElement.scrollTop = 0;
                })
                .catch(error => {
                    console.log(error.response)
                })
        })
    
  	    return {
			books,
			category_title
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