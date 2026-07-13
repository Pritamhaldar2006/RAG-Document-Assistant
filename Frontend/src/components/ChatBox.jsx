import Message from "./Message";

function ChatBox({ messages }) {
  return (
    <div className="chat-body">
      {messages.map((msg, index) => (
        <Message
          key={index}
          sender={msg.sender}
          text={msg.text}
        />
      ))}
    </div>
  );
}

export default ChatBox;