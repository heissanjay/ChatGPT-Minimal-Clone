<script setup>
import HeaderCard from './components/HeaderCard.vue';
import ListModel from './components/ListModel.vue';
import ChatInterface from './components/ChatInterface.vue';
import ImageGeneration from './components/ImageGeneration.vue';
import Footer from './components/Footer.vue';

import { ref } from 'vue';

const selectedModel = ref('gpt-35-turbo');

function handleModelSelected(model) {
  selectedModel.value = model;
}
</script>

<template>
  <div class="App">
    <HeaderCard></HeaderCard>
    <ListModel @model-selected="handleModelSelected"></ListModel>
    <ChatInterface v-if="selectedModel === 'gpt-35-turbo'" />
    <ImageGeneration v-if="selectedModel === 'DALL-E'"  />
    <Footer></Footer>
  </div>
</template>
