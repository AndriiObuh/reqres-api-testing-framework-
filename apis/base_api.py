import os
import allure
import requests
from loguru import logger
from dotenv import load_dotenv

load_dotenv()
os.makedirs("logs", exist_ok=True)
logger.add("logs/api.log", rotation="500 KB", retention="10 days", level="INFO")


class BaseAPI:
    """Base class for making API requests with headers and logging."""

    BASE_URL = "https://reqres.in/"
    HEADERS = {"x-api-key": os.getenv("API_KEY")}

    def request(self, method: str, endpoint: str, **kwargs):
        """Send an HTTP request and return the response."""
        url = f"{self.BASE_URL}{endpoint}"
        masked_headers = self.HEADERS.copy()
        if "x-api-key" in masked_headers:
            masked_headers["x-api-key"] = "****MASKED****"

        logger.info(f"{method.upper()} {url}")
        logger.info(f"Request headers: {masked_headers}")
        logger.info(f"Request data: {kwargs}")

        with allure.step(f"{method.upper()} {endpoint}"):
            response = requests.request(method, url, headers=self.HEADERS, **kwargs)
            logger.info(f"Response: {response.status_code} {response.text}")
            return response
