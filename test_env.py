import os

def test_api_key_loaded():
    api_key = os.getenv("API_KEY")
    assert api_key is not None and api_key != "", "API_KEY не завантажено!"
    print(f"✅ API_KEY successfully loaded.\n🔒 API_KEY: {api_key[:4]}****")

if __name__ == "__main__":
    test_api_key_loaded()