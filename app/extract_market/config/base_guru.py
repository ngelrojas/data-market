import os


API_BASE_URL = os.environ.get("GURU_BASE_URL", "http://localhost:8000")
API_TOKEN = os.environ.get("GURU_API_TOKEN", "token")

API_PUBLIC_URL = f"{API_BASE_URL}/public/user/{API_TOKEN}"
