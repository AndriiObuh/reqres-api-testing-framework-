# Reqres API Testing Framework

This is an API automation testing framework for [reqres.in](https://reqres.in) using Python, Pytest, and Allure.

## Features

- Test automation using Pytest  
- API Object Model structure  
- Allure test reporting  
- Environment variables managed via .env (locally) and GitHub Secrets (in CI)  
- Structured test cases (positive & negative)  
- Logging via Loguru  
- Dockerized test execution  
- Continuous Integration with GitHub Actions 

## Installation
```bash
git clone git@github.com:AndriiObuh/reqres-api-testing-framework-.git
cd reqres-api-testing-framework-
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```


## Environment Setup
- Local:
Create a .env file in the project root (this file is in .gitignore) with your API key:
```bash
API_KEY=your_api_key_here
```
Replace your_api_key_here with your actual API key.

- CI / GitHub Actions:
The API key must be stored securely in GitHub Secrets:
Go to Settings → Secrets and variables → Actions → Repository secrets and add:
  - Name: API_KEY
  - Value: (your actual API key)

## Running Tests Locally
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## Running Tests with Docker
Build the Docker image:
```bash
docker build -t reqres-api-testing-framework .
```

Run tests inside Docker container (pass API key as environment variable):

```bash
# Replace <your_api_key> with your actual API key
docker run --rm \
  -e API_KEY=<your_api_key> \
  -v $(pwd)/allure-results:/app/allure-results \
  reqres-api-testing-framework
```

## Continuous Integration (GitHub Actions)
The workflow automatically builds the Docker image and runs tests on every push or pull request to the main branch.
Make sure the API_KEY secret is configured in your repository settings as described above.
Test results with Allure reports are uploaded as workflow artifacts.

## Project Structure
```plaintext
.
├── apis/
│   ├── base_api.py
│   ├── users_api.py
│   ├── auth_api.py
│   └── ...
├── tests/
│   ├── positive/
│   ├── negative/
│   └── conftest.py
├── .env.example
├── .gitignore
├── pytest.ini
├── requirements.txt
├── Dockerfile
├── .github/
│   └── workflows/
│       └── api_tests.yml
└── README.md
```

## Allure Reporting
Install Allure:

macOS:
```bash
brew install allure
```

Windows:
```bash
scoop install allure
```

Run and open report:
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## Author
Andrii Obuh
