
# Frontend Automation Framework

BDD automation framework for testing [Sauce Demo](https://www.saucedemo.com/) web application using **Behave** and **Selenium WebDriver** with **Page Object Model (POM)** design pattern.

---

## Tech Stack

- **Python 3.x** — Core language
- **Behave** — BDD test framework (Gherkin syntax)
- **Selenium WebDriver** — Browser automation
- **Page Object Model** — Design pattern for maintainable test code
- **HTML Reports** — Test execution reporting via behave-html-formatter

---

## Project Structure



---

## Features Tested

**Login Functionality** — Valid login, locked user login, empty credentials

**Product Search & Sort** — Product listing verification, price sorting, product detail navigation

**Shopping Cart** — Add to cart, add multiple products, remove from cart

---

## Visual Element Highlighting (UiPath-Style)

This framework includes a custom visual element highlighting capability inspired by UiPath's visual tracking. Every element interaction (click, type, find) is preceded by a visual highlight — a yellow background with a red border flashes on the target element before the action is performed.

This provides real-time visual feedback during test execution, making it easy to follow what the automation is doing at each step. The highlighting is built into the `BasePage` class, so every page object inherits this capability automatically without any additional code in step definitions.

The highlight behaviour (colour, border, duration) is configurable via the `highlight()` function in `utils/helper.py`.

---

## Setup and Installation

```bash
# Clone the repository
git clone https://github.com/sagyad/CreateFuture_TakeHomeTask_SagarYadav_frontend-automation-framework.git
cd CreateFuture_TakeHomeTask_SagarYadav_frontend-automation-framework

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run all tests
behave

# Run a specific feature
behave features/login.feature
behave features/search.feature
behave features/cart.feature

# Run with HTML report
behave --format html --outfile reports/full_report.html --format pretty

# Dry run (validate step definitions without executing)
behave --dry-run --no-capture --format steps.usage

BasePage
WebDriverWait
expected_conditions
time.sleep()
BasePage
config.py
environment.py
before_scenario
after_scenario
dev
main

Design Decisions

Page Object Model — All page interactions are encapsulated in page classes, keeping step definitions thin and maintainable. Locators are stored as class-level constants for easy updates. If the UI changes, only the page class needs updating — step definitions remain untouched.
BasePage Inheritance — Common methods (find, click, enter_text, get_text) are defined once in BasePage and inherited by all page classes, eliminating code duplication. Visual highlighting is embedded at this level, ensuring consistent tracking across all pages.
Explicit Waits — All element interactions use Selenium explicit waits (WebDriverWait with expected_conditions) instead of time.sleep(), ensuring reliable test execution across varying network conditions and page load times.
Visual Element Highlighting — Inspired by UiPath's visual tracking, every element interaction includes a highlight flash (yellow background, red border) before the action is performed. This is built into BasePage, so all page objects inherit it automatically.
Configurable Settings — Browser type, timeouts, and test credentials are centralised in config.py for easy environment switching between development, staging, and production.
Scenario Outline with Examples — Data-driven testing uses Behave's Examples tables to run the same scenario with multiple data sets, reducing feature file duplication.
Background Steps — Common setup steps (login) are defined once per feature file using Behave's Background keyword, avoiding repetition across scenarios.
Environment Hooks — Browser lifecycle (setup and teardown) is managed in environment.py using before_scenario and after_scenario hooks, ensuring clean browser state for every test.
Branching Strategy
    main — Stable, tested code only
    dev — Active development branch
All development work is done on the dev branch. Once features are tested and passing, they are merged into main to maintain a stable, deployable codebase at all times.