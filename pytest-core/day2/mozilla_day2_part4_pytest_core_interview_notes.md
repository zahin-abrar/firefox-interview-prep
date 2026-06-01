# Mozilla Firefox Round 2 Prep — Day 2 Part 4 Interview Notes

**Topic:** Pytest Core — Fixtures, Fixture Scope, Markers, and Parametrize  
**Context:** Firefox Software Test Engineering Student Worker — Round 2 technical preparation  
**Focus:** Pytest structure for Selenium automation, setup/teardown, fixture design, test grouping, CI selection, and data-driven testing.

---

## 1. Why Part 4 Matters

Pytest is one of the most important parts of the Mozilla Round 2 preparation because the target role likely involves contributing to and reviewing Selenium/Python/Pytest automation code.

This section focused on how Pytest helps structure an automation framework through:

- fixtures,
- setup and teardown,
- fixture scope,
- markers,
- custom test grouping,
- parametrization,
- data-driven testing,
- cleaner Selenium test design.

The main interview goal is:

> Be able to explain how Pytest makes Selenium automation cleaner, reusable, maintainable, and CI-friendly.

---

# 2. Pytest Fixtures

## 2.1 What Is a Fixture?

A fixture is reusable test preparation logic.

In Selenium automation, fixtures commonly handle:

- browser initialization,
- browser cleanup,
- opening the base URL,
- maximizing the window,
- loading config,
- preparing test data,
- providing page objects,
- preparing reusable test context.

A simple Selenium-style fixture:

```python
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://example.com")

    yield driver

    driver.quit()
```

Test usage:

```python
def test_homepage_title(driver):
    assert "Example" in driver.title
```

---

## 2.2 Fixture Mental Model

A fixture means:

> Before this test runs, give it the thing it needs.

That “thing” can be:

- a browser,
- a page object,
- test data,
- config,
- an API client,
- a temporary file,
- or cleanup logic.

---

## 2.3 Fixtures Are Not Only for Setup and Teardown

A question came up:

> Is there any other usage of fixture other than setup and teardown?

Answer:

Yes. Fixtures are broader than setup/teardown. They provide reusable dependencies for tests.

### Example 1 — Providing Test Data

```python
@pytest.fixture
def valid_user():
    return {
        "email": "test@example.com",
        "password": "Password123"
    }
```

Usage:

```python
def test_login(valid_user):
    assert valid_user["email"] == "test@example.com"
```

---

### Example 2 — Providing Config

```python
@pytest.fixture
def app_config():
    return {
        "base_url": "https://tutorialsninja.com/demo/",
        "browser": "firefox"
    }
```

Useful for avoiding hardcoded values inside tests.

---

### Example 3 — Providing Page Objects

```python
@pytest.fixture
def login_page(driver):
    return LoginPage(driver)
```

Usage:

```python
def test_valid_login(login_page):
    login_page.login("user@example.com", "password")
```

This keeps test code cleaner.

---

### Example 4 — Preparing Temporary Files

```python
@pytest.fixture
def sample_report_file(tmp_path):
    file = tmp_path / "report.txt"
    file.write_text("status=passed")
    return file
```

Useful for testing utilities that read files, reports, logs, JSON, CSV, etc.

---

## 2.4 Interview Answer — Fixture Usage

> Fixtures are commonly used for setup and teardown, but they are broader than that. They provide reusable dependencies for tests, such as browser drivers, config, test data, page objects, API clients, or temporary resources. In Selenium automation, browser setup is the most visible use case, but fixtures help keep many kinds of repeated test preparation outside the test logic.

---

# 3. `yield`, `yield driver`, and Plain `yield`

## 3.1 Basic Fixture With `yield driver`

```python
@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    yield driver

    driver.quit()
```

Meaning:

```text
Before yield  → setup
During yield  → test runs
After yield   → teardown
```

The test receives the driver directly:

```python
def test_homepage(driver):
    driver.get("https://example.com")
```

Here, the `driver` parameter in the test comes from:

```python
yield driver
```

---

## 3.2 User Question — Do I Need to Write `yield driver`?

Answer:

Not always.

There are two common fixture patterns.

---

## Pattern A — Fixture Returns/Provides the Driver Directly

Use:

```python
yield driver
```

Example:

```python
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
```

Test:

```python
def test_login(driver):
    driver.get("https://example.com")
```

Use this when the test function needs the driver as a parameter.

---

