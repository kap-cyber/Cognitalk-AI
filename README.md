# 🤖 AI Chatbot — LangChain & Groq

A conversational AI chatbot built with **Python, Streamlit, LangChain, and Groq API**. The application supports contextual conversations, reusable prompt templates, and real-time streaming responses.

## 🚀 Features

- **Conversational AI:** Maintains conversation history across multiple interactions.
- **Real-Time Streaming:** Displays AI responses progressively as they are generated.
- **Context-Aware Responses:** Uses previous messages to maintain conversational context.
- **Reusable Prompt Templates:** Implements LangChain's `ChatPromptTemplate` for structured prompt management.
- **Dynamic Conversation History:** Uses `MessagesPlaceholder` to inject conversation history into prompts.
- **New Chat:** Allows users to clear existing conversation history and start fresh.
- **Input Validation:** Handles empty inputs and enforces a maximum message length of 5,000 characters.
- **Error Handling:** Handles API failures and missing API credentials gracefully.
- **Secure Configuration:** Loads API credentials from environment variables using `python-dotenv`.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.13.2 | Backend development |
| Streamlit | Chat interface |
| LangChain | LLM integration and orchestration |
| LangChain-Groq | Groq model integration |
| Groq API | LLM inference |
| python-dotenv | Environment variable management |

**LLM Model:** `openai/gpt-oss-20b`

## 🏗️ Project Architecture

```text
User Input
    |
    v
Streamlit Chat Interface
    |
    v
Session State
(Conversation History)
    |
    v
ChatPromptTemplate
    |
    v
MessagesPlaceholder
    |
    v
LangChain Chain (LCEL)
    |
    v
Groq LLM
    |
    v
Streaming Response
    |
    v
Streamlit UI
```

## 📁 Project Structure

```text
AI_Chatbot/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
└── chatBotENV/
```

> The virtual environment and `.env` file are excluded from version control.

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI_Chatbot.git
```

### 2. Navigate to the Project Directory

```bash
cd AI_Chatbot
```

### 3. Create a Virtual Environment

```bash
python -m venv chatBotENV
```

Activate it on Windows PowerShell:

```powershell
.\chatBotENV\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root directory:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from [Groq Console](https://console.groq.com/).


### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🧠 Key Concepts Implemented

This project demonstrates practical implementation of:

- LangChain Chat Models
- ChatPromptTemplate
- MessagesPlaceholder
- LangChain Expression Language (LCEL)
- HumanMessage and AIMessage
- Python Session State management
- LLM streaming using `chain.stream()`
- Python generators and `yield`
- Streamlit `st.write_stream()`
- Exception handling and input validation

## 🔮 Future Improvements

- Persistent conversation storage
- Multiple conversation management
- Chat export functionality
- Token usage tracking
- Conversation summarization
- Deployment to a cloud platform

## 👨‍💻 Author

**Kapil Panchal**

Full-Stack Developer | AI/LLM Engineering Enthusiast



---

⭐ If you find this project interesting, consider giving it a star!