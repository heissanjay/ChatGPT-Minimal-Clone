<template>
    <div class="content-wrapper">
        <div class="card-wrapper">
        <div class="limitations">
            <h4>Limitation</h4>
        <div class="lt-card">
            <ul v-for="limit in limits">
                <li>
                    {{ limit }}
                </li>
            </ul>
        </div>
        </div>
       <div class="merits">
        <h4>Merits</h4>
        <div class="lt-card">
            <ul v-for="merit in merits">
                <li>
                    {{ merit }}
                </li>
            </ul>
        </div>
       </div>
       
        </div>
    </div>
      
</template>

<script setup>

import {ref} from 'vue';
const limits = ref([
    "Cannot remember the conversation",
    "limited response frequency",
    "May produce irrelevant information"
]);

const merits = ref(
    [
        "powered by advanced model (gpt-3.5-turbo)",
        "faster response over any model",
        "completly free and effective"
    ]
)


</script>


<style scoped>
    .content-wrapper{
        position: relative;
        height: 550px;
        width: 700px;
        text-align: center;
        justify-content: center;
        margin: auto;
    }
    /* .intro-card{
    width: 500px;
    text-align: justify;
    margin:auto;
    height: 200px;
    padding-top: 30px;
    line-height: 1.5;
    border-radius: 20px;
    background: linear-gradient(225deg, #222325, #1d1e20);
    box-shadow:  -6px 6px 12px #19191b,
             6px -6px 12px #27292b;
    }

    .intro-card > p{
        padding: 20px;
    } */
    .lt-card {
        width: inherit;
        height: 200px;
        padding-top: 20px;
        text-align: center;
        justify-content: center;
    }
    h4 {
        text-align: left;
        padding-top: 30px;
        margin-left: 30px;
    }
    ul ,ol ,li {
        text-align: center;
        line-height: 2;
        justify-content: center;
    }

    .card-wrapper {
        display: flex;
    }

    li {
        text-align: justify;
    }
    .merits {
        padding-left: 50px;
    
    }

    @media (max-width: 600px) {
  .content-wrapper {
    width: 100%;
    height: auto;
    padding: 20px;
  }
  
  .card-wrapper {
    flex-direction: column;
  }
  
  .merits {
    padding-left: 0;
    margin-top: 30px;
  }
}


</style>