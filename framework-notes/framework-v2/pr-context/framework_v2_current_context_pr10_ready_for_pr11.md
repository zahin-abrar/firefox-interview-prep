# Framework V2 Current Context — PR10 Completed, Ready for PR11

**Project:** Mozilla Firefox Round 2 Technical Prep  
**Sub-project:** SauceDemo Selenium/Pytest Framework V2 + Gitea PR Review Lab  
**Current handoff purpose:** Use this document as the memory/context file for the next chat thread, starting with **PR11**.  
**Current state:** PR1–PR10 are completed and merged into `main`.

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
- screenshot-on-failure support
- basic framework logging
- PR review mindset
- protected-branch workflow
- contributor/contractor simulation
- interview explanation under pressure
- maintainable automation framework decisions

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

This aligns with the Mozilla role context, where the candidate may need to review automation PRs, support a contractor/manual QA team transitioning into automation, contribute to an automation suite, and investigate/debug failed automation runs.

---

## 2. Active Source Documents Considered

These source/context documents should continue to be considered in the next thread:

```text
mozilla_round2_technical_prep_roadmap.md
mozilla_firefox_interview_thread_knowledge_context.md
framework_v2_implementation_guide.md
gitea_workflow_progress_context.md
current_selenium_pytest_framework_context.md
framework_v2_current_context_pr8_ready_for_pr9.md
```

### Source document roles

| Document | Purpose |
|---|---|
| `mozilla_round2_technical_prep_roadmap.md` | Overall Mozilla Round 2 preparation plan: Python, Selenium/Pytest, PR review, CI/CD, interview fluency. |
| `mozilla_firefox_interview_thread_knowledge_context.md` | Mozilla role/interview context, Round 1 questions, role expectations, answer narratives. |
| `framework_v2_implementation_guide.md` | Main implementation plan for SauceDemo Selenium/Pytest + Gitea PR review lab. |
| `gitea_workflow_progress_context.md` | Local Gitea setup, multi-developer workflow, team permissions, branch protection, and PR simulation. |
| `current_selenium_pytest_framework_context.md` | Snapshot of older Selenium Python Hybrid Framework for comparison and familiarity. |
| `framework_v2_current_context_pr8_ready_for_pr9.md` | Handoff context after PR8 and before PR9. Superseded by this PR10-ready context but still useful for PR1–PR8 details. |

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
| `qa-contractor-1` | Contributor | Created PR1, PR3, PR5, PR7, PR9. |
| `qa-contractor-2` | Contributor | Created PR2, PR4, PR6, PR8, PR10. |

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

Important note from PR9 debugging:

- Terminal showed execution from `qa-contractor-1`, but Pytest was using a `.venv` path from `qa-contractor-2`.
- This was not the cause of the code error, but the interpreter/venv should be checked in PyCharm/terminal so each clone ideally uses its own `.venv`.

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
| PR9 | `feature/add-screenshot-on-failure` | `qa-contractor-1` | Merged | Added screenshot utility and Pytest hook/fixture teardown integration to capture screenshots on test failure. |
| PR10 | `feature/add-basic-logging` | `qa-contractor-2` | Merged | Added basic framework logging to `reports/logs/test_run.log`, including test start, pass/fail, screenshot path on failure, and browser close logs. |

---

## 7. Current Confirmed Test Expectation After PR10

Expected validation command:

```powershell
pytest -v
```

Expected result:

```text
8 passed
```

Expected marker behavior from PR8 onward:

```text
pytest -m smoke -v        → 3 selected
pytest -m negative -v     → 4 selected
pytest -m data_driven -v  → 4 selected
pytest -m regression -v   → 7 selected
pytest -v                 → 8 passed
```

The one non-regression test is likely:

```text
tests/test_smoke_setup.py::test_browser_can_open_base_url
```

---

## 8. Expected Current Folder Structure After PR10

