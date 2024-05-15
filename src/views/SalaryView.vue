<template>
    <section class="wrapper">
        <div class="separator">
            <!-- <div></div> -->
            <strong>Employees</strong>

            <div class="interaction">
                <div class="search-filter">
                    <div class="search-items">
                        <input
                            type="search"
                            placeholder="search..."
                        />
                    </div>
                </div>
            </div>
        </div>

        <div class="table-container">
            <div class="table-wrap-body">
                <table class="table">
                    <thead>
                        <tr>
                            <th>Id</th>
                            <th>Amount</th>
                            <th>Created at</th>
                            <th>person</th>
                            <th>Created by</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="salaire in salaires">
                          <td>{{ salaire.id }}</td>
                          <td>{{ salaire.montant }}</td>
                          <td>{{ salaire.created_at }}</td>
                          <td>{{ getPersonneFullname(salaire.personne) }}</td>
                          <td>{{ salaire.created_by }}</td>
                          <td>{{ salaire['ikindi kintu'] }}</td>
                        </tr>
                    </tbody>
                </table>
               
            </div>
        </div>
        
    </section>
</template>
<script>
import axios from "axios"
export default {
    data(){
        return{
            salaires:[]
        }
    },
    mounted(){
        this.fetchSalaires()
    },
    computed(){
        headers(); {
            return {
                headers:{
                    "Authorization":"Bearer "+this.$store.state.user.access
                }
            }
        }
    },
    methods:{
        getPersonneFullname(personne){
            return `${personne.nom} ${personne.prenom}`
        },
        fetchSalaires(){
            let header = `Bearer ${this.$store.state.user.access}`
            console.log(header)
            axios.get("/salaire/", {headers:{"Authorization":header}})
            .then((response)=>{
                this.salaires = response.data.results
                console.log(this.salaires)
            })
            .catch((error)=>{
                console.log(error)
            })
        }
    }
}
</script>

<style scoped>
.en_conge{
    background-color:orange;
}
</style>
