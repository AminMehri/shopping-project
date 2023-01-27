<template>
	<div class="container mt-5">
        <h1 class="alert alert-danger text-center">Authors</h1>

        
        <section class="container my-5">
            <div class="row d-flex">
                
                    <div v-for="author in authors" class="col-lg-3 col-md-4 col-sm-6 text-center mb-3">
                        <router-link :to="`/author/${author.slug}`">
                            <img class="rounded-circle mb-2 w-100" :src="`${author.cover}`" width="400px">
                            <strong class="text-danger d-block">{{author.full_name}}</strong>
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
    name: "All_Authors",
    setup() {
	    let authors = ref("")

        onMounted(() => {
            axios
                .get('ShowAuthors/')
                .then(response => {
                    authors.value = response.data
                })
                .catch(error => {
                    console.log(error.response)
                })
        })

	    return {
		    authors
	    }
    }

};
</script>


<style scoped>
a{
    text-decoration: none;
}

</style>