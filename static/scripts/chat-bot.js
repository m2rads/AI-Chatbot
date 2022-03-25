// Global Initializaitons
const chatBot = document.getElementById("chatbot-button");
const chatConversation = document.getElementById("chat_display");
let userInput = document.getElementById("userInput");
let cssClass;

// send message on key press event
userInput.onkeydown = async (e) => {
    if (e.which == 13) {
        chatBotClick(e);
    }
    return;
}

// send message on click event
chatBot.onclick = async (e) => chatBotClick(e);

// chatbot implementation
const chatBotClick = async (e) => {
    e.preventDefault();
    // console.log("clicked")
    // // get the messsage from the input box and log the meessage
    console.log(userInput.value)

    populateChatConversation("userInput" , userInput.value);

    await fetch ("/get", {
        method: "POST",
        headers: {'Content-Type': "application/json"},
        body: JSON.stringify({userInput:userInput.value})
    })
    .then(response => response.json())
    .then(data => {
        console.log(data['response'])
        populateChatConversation("botResponse", data['response']);
    })
    userInput.value = '';
}

// Displays the users and bot messages to the bot and vice versa
// received the user input and the chat display object fro dom
const populateChatConversation = async (flag, message) => {
    if (flag == 'userInput') {
        cssClass = 'messages__item messages__item--visitor';
    }
    else {
        cssClass = 'messages__item messages__item--operator';
    }
    chatConversation.innerHTML += `
        <p class="${cssClass}"> ${message} </p>
    `
}
