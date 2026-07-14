import os
from dotenv import load_dotenv
from pydantic import AliasChoices, Field, field_validator
load_dotenv()

class Settings:
    GEMINI_API_KEY= os.getenv("GEMINI_API_KEY")
    QDRANT_API_KEY= os.getenv("QDRANT_API_KEY")
    QDRANT_CLUSTER_ENDPOINT= os.getenv("QDRANT_CLUSTER_ENDPOINT")
    QDRANT_URL=os.getenv("QDRANT_CLUSTER_ENDPOINT")
    GROQ_API_KEY= os.getenv("GROQ_API_KEY")
    QDRANT_COLLECTION="enterprise_rag"
    GROQ_MODEL="llama-3.3-70b-versatile"
    PORTKEY_API_KEY=os.getenv("PORTKEY_API_KEY")
    GROQ_SLUG=os.getenv("GROQ_SLUG")
    GROQ_SLUG_2=os.getenv("GROQ_SLUG_2")
    


settings= Settings()