## Pattern B — Fixture Stores Driver Somewhere Else

Example:

```python
@pytest.fixture
def setup_and_teardown(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver

    yield

    driver.quit()
```

Then a test class can access:

```python
self.driver
```

In this case:

```python
yield
```

is enough because the driver is not being returned directly to the test function. It has already been attached to the test class.

---

## 3.3 Simple Rule

| Fixture Style | Use |
|---|---|
| Test function needs driver as parameter | `yield driver` |
| Driver is attached to class/object/context | `yield` |
| Need teardown after test | use `yield`, not only `return` |

---

## 3.4 Interview Answer — `yield` vs `yield driver`

> `yield driver` is used when the fixture directly provides the driver object to the test function. In my framework, only `yield` is used because the driver is attached to the test class using `request.cls.driver`. In that case, `yield` mainly separates setup from teardown.

---

# 4. Your Framework Fixture

## 4.1 Fixture Used in Your Selenium-Pytest Framework

```python
@pytest.fixture()
def setup_and_teardown(request):
    """
        Centralized test environment setup and teardown fixture.

        Responsibilities:
        - reads browser configuration from config file
        - initializes WebDriver
        - opens application URL
        - attaches driver to test class instance
        - quits driver after test completes

        This fixture ensures that:
        - tests remain clean
        - driver logic is reusable
        - environment setup is centralized
    """
    browser = ReadConfigurations.read_configuration("basic info", "browser")
    global driver
    driver = None

    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Unsupported browser. Please choose 'chrome', 'firefox', or 'edge'.")

    driver.maximize_window()
    url = ReadConfigurations.read_configuration("basic info", "url")
    driver.get(url)
    request.cls.driver = driver

    yield

    driver.quit()
```

---

## 4.2 What This Fixture Does Well

The fixture has a clear framework-style flow:

```text
1. Read browser from config
2. Start selected browser
3. Maximize window
4. Read URL from config
5. Open application
6. Attach driver to test class
7. Run test
8. Quit browser
```

This is a good structure for interview explanation.

---

## 4.3 Why Plain `yield` Works Here

Your framework uses:

```python
request.cls.driver = driver
yield
driver.quit()
```

So:

```python
yield driver
```

is not needed.

The test receives access through the class:

```python
self.driver
```

not through a test-function parameter.

---

## 4.4 Interview-Ready Explanation of Your Fixture

> In my framework, I use a Pytest fixture for centralized browser setup and teardown. The fixture reads the browser and URL from the configuration file, initializes the appropriate WebDriver, opens the application, and attaches the driver to the test class using `request.cls.driver`. I use `yield` to separate setup from teardown, so after the test finishes, `driver.quit()` runs and closes the browser session. This keeps tests cleaner and makes browser setup reusable across test classes.

---

# 5. Review Notes and Improvement Areas for Your Fixture

## 5.1 Avoid `global driver` if Possible

Current code:

```python
global driver
driver = None
```

This works, but global state can become risky.

Why?

- It can make debugging harder.
- It can create issues in parallel execution.
- It can cause unexpected shared state.
- It makes the fixture less self-contained.

Better:

```python
driver = None
```

inside the fixture.

Interview improvement statement:

> One improvement I would make is to avoid global driver state and keep the driver local to the fixture, because global state can make parallel execution or debugging harder.

---

## 5.2 Raise a Clear Error for Unsupported Browser

Current code:

```python
else:
    print("Unsupported browser. Please choose 'chrome', 'firefox', or 'edge'.")
```

Problem:

The code continues after this, and `driver` may still be `None`.

Then this line may fail:

```python
driver.maximize_window()
```

with a confusing error:

```text
AttributeError: 'NoneType' object has no attribute 'maximize_window'
```

Better:

```python
else:
    raise ValueError("Unsupported browser. Please choose 'chrome', 'firefox', or 'edge'.")
```

Interview phrasing:

> I would raise a clear exception for unsupported browser values instead of only printing a message, because otherwise the test may fail later with a less helpful `NoneType` error.

---

## 5.3 Normalize Browser Config

Current style:

```python
if browser.__eq__("chrome"):
```

More Pythonic style:

```python
browser = browser.lower().strip()

if browser == "chrome":
```

Why?

It handles values like:

```text
Chrome
 chrome
FIREFOX
```

Better:

```python
browser = ReadConfigurations.read_configuration("basic info", "browser").lower().strip()
```

