# OpenCart QA Automation Project

This project is a simulated QA automation framework to test OpenCart's e-commerce platform, created as a portfolio piece to demonstrate my hands-on knowledge in UI tests, API testing, and BDD with Gherkin syntax — built for scalability, clarity, and real-world CI/CD readiness, while testing.

It is not intended to be a full test suite of the entire OpenCart application, but rather a sample project with a selection of tests to showcase best practices in test design, automation, and framework structure.

---

## Project Overview

This project simulates how a QA Automation Engineer would work in an Agile team, covering:

- ✅ Manual test planning and strategy
- ✅ Selenium-based UI automation
- ✅ REST API testing with `Python requests`
- ✅ Behavior-Driven Development (BDD) with `Behave`
- ✅ Page Object Model (POM) for maintainability
- ✅ Integration with a MySQL database for dynamic test data
- ✅ Logging, assertions, and clean structure following SRP & DRY principles

---

## Technologies Used

- Python
- Selenium WebDriver (UI Automation)
- Pytest (UI test runner)
- Behave/Cucumber (BDD for UI and API scenarios)
- Allure Reports (Test reporting)
- Requests (API testing)
- MySQL Connector (Database interaction)

---

## Project Structure

```
OpenCartDemoSimulation/
├── features/                 # BDD feature files
│   └── steps/                # Step definitions (UI & API Testing)
├── pageObjects/             # Page classes for POM (UI)
├── tests/                   # Pytest-based test cases (UI)
├── utilities/               # Reusable config, database, logger, and helper functions
├── reports/                 # Allure results, generated reports and logfile
├── conftest.py              # DB and environment config
├── requirements.txt         # Python packages that need to be installed
└── README.md                # You're here!
```

---

## ⚙️ Setup Instructions

1. **Install OpenCart**:

   Install OpenCart v4.1.0.2
   https://www.opencart.com/index.php?route=cms/download

2. **Clone the repo**:

   ```bash
   git clone https://github.com/caioaza/OpenCartDemoSimulation

   ```

3. **Create and activate a virtual environment**:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # on Windows: .venv\Scripts\activate
   ```

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

## Running Tests

### Run All UI Tests (with Pytest HTML Report)

```bash
 py.test tests/ --html=../reports/report.html --tb=short
```

### Run Only One Specific Test

```bash
pytest tests/test_cart.py::TestCart::test_1_verify_items_data
```

---

## API Testing

### Run API Tests with Behave (Run from one level above the OpenCartDemoSimulation/ directory)

```bash
behave OpenCartDemoSimulation/features -t "@cart_bulk_api"
behave OpenCartDemoSimulation/features -t "@search_products_api"
```

### API Test Using DB-Driven Payload

- Pulls product IDs from local MySQL to build dynamic payload
- Sends POST requests to the OpenCart Bulk Cart API

---

## BDD Testing with Behave

### Run All Scenarios
(Run from one level above the OpenCartDemoSimulation/ directory)

```bash
behave OpenCartDemoSimulation/features/
```

### Run Specific UI Scenario
(Run from one level above the OpenCartDemoSimulation/ directory)

```bash
behave OpenCartDemoSimulation/features -t "@browser"
```

### Generate the Allure Report and open in Browser
(Run from one level above the OpenCartDemoSimulation/ directory)

```bash
# 1. Run tests
behave OpenCartDemoSimulation/features -f allure_behave.formatter:AllureFormatter -o OpenCartDemoSimulation/reports/allure-results

# 2. Generate Allure Report
allure generate OpenCartDemoSimulation/reports/allure-results -o OpenCartDemoSimulation/reports/allure-report --clean

# 3. Open report
allure open OpenCartDemoSimulation/reports/allure-report
```

---

## 📊 Allure Test Report Overview
This PDF summarises the test coverage and results from Allure.

[📄 View Report](./docs/Allure_Test_Report_Overview.pdf)


## Credentials & Config

Sensitive data like DB credentials, API keys, and URLs are managed via:

- `properties.ini`
- `configurations.py`

Make sure these are updated before running tests.

---

## Notable Features

- Page Object Model for test stability
- Handles stale elements & dynamic waits
- Clean test-data teardown (cart cleanup logic)
- Assertion messages for clear failures
- Allure Report
- Pytest HTML Report
- **Tests cover:**
- Product search & filtering
- Add to cart & quantity updates
- Price validation
- Login (positive/negative cases)
- API payload building from DB
- BDD integration

---

## About Me

I'm a QA Automation Engineer focused on **real-world testing scenarios**, clean architecture, and continuously learning modern testing tools. This project is my way to demonstrate what I can bring to your QA team — from code quality to test coverage to project structure.

---

## 📧 Contact

Feel free to reach out via [LinkedIn](https://www.linkedin.com/in/caio-aza) or GitHub if you'd like to discuss this project or QA opportunities.

---
