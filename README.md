# 🛒 OpenCart QA Automation Project

This is a comprehensive end-to-end QA Automation project developed using Python to test OpenCart's e-commerce platform. It includes UI tests, API testing, and BDD with Gherkin syntax — built for scalability, clarity, and real-world CI/CD readiness.

---

## 📌 Project Overview

This project simulates how a QA Automation Engineer would work in an Agile team, covering:

- ✅ Manual test planning and strategy
- ✅ Selenium-based UI automation
- ✅ REST API testing with `requests` and `Postman`
- ✅ Behavior-Driven Development (BDD) with `Behave`
- ✅ Page Object Model (POM) for maintainability
- ✅ Integration with a MySQL database for dynamic test data
- ✅ Logging, assertions, and clean structure following SRP & DRY principles

---

## 🧰 Tech Stack

| Area        | Tools/Libraries                       |
| ----------- | ------------------------------------- |
| Language    | Python 3.11+                          |
| UI Testing  | Selenium, Pytest, POM                 |
| API Testing | `requests`, Postman                   |
| BDD         | Behave, Gherkin                       |
| DB          | MySQL (via XAMPP)                     |
| Logging     | Python `logging` module               |
| Others      | Undetected ChromeDriver, ConfigParser |

---

## 🗂️ Project Structure

```
OpenCartDemoSimulation/
├── features/                 # BDD feature files
│   └── steps/                # Step definitions
├── pageObjects/             # Page classes for POM (UI)
├── tests/                   # Pytest-based test cases (UI & API)
├── utilities/               # Config, DB access, logger, helpers
├── resources.py             # API endpoint payloads
├── configurations.py        # DB & config management
├── properties.ini           # DB and environment config
└── README.md                # You're here!
```

---

## ⚙️ Setup Instructions

1. **Clone the repo**:

   ```bash
   git clone https://github.com/caioaza/opencart-qa-automation.git
   cd opencart-qa-automation
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # on Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up MySQL with XAMPP**:
   - Start Apache & MySQL via XAMPP Control Panel
   - Create the necessary DB and table(s) for test data
   - Update `properties.ini` with your credentials.

---

## 🧪 Running Tests

### ✅ Run All UI Tests (Pytest)

```bash
pytest OpenCartDemoSimulation/tests/
```

### ✅ Run Only One Specific Test

```bash
pytest OpenCartDemoSimulation/tests/test_cart.py::TestCart::test_1_verify_items_data
```

---

## 🌐 API Testing

### ▶️ Run API Tests via Pytest

```bash
pytest OpenCartDemoSimulation/tests/test_cart_api.py
```

### 📫 API Test Using DB-Driven Payload

- Pulls product IDs from local MySQL to build dynamic payload
- Sends POST requests to the OpenCart Bulk Cart API

---

## 🧪 BDD Testing with Behave

### ▶️ Run All Scenarios

```bash
behave OpenCartDemoSimulation/features/
```

### ▶️ Tag Specific Scenarios (UI or API)

```bash
behave -t @browser
behave -t @api
```

---

## 🔐 Credentials & Config

Sensitive data like DB credentials, API keys, and URLs are managed via:

- `properties.ini`
- `configurations.py`

Make sure these are updated before running tests.

---

## 📋 Notable Features

- 📦 Page Object Model for test stability
- 🐞 Handles stale elements & dynamic waits
- 🔁 Clean test-data teardown (cart cleanup logic)
- ✅ Assertion messages for clear failures
- 🧪 Tests cover:
  - Product search & filtering
  - Add to cart & quantity updates
  - Price validation
  - Login (positive/negative cases)
  - API payload building from DB
  - Full BDD integration

---

## 🙋‍♂️ About Me

I'm a QA Automation Engineer focused on **real-world testing scenarios**, clean architecture, and continuously learning modern testing tools. This project is my way to demonstrate what I can bring to your QA team — from code quality to test coverage to project structure.

---

## 📧 Contact

Feel free to reach out via [LinkedIn](https://www.linkedin.com/in/your-profile) or GitHub if you'd like to discuss this project or QA opportunities.

---
