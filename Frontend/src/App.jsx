import { useState } from "react";
import axios from "axios";
import "./App.css";

import ChatBox from "./components/ChatBox";
import ChatInput from "./components/ChatInput";

function App() {
  const [messages, setMessages] = useState([]);

  const sendQuestion = async (question) => {
    setMessages((prev) => [
      ...prev,
      { sender: "user", text: question }
    ]);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/chat",
        {
          question: question
        }
      );

      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",
          text: response.data.answer
        }
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",
          text: "Unable to connect to the backend."
        }
      ]);
    }
  };

  return (
    <div className="app">
      <div className="chat-container">

        <div className="chat-header">
          📚 College PDF Chatbot
        </div>

        <ChatBox messages={messages} />

        <ChatInput onSend={sendQuestion} />

      </div>
    </div>
  );
}

export default App;