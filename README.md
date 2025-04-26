# LangGraph AI Chat 💬

Smart. Friendly. Powerful.

---

## 🚀 Overview

**LangGraph AI Chat** is a lightweight, production-ready AI chatbot that dynamically selects LLMs from **Groq** and **OpenAI**.  
It supports real-time web search using **Tavily** to enhance responses when needed.

Built with:
- **FastAPI** (Backend API)
- **Streamlit** (Frontend Interface)
- **LangChain + LangGraph** (Agent Framework)
- **Pydantic** (Schema Validation)
- **Tavily** (Optional Real-Time Search)

---

## 🛠 Features

- 🔥 Dynamic LLM selection (Groq / OpenAI)
- 🧠 ReAct-based AI agent with LangGraph
- 🌐 Optional search tool integration (Tavily)
- 🖥️ Clean and responsive Streamlit frontend
- 📄 Swagger UI documentation (`/docs`)
- ⚡ Fast, minimalist, and easy to extend

---

## 📦 Project Structure


---

## ⚙️ Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/langgraph-ai-chat.git
   cd langgraph-ai-chat
```
pip install -r requirements.txt
export GROQ_API_KEY="your-groq-api-key"
export TAVILY_API_KEY="your-tavily-api-key"
export OPENAI_API_KEY="your-openai-api-key"
uvicorn main:app --reload --host 127.0.0.1 --port 8083
streamlit run streamlit_app.py
```
## API Usage
```
Request Body: 
{
  "model_name": "llama3-70b-8192",
  "model_provider": "Groq",
  "system_prompt": "Act as an AI chatbot who is smart and friendly",
  "messages": ["Hello, who are you?"],
  "allow_search": true
}
Response:
{
  "message": "success",
  "response": "Hello! I'm your smart and friendly AI assistant."
}
```
## Access full documentation at:
👉 http://127.0.0.1:8083/docs

## Future Improvements
 Multi-turn conversation history

 Add memory and personalization

 Plugin integrations

 Dark mode toggle for frontend

 🤝 Contributing
Pull requests are welcome.
For major changes, please open an issue first to discuss what you would like to change.



