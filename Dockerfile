FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copying the entire project
COPY . .

COPY .env .env

#Default command — run tests with Allure results
CMD ["pytest", "--alluredir=allure-results"]
