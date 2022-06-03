<template>
	<div class="container mt-5">
        <h1 class="alert alert-danger text-center">CATEGORIES</h1>

        
        <section class="container my-5">
            <div class="row d-flex">
                
                    <div v-for="category in categories" class="col-lg-3 col-md-4 col-sm-6 text-center mb-3">
                        <router-link :to="`/category/${category.slug}`">
                            <img class="rounded-circle mb-2" src="https://picsum.photos/200">
                            <strong class="text-danger d-block">{{category.title}}</strong>
                        </router-link>
                        
                        <p></p>
                    </div>

            </div>

        </section>
 
	</div>
</template>

<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'

export default {
    name: "All_Category",
    setup() {
	    let categories = ref("")

        onMounted(() => {
            axios
                .post('ShowCategories/')
                .then(response => {
                    categories.value = response.data.data
                })
                .catch(error => {
                    console.log(error.response)
                })
        })

	    return {
		    categories
	    }
    }

};
</script>


<style scoped>
a{
    text-decoration: none;
}

</style>