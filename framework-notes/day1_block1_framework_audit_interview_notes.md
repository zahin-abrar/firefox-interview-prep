# Day 1 Block 1 — Framework Baseline Audit Interview Notes

**Project:** Selenium Pytest Hybrid Automation Framework  
**Context:** Mozilla Firefox Software Test Engineering Student Worker — Round 2 Preparation  
**Day 1 Block:** Framework Baseline Audit  
**Purpose:** Understand the existing framework deeply enough to explain it, review it, identify improvement areas, and later build a cleaner framework mostly independently.

---

## 1. Why This Block Matters

The goal of Block 1 is not to refactor the existing framework immediately. The goal is to use the current project as a learning and interview-preparation artifact.

The framework helps demonstrate:

- Selenium WebDriver usage
- Pytest test execution
- Page Object Model design
- Pytest fixtures for setup and teardown
- Config-driven browser and URL handling
- Data-driven testing using Excel
- Allure screenshot-on-failure reporting
- Reusable support utilities
- Framework review and improvement thinking

For the Mozilla role, this is highly relevant because the role may involve automation framework work, Page Object Model maintenance, support scripts, PR review, CI-related thinking, and helping manual QA engineers transition toward automation.

---

## 2. Current Repository Structure

Observed root structure:

```text
SeleniumPythonHybridFramework/
├── .idea/
├── .pytest_cache/
├── .venv/
├── configurations/
├── docs/
├── ExcelFiles/
├── pages/
├── Reports/
├── tests/
├── utilities/
├── .gitignore
├── framework_architecture.png
└── README.md
```

Important framework folders:

```text
configurations/
└── config.ini

pages/
├── BasePage.py
├── HomePage.py
├── LoginPage.py
├── AccountPage.py
└── SearchPage.py

tests/
├── BaseTest.py
├── conftest.py
├── test_Login.py
└── test_Search.py

utilities/
├── ExcelUtils.py
└── ReadConfigurations.py

docs/
├── PART_1_Foundations.md
├── PART_2_Architecture.md
├── PART_3_Data_Reporting.md
├── PART_4_Design_Patterns.md
├── PART_5_Interview_Engineering.md
└── PART_6_Roadmap.md
```

---

## 3. High-Level Framework Explanation

Interview-ready version:

> This is a Selenium-Pytest hybrid automation framework built around the Page Object Model. The `pages` folder contains page classes such as `HomePage`, `LoginPage`, `SearchPage`, and `AccountPage`. These page classes hide Selenium locator and interaction details from the test layer. The `tests` folder contains Pytest test classes. Shared browser setup, teardown, and failure screenshot behavior are handled through Pytest fixtures in `conftest.py` and applied through `BaseTest`. Configuration values such as browser and URL are read from `config.ini`, and Excel-based test data is used with Pytest parametrization for data-driven testing.

Short version:

> The framework separates test scenarios, page interactions, reusable Selenium actions, configuration, and test data. This makes the test code cleaner and easier to maintain.

---

## 4. Architecture Flow

README architecture summary:

```text
Tests → BaseTest → Fixtures → Page Objects → BasePage → Selenium → Browser
```

Meaning:

1. Pytest discovers and runs test methods.
2. Test classes inherit from `BaseTest`.
3. `BaseTest` applies reusable fixtures.
4. Fixtures initialize WebDriver and open the application.
5. Test methods create page objects.
6. Page objects call reusable methods from `BasePage`.
7. `BasePage` calls Selenium WebDriver.
8. Selenium interacts with the browser.

Interview explanation:

> The test method stays readable because low-level Selenium operations are pushed downward into page classes and `BasePage`. This keeps the tests focused on scenario validation rather than locator mechanics.

---

## 5. Baseline Test Run Result

Command executed:

```powershell
pytest -v
```

Observed result:

```text
collected 5 items

tests/test_Login.py::TestLogin::test_login_with_valid_credentials[...] PASSED
tests/test_Login.py::TestLogin::test_login_with_valid_credentials[...] PASSED
tests/test_Search.py::TestSearch::test_search_for_a_valid_product PASSED
tests/test_Search.py::TestSearch::test_search_for_an_invalid_product PASSED
tests/test_Search.py::TestSearch::test_search_without_entering_any_product FAILED

1 failed, 4 passed in 43.35s
```

### Interpretation

The framework is runnable.

Working parts:

- Pytest discovery works.
- Browser setup and teardown work.
- `BaseTest` fixture application works.
- Excel-driven login parametrization works.
- Login POM flow works.
- Search POM flow works.
- Positive and negative search scenarios mostly work.

