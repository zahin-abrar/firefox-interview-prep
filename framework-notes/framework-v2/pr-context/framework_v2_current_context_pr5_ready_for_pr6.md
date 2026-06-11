# Framework V2 Current Context — PR5 Completed, Ready for PR6

**Project:** Mozilla Firefox Round 2 Technical Prep  
**Sub-project:** SauceDemo Selenium/Pytest Framework V2 + Gitea PR Review Lab  
**Current handoff purpose:** Use this document as the memory/context file for the next chat thread, starting with **PR6: Cart Badge Smoke Test**.  
**Last updated:** 2026-06-06  
**Current state:** PR1–PR5 are completed, merged into `main`, and all simulated developer clones should be synced to latest `main`.

---

## 1. Why This Project Exists

This project is part of preparation for the **Mozilla Firefox Software Test Engineering Student Worker** technical deep-dive.

The preparation is intentionally not just “write Selenium scripts.” The goal is to demonstrate and practice:

- Python/Selenium/Pytest automation ability
- Page Object Model understanding
- maintainable framework design
- fixture design and dependency injection
- PR review mindset
- protected-branch workflow
- working with contributors/contractors
- technical explanation under interview pressure
- CI/CD awareness
- calm debugging and uncertainty handling

The local Gitea lab simulates a realistic automation team workflow:

```text
Contributor branch
→ Pull Request
→ Maintainer review
→ Formal approval
→ Protected main merge
→ Branch cleanup
→ All clones synced
→ Next feature branch
```

This supports the Mozilla role context, where the candidate may need to review automation PRs, support a contractor/manual QA team transitioning into automation, and contribute to an automation suite.

---

## 2. Active Source Documents Considered

These project source documents are active context and should continue to be considered in future threads:

```text
mozilla_round2_technical_prep_roadmap.md
mozilla_firefox_interview_thread_knowledge_context.md
framework_v2_implementation_guide.md
gitea_workflow_progress_context.md
current_selenium_pytest_framework_context.md
framework_v2_pr2_completed_context_for_pr3.md
```

### Source document roles

| Document | Purpose |
|---|---|
| `mozilla_round2_technical_prep_roadmap.md` | Overall Mozilla Round 2 preparation plan: Python, Selenium/Pytest, PR review, CI/CD, interview fluency. |
| `mozilla_firefox_interview_thread_knowledge_context.md` | Mozilla role/interview context, Round 1 questions, role expectations, and answer narratives. |
| `framework_v2_implementation_guide.md` | Main implementation plan for SauceDemo Selenium/Pytest + Gitea PR review lab. |
| `gitea_workflow_progress_context.md` | Gitea setup and multi-developer workflow context. |
| `current_selenium_pytest_framework_context.md` | Snapshot of the previous Selenium Python Hybrid Framework for comparison and familiarity. |
| `framework_v2_pr2_completed_context_for_pr3.md` | Handoff context from PR2 completion to PR3. |

---

## 3. Repository and Gitea Setup

### Gitea organization

```text
firefox-qa-lab
```

### Repository

```text
saucedemo-pytest-automation
```

### Repository URL

```text
http://localhost:3000/firefox-qa-lab/saucedemo-pytest-automation.git
```

### Gitea installation

- Installed natively on Windows.
- Root directory:

```text
D:\Projects\Gitea
```

- SQLite is used.
- HTTP port: `3000`.
- SSH port adjusted to avoid port conflict.
- `main` is the default branch.
- `main` is protected.

---

## 4. Simulated Team / Developer Accounts

| User | Role in simulation | Current usage |
|---|---|---|
| `abrar` | Maintainer / reviewer | Reviews and merges PRs. |
| `qa-contractor-1` | Contributor | Created PR1, PR3, PR5. Recommended next? No — rotate to `qa-contractor-2` for PR6. |
| `qa-contractor-2` | Contributor | Created PR2 and PR4. Recommended for PR6. |

### Key identity lesson

There are two identities:

```text
Git commit identity      → git config user.name / user.email
Gitea authentication     → username/password used during push
```

Git identity controls commit author. Gitea authentication controls PR creator, push permission, and branch ownership.

### Username-specific remote URL strategy

Examples:

```text
http://abrar@localhost:3000/firefox-qa-lab/saucedemo-pytest-automation.git
http://qa-contractor-1@localhost:3000/firefox-qa-lab/saucedemo-pytest-automation.git
http://qa-contractor-2@localhost:3000/firefox-qa-lab/saucedemo-pytest-automation.git
```

This keeps contributor simulation realistic.

---

## 5. Local Multi-Clone Structure

```text
D:\Projects\Personal\git-workflow
├── abrar-maintainer
│   └── saucedemo-pytest-automation
├── qa-contractor-1
│   └── saucedemo-pytest-automation
└── qa-contractor-2
    └── saucedemo-pytest-automation
```

Each clone simulates a separate developer machine. Each clone may have its own `.venv`, dependencies, IDE interpreter settings, local branches, and Git config.

---

## 6. Framework V2 Current Actual State After PR5

### Completed PRs

| PR | Branch | Contributor | Status | Main purpose |
|---|---|---|---|---|
| PR1 | `feature/framework-skeleton` | `qa-contractor-1` | Merged | Framework skeleton, basic folders, pytest config, requirements, config placeholder. |
| PR2 | `feature/add-browser-fixture` | `qa-contractor-2` | Merged | Browser fixture, config reader, expanded config, smoke setup test. |
| PR3 | `feature/add-base-page` | `qa-contractor-1` | Merged | BasePage with explicit wait helpers and reusable Selenium actions. |
| PR4 | `feature/add-login-page-and-smoke-test` | `qa-contractor-2` | Merged | LoginPage + first valid login smoke/regression test. |
| PR5 | `feature/add-inventory-page-smoke-test` | `qa-contractor-1` | Merged | InventoryPage, logged-in inventory fixture, inventory product-list smoke/regression test, and LoginPage now returns InventoryPage after successful login. |

### Current confirmed test expectation

After PR5, expected validation:

```powershell
pytest --collect-only
pytest -m smoke -v
pytest -v
```

Expected results:

```text
3 tests collected
2 smoke tests selected, 1 setup test deselected when running -m smoke
3 passed when running pytest -v
```

Likely test files now:

```text
tests/test_smoke_setup.py
tests/test_login.py
tests/test_inventory.py
```

---

## 7. Expected Current Folder Structure After PR5

The exact folder tree should be verified in the repo, but after PR5 the current structure should roughly contain:

```text
saucedemo-pytest-automation/
├── config/
│   └── config.json
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   └── inventory_page.py
├── tests/
│   ├── __init__.py
│   ├── test_smoke_setup.py
│   ├── test_login.py
│   └── test_inventory.py
├── utils/
│   ├── __init__.py
│   └── config_reader.py
├── reports/
│   ├── screenshots/
│   │   └── .gitkeep
│   ├── logs/
│   │   └── .gitkeep
│   └── allure-results/
│       └── .gitkeep
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

Optional planned but not yet urgent:

```text
docs/
test_data/
pages/cart_page.py
pages/checkout_page.py
utils/excel_reader.py
utils/screenshot_utils.py
utils/logger.py
```

---

## 8. Current Important Files and Intended Code Shape

### 8.1 `config/config.json`

Expected current content:

```json
{
  "base_url": "https://www.saucedemo.com/",
  "browser": "firefox",
  "headless": false,
  "default_timeout": 10,
  "users": {
    "standard": {
      "username": "standard_user",
      "password": "secret_sauce"
    },
    "locked": {
      "username": "locked_out_user",
      "password": "secret_sauce"
    }
  }
}
```

### 8.2 `utils/config_reader.py`

```python
import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG_PATH = PROJECT_ROOT / "config" / "config.json"


def read_config(config_path: str | Path = DEFAULT_CONFIG_PATH) -> dict:
    path = Path(config_path)

    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")

    with path.open(encoding="utf-8") as file:
        return json.load(file)
```

### 8.3 `conftest.py`

Expected current shape after PR5:

```python
import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from utils.config_reader import read_config


@pytest.fixture(scope="session")
def config():
    return read_config()


@pytest.fixture(scope="session")
def base_url(config):
    return config["base_url"]


