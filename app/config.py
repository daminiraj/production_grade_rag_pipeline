import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    GEMINI_API_KEY= os.getenv("GEMINI_API_KEY")
    QDRANT_API_KEY= os.getenv("QDRANT_API_KEY")
    QDRANT_CLUSTER_ENDPOINT= os.getenv("QDRANT_CLUSTER_ENDPOINT")
    GROQ_API_KEY= os.getenv("GROQ_API_KEY")
    QDRANT_COLLECTION="enterprise_rag"
    GROQ_MODEL="llama-3.3-70b-versatile"

settings= Settings()