### Failing Test Diagnosis

The failing test is:

```python
test_search_without_entering_any_product
```

But the implementation searches for:

```python
"Honda"
```

and expects:

```python
"There is no product that matches the search criteria ABC."
```

Actual UI message:

```python
"There is no product that matches the search criteria."
```

This is not a product bug. It is a test-design issue.

Interview explanation:

> The framework ran successfully and 4 out of 5 tests passed. The failing test is caused by an inconsistency between test name, test input, and expected result. The test says it validates empty search, but it searches for `Honda`, and the expected message contains an intentionally incorrect suffix. I would align the test intent, input, and assertion before considering it a real regression failure.

---

## 6. Pytest Fixture and Driver Setup

### File

```text
tests/conftest.py
```

### Main fixtures

```python
setup_and_teardown
log_on_failure
pytest_runtest_makereport
```

### What `setup_and_teardown` does

The fixture:

1. reads browser from `config.ini`
2. creates the correct WebDriver
3. maximizes browser
4. reads URL from `config.ini`
5. opens the application
6. injects driver into the test class with `request.cls.driver`
7. yields control to the test
8. quits the browser after test execution

### What `log_on_failure` does

The fixture:

1. waits until the test finishes
2. checks test result status
3. attaches a screenshot to Allure if the test failed

### What `pytest_runtest_makereport` does

This Pytest hook stores test execution status on the test item so that the screenshot fixture can detect whether the test failed.

### Interview Explanation

> The framework uses Pytest fixtures to centralize browser setup and teardown. The browser and URL are read from config, then WebDriver is initialized and injected into the test class. After test execution, the browser is closed. A separate failure hook attaches screenshots to the Allure report when tests fail, which improves debugging.

### Strengths

- Reusable setup and teardown
- Config-driven browser execution
- Screenshot capture on failure
- Keeps browser lifecycle outside test methods
- Uses `yield`, which is the correct fixture pattern for setup + teardown

### Improvement Ideas for Future Framework

- Avoid global driver state.
- Raise a clear error for unsupported browser values.
- Normalize browser values using `.lower().strip()`.
- Make screenshot capture defensive for setup failures.
- Consider a dedicated `driver` fixture.
- Prepare for future parallel execution by avoiding global shared driver.

---

## 7. BaseTest Design

### File

```text
tests/BaseTest.py
```

### Current responsibility

`BaseTest` applies shared fixtures to every test class:

```python
@pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
class BaseTest:
    pass
```

### Interview Explanation

> `BaseTest` is a common parent class for test classes. It applies shared Pytest fixtures so individual test classes do not need to repeat setup, teardown, and failure-screenshot decorators. This keeps test classes cleaner.

### Strengths

- Reduces repeated fixture declarations
- Standardizes setup and teardown
- Makes test classes cleaner

### Improvement Ideas for Future Framework

- Keep fixture usage clear and documented.
- Consider whether class-based tests are necessary or whether function-based Pytest style would be simpler for some suites.
- Keep `BaseTest` lightweight.

---

## 8. BasePage Design

### File

```text
pages/BasePage.py
```

### Current responsibility

`BasePage` is the shared parent for all page objects.

It provides reusable Selenium wrapper methods:

```python
type_into_element()
element_click()
check_display_status_of_element()
retrieve_element_text()
get_element()
```

### Locator Resolver Design

`get_element()` uses locator-name suffixes to determine locator strategy.

Examples:

```text
email_address_field_id      → By.ID
password_field_id           → By.ID
login_button_xpath          → By.XPATH
search_box_field_name       → By.NAME
login_option_link_text      → By.LINK_TEXT
```

### Interview Explanation

> `BasePage` centralizes common Selenium actions such as typing, clicking, retrieving text, checking visibility, and resolving locators. Child page classes inherit these methods, which reduces duplicate WebDriver code and keeps page classes easier to maintain.

### Strengths

- Centralizes low-level Selenium actions
- Reduces repeated `find_element()` calls
- Keeps test files away from locators
- Provides reusable behavior for all page objects
- Demonstrates abstraction and separation of concerns

### Improvement Ideas for Future Framework

- Add explicit waits for visibility and clickability.
- Raise clear errors for unsupported locator suffixes.
- Avoid returning `None` silently when locator type is unsupported.
- Add better exception handling and logging.
- Consider standard method names such as `click`, `type_text`, `get_text`, and `is_displayed`.

### Important Interview Point

