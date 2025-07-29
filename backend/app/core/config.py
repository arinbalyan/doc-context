from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SUPABASE_URL: str
    SUPABASE_KEY: str
    QDRANT_URL: str
    QDRANT_API_KEY: str
    OPENROUTER_API_KEY: str
    API_BEARER_TOKEN: str
    QDRANT_COLLECTION_NAME: str = "hackrx_documents"

    class Config:
        env_file = ".env"

settings = Settings()
