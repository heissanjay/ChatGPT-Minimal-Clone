<template>
  <div class="container-img">
    <p class="intro">
      Start with a detailed description
    </p>
    <div class="prompt-card">
        <input
        type="text"
        :placeholder="examplePrompt"
        name="user-prompt"
        class="prompt-user-text"
        v-model="userPromptText"
        @keyup.enter="handleUserSubmit"
        />
        <button
        type="submit"
        name="generate-image"
        class="submit-btn"
        @click="handleUserSubmit"
        >Generate</button>
    </div>
    <div class="gen-info" v-if="startGenerate && outputImgURL === ''">
      <p>
        Generating Image ... Please Wait
      </p>
    </div>
    <div v-if="isImageGenerated" class="img-gen-output">
      <div class="img-container">
        <a :href="outputImgURL" download>
          <img :src="outputImgURL" :alt="userPromptText" />
        </a>
      </div>
    </div>
    <div v-else class="hideBlock"></div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      examplePrompt: "An Impressionist oil painting of sunflowers in a purple vase...",
      isImageGenerated: false,
      startGenerate:false,
      outputImgURL: "",
      userPromptText: "",
    }
  },
  methods: {
    handleUserSubmit() {
      // get the user prompt test

      if (this.userPromptText === "") {
        return alert("Please Enter Some Text to Generate Image");
      }

      const userQueryText = {
        "role": "user",
        "content": this.userPromptText
      }
      
      this.startGenerate = true;

      try {
        fetch('http://localhost:5000/generate_image', {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(userQueryText),
        })
          .then((response) => response.json())
          .then((data) => {
            this.isImageGenerated = true;
            this.outputImgURL = data.url;
            console.log(data);
          })

      } catch (err) {
        console.error(err);
      }
      this.userPromptText = '';
    }
  }
}
</script>


<style scoped
>

.container-img {
justify-content: center;
text-align: center;
margin: auto;
display: inline-block;
}

.intro {
font-size: larger ;
float: left;
padding-bottom: 20px;
}

input {
width: 50rem;
height: 50px; 
background-color: rgba(128, 128, 128, 0.484);
border: none;
padding: 10px;
border-radius: 5px;
font-size: larger;
}


button {
margin-left: 10px;
margin-bottom: 10px;
width: 80px;
height: 50px;
background-color: #00A67E;
color: #fff;
border: none;
cursor: pointer;
border-radius: 3px;
}

button:hover {
background-color: #2b2d2f;
}

.img-gen-output, .hideBlock {
  margin: auto;
  width: 900px;
  height: 380px;
  margin-top: 10px;
  text-align: center;
  justify-content: center;
}

.img-container   {  
  margin: auto;
  justify-content: center;
  text-align: center;
  width:fit-content;
  height:fit-content;

}

img {
  width:fit-content;
  height: fit-content;
}

</style>