The exact folder tree should be verified in the repo, but after PR10 the structure should roughly contain:

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
│   ├── json_reader.py
│   ├── screenshot_utils.py
│   └── logger.py
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
allure-pytest integration
CI workflow
```

---

## 9. Current Important Files and Code Shape

### 9.1 `utils/screenshot_utils.py`

Added in PR9.

```python
from datetime import datetime
from pathlib import Path
import re


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCREENSHOT_DIR = PROJECT_ROOT / "reports" / "screenshots"


def sanitize_filename(name: str) -> str:
    """
    Convert a test name/node id into a safe filename.
    """
    return re.sub(r"[^a-zA-Z0-9_-]", "_", name)


def take_screenshot(
    driver,
    test_name: str,
    directory: str | Path = DEFAULT_SCREENSHOT_DIR
) -> str:
    """
    Save a screenshot for the current browser state.
    """
    screenshot_dir = Path(directory)
    screenshot_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_test_name = sanitize_filename(test_name)
    screenshot_path = screenshot_dir / f"{safe_test_name}__{timestamp}.png"

    driver.save_screenshot(str(screenshot_path))

    return str(screenshot_path)
```

Key behavior:

- `re` is Python’s regular expression module.
- `sanitize_filename()` replaces unsafe filename characters with `_`.
- `mkdir(parents=True, exist_ok=True)` creates the screenshot folder safely.
- `strftime("%Y%m%d_%H%M%S")` creates timestamp strings like `20260606_154530`.
- `driver.save_screenshot(str(screenshot_path))` uses Selenium WebDriver’s screenshot API.
- `str(screenshot_path)` converts a `Path` object into a string path because Selenium expects a path-like string.

---

### 9.2 `utils/logger.py`

Added in PR10.

```python
import logging
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LOG_DIR = PROJECT_ROOT / "reports" / "logs"
DEFAULT_LOG_FILE = DEFAULT_LOG_DIR / "test_run.log"


