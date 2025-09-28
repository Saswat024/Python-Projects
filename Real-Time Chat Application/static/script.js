const username = prompt("Enter your username: ") || "Anonymous";
const room = prompt("Enter room name: ") || "General";
const ws = new WebSocket(`ws://${window.location.host}/ws/${username}/${room}`);
const messages = document.getElementById("messages");
const messageInput = document.getElementById("messageInput");
const sendButton = document.getElementById("sendButton");
const roomName = document.getElementById("room-name");

roomName.textContent = `Chat Room: ${room}`;

// Receive messages
ws.onmessage = function (event) {
  const messageDiv = document.createElement("div");
  messageDiv.className = "message";
  const messageContentDiv = document.createElement("div");
  messageContentDiv.className = "message-content";

  const data = JSON.parse(event.data);

  // Add sender name
  const senderDiv = document.createElement("div");
  senderDiv.className = "message-sender";
  senderDiv.textContent = data.sender;

  // Add message content
  messageContentDiv.textContent = data.message;

  // Add timestamp
  const timeDiv = document.createElement("div");
  timeDiv.className = "message-time";
  const now = new Date();
  timeDiv.textContent = now.toLocaleTimeString();

  // Style based on sender
  if (data.sender === username) {
    messageDiv.classList.add("user-message");
  } else {
    messageDiv.classList.add("other-message");
  }

  // Append elements
  messageDiv.appendChild(senderDiv);
  messageDiv.appendChild(messageContentDiv);
  messageDiv.appendChild(timeDiv);

  messages.appendChild(messageDiv);
  messages.scrollTop = messages.scrollHeight;
};

// Send message on button click
sendButton.onclick = function () {
  const message = messageInput.value.trim();
  if (message) {
    ws.send(
      JSON.stringify({
        message: message,
        sender: username,
        room: room,
      })
    );
    messageInput.value = "";
  }
};

// Send message on Enter key
messageInput.onkeypress = function (e) {
  if (e.key === "Enter") {
    sendButton.click();
  }
};

// Handle connection closed
ws.onclose = function () {
  const messageDiv = document.createElement("div");
  messageDiv.className = "message";
  messageDiv.textContent = "Disconnected from chat server";
  messages.appendChild(messageDiv);
};

// Handle errors
ws.onerror = function (error) {
  console.error("WebSocket error:", error);
};
