# 📚 RAG Document Assistant

A Retrieval-Augmented Generation (RAG) chatbot that answers questions based on a college resource PDF. The application extracts information from the PDF, stores it in a FAISS vector database, retrieves the most relevant content for each query, and uses Google's Gemini model to generate accurate, context-aware responses.

## 🚀 Features

* 📄 Chat with your college PDF
* 🤖 AI-powered answers using the Gemini API (Any other APIs can be used as well)
* 🔍 Semantic search with FAISS vector database
* 🧠 Sentence Transformer embeddings
* ⚡ FastAPI backend
* 💬 React frontend with a chatbot interface
* 💾 Persistent chat history using Local Storage
* 🚫 Responds with an appropriate message when the answer is not available in the uploaded PDF

---

## 🛠️ Tech Stack

### Frontend

* React
* Vite
* Axios
* CSS

### Backend

* FastAPI
* LangChain
* Google Gemini API

### RAG Components

* PyPDFLoader
* RecursiveCharacterTextSplitter
* Sentence Transformers (`all-MiniLM-L6-v2`)
* FAISS Vector Store

---

## 📂 Project Structure

```text
PDF-Chatbot/
│
├── App/
│   ├── config.py
│   ├── ingest.py
│   ├── main.py
│   ├── prompt.py
│   └── rag.py
│
├── data/
│   └── notes.pdf
│
├── database/
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
│
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ How It Works

1. Load the PDF using `PyPDFLoader`.
2. Split the document into smaller chunks.
3. Generate embeddings for each chunk.
4. Store embeddings in a FAISS vector database.
5. Convert the user's question into an embedding.
6. Retrieve the most relevant document chunks.
7. Send the retrieved context and question to the Gemini model.
8. Return the generated answer to the React frontend.

---

## 🔄 Workflow

```text
College PDF
      │
      ▼
PDF Loader
      │
      ▼
Text Chunking
      │
      ▼
Sentence Embeddings
      │
      ▼
FAISS Vector Database
      │
      ▼
User Question
      │
      ▼
Similarity Search
      │
      ▼
Relevant Context
      │
      ▼
Gemini API
      │
      ▼
Generated Answer
      │
      ▼
React Chat Interface
```

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/<repository-name>.git
cd <repository-name>
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 3. Install Backend Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

### 5. Add Your PDF

Place your PDF inside the `data` directory.

Example:

```text
data/
└── notes.pdf
```

---

### 6. Create the FAISS Vector Database

```bash
python App/ingest.py
```

---

### 7. Start the FastAPI Server

```bash
uvicorn App.main:app --reload
```

The backend will run at:

```
http://127.0.0.1:8000
```

API documentation:

```
http://127.0.0.1:8000/docs
```

---

### 8. Start the React Frontend

Open a new terminal.

```bash
cd frontend
npm install
npm run dev
```

The frontend will be available at:

```
http://localhost:5173
```

---

## 📸 Screenshots

Add screenshots here after uploading the project.

### Chat Interface

```
(Add Screenshot)
```

### API Documentation

```
(Add Screenshot)
```

---

## 🔮 Future Improvements

* Upload multiple PDFs
* Display page numbers and source citations
* Conversation memory using a database
* User authentication
* Streaming AI responses
* Markdown support
* Dark/Light theme toggle
* Voice input and speech output
* Docker support
* Cloud deployment

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.


---

## 👨‍💻 Author

**Pritam Haldar**

If you found this project helpful, consider giving it a ⭐ on GitHub!