---

## 5.4 Slightly Improved Fixture Version

```python
@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfigurations.read_configuration("basic info", "browser").lower().strip()
    url = ReadConfigurations.read_configuration("basic info", "url")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser. Please choose 'chrome', 'firefox', or 'edge'.")

    driver.maximize_window()
    driver.get(url)

    request.cls.driver = driver

    yield

    driver.quit()
```

---

## 5.5 More Defensive Fixture Version

```python
@pytest.fixture()
def setup_and_teardown(request):
    driver = None

    browser = ReadConfigurations.read_configuration("basic info", "browser").lower().strip()
    url = ReadConfigurations.read_configuration("basic info", "url")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser. Please choose 'chrome', 'firefox', or 'edge'.")

    driver.maximize_window()
    driver.get(url)
    request.cls.driver = driver

    yield

    if driver:
        driver.quit()
```

---

## 5.6 Improvement Answer for Interview

> If I improved this fixture further, I would avoid global driver state, normalize the browser config value, and raise a clear exception for unsupported browsers. These changes would make the setup more robust and easier to debug.

---

# 6. Why Fixtures Are Better Than Creating Driver Inside Every Test

## Bad Style

```python
def test_login():
    driver = webdriver.Chrome()
    driver.get("https://example.com")
    # test steps
    driver.quit()

def test_search():
    driver = webdriver.Chrome()
    driver.get("https://example.com")
    # test steps
    driver.quit()
```

## Problems

- repeated setup code in every test,
- easy to forget `driver.quit()`,
- harder to change browser from Chrome to Firefox,
- harder to add screenshots, config, headless mode, or base URL,
- test files become noisy,
- cleanup may not happen properly if the test crashes before `driver.quit()`.

## Fixture Benefit

```python
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
```

Now the setup/teardown is centralized.

## Interview Answer

> Using a fixture avoids repeating browser setup and teardown in every test. It keeps tests focused on the scenario, makes cleanup more reliable, and centralizes browser configuration. If I need to change the browser, add Firefox support, enable headless mode, or improve teardown, I can update the fixture instead of editing every test.

---

# 7. Fixture Scope

## 7.1 What Is Fixture Scope?

Fixture scope controls how often a fixture runs.

Simple idea:

> Fixture scope decides the lifetime of the setup resource.

For Selenium, that setup resource is usually the browser driver.

---

## 7.2 Default Scope — `function`

If no scope is written:

```python
@pytest.fixture()
def setup_and_teardown():
    ...
```

it is equivalent to:

```python
@pytest.fixture(scope="function")
def setup_and_teardown():
    ...
```

Meaning:

```text
Test 1 starts → browser opens → test runs → browser closes
Test 2 starts → browser opens → test runs → browser closes
Test 3 starts → browser opens → test runs → browser closes
```

Best for:

- Selenium UI tests,
- isolated tests,
- avoiding state leakage,
- reducing flaky behavior.

Downside:

- slower because a new browser opens for each test.

Interview answer:

> Function scope is usually safest for Selenium UI tests because each test gets a clean browser session. This reduces hidden dependency between tests and makes failures easier to debug.

---

## 7.3 `class` Scope

```python
@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
```

Meaning:

```text
Test class starts → browser opens
test_1 runs
test_2 runs
test_3 runs
Test class ends → browser closes
```

Best for:

- grouped tests that intentionally share expensive setup,
- reducing browser startup time,
- test classes where shared state is controlled carefully.

Risk:

- cookies can leak,
- login state can leak,
- cart data can leak,
- page state can leak,
- local storage can leak,
- one test failure can affect the next test.

Interview answer:

> Class scope can improve speed by reusing setup across a test class, but I would use it carefully in Selenium because shared browser state can make tests dependent on each other.

---

## 7.4 `module` Scope

```python
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
```

Meaning:

```text
Test file starts → browser opens
all tests in this file run
Test file ends → browser closes
```

Best for:

- expensive setup reused across a test file,
- non-UI resources like API clients, test files, or config objects.

For Selenium UI browser usage, module scope can be risky because all tests in the file share browser state.

Interview answer:

> Module scope can reduce setup time, but for Selenium UI tests I would be cautious because all tests in the file share the same browser state.

---

## 7.5 `session` Scope

```python
@pytest.fixture(scope="session")
def app_config():
    return load_config()
```

Meaning:

```text
Fixture runs once for the entire test run
```

