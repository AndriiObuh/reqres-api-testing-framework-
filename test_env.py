import os
from dotenv import load_dotenv

# Завантажуємо .env тільки якщо змінна не задана через середовище (наприклад, в CI)
if not os.getenv("API_KEY"):
    load_dotenv()

api_key = os.getenv("API_KEY")

if api_key:
    print("✅ API_KEY successfully loaded.")
    print(f"🔒 API_KEY: {api_key[:4]}****")  # часткове відображення ключа для перевірки
else:
    print("❌ API_KEY not found. Check your .env file or environment variables.")