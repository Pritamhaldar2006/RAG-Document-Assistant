from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

from App.prompt import PROMPT
from App.config import GOOGLE_API_KEY

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "database",
    embedding,
    allow_dangerous_deserialization=True
)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY
)

def ask(question):

    docs = db.similarity_search(question, k=3)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    prompt = PROMPT.format(
        context=context,
        question=question
    )

    response = llm.invoke(prompt)

    return response.content