import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME: str = "Fintech Trading System"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/trades_db")
    REDIS_BROKER_URL: str = os.getenv("REDIS_BROKER_URL", "redis://redis:6379/0")
    AWS_ACCESS_KEY_ID: str = os.getenv("AWS_ACCESS_KEY_ID", "")
    AWS_SECRET_ACCESS_KEY: str = os.getenv("AWS_SECRET_ACCESS_KEY", "")
    AWS_S3_BUCKET: str = os.getenv("AWS_S3_BUCKET", "your-bucket-name")

settings = Settings()
