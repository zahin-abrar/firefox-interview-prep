# Framework V2 Current Context — PR8 Completed, Ready for PR9

**Project:** Mozilla Firefox Round 2 Technical Prep  
**Sub-project:** SauceDemo Selenium/Pytest Framework V2 + Gitea PR Review Lab  
**Current handoff purpose:** Use this document as the memory/context file for the next chat thread, starting with **PR9: Screenshot on Failure / Debuggability Support**.  
**Current state:** PR1–PR8 are completed, merged into `main`, and all simulated developer clones should be synced to latest `main`.

---

## 1. Why This Project Exists

This project is part of preparation for the **Mozilla Firefox Software Test Engineering Student Worker** technical deep-dive.

The goal is not only to write Selenium scripts. The project intentionally practices:

- Python/Selenium/Pytest automation
- Page Object Model design
- reusable fixtures and fixture composition
- explicit waits and stable Selenium interaction patterns
- parametrization
- JSON data-driven testing
- PR review mindset
- protected-branch workflow
- contributor/contractor simulation
- interview explanation under pressure
- framework maintainability decisions

The local Gitea workflow simulates a realistic automation team process:

```text
Contributor branch
→ Pull Request
→ Maintainer review
→ Formal approval
→ Protected main merge
→ Branch cleanup
→ All clones synced
→ Next focused PR
```

This aligns with the Mozilla role context, where the candidate may need to review automation PRs, support a contractor/manual QA team transitioning into automation, and contribute to an automation suite.

---

## 2. Active Source Documents Considered

The following source/context documents are active and should continue to be considered in the next thread:

```text
mozilla_round2_technical_prep_roadmap.md
mozilla_firefox_interview_thread_knowledge_context.md
framework_v2_implementation_guide.md
gitea_workflow_progress_context.md
current_selenium_pytest_framework_context.md
framework_v2_current_context_pr5_ready_for_pr6.md
```

### Source document roles

| Document | Purpose |
|---|---|
| `mozilla_round2_technical_prep_roadmap.md` | Overall Mozilla Round 2 preparation plan: Python, Selenium/Pytest, PR review, CI/CD, interview fluency. |
| `mozilla_firefox_interview_thread_knowledge_context.md` | Mozilla role/interview context, Round 1 questions, role expectations, and answer narratives. |
| `framework_v2_implementation_guide.md` | Main implementation plan for SauceDemo Selenium/Pytest + Gitea PR review lab. |
| `gitea_workflow_progress_context.md` | Local Gitea setup, multi-developer workflow, team permissions, branch protection, and PR simulation. |
| `current_selenium_pytest_framework_context.md` | Snapshot of older Selenium Python Hybrid Framework for comparison and familiarity. |
| `framework_v2_current_context_pr5_ready_for_pr6.md` | Handoff context after PR5 and before PR6; now superseded by this PR8-ready context. |

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
- `main` is the default branch.
- `main` is protected.
- PR-based workflow is active.

---

## 4. Simulated Team / Developer Accounts

| User | Role in simulation | Current usage |
|---|---|---|
| `abrar` | Maintainer / reviewer | Reviews and merges PRs. |
| `qa-contractor-1` | Contributor | Created PR1, PR3, PR5, PR7. |
| `qa-contractor-2` | Contributor | Created PR2, PR4, PR6, PR8. Recommended next? Rotate to `qa-contractor-1` for PR9 unless intentionally assigning debug/reporting infra to contractor-2. |

### Key identity lesson

There are two identities:

```text
Git commit identity      → git config user.name / user.email
Gitea authentication     → username/password used during push
```

Git identity controls commit author.  
Gitea authentication controls PR creator, push permission, and branch ownership.

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

## 6. Completed PRs So Far