Best for:

- config loading,
- environment setup,
- API clients,
- database connection setup,
- test metadata,
- expensive non-UI resources.

Usually risky for a Selenium browser driver because one browser session shared across the whole run can create heavy state leakage.

Good session fixture example:

```python
@pytest.fixture(scope="session")
def app_config():
    return {
        "base_url": "https://tutorialsninja.com/demo/",
        "browser": "firefox"
    }
```

Interview answer:

> Session scope is useful for shared resources that do not need to be reset between tests, such as configuration. But I would usually avoid a session-scoped browser for Selenium UI tests unless there is a very specific reason and strong cleanup strategy.

---

## 7.6 Scope Comparison Table

| Scope | Runs How Often? | Selenium Browser Use | Risk |
|---|---|---|---|
| `function` | once per test | safest default | slower |
| `class` | once per test class | okay if controlled | shared state |
| `module` | once per test file | risky for UI | more shared state |
| `session` | once per full run | usually avoid for browser | highest state leakage |

---

# 8. Your Framework Scope

Your fixture uses:

```python
@pytest.fixture()
def setup_and_teardown(request):
    ...
```

Since no scope is specified, Pytest uses:

```python
scope="function"
```

So your framework currently means:

> For each test method, read config, open browser, attach driver to the class, run the test, then quit the browser.

This is a safe default for Selenium UI tests.

---

# 9. Important Distinction — Driver Access vs Fixture Lifetime

Two concepts were clarified.

## 9.1 How the Test Receives the Resource

```python
yield driver
```

or:

```python
request.cls.driver = driver
yield
```

This answers:

> How does the test access the driver?

## 9.2 How Long the Resource Lives

```python
scope="function"
scope="class"
scope="module"
scope="session"
```

This answers:

> How often does the fixture run?

Your fixture uses:

```python
request.cls.driver = driver
```

for access, and default:

```python
scope="function"
```

for lifetime.

---

# 10. Fixture Scope Mini Exercise

## Question

Suppose there are 5 test methods inside one test class.

If the fixture is:

```python
@pytest.fixture(scope="function")
```

How many times will the browser open and close?

## User's Answer

> Browser will open and close 5 times because every test function will get a new resource instance.

Correct.

## Explanation

```text
open browser → test_1 → close browser
open browser → test_2 → close browser
open browser → test_3 → close browser
open browser → test_4 → close browser
open browser → test_5 → close browser
```

So:

```text
5 opens, 5 closes
```

---

## Question

If the fixture is:

```python
@pytest.fixture(scope="class")
```

How many times will the browser open and close?

## User's Answer

> One browser will be shared for all test functions.

Correct.

## Explanation

```text
open browser once
test_1
test_2
test_3
test_4
test_5
close browser once
```

So:

```text
1 open, 1 close
```

---

## Fixture Scope Tradeoff

| Scope | Speed | Isolation | Risk |
|---|---:|---:|---|
| `function` | slower | high | low |
| `class` | faster | lower | higher |

Interview phrasing:

> Function scope is safer for UI tests because every test starts from a clean browser state. Class scope can improve speed by reusing the browser across tests in a class, but it can introduce state leakage if one test leaves cookies, login state, cart data, or page state behind.

---

# 11. Continuous Browser Context Question

## User Question

> If there is a scenario where we need continuous browser context, like a chain of actions for a logged-in user, is it better to use class scope?

## Answer

Yes, class scope can be appropriate, but only if the tests are intentionally designed to share browser/session context.

However, if the actions are part of one dependent end-to-end journey, it is often better to model them as one test scenario instead of several tests that depend on each other.

---

## Example — Better as One E2E Test

Flow:

```text
login → add product → checkout → verify order
```

This is probably one end-to-end test:

```python
def test_user_can_complete_checkout(driver):
    login_page.login(...)
    product_page.add_product(...)
    cart_page.checkout(...)
    assert order_page.success_message_is_displayed()
```

Why?

If login fails, checkout cannot meaningfully run anyway.

---

## When Class Scope Makes Sense

Class scope can make sense when several related tests share expensive setup, such as:

```text
Open browser once
Login once
Run several profile/account tests
Quit browser
```

But the risk is state leakage:

```text
test_1 changes profile name
test_2 expects old profile name
test_3 fails because test_1 changed state
```

---

## Better Pattern for Logged-In Tests

Often, a balanced approach is:

