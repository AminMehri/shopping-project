<template>

	<nav id="nav" class="navbar navbar-dark bg-dark fixed-top">
		<div class="container-fluid">

			<router-link type="button" class="btn text-danger bg-white" to="/shopcard" v-if="$store.state.isAuthenticated"><svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-cart-plus" viewBox="0 0 16 16"><path d="M9 5.5a.5.5 0 0 0-1 0V7H6.5a.5.5 0 0 0 0 1H8v1.5a.5.5 0 0 0 1 0V8h1.5a.5.5 0 0 0 0-1H9V5.5z"/><path d="M.5 1a.5.5 0 0 0 0 1h1.11l.401 1.607 1.498 7.985A.5.5 0 0 0 4 12h1a2 2 0 1 0 0 4 2 2 0 0 0 0-4h7a2 2 0 1 0 0 4 2 2 0 0 0 0-4h1a.5.5 0 0 0 .491-.408l1.5-8A.5.5 0 0 0 14.5 3H2.89l-.405-1.621A.5.5 0 0 0 2 1H.5zm3.915 10L3.102 4h10.796l-1.313 7h-8.17zM6 14a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm7 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0z"/></svg> <span class="badge bg-secondary">{{Number_of_books_in_the_shopcart}}</span></router-link>
			<router-link type="button" class="btn fw-bold text-white mx-2 navbar-button d-none d-sm-block d-print-block" to="/login" v-if="!$store.state.isAuthenticated">Sign up/in</router-link>
			<router-link type="button" class="btn fw-bold text-white navbar-button d-none d-md-block d-print-block" to="/profile" v-if="$store.state.isAuthenticated">Profile</router-link>

			<router-link class="navbar-brand mx-md-auto" to="/">
				<div class="d-flex">
					<h2 class="font-weight-bold mr-2 px-3" style="color:#16151a; background-color:#957bda" > P </h2>
					<h2 style="color: #957bda">HILOSOPHY</h2>
				</div>
			</router-link>
			<button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar">
				<span class="navbar-toggler-icon"></span>
			</button>
			<div class="offcanvas offcanvas-end bg-dark" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
			<div class="offcanvas-header">
				<h5 class="offcanvas-title" id="offcanvasNavbarLabel">Some Philosophy</h5>
				<button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas" aria-label="Close"></button>
			</div>
			<div class="offcanvas-body">
				<ul class="navbar-nav justify-content-end flex-grow-1 pe-3">
					<li class="nav-item">
						<router-link class="nav-link" to="/">Home</router-link>
					</li>
					<li class="nav-item">
						<router-link class="nav-link" to="/about">About</router-link>
					</li>
					<li class="nav-item">
						<router-link class="nav-link" to="/contact">Contact</router-link>
					</li>
					<li class="nav-item">
						<router-link class="nav-link show-in-sm" to="/login" v-if="!$store.state.isAuthenticated">Sign up/in</router-link>
					</li>
					<li class="nav-item">
						<router-link class="nav-link show-in-sm" to="/profile" v-if="$store.state.isAuthenticated">Profile</router-link>
					</li>
					<li class="nav-item">
						<router-link class="nav-link" to="/categories">Categories</router-link>
					</li>
					<li class="nav-item">
						<router-link class="nav-link" to="/authors">Authors</router-link>
					</li>
				</ul>
				<form class="d-flex">
					<input v-model="searchInput" class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
					<button @click="search()" class="btn btn-outline-success" type="button">Search</button>
				</form>
			</div>
			</div>
		</div>
	</nav>


	<router-view/>
	<Home :data=showSearchResult />

	<div class="mt-5">
				
				<div class="card">
					<div class="row mb-4 ">
						
						<div class="col-md-4 col-sm-11 col-xs-11">
							<div class="footer-text pull-left">
								<div class="d-flex">
									<h1 class="font-weight-bold mr-2 px-3" style="color:#16151a; background-color:#957bda" > P </h1>
									<h1 style="color: #957bda">HILOSOPHY</h1>
								</div>
								<p class="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Commodi non pariatur numquam animi nam at impedit odit nisi.</p>

								<div class="social mt-2 mb-3">

									<i class="fa fa-facebook-official fa-lg" ></i>
									<i class="fa fa-instagram fa-lg"></i>
									<i class="fa fa-twitter fa-lg"></i>
									<i class="fa fa-linkedin-square fa-lg"></i>
									<i class="fa fa-facebook"></i>

								</div>
							
							</div>
						</div>
						
						
						<div class="col-md-2 col-sm-1 col-xs-1 mb-2"></div>
						
						<div class="col-md-2 col-sm-4 col-xs-4">
					
							<h5 class="heading">Popular categories</h5>
							<ul >
								<!-- <li><router-link class="text-decoration-none" to="/category/philosophy">Philosophy</router-link></li>
								<li><router-link class="text-decoration-none" to="/category/novel">Novel</router-link></li> -->
							</ul>
					
						</div>
					
					
						<div class="col-md-2 col-sm-4 col-xs-4">
					
							<h5 class="heading">Popular authors</h5>
							<ul class="card-text">
								<!-- <li><router-link class="text-decoration-none" to="/author/irwin-yalom">Irwin D.yalom</router-link></li>
								<li><router-link class="text-decoration-none" to="/author/arthur-schopenhauer">Schopenhauer</router-link></li>
								<li><router-link class="text-decoration-none" to="/author/friedrich-nietzsche">Nietzsche</router-link></li>
								<li><router-link class="text-decoration-none" to="/author/george-orwell">George orwell</router-link></li> -->
							</ul>
					
						</div>

					
						<div class="col-md-2 col-sm-4 col-xs-4">

							<h5 class="heading">Philosophy company</h5>
							<ul class="card-text">
								<li><router-link class="text-decoration-none" to="/about">About Us</router-link></li>
								<li><router-link class="text-decoration-none" to="/contact">Contact</router-link></li>
							</ul>

						</div>

					</div>
					
					
					<div class="divider mb-4" >   
					</div>
		
				
					<div class="row" style="font-size:10px;">
					
					<div class="col-md-6 col-sm-6 col-xs-6">
						
						<div class="pull-left">
							
							<p><i class="fa fa-copyright"></i> 2022 Amin mehri</p>
							
						</div>
						
					</div>
					
					

					<div class="col-md-6 col-sm-6 col-xs-6">
					
					
						<div class="pull-right mr-4 d-flex policy">
							
							<div>Terms of Use</div>
							<div>Privacy Policy</div>
							<div>Cookie Policy</div>
							
						</div>
						
						
						
					</div>
					
					
					
				</div>
				</div>
				
	</div>