| PR | Branch | Contributor | Status | Main purpose |
|---|---|---|---|---|
| PR1 | `feature/framework-skeleton` | `qa-contractor-1` | Merged | Framework skeleton, basic folders, pytest config, requirements, config placeholder. |
| PR2 | `feature/add-browser-fixture` | `qa-contractor-2` | Merged | Browser fixture, config reader, expanded config, smoke setup test. |
| PR3 | `feature/add-base-page` | `qa-contractor-1` | Merged | BasePage with explicit wait helpers and reusable Selenium actions. |
| PR4 | `feature/add-login-page-and-smoke-test` | `qa-contractor-2` | Merged | LoginPage + first valid login smoke/regression test. |
| PR5 | `feature/add-inventory-page-smoke-test` | `qa-contractor-1` | Merged | InventoryPage, logged-in inventory fixture, inventory product-list smoke/regression test, and LoginPage returns InventoryPage after successful login. |
| PR6 | `feature/add-cart-badge-smoke-test` | `qa-contractor-2` | Merged | Cart badge smoke test: add one inventory item and verify badge count is `1`. |
| PR7 | `feature/add-negative-login-parametrization` | `qa-contractor-1` | Merged | Added `login_page` fixture, refactored login fixture flow, added `attempt_login()`, `get_error_message()`, and parametrized negative login tests. |
| PR8 | `feature/add-json-login-data` | `qa-contractor-2` | Merged | Moved negative login test cases to JSON, added `utils/json_reader.py`, updated parametrized test to use JSON data and readable case IDs. |

---

## 7. Current Confirmed Test Expectation After PR8

User confirmed after PR8:

```text
8 tests collected
8 tests passed
```

Expected validation commands:

```powershell
pytest --collect-only
pytest -m smoke -v
pytest -m negative -v
pytest -m data_driven -v
pytest -m regression -v
pytest -v
```

Expected marker behavior after PR8:

```text
pytest -m smoke -v        → 3 selected
pytest -m negative -v     → 4 selected
pytest -m data_driven -v  → 4 selected
pytest -m regression -v   → 7 selected
pytest -v                 → 8 passed
```

The one non-regression test is likely the basic setup/environment validation test:

```text
tests/test_smoke_setup.py::test_browser_can_open_base_url
```

---

## 8. Expected Current Folder Structure After PR8

The exact folder tree should be verified in the repo, but after PR8 the structure should roughly contain:

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
│   ├── test_inventory.py
│   └── test_cart.py
├── test_data/
│   └── login_data.json
├── utils/
│   ├── __init__.py
│   ├── config_reader.py
│   └── json_reader.py
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

Optional planned but not yet implemented:

```text
docs/
pages/cart_page.py
pages/checkout_page.py
utils/excel_reader.py
utils/screenshot_utils.py
utils/logger.py
```

---

## 9. Current Important Files and Code Shape

### 9.1 `config/config.json`

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

---

### 9.2 `utils/config_reader.py`

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

---

### 9.3 `utils/json_reader.py`

Added in PR8.

```python
import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def read_json(file_path: str | Path) -> list[dict]:
    """
    Read a JSON file and return its parsed content.

    Args:
        file_path: Relative or absolute path to the JSON file.

    Returns:
        list[dict]: Parsed JSON data.
    """
    path = Path(file_path)

    if not path.is_absolute():
        path = PROJECT_ROOT / path

    if not path.exists():
        raise FileNotFoundError(f"JSON test data file not found: {path}")

    with path.open(encoding="utf-8") as file:
        return json.load(file)
```

Key concepts discussed:

- `Path(__file__).resolve().parents[1]` calculates the project root from `utils/json_reader.py`.
- `file_path: str | Path` means the function accepts either a string path or a `Path` object.
- `-> list[dict]` documents that the JSON file is expected to return a list of test case dictionaries.
- `str | Path` uses the modern Python union type syntax, available from Python 3.10+.

---

### 9.4 `test_data/login_data.json`

Added in PR8.

```json
[
  {
    "case_id": "TC_LOGIN_002",
    "username": "locked_out_user",
    "password": "secret_sauce",
    "expected_error": "Epic sadface: Sorry, this user has been locked out."
  },
  {
    "case_id": "TC_LOGIN_003",
    "username": "standard_user",
    "password": "wrong_password",
    "expected_error": "Epic sadface: Username and password do not match any user in this service"
  },
  {
    "case_id": "TC_LOGIN_004",
    "username": "",
    "password": "secret_sauce",
    "expected_error": "Epic sadface: Username is required"
  },
  {
    "case_id": "TC_LOGIN_005",
    "username": "standard_user",
    "password": "",
    "expected_error": "Epic sadface: Password is required"
  }
]
```

---

### 9.5 `conftest.py`

Expected current shape after PR7:

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
def login_page(driver, base_url, config):
    """
    Open the SauceDemo login page and return a LoginPage object.

    This fixture is useful for tests that start from the login page,
    including both successful and negative login scenarios.
    """
    timeout = config.get("default_timeout", 10)

    page = LoginPage(
        driver=driver,
        base_url=base_url,
        timeout=timeout
    )
    page.open()

    return page