@pytest.fixture
def driver(config):
    browser = config.get("browser", "firefox").lower()
    headless = config.get("headless", False)

    if browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)

    elif browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_inventory_page(driver, base_url, config):
    """
    Log in as a standard user and return the InventoryPage object.

    This fixture is useful for tests that need an authenticated user
    already landed on the inventory page.
    """
    timeout = config.get("default_timeout", 10)
    standard_user = config["users"]["standard"]

    login_page = LoginPage(
        driver=driver,
        base_url=base_url,
        timeout=timeout
    )
    login_page.open()

    return login_page.login(
        standard_user["username"],
        standard_user["password"]
    )
```

### 8.4 `pages/base_page.py`

```python
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """
    Base class for all Page Objects.

    Centralizes common Selenium actions so page classes do not repeat
    raw WebDriver wait/click/type/text logic.
    """

    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.timeout = timeout

    def open_url(self, url: str) -> None:
        """Open the given URL in the current browser session."""
        self.driver.get(url)

    def find_visible(self, locator: tuple[str, str]) -> WebElement:
        """Wait until an element is visible and return it."""
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def find_clickable(self, locator: tuple[str, str]) -> WebElement:
        """Wait until an element is clickable and return it."""
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator: tuple[str, str]) -> None:
        """Click an element after waiting for it to be clickable."""
        self.find_clickable(locator).click()

    def type_text(self, locator: tuple[str, str], text: str) -> None:
        """Clear an input field and type text into it."""
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple[str, str]) -> str:
        """Return visible text from an element."""
        return self.find_visible(locator).text

    def is_visible(self, locator: tuple[str, str]) -> bool:
        """Return True if an element becomes visible within the timeout."""
        try:
            self.find_visible(locator)
            return True
        except TimeoutException:
            return False
```

### 8.5 `pages/login_page.py`

Current recommended PR5 shape:

```python
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.inventory_page import InventoryPage


