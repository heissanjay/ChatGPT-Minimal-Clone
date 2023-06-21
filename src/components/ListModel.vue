<template>
  <div class="model-list">
  <label>Choose the Preferred Model </label><br />
    <select v-model="selectedModel" @change="emitSelectedModel">
      <option v-for="option in modelOptions" :key="option.value" :value="option.value">
        {{ option.label }}
      </option>
    </select>
  </div>
</template>

<script>
//   option API
export default {
  data() {
    return {
      selectedModel:'gpt-35-turbo', 
      modelOptions: [
        { label: 'GPT-3.5-turbo', value: 'gpt-35-turbo' },
        { label: 'Image generation with DALL-E', value: 'DALL-E' }
      ]
    };
  },
  methods: {
    emitSelectedModel() {
      this.$emit('model-selected', this.selectedModel);
    }
  }
};
</script>

<style>
.model-list{
  padding: 20px;
  font-size: 20px;
}
select {
width: 250px;
padding: 8px;
margin-top: 20px;
font-size: 16px;
border: none;
color: #fff;
outline: none;
background-color: #40414F;
}

option {
padding: 10px;
font-size: 18px;
width: inherit;
color: #333;
background-color: #f2f2f2;
}

option:hover {
background-color: #f5f5f5;
}

option:selected {
background-color: #007bff;
color: #fff;
}



</style>