@pytest.fixture
def logged_in_inventory_page(login_page, config):
    """
    Log in as a standard user and return the InventoryPage object.

    This fixture is useful for tests that need an authenticated user
    already landed on the inventory page.
    """
    standard_user = config["users"]["standard"]

    return login_page.login(
        standard_user["username"],
        standard_user["password"]
    )
```

Important design after PR7:

```text
driver + base_url + config
        ↓
login_page
        ↓
logged_in_inventory_page
```

---

### 9.6 `pages/base_page.py`

Current expected shape:

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

---

### 9.7 `pages/login_page.py`

Expected current shape after PR7:

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
    - perform successful and unsuccessful login actions
    - return InventoryPage only after successful login
    """

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

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

    def attempt_login(self, username: str, password: str) -> None:
        """
        Attempt login without assuming success.

        Useful for negative login tests where the user should remain
        on the login page and see an error message.
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def get_error_message(self) -> str:
        """Return the login error message text."""
        return self.get_text(self.ERROR_MESSAGE)
```

Key design:

```text
login()         → successful login, returns InventoryPage
attempt_login() → negative/uncertain login, does not return InventoryPage
```

---

### 9.8 `pages/inventory_page.py`

Expected current shape after PR6:

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
    - support simple cart badge validation from the inventory page
    """

    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")

    ADD_BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver, timeout: int = 10):
        super().__init__(driver, timeout)

    def is_inventory_list_visible(self) -> bool:
        """Return True if the inventory list is visible."""
        return self.is_visible(self.INVENTORY_LIST)

    def get_inventory_item_count(self) -> int:
        """Return the number of products displayed on the inventory page."""
        self.find_visible(self.INVENTORY_LIST)
        return len(self.driver.find_elements(*self.INVENTORY_ITEMS))

    def add_backpack_to_cart(self) -> None:
        """Add Sauce Labs Backpack to the cart."""
        self.click(self.ADD_BACKPACK_BUTTON)

    def get_cart_badge_count(self) -> str:
        """Return the cart badge count text."""
        return self.get_text(self.CART_BADGE)
```

Design decision:

- Do not create `CartPage` yet for PR6 because the test only checks the badge visible from the Inventory page.
- Add `CartPage` later when navigating to the cart, validating cart contents, removing items, or starting checkout.

---

### 9.9 `tests/test_smoke_setup.py`

```python
def test_browser_can_open_base_url(driver, base_url):
    driver.get(base_url)

    assert "saucedemo" in driver.current_url
```

This is a framework/environment validation test, not currently marked as smoke.

---

### 9.10 `tests/test_login.py`

Expected current shape after PR8:

```python
import pytest

from utils.json_reader import read_json


NEGATIVE_LOGIN_DATA = read_json("test_data/login_data.json")


@pytest.mark.smoke
@pytest.mark.regression
def test_standard_user_can_login(login_page, config):
    user = config["users"]["standard"]

    inventory_page = login_page.login(
        user["username"],
        user["password"]
    )

    assert inventory_page.is_inventory_list_visible(), (
        "Expected inventory list to be visible after successful login."
    )


@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.data_driven
@pytest.mark.parametrize(
    "login_case",
    NEGATIVE_LOGIN_DATA,
    ids=[case["case_id"] for case in NEGATIVE_LOGIN_DATA]
)
def test_invalid_login_shows_error(login_page, login_case):
    login_page.attempt_login(
        login_case["username"],
        login_case["password"]
    )

    actual_error = login_page.get_error_message()

    assert actual_error == login_case["expected_error"], (
        f"Expected login error message to be "
        f"'{login_case['expected_error']}', "
        f"but found '{actual_error}'."
    )
```

Important design:

- `login_page` is a fixture.
- `login_case` is not a fixture; it is a parametrized argument from `@pytest.mark.parametrize`.
- `ids=[case["case_id"] for case in NEGATIVE_LOGIN_DATA]` makes Pytest output readable, e.g.:

```text
test_invalid_login_shows_error[TC_LOGIN_002]
```

---

### 9.11 `tests/test_inventory.py`

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

### 9.12 `tests/test_cart.py`

Added in PR6.

```python
import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_add_one_item_to_cart_updates_badge(logged_in_inventory_page):
    logged_in_inventory_page.add_backpack_to_cart()

    cart_badge_count = logged_in_inventory_page.get_cart_badge_count()

    assert cart_badge_count == "1", (
        f"Expected cart badge count to be '1' after adding one item, "
        f"but found '{cart_badge_count}'."
    )
```

---

## 10. PR6 Summary — Cart Badge Smoke Test

### Contributor

```text
qa-contractor-2
```

### Branch

```text
feature/add-cart-badge-smoke-test
```

### Files touched

```text
pages/inventory_page.py
tests/test_cart.py
```

### Purpose

Add the first cart interaction:

```text
logged-in user
→ add Sauce Labs Backpack to cart
→ verify shopping cart badge count is "1"
```

### Key design decisions

- Keep PR small.
- Do not create `CartPage` yet.
- Add cart badge and add-to-cart behavior to `InventoryPage` because the badge is visible there.
- Use existing `logged_in_inventory_page` fixture.
- No repeated login in the test.
- Mark test as `smoke` and `regression`.

### Expected result after PR6

```text
4 tests collected
4 passed
```

### Interview explanation

> I expanded the smoke suite from login and inventory visibility to the first cart interaction. Since the user is already logged in through the reusable fixture, the test simply adds one product from the inventory page and verifies that the cart badge updates to 1. I kept the PR small by adding cart-badge behavior to `InventoryPage` instead of creating a full `CartPage` too early. A separate `CartPage` will make more sense when we start validating cart contents, removal, or checkout.

---

## 11. PR7 Summary — Login Fixture Refactor + Negative Login Parametrization

### Contributor

```text
qa-contractor-1
```

### Branch

```text
feature/add-negative-login-parametrization
```

### Files touched

```text
conftest.py
pages/login_page.py
tests/test_login.py
```

### Purpose

Add negative login validation and refactor login setup.

### Key changes

- Added `login_page` fixture.
- Refactored successful login test to use `login_page`.
- Refactored `logged_in_inventory_page` to depend on `login_page`.
- Added `ERROR_MESSAGE` locator to `LoginPage`.
- Added `attempt_login()` for failed/uncertain login attempts.
- Added `get_error_message()` for login error validation.
- Added parametrized negative login test with four cases:
  - locked-out user
  - wrong password
  - empty username
  - empty password

### Fixture composition after PR7

```text
driver + base_url + config
        ↓
login_page
        ↓
logged_in_inventory_page
```

### Design reasoning

Before PR7, `test_standard_user_can_login()` manually created and opened `LoginPage`. Since the negative login test also needed the same login page setup, the repeated setup was moved into a fixture.

This is proper Pytest fixture composition:

```text
fixture creates reusable test context
test consumes prepared context
page object handles UI interaction
```

### Expected result after PR7

```text
8 tests collected
8 passed
```

### Interview explanation

> In PR7, I added a reusable `login_page` fixture because multiple login tests now need the same setup: create the LoginPage, apply the configured timeout, and open the login URL. I then refactored the successful login test to use that fixture and added parametrized negative login tests. I also separated successful login from failed login behavior: `login()` returns `InventoryPage`, while `attempt_login()` does not assume navigation and is used for error validation.

---

## 12. PR8 Summary — JSON Data-Driven Negative Login Tests

### Contributor

```text
qa-contractor-2
```

### Branch

```text
feature/add-json-login-data
```

### Files touched

```text
test_data/login_data.json
utils/json_reader.py
tests/test_login.py
```

### Purpose

Move negative login test data out of inline parametrization and into JSON.

### Key changes

- Added `test_data/login_data.json`.
- Added reusable `utils/json_reader.py`.
- Updated negative login test to load data from JSON.
- Added `data_driven` marker to negative login test.
- Used `ids=[case["case_id"] for case in NEGATIVE_LOGIN_DATA]` so Pytest output displays clean case IDs.

### Expected result after PR8

Confirmed by user:

```text
8 tests collected
8 passed
```

### Interview explanation

> In PR8, I moved the negative login input combinations from inline parametrization into a JSON file. The test still uses Pytest parametrization, but now the data is externalized and easier to review or extend. I added a small JSON reader utility so the test file stays focused on behavior instead of file-handling details. I also used readable case IDs so the Pytest output clearly shows which login scenario passed or failed.

---

## 13. Key Design Decisions Made Through PR8

### 13.1 Fixtures are injected into tests and fixtures, not page objects

Pytest injects fixtures by function parameter name:

```python
def test_standard_user_can_login(login_page, config):
    ...
```

Page objects do not ask Pytest for fixtures. They receive normal Python arguments from tests or fixtures.

Flow:

```text
Pytest fixture system
    ↓
injects driver/base_url/config/login_page into test or another fixture
    ↓
test/fixture creates page object
    ↓
page object uses self.driver and its own methods
```

### 13.2 `login_page` fixture is a Pytest convenience layer

The fixture is not a Page Object feature. It is a reusable setup layer that:

```text
creates LoginPage
passes driver/base_url/timeout
opens the login page
returns the ready LoginPage object
```

### 13.3 `logged_in_inventory_page` now composes from `login_page`

Instead of repeating LoginPage creation inside `logged_in_inventory_page`, it reuses `login_page`.

This creates one source of truth for login page setup.

### 13.4 `login()` vs `attempt_login()`

```text
login()         → use only when expecting successful login; returns InventoryPage
attempt_login() → use when success is not assumed; stays on LoginPage; useful for negative tests
```

### 13.5 JSON reader uses project-root-based paths

`Path(__file__).resolve().parents[1]` finds the project root from `utils/json_reader.py`.

For:

```text
saucedemo-pytest-automation/utils/json_reader.py
```

the parents are:

```text
parents[0] = saucedemo-pytest-automation/utils
parents[1] = saucedemo-pytest-automation
```

So:

```python
PROJECT_ROOT = Path(__file__).resolve().parents[1]
```

allows stable loading of:

```text
test_data/login_data.json
```

from project root, regardless of the terminal working directory.

### 13.6 `file_path: str | Path`

In:

```python
def read_json(file_path: str | Path) -> list[dict]:
```

`str | Path` means the function accepts either a string path or a `Path` object.

This is modern Python union type syntax, available in Python 3.10+.

### 13.7 `-> list[dict]`

This return type hint documents that the JSON content should be a list of dictionaries.

This matches the login JSON shape:

```python
[
    {
        "case_id": "TC_LOGIN_002",
        "username": "locked_out_user",
        "password": "secret_sauce",
        "expected_error": "..."
    }
]
```

### 13.8 Parametrization with one dictionary argument

In PR8:

```python
@pytest.mark.parametrize(
    "login_case",
    NEGATIVE_LOGIN_DATA,
    ids=[case["case_id"] for case in NEGATIVE_LOGIN_DATA]
)
```

means:

```text
For each dictionary in NEGATIVE_LOGIN_DATA:
    run the same test
    pass the dictionary as login_case
    show the case_id in Pytest output
```

### 13.9 `ids`

`ids` controls the display name of parametrized test cases in Pytest output.

Without `ids`, output may be generic or noisy.

With `ids`, output becomes:

```text
test_invalid_login_shows_error[TC_LOGIN_002]
test_invalid_login_shows_error[TC_LOGIN_003]
test_invalid_login_shows_error[TC_LOGIN_004]
test_invalid_login_shows_error[TC_LOGIN_005]
```

### 13.10 List comprehension

This:

```python
[case["case_id"] for case in NEGATIVE_LOGIN_DATA]
```

is a list comprehension.

It is equivalent to:

```python
ids = []

for case in NEGATIVE_LOGIN_DATA:
    ids.append(case["case_id"])
```

---

## 14. Current Golden Workflow for Future PRs

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
pytest -m negative -v
pytest -m data_driven -v
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

## 15. Post-PR8 Sync Commands Needed

After PR8 merge, each clone should run the following.

### Maintainer clone: `abrar`

```powershell
cd D:\Projects\Personal\git-workflow\abrar-maintainer\saucedemo-pytest-automation

git checkout main
git pull origin main
git fetch --prune origin
pytest -v
```

Expected:

```text
8 passed
```

### Contractor 1 clone: `qa-contractor-1`

```powershell
cd D:\Projects\Personal\git-workflow\qa-contractor-1\saucedemo-pytest-automation

git checkout main
git pull origin main
git fetch --prune origin
pytest -v
```

Expected:

```text
8 passed
```

### Contractor 2 clone: `qa-contractor-2`

PR8 branch was created here, so delete local feature branch after switching to main:

```powershell
cd D:\Projects\Personal\git-workflow\qa-contractor-2\saucedemo-pytest-automation

git checkout main
git pull origin main
git fetch --prune origin
git branch -d feature/add-json-login-data
pytest -v
```

Expected:

```text
8 passed
```

If Gitea deleted the remote PR branch, `git fetch --prune origin` removes stale remote-tracking references such as:

```text
origin/feature/add-json-login-data
```

---

## 16. Recommended Next PR: PR9

### Recommended PR title

```text
Add screenshot capture on test failure
```

### Recommended branch

```text
feature/add-screenshot-on-failure
```

### Recommended contributor

```text
qa-contractor-1
```

Reason: PR8 was done by `qa-contractor-2`, so rotate back to `qa-contractor-1`.

### Why PR9 is the next logical PR

After PR8, the framework has:

- browser fixture
- config reader
- BasePage
- LoginPage
- InventoryPage
- positive login smoke
- inventory smoke
- cart badge smoke
- negative login parametrization
- JSON data-driven testing

The next highest-value improvement is debuggability.

The implementation guide includes screenshot and logging support later, and the older framework already had an Allure screenshot-on-failure concept. PR9 should implement a simple, framework-native screenshot-on-failure hook before adding logging or Allure integration.

### Suggested PR9 scope

Recommended files:

```text
utils/screenshot_utils.py
conftest.py
```

Potentially touched:

```text
reports/screenshots/.gitkeep
```

Avoid in PR9:

```text
utils/logger.py
allure-pytest integration
pytest-html
full reporting dashboard
checkout flow
Excel data-driven testing
```

### Suggested PR9 functionality

- Add `sanitize_filename(test_name)` helper.
- Add `take_screenshot(driver, test_name, directory="reports/screenshots")`.
- Add Pytest hook support in `conftest.py` so failed tests automatically save screenshots.
- Store screenshots under:

```text
reports/screenshots/
```

- Filename format:

```text
<test_name>__<YYYYMMDD_HHMMSS>.png
```

Example:

```text
test_invalid_login_shows_error_TC_LOGIN_003__20260606_154500.png
```

### Suggested validation for PR9

1. Temporarily force one assertion failure.
2. Run the failing test.
3. Confirm screenshot appears in `reports/screenshots/`.
4. Revert the forced failure.
5. Run the full suite.

Expected final validation:

```powershell
pytest -v
```

Expected:

```text
8 passed
```

### PR9 interview explanation target

> I added automatic screenshot capture on test failure to improve debuggability. When a UI test fails, a screenshot helps quickly decide whether the issue is a product defect, locator/wait problem, test data issue, or environment problem. I kept this PR focused on screenshots only and left logging/Allure integration for later so the change stayed small and reviewable.

---

## 17. PR9 Review Checklist

```text
[ ] Screenshot utility is reusable and not tied to one test.
[ ] Screenshot filenames are sanitized.
[ ] Screenshot filenames include timestamp.
[ ] Screenshots are saved under reports/screenshots/.
[ ] Hook captures screenshot only when a test fails.
[ ] Hook does not break passing tests.
[ ] No screenshot code inside individual test files.
[ ] No Allure added in this PR unless intentionally decided.
[ ] No logging added in this PR unless intentionally decided.
[ ] Forced failure test generates screenshot.
[ ] Forced failure is reverted before merge.
[ ] pytest -v passes after cleanup.
```

---

## 18. Final Current Status Summary

```text
Current milestone: PR8 completed and merged.
Current framework ability:
  - launch browser from fixture
  - read JSON config
  - open SauceDemo
  - use BasePage explicit waits
  - log in with standard user
  - return InventoryPage after successful login
  - use login_page fixture
  - use logged_in_inventory_page fixture
  - verify inventory list and product count
  - add one product to cart and verify cart badge
  - run negative login tests with parametrization
  - load negative login data from JSON
  - show readable parametrized case IDs in Pytest output

Current tests:
  - setup/environment validation
  - standard user login smoke/regression
  - inventory product-list smoke/regression
  - cart badge smoke/regression
  - negative login data-driven regression tests

Expected current validation:
  pytest -v → 8 passed

Next milestone:
  PR9 screenshot capture on failure.

Recommended next contributor:
  qa-contractor-1.

Recommended next branch:
  feature/add-screenshot-on-failure.
```