Current `BasePage` directly calls:

```python
self.driver.find_element(...)
```

This works, but can cause flaky tests if elements load asynchronously.

Future improvement:

> Add explicit waits in `BasePage` so all page actions become more stable.

---

## 9. Login Flow Review

### Files

```text
pages/HomePage.py
pages/LoginPage.py
pages/AccountPage.py
tests/test_Login.py
```

### Flow

```text
TestLogin
  ↓
HomePage(self.driver)
  ↓
home_page.navigate_to_login_page()
  ↓
LoginPage
  ↓
login_page.login_to_application(email, password)
  ↓
AccountPage
  ↓
assert account_page.display_status_of_edit_your_account_information_option()
```

### What `LoginPage` Does Well

`LoginPage` has:

- locators
- atomic actions
- workflow method

Atomic actions:

```python
enter_email_address()
enter_password()
click_login_button()
```

Workflow method:

```python
login_to_application()
```

### Interview Explanation

> The login flow starts from `HomePage`, navigates to `LoginPage`, performs the login workflow, and returns an `AccountPage` object for validation. The test does not directly interact with locators. It calls readable page methods, which keeps the test scenario clear.

### Data-Driven Login

The login test uses:

```python
@pytest.mark.parametrize(
    "email_address, password",
    ExcelUtils.get_data_from_excel("ExcelFiles/TestData.xlsx", "LoginTest")
)
```

Interview explanation:

> I used Pytest parametrization with Excel data, so the same login test can run with multiple credential rows without duplicating test logic.

### Strengths

- Clean POM flow
- Page chaining from `LoginPage` to `AccountPage`
- Reusable atomic actions
- Business-level workflow method
- Excel-driven test data
- Test logic remains readable

### Improvement Ideas for Future Framework

- Remove `time.sleep(3)`.
- Replace visual waits with explicit waits.
- Add descriptive assertion messages.
- Separate positive and negative login data clearly.
- For invalid login, remain on `LoginPage` and validate warning/error message instead of returning `AccountPage`.

---

## 10. Search Flow Review

### Files

```text
pages/HomePage.py
pages/SearchPage.py
tests/test_Search.py
```

### Flow

```text
TestSearch
  ↓
HomePage(self.driver)
  ↓
home_page.search_for_a_product(product_name)
  ↓
SearchPage
  ↓
assert valid product / no-product message
```

### Search Tests

Current tests:

```python
test_search_for_a_valid_product
test_search_for_an_invalid_product
test_search_without_entering_any_product
```

### Interview Explanation

> The search tests use `HomePage` to perform the search workflow and then use `SearchPage` to validate the result. This keeps the tests readable and separates UI interaction from test assertion logic.

### Strengths

- Positive search scenario included
- Negative search scenario included
- Search workflow is encapsulated in `HomePage`
- `SearchPage` hides search-result locators from tests
- Test files remain business-readable

### Important Audit Finding

`test_search_without_entering_any_product` has mismatched intent:

- test name says empty search
- implementation searches for `"Honda"`
- expected message includes `"ABC"` incorrectly

Interview explanation:

> This is a good PR-review example. A test can be executable but still poorly aligned if its name, input, and expected result do not match.

### Improvement Ideas for Future Framework

- Fix test intent/input/expected-result mismatch.
- Replace `.__eq__()` with `==`.
- Add assertion messages.
- Parameterize search test data.
- Make product validation dynamic.
- Replace brittle absolute XPath locators.
- Add explicit waits before result validation.

---

## 11. SearchPage Review

### File

```text
pages/SearchPage.py
```

### Current responsibility

`SearchPage` represents the search results page.

It provides:

```python
display_status_of_valid_products()
retrieve_no_product_message()
```

### Interview Explanation

> `SearchPage` exposes validation methods for positive and negative search scenarios. For a valid search, it checks whether a known product appears. For an invalid or empty search, it retrieves the no-results message for assertion.

### Strengths

- Clear page responsibility
- Locators hidden from tests
- Supports positive and negative search validation
- Keeps UI retrieval logic in the page layer

### Improvement Ideas for Future Framework

- Rename `display_status_of_valid_products()` because it checks one specific HP product.
- Make product validation dynamic.
- Add explicit waits through `BasePage`.
- Align docstrings with actual Selenium behavior when missing elements raise exceptions.

---

## 12. Utility Layer Review

### Files

```text
utilities/ReadConfigurations.py
utilities/ExcelUtils.py
```

---

### 12.1 ReadConfigurations.py

