<script setup>
import { ref, reactive, watch , onMounted} from 'vue';

const userQueryText = ref("");
const chatContainer = ref(null);
const messages = reactive([]);


function handleUserSubmit() {
  scrollToBottom();
  const userMsg = {
    role: "user",
    message: userQueryText.value,
  };
  messages.push(userMsg);
  userQueryText.value = "";
  scrollToBottom();

  const assistantMsg = {
    role: "assistant",
    message: "Loading...",
  };
  messages.push(assistantMsg);
  scrollToBottom();

  const msg = {
    role: "user",
    message: userMsg.message,
  };

  try {
    fetch("http://localhost:5000/process_request", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(msg),
    })
      .then((response) => response.json())
      .then((data) => {
        const assistantResponse = {
          role: "assistant",
          message: data.content, 
        };
        const index = messages.indexOf(assistantMsg);
        if (index !== -1) {
          messages.splice(index, 1, assistantResponse);
        }
        localStorage.setItem('messages', JSON.stringify(messages));
        scrollToBottom();
      });
  } catch (err) {
    console.log(err);
  }
}

function scrollToBottom() {
  if (chatContainer.value) {
    chatContainer.value.scrollTop = chatContainer.value.scrollHeight;
  }
}

onMounted(
  ()=> {
    const previousMessage = JSON.parse(localStorage.getItem('messages')) || [];
    messages.push(...previousMessage);
    scrollToBottom();
  }
);

watch(messages, () => {
  scrollToBottom();
});

</script>

<template>
  <div class="chat-container">
    <!-- <HomeIntro v-if="messages.length == 0"></HomeIntro> -->
    <div class="chat-messages" ref="chatContainer">
      <div v-for="message in messages" :key="message.id">
        <div class="chat-bubble" :class="message.role">
          <div class="msg-content">
            <img v-if="message.role === 'assistant'" src="../assets/ai-bot-logo.jpg" />
            <img v-if="message.role === 'user'" src="../assets/human-logo.jpg" />
            <p class="msg">{{ message.message }}</p>
          </div>
        </div>
      </div>
    </div>
    <div class="chat-input">
      <input
        type="text"
        v-model="userQueryText"
        id="input-box"
        placeholder="Send a message"
        class="message-input"
        @keyup.enter="handleUserSubmit"
      />
      <button @click="handleUserSubmit" class="send-button">Send</button>
    </div>
  </div>
</template>


<style>
.chat-container {
 display: flex;
 flex-direction: column;
 width: 900px;
 margin: auto;
 height: 500px; 
 overflow-y: auto;
 border: none;
}

.chat-messages {
flex-grow: 1;
overflow-y: auto;
}

.chat-input {
display: flex;
align-items: center;
padding: 10px;
height: 50px;
background-color: #40414F;
border-radius: 4px;
width: inherit;

}

img {
width: 40px;
height: 40px;
float: left;
}
.message-input {
flex-grow: 1;
padding: 8px;
border: 1px solid #ccc;
border-radius: 4px;
width: inherit;
}

.send-button {
margin-left: 10px;
padding: 8px 12px;
background-color: #00A67E;
color: #fff;
border: none;
border-radius: 4px;
cursor: pointer;
}

.send-button:hover {
background-color: #2b2d2f;
}

.send-button:active {
background-color: #255ad0;
}

.chat-bubble {
display: flex;
flex-direction: column;
align-items: flex-start;
}


.user {
background-color: #343541;
color: #fff;
}
.message-input {
background-color: #40414F;
border: none;
font-size: 20px;
color: #fff;
}
.msg {
margin-left: 60px;
}
input:focus{
outline: none;
border: none;
color: #fff;
}

.model {
background-color: #444654;
color: #fff;
}

.msg-content{
text-align: left;
padding: 20px;
}

.bubble-head {
display: flex;
}

.chat-messages {
padding: 10px;
background-color: #202123;
}

.msg-party{
font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
font-weight: bolder;
padding-left: 10px;
}

::-webkit-scrollbar {
width: 2px;
}

::-webkit-scrollbar-thumb {
background-color: #2E2F39;
border-radius: 50px;
}

::-webkit-scrollbar-thumb:hover {
background-color: #555; 
}


::-webkit-scrollbar-track {
background-color: #1c1a1a; 
}

@media (max-width: 600px) {
  .chat-container {
    width: 100%;
  }

  .chat-input {
    flex-direction: column;
    align-items: stretch;
    height: auto;
    padding: 20px;
  }

  .chat-input .message-input {
    margin-top: 10px;
    width: 100%;
  }
}

/* Styles for screens with a minimum width of 601px */
@media (min-width: 601px) {
  .chat-container {
    width: 900px;
  }

  .chat-input {
    flex-direction: row;
    align-items: center;
    padding: 10px;
    height: 50px;
  }

  .chat-input .message-input {
    margin-top: 0;
    width: inherit;
  }
}

</style>
 

