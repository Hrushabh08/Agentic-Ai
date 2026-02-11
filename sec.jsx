import { useState } from "react";
import axios from "axios";

export default function Chat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input) return;
    const newMessages = [...messages, { type: "user", text: input }];
    setMessages(newMessages);

    try {
      const res = await axios.post("http://127.0.0.1:8000/chat", { message: input });
      setMessages([...newMessages, { type: "agent", text: res.data.response }]);
      setInput("");
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="p-4 max-w-md mx-auto border rounded shadow mt-10 bg-white">
      <div className="h-80 overflow-y-auto border-b p-2">
        {messages.map((msg, idx) => (
          <div key={idx} className={msg.type === "user" ? "text-right" : "text-left"}>
            <p className="p-2 my-1 rounded inline-block bg-gray-200">{msg.text}</p>
          </div>
        ))}
      </div>
      <div className="flex mt-2">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="flex-1 p-2 border rounded"
          placeholder="Type your message..."
        />
        <button onClick={sendMessage} className="ml-2 bg-blue-500 text-white p-2 rounded">
          Send
        </button>
      </div>
    </div>
  );
}