Current responsibility:

```python
read_configuration(category, key)
```

It reads values from:

```text
configurations/config.ini
```

Example:

```ini
[basic info]
browser=chrome
url=https://tutorialsninja.com/demo/
```

Interview explanation:

> `ReadConfigurations.py` centralizes configuration access. Browser and URL values are read from `config.ini`, so test setup does not hardcode execution settings.

Strengths:

- Separates config values from code
- Makes browser/URL switching easier
- Supports cleaner fixture design

Future improvements:

- Add handling for missing config file
- Add handling for missing section/key
- Normalize config values
- Consider environment-specific config profiles later

---

### 12.2 ExcelUtils.py

Current responsibility:

```python
get_data_from_excel(path, sheet_name)
```

It:

1. opens an Excel workbook
2. selects a sheet
3. skips the header row
4. reads each data row
5. returns a list of rows for `pytest.mark.parametrize`

Example return value:

```python
[
    ["user1@example.com", "pass1"],
    ["user2@example.com", "pass2"]
]
```

Interview explanation:

> `ExcelUtils.py` supports data-driven testing. It reads rows from Excel and returns them in a format Pytest can use for parametrization. This allows one test method to run with multiple input combinations.

Strengths:

- Supports data-driven testing
- Keeps test data outside test code
- Avoids duplicated login tests
- Easy to explain to manual QA engineers

Future improvements:

- Add handling for missing file or sheet
- Skip empty rows if needed
- Validate expected column count
- Consider returning dictionaries using header names
- Consider CSV or JSON for simpler Git diffs

---

## 13. README Review

The README already explains:

- project overview
- architecture summary
- key features
- tech stack
- folder structure
- execution flow
- data-driven testing
- design decisions
- framework strengths
- improvement roadmap
- interview talking points

### Strengths

- Clear project framing
- Good feature list
- Execution flow is easy to explain
- Design decisions are useful for interview prep
- Improvement roadmap already includes important next steps
- Architecture image is a nice portfolio artifact

### Issues / Improvement Ideas

- Fix encoding issues such as `â†’` and broken folder-tree characters.
- Reword “production-style” as “portfolio framework inspired by production-style architecture.”
- Replace “Why no driver in tests?” with “Why centralized driver setup?”
- Add a “Current Limitations” section.
- Add dependency installation through `requirements.txt`.

### Interview-Friendly README Framing

> This is a learning and portfolio framework inspired by production-style architecture. It demonstrates POM, Pytest fixtures, reusable BasePage methods, Excel data-driven testing, config-driven execution, and Allure reporting. Reviewing it now also helps me identify improvements for a cleaner next framework.

---

## 14. Supporting Documentation Folder

The `docs/` folder contains six supporting learning documents:

```text
PART_1_Foundations.md
PART_2_Architecture.md
PART_3_Data_Reporting.md
PART_4_Design_Patterns.md
PART_5_Interview_Engineering.md
PART_6_Roadmap.md
```

Most relevant for Mozilla prep:

1. `PART_2_Architecture.md`  
   Useful for explaining framework layers, POM, fixtures, BasePage, and separation of concerns.

2. `PART_3_Data_Reporting.md`  
   Useful for explaining Excel data-driven testing and Allure reporting.

3. `PART_5_Interview_Engineering.md`  
   Useful for mock interview preparation.

4. `PART_6_Roadmap.md`  
   Useful for “what would you improve next?” answers.

---

## 15. Current Framework Strengths

The current framework demonstrates:

- Page Object Model structure
- Separation of tests and page interactions
- Reusable `BasePage`
- Pytest fixture-based setup and teardown
- Config-driven execution
- Excel data-driven testing
- Allure screenshot-on-failure reporting
- Positive and negative test scenarios
- Layered architecture thinking
- Support utility design
- Documentation effort

Interview phrase:

> This project helped me understand how test automation frameworks are structured beyond simple test scripts.

---

## 16. Current Limitations / Improvement Ideas

These are not immediate changes for the current framework. They are notes for the next cleaner framework after Day 5.

### Selenium Stability

- Add explicit waits.
- Avoid `time.sleep`.
- Improve handling of dynamic elements.
- Replace brittle absolute XPath.

### Pytest / Fixture Design

- Avoid global driver state.
- Create a cleaner `driver` fixture.
- Improve screenshot handling for setup failures.
- Add markers such as `smoke` and `regression`.

### Assertions

- Use `==` instead of `.__eq__()`.
- Add descriptive assertion messages.
- Align test names, inputs, and expected results.

