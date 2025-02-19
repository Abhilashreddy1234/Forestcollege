document.addEventListener("DOMContentLoaded", function() {
    // Chatbot Elements
    const chatbotBtn = document.getElementById("chatbot-btn");
    const chatbotContainer = document.getElementById("chatbot-container");
    const closeChat = document.getElementById("close-chat");

    // Create iframe for embedding chatbot
    let chatbotIframe = document.createElement("iframe");
    chatbotIframe.src = "https://chatbot-1jmc.onrender.com/"; // Make sure this URL is correct
    chatbotIframe.style.width = "100%";
    chatbotIframe.style.height = "100%";
    chatbotIframe.style.border = "none";

    // Append iframe to chatbot container
    chatbotContainer.innerHTML = ""; // Clear any previous content
    chatbotContainer.appendChild(chatbotIframe);

    // Ensure chatbot container is hidden by default
    chatbotContainer.style.display = "none";

    // Toggle chatbot visibility when button is clicked
    chatbotBtn.addEventListener("click", () => {
        if (chatbotContainer.style.display === "block") {
            chatbotContainer.style.display = "none";
        } else {
            chatbotContainer.style.display = "block";
        }
    });

    // Close chatbot when close button is clicked
    closeChat.addEventListener("click", () => {
        chatbotContainer.style.display = "none";
    });
});