class LoginPage(BasePage):
    """
    Page Object for the SauceDemo login page.

    Responsibilities:
    - store login page locators
    - open the login page
    - perform login-related UI actions
    - return InventoryPage after successful login
    """

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver, base_url: str, timeout: int = 10):
        super().__init__(driver, timeout)
        self.base_url = base_url

    def open(self) -> None:
        """Open the SauceDemo login page."""
        self.open_url(self.base_url)

    def enter_username(self, username: str) -> None:
        """Type username into the username field."""
        self.type_text(self.USERNAME_INPUT, username)

    def enter_password(self, password: str) -> None:
        """Type password into the password field."""
        self.type_text(self.PASSWORD_INPUT, password)

    def click_login_button(self) -> None:
        """Click the login button."""
        self.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str) -> InventoryPage:
        """
        Perform login with valid credentials.

        Returns:
            InventoryPage: the page object representing the page reached
            after successful login.
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

        return InventoryPage(self.driver, timeout=self.timeout)
```

Important note for later PRs:

- `login()` returning `InventoryPage` is good for successful login.
- For negative login tests later, add a separate method such as `attempt_login()` or `submit_login()` that does **not** return `InventoryPage`.

### 8.6 `pages/inventory_page.py`

```python
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):
    """
    Page Object for the SauceDemo inventory page.

    Responsibilities:
    - represent the post-login product listing page
    - verify inventory list visibility
    - provide product count for tests
    """

    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")

    def __init__(self, driver, timeout: int = 10):
        super().__init__(driver, timeout)

    def is_inventory_list_visible(self) -> bool:
        """Return True if the inventory list is visible."""
        return self.is_visible(self.INVENTORY_LIST)

    def get_inventory_item_count(self) -> int:
        """Return the number of products displayed on the inventory page."""
        self.find_visible(self.INVENTORY_LIST)
        return len(self.driver.find_elements(*self.INVENTORY_ITEMS))
```

### 8.7 `tests/test_smoke_setup.py`

```python
def test_browser_can_open_base_url(driver, base_url):
    driver.get(base_url)

    assert "saucedemo" in driver.current_url
```

This is a framework/environment validation test, not currently marked as smoke.

### 8.8 `tests/test_login.py`

Current recommended PR5 shape:

```python
import pytest

from pages.login_page import LoginPage


@pytest.mark.smoke
@pytest.mark.regression
def test_standard_user_can_login(driver, base_url, config):
    user = config["users"]["standard"]
    timeout = config.get("default_timeout", 10)

    login_page = LoginPage(
        driver=driver,
        base_url=base_url,
        timeout=timeout
    )
    login_page.open()

    inventory_page = login_page.login(user["username"], user["password"])

    assert inventory_page.is_inventory_list_visible(), (
        "Expected inventory list to be visible after successful login."
    )
```

This replaced the earlier URL-only assertion:

```python
assert "inventory.html" in driver.current_url
```

The newer assertion is stronger because it checks the post-login inventory UI, not only the URL.

### 8.9 `tests/test_inventory.py`

```python
import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_inventory_page_shows_product_list(logged_in_inventory_page):
    assert logged_in_inventory_page.is_inventory_list_visible(), (
        "Expected inventory list to be visible after login."
    )

    product_count = logged_in_inventory_page.get_inventory_item_count()

    assert product_count > 0, (
        f"Expected inventory page to show at least one product, "
        f"but found {product_count}."
    )
```

---

## 9. PR3 Summary — BasePage

### Contributor

```text
qa-contractor-1
```

### Branch

```text
feature/add-base-page
```

### Files touched

```text
pages/base_page.py
```

### Purpose

Add the reusable Selenium interaction layer:

- `open_url()`
- `find_visible()`
- `find_clickable()`
- `click()`
- `type_text()`
- `get_text()`
- `is_visible()`

### Key design decisions

- BasePage receives the `driver`; it does **not** create the driver.
- The `driver` is still created by the Pytest fixture in `conftest.py`.
- `BasePage` stores the fixture-created driver as `self.driver` so page methods can use it.
- Uses `WebDriverWait` and Selenium expected conditions.
- Avoids `time.sleep()`.
- Uses locator tuple style such as `(By.ID, "login-button")`.
- `is_visible()` catches `TimeoutException`, not broad `Exception`.

### Validation

```powershell
pytest --collect-only
pytest -v
```

Expected at PR3 time:

```text
1 test collected
1 passed
```

### Interview explanation

> I added a `BasePage` class to centralize common Selenium operations such as opening URLs, waiting for visible/clickable elements, clicking, typing, and reading text. This keeps Page Objects smaller and prevents repeated raw `driver.find_element` calls across the framework. I used explicit waits through `WebDriverWait` and expected conditions instead of hard sleeps, which improves reliability and reduces flaky timing issues.

---

## 10. PR4 Summary — LoginPage + First Valid Login Smoke Test

### Contributor

```text
qa-contractor-2
```

### Branch

```text
feature/add-login-page-and-smoke-test
```

### Files touched

```text
pages/login_page.py
tests/test_login.py
```

### Purpose

Add the first real user-flow test:

```text
Open login page
→ enter valid standard user credentials
→ click login
→ verify inventory page reached
```

### Key design decisions

- `LoginPage` inherits from `BasePage`.
- `LoginPage.__init__()` receives `driver`, `base_url`, and `timeout`.
- It calls `super().__init__(driver, timeout)` so BasePage stores shared state.
- `self.base_url = base_url` is stored in LoginPage because this is page-specific.
- Test uses `config` fixture credentials, not hardcoded values in the test body.
- Test is marked with both `smoke` and `regression`.
- Initial PR4 assertion checked URL: `"inventory.html" in driver.current_url`.
- In PR5 this was improved to use `InventoryPage.is_inventory_list_visible()`.

### Validation after PR4

```powershell
pytest -m smoke -v
pytest -v
```

Expected after PR4:

```text
2 tests collected
1 smoke test selected, 1 deselected when running -m smoke
2 passed when running pytest -v
```

### Interview explanation

> After adding BasePage, I created a LoginPage object for the SauceDemo login screen. The test reads like a user scenario: open the login page, log in with a valid user, and verify that the inventory page is reached. This keeps Selenium interaction details inside the page object while the test focuses on the behavior being validated.

---

## 11. PR5 Summary — InventoryPage + Inventory Smoke Test

### Contributor

```text
qa-contractor-1
```

### Branch

```text
feature/add-inventory-page-smoke-test
```

### Files touched

```text
pages/inventory_page.py
pages/login_page.py
conftest.py
tests/test_login.py
tests/test_inventory.py
```

### Purpose

Add the post-login InventoryPage and a smoke test for inventory products.

### Why `pages/login_page.py` was touched again

During PR5, the design was improved so that successful login returns the next page object:

```python
return InventoryPage(self.driver, timeout=self.timeout)
```

This mirrors the older framework style where a successful login returned the next page object (`AccountPage` in the TutorialNinja project). In Framework V2, SauceDemo successful login lands on InventoryPage.

### New fixture

`logged_in_inventory_page` fixture was added to `conftest.py`:

```text
create LoginPage
→ open login page
→ log in as standard user
→ return InventoryPage
```

This avoids repeating login steps in every test that needs authenticated state.

### New inventory test

`tests/test_inventory.py` validates:

- inventory list is visible
- product count is greater than 0

### Validation after PR5

```powershell
pytest --collect-only
pytest -m smoke -v
pytest -v
```

Expected after PR5:

```text
3 tests collected
2 smoke tests selected, 1 deselected when running -m smoke
3 passed when running pytest -v
```

### Interview explanation

> After adding the login page and first login smoke test, I added an `InventoryPage` object to represent the post-login product listing page. I also added a `logged_in_inventory_page` fixture so tests that require an authenticated state do not repeat login setup. The new smoke test verifies that a logged-in user can see the inventory product list, which expands coverage from authentication to the next critical user-facing page.

---

## 12. Key Design Decisions Made in PR3–PR5

### 12.1 Driver ownership

```text
Fixture creates driver.
Page object receives driver.
BasePage stores driver.
```

BasePage does not create WebDriver. It only stores the WebDriver that Pytest fixture already created.

### 12.2 `self`

`self` means the current object instance.

Example:

```python
self.driver
```

means:

```text
this page object's driver
```

### 12.3 `super().__init__(driver, timeout)`

`LoginPage` inherits from `BasePage`. Calling:

```python
super().__init__(driver, timeout)
```

initializes the BasePage portion of the same LoginPage object. It stores:

```python
self.driver = driver
self.timeout = timeout
```

### 12.4 Fixture injection

Pytest automatically injects fixtures by matching test function parameter names:

```python
def test_standard_user_can_login(driver, base_url, config):
    ...
```

Pytest sees `driver`, `base_url`, and `config`, finds matching fixtures in `conftest.py`, runs them, and passes their values into the test.

### 12.5 Page objects do not directly call fixtures

The flow is:

```text
Pytest fixture system
    ↓
injects driver/base_url/config into test or fixture
    ↓
test/fixture creates page object using those values
    ↓
page object uses self.driver
```

### 12.6 Locator tuple style

Framework V2 uses standard Selenium locator tuples:

```python
USERNAME_INPUT = (By.ID, "user-name")
```

This is clearer than the old suffix-based locator resolver:

```python
email_address_field_id = "input-email"
self.type_into_element(email, "email_address_field_id", self.email_address_field_id)
```

### 12.7 `*` tuple unpacking

`find_elements()` expects two separate arguments:

```python
driver.find_elements(By.CLASS_NAME, "inventory_item")
```

But our locator is stored as one tuple:

```python
INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
```

So we unpack it:

```python
self.driver.find_elements(*self.INVENTORY_ITEMS)
```

### 12.8 Expected conditions return WebElements

These return a `WebElement` when successful:

```python
EC.visibility_of_element_located(locator)
EC.element_to_be_clickable(locator)
```

So BasePage can write:

```python
element = self.find_visible(locator)
element.clear()
element.send_keys(text)
```

### 12.9 Assertion structure

Python assert syntax:

```python
assert condition, failure_message
```

Example:

```python
assert product_count > 0, (
    f"Expected inventory page to show at least one product, "
    f"but found {product_count}."
)
```

The message is shown only if the condition fails.

### 12.10 Keyword vs positional arguments

This is valid:

```python
LoginPage(driver, base_url, timeout=timeout)
```

Meaning:

```text
driver and base_url are positional arguments
timeout is passed explicitly as a keyword argument
```

For learning clarity, fully explicit style is also recommended:

```python
LoginPage(
    driver=driver,
    base_url=base_url,
    timeout=timeout
)
```

---

## 13. Current Golden Workflow for Future PRs

For each new PR:

```powershell
git checkout main
git pull origin main
git fetch --prune origin
git checkout -b feature/short-task-name
```

Implement.

Validate:

```powershell
pytest --collect-only
pytest -v
```

If markers are involved:

```powershell
pytest -m smoke -v
pytest -m regression -v
```

Commit and push:

```powershell
git status
git add .
git commit -m "Clear meaningful commit message"
git push origin feature/short-task-name
```

Create PR in Gitea.

Review as `abrar`.

Merge.

Sync all clones:

```powershell
git checkout main
git pull origin main
git fetch --prune origin
```

Delete local feature branches when safe:

```powershell
git branch -d feature/short-task-name
```

---

## 14. Post-PR5 Sync Commands Already Needed/Used

After PR5 merge, each clone should run the following.

### Maintainer clone: `abrar`

```powershell
cd D:\Projects\Personal\git-workflow\abrar-maintainer\saucedemo-pytest-automation

git checkout main
git pull origin main
git fetch --prune origin
pytest -v
```

### Contractor 1 clone: `qa-contractor-1`

PR5 branch was created here, so delete local feature branch after switching to main:

```powershell
cd D:\Projects\Personal\git-workflow\qa-contractor-1\saucedemo-pytest-automation

git checkout main
git pull origin main
git fetch --prune origin
git branch -d feature/add-inventory-page-smoke-test
pytest -v
```

### Contractor 2 clone: `qa-contractor-2`

```powershell
cd D:\Projects\Personal\git-workflow\qa-contractor-2\saucedemo-pytest-automation

git checkout main
git pull origin main
git fetch --prune origin
pytest -v
```

Expected:

```text
3 passed
```

---

## 15. Recommended Next PR: PR6

### Recommended PR title

```text
Add cart badge smoke test
```

### Recommended branch

```text
feature/add-cart-badge-smoke-test
```

### Recommended contributor

```text
qa-contractor-2
```

Reason: PR5 was done by `qa-contractor-1`, so rotate back to `qa-contractor-2`.

### Why this is the next logical PR

The implementation guide’s Phase 5 includes both inventory and cart smoke coverage. We intentionally split it:

```text
PR5 → InventoryPage + inventory product-list smoke test
PR6 → Cart badge smoke test
```

This keeps PRs small, easier to review, and easier to explain.

### Suggested PR6 scope

Likely touch:

```text
pages/inventory_page.py
tests/test_cart.py
```

Optional, depending on design decision:

```text
pages/cart_page.py
```

For the smallest PR6, do **not** create full CartPage yet. Add cart-related behavior to `InventoryPage` first:

- add item to cart by product name or fixed known item
- verify cart badge count

Suggested test:

```text
TC_CART_001 — Add one item to cart updates badge
Markers: smoke, regression
```

### Suggested PR6 validation

```powershell
pytest --collect-only
pytest -m smoke -v
pytest -v
```

Expected after PR6:

```text
4 tests collected
3 smoke tests selected, 1 deselected when running -m smoke
4 passed when running pytest -v
```

### PR6 review checklist

```text
[ ] Cart badge test is focused on one behavior
[ ] Uses logged_in_inventory_page fixture
[ ] No repeated login steps inside test
[ ] No time.sleep()
[ ] Locators are stable
[ ] Test has smoke and regression markers
[ ] Test assertion is specific: badge count/value
[ ] No checkout logic included yet
[ ] pytest -m smoke -v passes
[ ] pytest -v passes
```

### PR6 interview explanation target

> I expanded the smoke suite from login and inventory visibility to the first cart interaction. The test logs in through the reusable fixture, adds one product to the cart, and verifies that the cart badge updates. This validates a critical user-facing e-commerce behavior while keeping the PR small and focused.

---

## 16. Final Current Status Summary

```text
Current milestone: PR5 completed and merged.
Current framework ability:
  - launch browser from fixture
  - read JSON config
  - open SauceDemo
  - use BasePage explicit waits
  - log in with standard user
  - return InventoryPage after successful login
  - reuse logged_in_inventory_page fixture
  - verify inventory list and product count

Current tests:
  - setup smoke/environment validation
  - standard user login smoke/regression
  - inventory product-list smoke/regression

Expected current validation:
  pytest -v → 3 passed

Next milestone: PR6 cart badge smoke test.
Next contributor recommended: qa-contractor-2.
Next branch recommended: feature/add-cart-badge-smoke-test.
```