def get_logger(name: str = "framework") -> logging.Logger:
    """
    Create and return a reusable framework logger.

    The logger writes messages to reports/logs/test_run.log.
    Duplicate handlers are avoided so repeated calls do not duplicate log lines.
    """
    DEFAULT_LOG_DIR.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    file_handler = logging.FileHandler(DEFAULT_LOG_FILE, encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
```

Key behavior:

- Uses Python’s built-in `logging` module.
- Writes logs to `reports/logs/test_run.log`.
- Default `FileHandler` mode is append mode (`mode="a"`).
- Both logger and file handler levels are set to `INFO`.
- `if logger.handlers: return logger` avoids duplicate handlers and duplicated log lines.

---

### 9.3 `conftest.py`

Expected current shape after PR10:

```python
import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from utils.config_reader import read_config
from utils.logger import get_logger
from utils.screenshot_utils import take_screenshot


logger = get_logger()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    Store test execution result on the test item.

    This allows fixtures to know whether the test failed
    after the test body has executed.
    """
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


@pytest.fixture(scope="session")
def config():
    return read_config()


@pytest.fixture(scope="session")
def base_url(config):
    return config["base_url"]


@pytest.fixture
def driver(config, request):
    browser = config.get("browser", "firefox").lower()
    headless = config.get("headless", False)

    logger.info(
        "Starting test: %s | browser=%s | headless=%s",
        request.node.nodeid,
        browser,
        headless
    )

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
        logger.error("Unsupported browser requested: %s", browser)
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()

    yield driver

    test_failed = (
        hasattr(request.node, "rep_call")
        and request.node.rep_call.failed
    )

    if test_failed:
        screenshot_path = take_screenshot(driver, request.node.nodeid)
        logger.error(
            "Test failed: %s | screenshot=%s",
            request.node.nodeid,
            screenshot_path
        )
        print(f"\nScreenshot saved for failed test: {screenshot_path}")
    else:
        logger.info("Test passed: %s", request.node.nodeid)

    driver.quit()
    logger.info("Browser closed for test: %s", request.node.nodeid)


@pytest.fixture
def login_page(driver, base_url, config):
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
    standard_user = config["users"]["standard"]

    return login_page.login(
        standard_user["username"],
        standard_user["password"]
    )
```

Important review lesson from PR9:

- This line was incorrectly auto-imported by PyCharm and should **not** exist:

```python
from urllib3 import request
```

Reason:

- `request` is a built-in Pytest fixture injected through `def driver(config, request)`.
- It should not be imported from `urllib3`.

---

## 10. PR9 Summary — Screenshot Capture on Failure

### Contributor

```text
qa-contractor-1
```

### Branch

```text
feature/add-screenshot-on-failure
```

### Status

```text
Merged
```

### Files touched

```text
utils/screenshot_utils.py
conftest.py
```

### Purpose

Add automatic screenshot capture when a Selenium test fails.

### Key changes

- Added `utils/screenshot_utils.py`.
- Added `sanitize_filename(test_name)`.
- Added `take_screenshot(driver, test_name, directory=DEFAULT_SCREENSHOT_DIR)`.
- Added `pytest_runtest_makereport` hook in `conftest.py`.
- Added `request` fixture dependency to `driver(config, request)`.
- Driver teardown checks whether the test failed after `yield driver`.
- Screenshot captured before `driver.quit()`.

### Validation performed

- Temporarily forced a test failure in `test_cart.py` by expecting cart badge `"2"` instead of `"1"`.
- Screenshot was successfully generated.
- Forced failure was reverted.
- Final test run passed: `8 passed`.

### PR9 review issue caught

PyCharm auto-imported:

```python
from urllib3 import request
```

This was incorrect. Review comment recommended removing it because `request` is a built-in Pytest fixture, not an import from `urllib3`.

### PR9 Git recovery issue

The PR9 code was initially committed on local `main` by mistake.

Recovery commands used:

```powershell
git checkout -b feature/add-screenshot-on-failure
git push origin feature/add-screenshot-on-failure
git checkout main
git reset --hard origin/main
```

Why it worked:

- A Git branch is a pointer to a commit.
- `git checkout -b feature/add-screenshot-on-failure` created a new branch pointing at the current PR9 commit.
- `git reset --hard origin/main` moved only local `main` back to `origin/main`.
- The PR9 commit stayed safe on the feature branch.

---

## 11. PR10 Summary — Basic Framework Logging

### Contributor

```text
qa-contractor-2
```

### Branch

```text
feature/add-basic-logging
```

### Status

```text
Merged
```

### Files touched

```text
utils/logger.py
conftest.py
```

### Purpose

Add basic framework logging so test execution has useful runtime context beyond screenshots.

### Key changes

- Added `utils/logger.py`.
- Added reusable `get_logger(name="framework")`.
- Logs are written to `reports/logs/test_run.log`.
- `conftest.py` imports `get_logger`.
- A module-level logger is created: `logger = get_logger()`.
- Driver fixture now logs:
  - test start
  - browser and headless mode
  - unsupported browser error
  - failed test with screenshot path
  - passed test
  - browser closed

### Example generated log

```text
2026-06-06 23:47:08 | INFO | framework | Starting test: tests/test_cart.py::test_add_one_item_to_cart_updates_badge | browser=firefox | headless=False
2026-06-06 23:47:15 | INFO | framework | Test passed: tests/test_cart.py::test_add_one_item_to_cart_updates_badge
2026-06-06 23:47:18 | INFO | framework | Browser closed for test: tests/test_cart.py::test_add_one_item_to_cart_updates_badge
```

### Important refinement during PR10

Initial logs showed:

```text
Starting test...
Browser closed...
```

The `Test passed` log line was missing. This was identified and added before merge.

Final expected lifecycle for passing tests:

```text
Starting test...
Test passed...
Browser closed...
```

Final expected lifecycle for failing tests:

```text
Starting test...
Test failed... | screenshot=...
Browser closed...
```

### Logging behavior

Current `FileHandler` code:

```python
file_handler = logging.FileHandler(DEFAULT_LOG_FILE, encoding="utf-8")
```

This uses append mode by default:

```python
mode="a"
```

Generated `.log` files should not be committed if `.gitignore` ignores:

```text
reports/logs/*.log
```

---

## 12. Current Git Workflow for Future PRs

For each new PR:

```powershell
git checkout main
git pull origin main
git fetch --prune origin
git checkout -b feature/short-task-name
```

Implement and validate:

```powershell
pytest --collect-only
pytest -v
```

Commit and push:

```powershell
git status
git add .
git commit -m "Clear meaningful commit message"
git push origin feature/short-task-name
```

Create PR in Gitea, review as `abrar`, merge, delete branch, and sync all clones.

---

## 13. Post-PR10 Sync Commands Needed

### Maintainer clone: `abrar`

```powershell
cd D:\Projects\Personal\git-workflow\abrar-maintainer\saucedemo-pytest-automation

git checkout main
git pull origin main
git fetch --prune origin
pytest -v
```

### Contractor 1 clone: `qa-contractor-1`

```powershell
cd D:\Projects\Personal\git-workflow\qa-contractor-1\saucedemo-pytest-automation

git checkout main
git pull origin main
git fetch --prune origin
pytest -v
```

### Contractor 2 clone: `qa-contractor-2`

```powershell
cd D:\Projects\Personal\git-workflow\qa-contractor-2\saucedemo-pytest-automation

git checkout main
git pull origin main
git fetch --prune origin
git branch -d feature/add-basic-logging
pytest -v
```

Expected: `8 passed`.

---

## 14. Generated Artifacts and `.gitignore`

Generated runtime files are local artifacts and should usually not be committed.

Expected ignored artifacts:

```text
reports/screenshots/*.png
reports/logs/*.log
reports/allure-results/*
```

Expected tracked placeholders:

```text
reports/screenshots/.gitkeep
reports/logs/.gitkeep
reports/allure-results/.gitkeep
```

Important reminders:

- `.gitignore` prevents tracking/committing files.
- `.gitignore` does **not** delete local files.
- Local screenshots/logs may remain on disk after pull/merge.

---

## 15. Recommended Next PR: PR11

### Recommended PR title

```text
Add Allure reporting support
```

### Recommended branch

```text
feature/add-allure-reporting
```

### Recommended contributor

```text
qa-contractor-1
```

Reason: PR10 was done by `qa-contractor-2`, so rotate back to `qa-contractor-1`.

### Why PR11 is the next logical PR

After PR10, the framework now has:

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
- screenshots on failure
- basic framework logging

The next reporting/debuggability layer in the implementation guide is **Allure reporting**.

### Suggested PR11 scope

Recommended files:

```text
requirements.txt
README.md
```

Possibly touched:

```text
reports/allure-results/.gitkeep
conftest.py
```

Recommended starting scope:

```text
Add allure-pytest dependency.
Document Allure commands in README.
Generate Allure results under reports/allure-results/.
Do not attach screenshots yet unless intentionally decided.
```

### Suggested validation for PR11

```powershell
pytest -v
pytest --alluredir=reports/allure-results
```

Expected: `8 passed`.

If Allure CLI is installed:

```powershell
allure serve reports/allure-results
```

If not installed, document that the Python package generates result files but the Allure command-line tool is needed to render/serve the report.

### PR11 interview explanation target

> After adding screenshots and logging, I added Allure reporting support so test execution results can be reviewed in a more structured way. I started with minimal Allure result generation rather than immediately adding advanced attachments, because the first step is to make the reporting pipeline work reliably. This keeps the PR small and easier to review.

---

## 16. Final Current Status Summary

```text
Current milestone: PR10 completed and merged.

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
  - capture screenshots automatically on test failure
  - write framework logs to reports/logs/test_run.log

Current tests:
  - setup/environment validation
  - standard user login smoke/regression
  - inventory product-list smoke/regression
  - cart badge smoke/regression
  - negative login data-driven regression tests

Expected current validation:
  pytest -v → 8 passed

Next milestone:
  PR11 Allure reporting support.

Recommended next contributor:
  qa-contractor-1.

Recommended next branch:
  feature/add-allure-reporting.
```
