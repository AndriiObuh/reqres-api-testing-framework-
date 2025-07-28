# Reqres API Testing Framework

This is an API automation testing framework for [reqres.in](https://reqres.in) using Python, Pytest, and Allure.

##  Features

-  Test automation using Pytest
-  API Object Model structure
-  Allure test reporting
-  Environment variables via `.env`
-  Structured test cases (positive & negative)
-  Logging via Loguru

---

Installation

```bash
git clone git@github.com:AndriiObuh/reqres-api-testing-framework-.git
cd reqres-api-testing-framework-
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt


Run Tests

pytest --alluredir=allure-results
allure serve allure-results

Project Structure

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
└── README.md

Allure Reporting

1. Install Allure:

brew install allure            # for Mac
scoop install allure           # for Windows

2. Run and open report:

pytest --alluredir=allure-results
allure serve allure-results

Author
Andrii Obuh