> Use a function-scoped fixture that logs in before each test.

Example:

```python
@pytest.fixture
def logged_in_user(driver):
    login_page = LoginPage(driver)
    login_page.login("user@example.com", "password")
    return driver
```

Then every test starts logged in but remains isolated.

---

## Comparison

| Approach | Benefit | Risk |
|---|---|---|
| Function-scoped login fixture | isolated, reliable | slower |
| Class-scoped browser/login | faster | shared state risk |
| One E2E test flow | good for true chain scenario | longer test |

## Interview-Ready Answer

> If the browser context must be continuous, class scope can be useful, especially for related tests that share an expensive login/setup. But I would be careful because shared browser state can make tests dependent on each other. If the steps are actually one user journey, I would write them as one end-to-end test. For independent logged-in tests, I would usually prefer a function-scoped fixture that logs in fresh for each test, because reliability and isolation matter more than speed in UI automation.

---

# 12. Pytest Markers

## 12.1 What Are Markers?

Markers help label tests so selected groups can be run instead of always running everything.

Example:

```python
import pytest

@pytest.mark.smoke
def test_user_can_login():
    assert True
```

Run only smoke tests:

```bash
pytest -m smoke
```

---

## 12.2 Why Markers Matter

Markers are useful for organizing test execution.

| Marker | Meaning |
|---|---|
| `smoke` | critical fast checks |
| `regression` | broader coverage |
| `slow` | tests that take longer |
| `flaky` | unstable tests needing attention |
| `integration` | tests involving multiple systems/components |

CI/CD usage:

```bash
pytest -m smoke
```

can run on every PR.

```bash
pytest -m regression
```

can run nightly or before release.

---

## 12.3 Strong Interview Answer — Markers

> Pytest markers help organize and selectively run tests. For example, I can mark critical tests as smoke and run them frequently in CI for quick feedback, while broader regression tests can run on a schedule or before release. This helps balance feedback speed and coverage.

---

## 12.4 Registering Markers in `pytest.ini`

To avoid marker warnings and document the suite, define custom markers:

```ini
[pytest]
markers =
    smoke: critical fast checks for build validation
    regression: broader coverage for existing functionality
    slow: tests that take longer to execute
    flaky: unstable tests that need investigation
```

---

## 12.5 Markers in a Selenium Framework

```python
import pytest

@pytest.mark.smoke
def test_valid_login(self):
    login_page = LoginPage(self.driver)
    login_page.login("user@example.com", "password")
    assert login_page.is_login_successful()
```

Regression example:

```python
@pytest.mark.regression
def test_invalid_login_shows_error(self):
    login_page = LoginPage(self.driver)
    login_page.login("wrong@example.com", "wrongpass")
    assert login_page.get_error_message() == "Warning: No match for E-Mail Address and/or Password."
```

---

# 13. Marker Classification Exercise

## Test List

```text
test_homepage_loads
test_valid_login
test_invalid_login
test_search_existing_product
test_search_non_existing_product
test_add_to_cart
test_checkout_flow
```

## User's Classification

| Test | Marker |
|---|---|
| `test_homepage_loads` | smoke |
| `test_valid_login` | smoke |
| `test_invalid_login` | regression |
| `test_search_existing_product` | smoke |
| `test_search_non_existing_product` | regression |
| `test_add_to_cart` | smoke |
| `test_checkout_flow` | regression |

## Review

This classification is good.

### Reasoning

- Homepage load = fast critical check.
- Valid login = critical user access check.
- Existing product search = important core functionality.
- Add to cart = key user journey step.
- Invalid login = important but negative-path behavior, better in regression.
- Non-existing product search = broader behavior, regression.
- Checkout flow = business-critical but often longer/more state-dependent, so regression is reasonable.

---

## Nuance — Checkout Flow

Checkout may be business-critical, so some teams may include a lightweight checkout smoke test.

But full checkout tests are often:

- longer,
- more data-dependent,
- more fragile,
- dependent on payment/cart/session state.

So marking full checkout as regression is a mature choice unless the team has a very stable simplified checkout smoke path.

## Polished Interview Answer

> I would mark homepage load, valid login, existing product search, and add-to-cart as smoke because they are fast critical checks that give confidence the main application is usable. I would mark invalid login, non-existing product search, and full checkout flow as regression because they provide broader behavioral coverage. Checkout is business-critical, but because it is usually longer and more state-dependent, I would only include it in smoke if we had a stable simplified checkout path.

