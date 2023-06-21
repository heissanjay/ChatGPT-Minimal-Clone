<script setup>
import {ref} from 'vue';
const titleName = ref("Chat with GPT")

</script>

<template>
    <div class="container">
        <div class="title-card">
            <h1 class="title">
                {{ titleName }}
            </h1>
        </div>
    </div>
</template>

<style>
.container {
    margin: auto 0;
    padding: 10px 0;
    user-select: none;  
}
.title {
    font-size: 2.3rem;
    font-weight: bolder;
}

</style>