### Config / Test Data

- Add defensive config reading.
- Validate Excel sheet/file existence.
- Consider CSV/JSON or dictionary-based test data.

### Project Setup

- Add `requirements.txt`.
- Add `pytest.ini`.
- Expand `.gitignore`.
- Add CI workflow later.
- Fix README encoding issues.

### Framework Maturity

- Add logging.
- Add reporting artifacts.
- Add CI/CD integration.
- Add test monitoring concept.
- Consider parallel execution support.
- Add cleaner folder naming using Python conventions.

---

## 17. PR Review Practice Notes

This framework gives several useful PR-review scenarios.

### Example PR Review Comments

Good:

```text
- The framework follows Page Object Model and keeps locators out of test files.
- BasePage reduces repeated Selenium code.
- Fixtures centralize setup and teardown.
- Excel data supports data-driven login testing.
- Allure screenshot capture improves debugging.
```

Requested improvements:

```text
- Replace hard sleeps with explicit waits.
- Avoid global driver state.
- Add clearer error handling for unsupported browser config.
- Replace brittle absolute XPath locators.
- Add assertion messages.
- Fix the search test where name, input, and expected result do not match.
- Use `==` instead of directly calling `.__eq__()`.
```

Interview framing:

> A good automation PR should not only run. It should be readable, stable, maintainable, and easy to debug when it fails.

---

## 18. QA Perspective: Why This Framework Matters

### POM

Useful because UI changes often require updating locators or interactions in one page class instead of many test files.

### Fixtures

Useful because browser setup and teardown should not be duplicated across every test.

### Config Reader

Useful because tests should not hardcode browser or environment values.

### Excel Data Reader

Useful because the same test scenario can be executed with multiple data combinations.

### Allure Screenshot on Failure

Useful because failed UI tests need evidence for debugging.

### BasePage

Useful because common Selenium actions should be reusable and consistent.

### PR Review Mindset

Useful because automation quality is not only about whether a test passes once. It is about whether the test remains stable, readable, and valuable over time.

---

## 19. 2-Minute Framework Walkthrough

> This is my Selenium-Pytest hybrid automation framework project. I built it to practice framework design using Python, Selenium WebDriver, Pytest, Page Object Model, Excel test data, and Allure reporting.
>
> The framework has separate layers. Test classes are under `tests`, page objects are under `pages`, reusable utilities are under `utilities`, and execution settings are under `configurations`. Test classes inherit from `BaseTest`, which applies Pytest fixtures for browser setup, teardown, and failure screenshot handling.
>
> Page classes such as `HomePage`, `LoginPage`, `SearchPage`, and `AccountPage` inherit from `BasePage`. `BasePage` centralizes common Selenium actions like clicking, typing, retrieving text, checking visibility, and resolving locators.
>
> For login testing, I used Pytest parametrization with Excel data so the same test can run with multiple credential rows. For reporting, failed tests can attach screenshots to Allure.
>
> Reviewing the framework now, I can also identify improvements for a cleaner next version, such as adding explicit waits, removing hard sleeps, avoiding global driver state, using more stable locators, adding assertion messages, adding `pytest.ini` and `requirements.txt`, and preparing CI integration.

---

## 20. 30-Second Framework Walkthrough

> This framework demonstrates Selenium UI automation with Pytest and Page Object Model. Tests are separated from page interactions, common Selenium actions are centralized in `BasePage`, browser setup and teardown are handled by fixtures, configuration is read from `config.ini`, and Excel is used for data-driven login testing. It is a learning/portfolio framework, and my next version would improve explicit waits, driver fixture design, locator stability, assertion clarity, and CI readiness.

---

## 21. “What Would You Improve Next?” Answer

> I would not start by rewriting everything. First, I would improve test stability by adding explicit waits in `BasePage` and removing `time.sleep`. Then I would clean up driver management by avoiding global state and using a dedicated driver fixture. After that, I would improve maintainability by replacing brittle absolute XPath locators, adding assertion messages, introducing `pytest.ini` markers such as smoke and regression, adding `requirements.txt`, and setting up a simple CI workflow. These changes would make the framework more stable, easier to run, and easier for a team to maintain.

---

## 22. Final Takeaway

This framework is valuable because it gives a concrete artifact to discuss in the Mozilla technical deep dive.

It is not perfect, and that is okay.

The important interview message is:

> I understand what this framework does, why each layer exists, what works well, and what I would improve in the next version.

That is stronger than pretending the framework is already production-perfect.
