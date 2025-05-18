# setup_config.py
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 환경변수 읽기
API_KEY = os.getenv("API_KEY")
DB_URL  = os.getenv("DB_URL")
DEBUG   = os.getenv("DEBUG")

def print_config():
    print("===== Loaded Configuration =====")
    print(f"API_KEY = {API_KEY}")
    print(f"DB_URL  = {DB_URL}")
    print(f"DEBUG   = {DEBUG}")

if __name__ == "__main__":
    print_config()