</template>


<script>
import { useStore } from 'vuex'
import { useRoute, useRouter } from 'vue-router'
import { ref, onMounted } from "vue";
import axios from 'axios'



export default {
	setup() {
		let Number_of_books_in_the_shopcart = ref("")
		const store = useStore()
        const route = useRoute()

		let searchInput = ref('')
		let showSearchResult = ref('')

    
  	    onMounted(() => {
			store.dispatch('onStart')

            axios
                .post('ShowShopcard/')
                .then(response => {
                    Number_of_books_in_the_shopcart.value = response.data.Number_of_books_in_the_shopcart
                })
                .catch(error => {
                    console.log(error.response)
                })
        })


		function search(){
			axios
                .get(`ShowBooks/?search=${searchInput.value}`)
                .then(response => {
					showSearchResult.value = response.data
                })
                .catch(error => {
                    console.log(error.response)
                })
		}

    
  	    return {
            Number_of_books_in_the_shopcart,
			search,
			searchInput,
			showSearchResult
  	    }
    },

	watch: {
		$route() {
			this.$store.dispatch('onStart')
			axios
                .post('ShowShopcard/')
                .then(response => {
                    this.Number_of_books_in_the_shopcart = response.data.Number_of_books_in_the_shopcart
                })
                .catch(error => {
                    console.log(error.response)
                })
		},

	},
}

</script>



<style>
#app {
	font-family: Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	color: #2c3e50;
}


nav {
	padding: 40px;
	height: 4rem;
}

nav a {
	font-weight: bold;
	color: #2c3e50;
}

#nav a.router-link-exact-active {
	color: #957bda;
}


@media only screen and (min-width: 600px){
	#nav a.navbar-brand:hover {
		letter-spacing: 8px;
		transition-duration: 0.5s;
	}
}

.navbar-button:hover {
	background-color: white;
	color: rgb(146, 145, 158) !important;
}


@media only screen and (min-width: 576px){
	.show-in-sm {
		display: none !important;
	}
}







@import url('https://fonts.googleapis.com/css2?family=Titillium+Web:wght@700&display=swap');
        
body{
	background-color:#f3f6fd ;
	font-size: 11.5px;
	font-weight: bold;
	color: rgb(189, 196, 203);
}

.card{
	padding: 2% 7%;
	color: #646771;
	background-color: #16151a !important;
}

ul{
	list-style-type: none;
	margin: 0;
	padding: 0;
}

ul >li{
	padding: 4px;
}

ul > li:hover{
	color:#957bda;
	cursor: pointer;
}

hr{
	border-width: 3px;
}

.social > i{
	padding: 1%;
	font-size: 15px;
}

.social > i:hover{
	color:#957bda;
	cursor:pointer;
}

.policy > div{
	padding: 4px;
}

.heading{
	font-family: 'Titillium Web', sans-serif;
	color: white;
}

.divider{
	border-top: 2px solid rgba(189, 196, 203, 0.5);;
}


</style>
