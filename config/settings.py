import os

from dotenv import load_dotenv


load_dotenv()


# =========================
# BASE DE DATOS
# =========================

DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


# =========================
# INTELIGENCIA ARTIFICIAL
# =========================

AI_PROVIDER = os.getenv(
    "AI_PROVIDER",
    "gemini"
)

AI_MODEL = os.getenv(
    "AI_MODEL",
    "gemini-2.5-flash"
)

OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY"
)

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY"
)