---

# 14. Built-In vs Custom Markers

## User Question

> Are the markers predefined? Do we always have to use smoke/regression/slow, or can we use anything defined in pytest.ini?

## Answer

Markers are not limited to `smoke`, `regression`, or `slow`.

Pytest has built-in markers, and teams can also define custom markers.

---

## 14.1 Built-In Markers

Examples:

```python
@pytest.mark.skip
@pytest.mark.skipif
@pytest.mark.xfail
@pytest.mark.parametrize
@pytest.mark.usefixtures
```

These have special built-in behavior.

You can view available markers with:

```bash
pytest --markers
```

---

## 14.2 Custom Markers

Examples:

```python
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.slow
@pytest.mark.flaky
@pytest.mark.integration
```

These are usually custom/team-defined markers.

Teams can define project-specific markers:

```python
@pytest.mark.login
@pytest.mark.checkout
@pytest.mark.firefox
@pytest.mark.cross_browser
@pytest.mark.accessibility
```

---

## 14.3 Best Practice

Register custom markers in `pytest.ini`.

Example:

```ini
[pytest]
markers =
    smoke: critical fast checks for build validation
    regression: broader coverage for existing functionality
    firefox: tests specifically important for Firefox execution
    accessibility: accessibility-related checks
```

Then:

```python
@pytest.mark.firefox
def test_login_in_firefox():
    ...
```

Run only Firefox-marked tests:

```bash
pytest -m firefox
```

---

## Interview Answer — Built-In vs Custom Markers

> Pytest has built-in markers like `skip`, `xfail`, `usefixtures`, and `parametrize`. For suite organization, teams often define custom markers like `smoke` or `regression`. These are conventions, not fixed pytest requirements. I would register custom markers in `pytest.ini` so the suite is self-documented and typo-safe.

---

# 15. Parametrize

## 15.1 What Is `parametrize`?

`parametrize` is used when the same test logic should run with multiple input combinations.

It helps avoid duplicate test code.

Instead of writing separate tests:

```python
def test_valid_login():
    username = "valid_user"
    password = "valid_password"
    expected = "success"
    # test logic


def test_invalid_login():
    username = "wrong_user"
    password = "valid_password"
    expected = "error"
    # same test logic again
```

Use one parametrized test:

```python
import pytest

@pytest.mark.parametrize("username,password,expected", [
    ("valid_user", "valid_password", "success"),
    ("wrong_user", "valid_password", "error"),
    ("valid_user", "wrong_password", "error"),
])
def test_login(username, password, expected):
    print(username, password, expected)
```

Pytest runs this test once per data row.

---

## 15.2 Mental Model

This:

```python
@pytest.mark.parametrize("username,password,expected", [
    ("valid_user", "valid_password", "success"),
    ("wrong_user", "valid_password", "error"),
])
```

means:

```text
Run test_login once with:
username = valid_user
password = valid_password
expected = success

Run test_login again with:
username = wrong_user
password = valid_password
expected = error
```

---

## 15.3 Why Parametrize Matters in Automation

Useful for:

- login with different credentials,
- search with different keywords,
- form validation,
- boundary value testing,
- role/permission testing,
- browser combinations,
- API response validation.

Example:

```python
@pytest.mark.parametrize("search_term,expected_result", [
    ("iphone", True),
    ("nonexistingproduct123", False),
    ("", False),
])
def test_search(search_term, expected_result):
    # same search logic, different data
    pass
```

---

## 15.4 Strong Interview Answer — Parametrize

> Parametrize is useful for data-driven testing. It lets us run the same test logic with multiple input combinations, which reduces duplicate code and makes the test easier to maintain. For example, login validation can use one test function with several username/password/expected-result combinations.

---

# 16. Parametrize Mini Exercise

## Scenario

Test login with these scenarios:

| Email | Password | Expected |
|---|---|---|
| `valid@example.com` | `valid123` | `success` |
| `wrong@example.com` | `valid123` | `error` |
| `valid@example.com` | `wrong123` | `error` |
| empty email | `valid123` | `error` |

## User's Attempt

```python
@pytest.mark.parametrze("email, password, expected", [
("valid@example.com", "valid123", "success"),
("wrong@example.com", "valid123", "error"),
("valid@example.com", "wrong123", "error"),
("", "valid123", "error")])
def test_login(username, password, expected):
```

## Issues

