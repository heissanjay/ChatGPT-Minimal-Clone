<script setup>
    import {ref} from "vue";
    const bioLink = ref("https://linktr.ee/xSanjayy");
</script>

<template>
    <footer>
        <div class="container-ft">
            <p>Made with <span class="heart-icon">&hearts;</span> by 
            <a :href="bioLink">San_J</a>
            </p>
        </div>
    </footer>
</template>

<style scoped>
.container-ft{
    max-width: 960px;
    padding: 30px;
    margin: 0 auto;
}

.heart-icon {
  color: red;
}
a {
  color: inherit;
  text-decoration: underline;
}

a:hover {
  text-decoration: underline; 
}

a:visited {
  color: inherit;
}

</style>