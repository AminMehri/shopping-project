<template>
	<div class="container Single-author">
		<div id="carouselExampleIndicators" class="carousel slide w-100 mx-auto" data-bs-ride="carousel">
			<div class="carousel-indicators">
				<button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
				<button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
				<button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
			</div>
			<div class="carousel-inner">
				<div class="carousel-item active">
					<img :src="`http://127.0.0.1:8000/media${author.image1}`" width="800" height="500" class="d-block w-100">
				</div>
				<div class="carousel-item">
					<img :src="`http://127.0.0.1:8000/media${author.image2}`" width="800" height="500" class="d-block w-100">
				</div>
				<div class="carousel-item">
					<img :src="`http://127.0.0.1:8000/media${author.image3}`" width="800" height="500" class="d-block w-100">
				</div>
			</div>
			<button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
				<span class="carousel-control-prev-icon" aria-hidden="true"></span>
				<span class="visually-hidden">Previous</span>
			</button>
			<button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
				<span class="carousel-control-next-icon" aria-hidden="true"></span>
				<span class="visually-hidden">Next</span>
			</button>
		</div>
		
        <h1 class="alert alert-success text-center">{{author.full_name}}</h1>

		<div class="row">
			<div class="col-md-8 mx-auto">
				<p>{{author.description}}</p>
			</div>
		</div>

		<section class="py-5">
			<div class="container">
				<!-- FOR DEMO PURPOSE -->
				<div class="row">
					<div class="col-lg-6 mx-auto">
						<header class="text-center pb-5">
							<h1 class="h2">{{author.full_name}}'s quotes</h1>
						</header>
					</div>
				</div><!-- END -->


				<div class="row">
					<div class="col-lg-6">

						<!-- CUSTOM BLOCKQUOTE -->
						<blockquote class="blockquote blockquote-custom bg-white p-5 shadow rounded">
							<div class="blockquote-custom-icon bg-info shadow-sm"><i class="fa fa-quote-left text-white"></i></div>
							<p class="mb-0 mt-2 font-italic">"{{quotes.description}}"</p>
							<footer class="blockquote-footer pt-4 mt-4 border-top">{{author.full_name}} >>&nbsp;
								<cite title="Source Title">{{quotes.source}}</cite>
							</footer>
						</blockquote><!-- END -->

					</div>

				</div>
			</div>
		</section>

		<h3>Books by {{author.full_name}} <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-arrow-right-circle-fill" viewBox="0 0 16 16"><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0zM4.5 7.5a.5.5 0 0 0 0 1h5.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5H4.5z"/></svg></h3>


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
		let author = ref("")
		let quotes = ref("")
        const route = useRoute();
        let slug = ref("")
        slug.value = route.params.slug
        
  	    onMounted(() => {
            axios
                .post('ShowSingleAuthor/', {
                    slug: slug.value
                })
                .then(response => {
                    books.value = response.data.data
                    author.value = response.data.author_data[0]
                    quotes.value = response.data.quotes_data[0]
					console.log(author.value.description)
					document.documentElement.scrollTop = 0;
                })
                .catch(error => {
                    console.log(error.response)
                })
        })
    
  	    return {
			books,
			author,
			quotes
  	    }
    }

};
</script>


<style scoped>
body {
	font-family: Varela Round;
	background: #f1f1f1;
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

.Single-author{
	margin-top: 4rem;
}

.blockquote-custom {
  position: relative;
  font-size: 1.1rem;
}

.blockquote-custom-icon {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  position: absolute;
  top: -25px;
  left: 50px;
}

</style>