### Issue 1 — Typo

```python
@pytest.mark.parametrze
```

should be:

```python
@pytest.mark.parametrize
```

### Issue 2 — Parameter Names Must Match

Decorator:

```python
"email, password, expected"
```

Function signature:

```python
def test_login(username, password, expected):
```

These must match.

---

## Correct Version

```python
import pytest

@pytest.mark.parametrize("email, password, expected", [
    ("valid@example.com", "valid123", "success"),
    ("wrong@example.com", "valid123", "error"),
    ("valid@example.com", "wrong123", "error"),
    ("", "valid123", "error"),
])
def test_login(email, password, expected):
    pass
```

---

## Interview Explanation

> I used `parametrize` to run the same login test logic with multiple credential combinations. This avoids duplicating the test body while still covering valid login, invalid email, invalid password, and empty email scenarios.

---

# 17. Part 4 Final Mini Summary

Pytest helps structure automation by:

- separating setup and teardown through fixtures,
- controlling fixture lifetime through scope,
- organizing test execution through markers,
- reducing duplicate test code through parametrization.

Framework-specific answer:

> In my framework, I use a Pytest fixture to read browser and URL configuration, initialize WebDriver, attach the driver to the test class using `request.cls.driver`, and quit the browser after test execution. Since no scope is specified, it uses function scope by default, which gives each UI test isolated setup and teardown.

---

# 18. Interview-Ready Combined Answer

If asked:

> How do you use Pytest in your Selenium framework?

Answer:

> I use Pytest to structure the automation framework. Fixtures handle browser setup and teardown, including reading browser and URL configuration, creating the WebDriver, attaching it to the test class, and quitting the browser after execution. Fixture scope controls how often that setup runs; for Selenium UI tests I usually prefer function scope because it keeps tests isolated. Markers help group tests into smoke, regression, or other categories so CI can run the right level of coverage. Parametrize supports data-driven testing by running the same test logic with multiple input combinations without duplicating code.

---

# 19. Strengths Observed in Part 4

## 1. Good Framework Connection

The Pytest fixture concepts were connected directly to the existing Selenium-Pytest framework.

## 2. Good Follow-Up Questions

Important questions were asked about:

- fixture usages beyond setup/teardown,
- `yield driver` vs plain `yield`,
- fixture scope,
- shared browser context,
- predefined vs custom markers.

These are exactly the kinds of practical questions that lead to deeper automation understanding.

## 3. Good Understanding of Scope Tradeoff

The function vs class scope tradeoff was understood:

```text
function scope = better isolation, slower
class scope = faster, more state sharing risk
```

## 4. Good Smoke/Regression Judgment

The marker classification exercise showed good practical prioritization.

---

# 20. Improvement Areas

## 1. Avoid Confusing Fixture Scope With Driver Access

Remember:

```text
yield driver vs yield = how the test receives/accesses the resource
scope=function/class/module/session = how often the fixture runs
```

They are related but separate ideas.

---

## 2. Function Scope Is Usually Safer for Selenium

Class scope can be useful, but for UI tests:

> Start with isolation first, optimize speed later.

---

## 3. Be Careful With Parametrize Naming

Parameter names in the decorator must match the function signature.

Correct:

```python
@pytest.mark.parametrize("email, password, expected", [...])
def test_login(email, password, expected):
```

Incorrect:

```python
@pytest.mark.parametrize("email, password, expected", [...])
def test_login(username, password, expected):
```

---

## 4. Mention CI/CD When Explaining Markers

Markers are not just labels. They help control test execution in CI.

Example:

```bash
pytest -m smoke
```

for PR validation.

---

# 21. Final Part 4 Takeaways

The most important takeaways:

- fixtures keep setup/teardown and reusable dependencies outside test logic,
- `yield` separates setup from teardown,
- `yield driver` is only needed when the test function receives the driver directly,
- `request.cls.driver = driver` allows class-based tests to access `self.driver`,
- fixture scope controls fixture lifetime,
- function scope is safest for Selenium UI tests,
- class scope can be used carefully for shared context,
- markers organize tests for selective execution,
- custom markers should be registered in `pytest.ini`,
- parametrization enables clean data-driven testing,
- Pytest structure helps make Selenium frameworks maintainable and CI-friendly.

The next section should move into **Firefox Execution and GeckoDriver**, which connects Selenium/Pytest knowledge directly to the Mozilla Firefox role.
