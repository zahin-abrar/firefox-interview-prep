# Framework V2 Current Context — PR2 Completed, Ready for PR3

**Project:** Mozilla Firefox Round 2 Technical Prep  
**Sub-project:** SauceDemo Selenium/Pytest Framework V2 + Gitea PR Review Lab  
**Current handoff purpose:** Use this document as the memory/context file for the next chat thread, starting with **PR3: BasePage**.  
**Last updated:** 2026-06-03  
**Current state:** PR1 and PR2 are completed, merged into `main`, and all simulated developer clones are synced to latest `main`.

---

## 1. Why This Project Exists

This project is part of preparation for the **Mozilla Firefox Software Test Engineering Student Worker** technical deep-dive.

The preparation is intentionally not just “write Selenium scripts.” The goal is to demonstrate and practice:

- Python/Selenium/Pytest automation ability
- Page Object Model understanding
- maintainable framework design
- PR review mindset
- working with contributors/contractors
- protected-branch workflow
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

This directly supports the Mozilla role context, where the user may need to review automation PRs, support a contractor/manual QA team transitioning into automation, and contribute to an automation suite.

---

## 2. Main Source Documents Currently Used

The following files are loaded into the project and should remain treated as active context:

```text
mozilla_round2_technical_prep_roadmap.md
mozilla_firefox_interview_thread_knowledge_context.md
framework_v2_implementation_guide.md
gitea_workflow_progress_context.md
gitea_framework_v2_progress_interview_context.md
current_selenium_pytest_framework_context.md
```

### Source document roles

| Document | Purpose |
|---|---|
| `mozilla_round2_technical_prep_roadmap.md` | Overall Mozilla Round 2 preparation plan: Python, Selenium/Pytest, PR review, CI/CD, interview fluency. |
| `mozilla_firefox_interview_thread_knowledge_context.md` | Full Mozilla role/interview context, Round 1 questions, role expectations, and answer narratives. |
| `framework_v2_implementation_guide.md` | Main implementation plan for SauceDemo Selenium/Pytest + Gitea PR review lab. |
| `gitea_workflow_progress_context.md` | Earlier Gitea setup and multi-developer workflow context. |
| `gitea_framework_v2_progress_interview_context.md` | Progress context up to PR1 completion and PR2 recommendation. |
| `current_selenium_pytest_framework_context.md` | Snapshot of the previous Selenium Python Hybrid Framework for comparison and familiarity. |

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

| User | Role in simulation | Notes |
|---|---|---|
| `abrar` | Maintainer / reviewer | Reviews and merges PRs. |
| `qa-contractor-1` | Contributor | Created PR1 framework skeleton. Recommended for PR3. |
| `qa-contractor-2` | Contributor | Created PR2 browser fixture + config reader. Also useful for future flawed PR exercises. |

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

Each clone simulates a separate developer machine.

---

## 6. Previous Framework Reference

The old framework is available as a reference point:

```text
D:\Projects\Personal\Python\SeleniumPythonHybridFramework
```

### Previous framework key structure

```text
SeleniumPythonHybridFramework/
├── configurations/
│   └── config.ini
├── pages/
│   ├── BasePage.py
│   ├── LoginPage.py
│   ├── HomePage.py
│   ├── AccountPage.py
│   └── SearchPage.py
├── tests/
│   ├── BaseTest.py
│   ├── conftest.py
│   ├── test_Login.py
│   └── test_Search.py
├── utilities/
│   ├── ReadConfigurations.py
│   └── ExcelUtils.py
├── ExcelFiles/
├── Reports/
├── docs/
└── README.md
```

### Previous config approach

```ini
[basic info]
browser=chrome
url=https://tutorialsninja.com/demo/
```

### Previous driver setup approach

```text
BaseTest
→ setup_and_teardown fixture
→ ReadConfigurations.read_configuration()
→ webdriver.Chrome() / webdriver.Firefox() / webdriver.Edge()
→ driver.get(url)
→ request.cls.driver = driver
→ test uses self.driver
→ driver.quit()
```

### Previous test style

The previous framework used class-based tests:

```python
class TestLogin(BaseTest):
    def test_login_with_valid_credentials(self, email_address, password):
        home_page = HomePage(self.driver)
```

This worked, but Framework V2 is currently using more direct Pytest fixture injection to make test dependencies visible.

---

## 7. Framework V2 Target Architecture

The implementation guide target structure is:

```text
saucedemo-pytest-automation/
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_checkout.py
├── test_data/
│   ├── login_data.json
│   ├── login_data.xlsx
│   └── users.json
├── utils/
│   ├── __init__.py
│   ├── config_reader.py
│   ├── excel_reader.py
│   ├── screenshot_utils.py
│   ├── logger.py
│   └── wait_utils.py
├── config/
│   └── config.json
├── reports/
│   ├── screenshots/
│   ├── logs/
│   └── allure-results/
├── docs/
│   ├── PR_REVIEW_CHECKLIST.md
│   ├── TEST_STRATEGY.md
│   ├── DAILY_NOTES.md
│   └── INTERVIEW_EXPLANATION_NOTES.md
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

Current actual implementation is earlier than the full target; do not assume all folders/files exist yet.

---

## 8. Current Framework V2 State After PR2

### Completed PRs

| PR | Branch | Contributor | Status | Main purpose |
|---|---|---|---|---|
| PR1 | `feature/framework-skeleton` | `qa-contractor-1` | Merged | Framework skeleton, basic folders, pytest config, requirements, config placeholder. |
| PR2 | `feature/add-browser-fixture` | `qa-contractor-2` | Merged | Browser fixture, config reader, expanded config, smoke setup test. |

### Current confirmed state

- PR2 has been merged to `main`.
- All dev accounts/clones are synced to latest `main`.
- `pytest --collect-only` collects 1 test.
- `pytest tests/test_smoke_setup.py -v` passes.
- Browser fixture works.
- Config loading works.
- Firefox can launch and open SauceDemo.
- Root-level `conftest.py` is working.

---

## 9. Expected Current Folder Structure After PR2

The exact folder tree should be verified in the repo, but based on completed PRs the current structure should roughly contain:

```text
saucedemo-pytest-automation/
├── config/
│   └── config.json
├── pages/
│   └── __init__.py
├── tests/
│   ├── __init__.py
│   └── test_smoke_setup.py
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
```

---

## 10. PR1 Summary — Framework Skeleton

### Contributor

```text
qa-contractor-1
```

### Branch

```text
feature/framework-skeleton
```

### Purpose

Establish the basic framework structure before adding Selenium implementation.

### Files/folders added

```text
.gitignore
config/
pages/
pytest.ini
reports/
requirements.txt
tests/
utils/
```

### Validation

```powershell
pytest --collect-only
```

Expected and observed at that time:

```text
collected 0 items
```

This was correct because there were no tests yet. It confirmed:

- venv worked
- pytest installed
- `pytest.ini` detected
- `tests/` path detected
- generated/local files were ignored

### PR result

- Opened by `qa-contractor-1`.
- Reviewed as `abrar`.
- Approved from Gitea **Files Changed** tab.
- Merged with create merge commit.
- Remote feature branch deleted after merge.

---

## 11. PR2 Summary — Browser Fixture + Config Reader

### Contributor

```text
qa-contractor-2
```

### Branch

```text
feature/add-browser-fixture
```

### Purpose

Add framework execution infrastructure:

- JSON config reader
- `config` fixture
- `base_url` fixture
- `driver` fixture
- Firefox support first
- optional Chrome support structure
- setup smoke test validating browser can open SauceDemo

### Files touched

```text
conftest.py
utils/config_reader.py
config/config.json
tests/test_smoke_setup.py
```

### Important decision

`conftest.py` is placed at the project root, not inside `tests/`.

Reason:

```text
Root-level conftest.py = framework-wide fixture scope
Tests folder = test cases only
```

This aligns with the V2 target structure and makes fixtures like `driver`, `config`, and `base_url` globally available to tests.

---

## 12. PR2 Implementation Details

### `config/config.json`

Recommended current content:

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

### `utils/config_reader.py`

Recommended robust implementation:

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

### `conftest.py`

PR2 fixture direction:

```python
import pytest
from selenium import webdriver

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
```

### `tests/test_smoke_setup.py`

```python
def test_browser_can_open_base_url(driver, base_url):
    driver.get(base_url)

    assert "saucedemo" in driver.current_url
```

This test does not need `import pytest` because it does not directly use `pytest.mark`, `pytest.raises`, `pytest.fixture`, or other Pytest objects. Pytest discovers it from the `test_` naming pattern.

---

## 13. PR2 Validation Output

### Command

```powershell
pytest --collect-only
```

### Observed result

```text
collected 1 item

<Dir saucedemo-pytest-automation>
  <Package tests>
    <Module test_smoke_setup.py>
      <Function test_browser_can_open_base_url>

1 test collected in 0.01s
```

### Command

```powershell
pytest tests/test_smoke_setup.py -v
```

### Observed result

```text
tests/test_smoke_setup.py::test_browser_can_open_base_url PASSED [100%]

1 passed in 11.71s
```

### What PR2 proves

```text
✔ pytest discovery works
✔ root-level conftest.py works
✔ fixture injection works
✔ config loading works
✔ Firefox launch works
✔ SauceDemo is reachable
✔ browser teardown works
✔ first executable smoke validation works
```

---

## 14. Key Design Decisions Made in This Thread

### 14.1 Use JSON instead of INI for Framework V2 runtime config

The old framework used:

```ini
[basic info]
browser=chrome
url=https://tutorialsninja.com/demo/
```

Framework V2 uses JSON because the configuration is now more structured:

```text
base_url
browser
headless
default_timeout
users.standard.username
users.standard.password
users.locked.username
users.locked.password
```

Benefits:

- natural nested data
- better boolean/number handling
- easy future extension
- aligns with planned JSON test data
- clear Git diffs in PR reviews

Important nuance:

```text
INI is fine for flat config.
JSON is better here because V2 config is structured.
```

### 14.2 Root-level `conftest.py`

Chosen structure:

```text
saucedemo-pytest-automation/conftest.py
```

not:

```text
saucedemo-pytest-automation/tests/conftest.py
```

Reason:

- `driver`, `config`, `base_url` are framework-wide fixtures.
- `tests/` should stay focused on test cases.
- root-level fixtures are easier to share across all test modules.

### 14.3 Function-based tests for now

Framework V2 currently uses:

```python
def test_browser_can_open_base_url(driver, base_url):
    ...
```

instead of:

```python
class TestSomething(BaseTest):
    def test_something(self):
        ... self.driver ...
```

Reason:

- direct fixture dependencies are visible in test signatures
- easier for contributors/manual QA learners
- less hidden inheritance wiring
- more idiomatic/simple Pytest start

Important nuance:

```text
Function-based tests do NOT mean no classes in the framework.
Page Object Model will still use classes.
```

### 14.4 POM remains class-based

The framework will still use:

```python
class BasePage:
    ...

class LoginPage(BasePage):
    ...
```

POM classes are separate from test classes.

```text
Page Objects → class-based
Current tests → function-based
```

### 14.5 Fixture delivery changed from class side-effect to direct injection

Old framework:

```python
request.cls.driver = driver
yield
driver.quit()
```

V2:

```python
yield driver
driver.quit()
```

Old flow:

```text
fixture → request.cls.driver → test uses self.driver
```

New flow:

```text
fixture → yield driver → test receives driver parameter
```

The setup/teardown concept is the same; the delivery mechanism changed.

### 14.6 `yield driver` purpose

`yield driver` is used because the fixture has both setup and teardown responsibilities.

```text
Before yield  → setup browser
At yield      → provide driver to test
After yield   → quit browser
```

This is not because tests are function-based; `yield` works for both function-based and class-based tests. The difference is whether the fixture passes the object directly or attaches it to a class.

### 14.7 Browser options

`webdriver.FirefoxOptions()` and `webdriver.ChromeOptions()` configure browser startup before Selenium launches the browser.

Used now for:

```text
headless mode
```

Potential later uses:

```text
window size
browser profile
download directory
proxy
extensions
certificate behavior
binary path
```

Firefox headless argument:

```python
options.add_argument("-headless")
```

Chrome headless argument used in guide:

```python
options.add_argument("--headless=new")
```

Reason: browser-specific command-line flags differ.

---

## 15. Current Golden Workflow

For each new PR:

```powershell
git checkout main
git pull origin main
git checkout -b feature/short-task-name
```

Implement.

Validate:

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

## 16. Current Completed Workflow State

The following have been completed:

```text
PR1 created by qa-contractor-1
PR1 reviewed and merged by abrar
PR2 created by qa-contractor-2
PR2 reviewed and merged by abrar
Remote feature branches cleaned/deleted
All dev accounts synced to latest main
```

This is important because PR3 can safely begin from latest `main`.

---

## 17. Recommended Next Thread Starting Point

Start PR3 in a new thread.

### Recommended PR3

```text
PR3: Add BasePage
```

### Recommended branch

```text
feature/add-base-page
```

### Recommended contributor

```text
qa-contractor-1
```

Reason: PR1 came from `qa-contractor-1`, PR2 from `qa-contractor-2`, so rotating back to `qa-contractor-1` keeps the multi-contributor simulation realistic.

### Start commands

```powershell
cd D:\Projects\Personal\git-workflow\qa-contractor-1\saucedemo-pytest-automation

git checkout main
git pull origin main
git branch -a
git checkout -b feature/add-base-page
```

---

## 18. PR3 Scope Recommendation

### Files to touch

```text
pages/base_page.py
```

Possibly:

```text
pages/__init__.py
```

No LoginPage yet. No tests beyond collection validation unless needed.

### PR3 goal

Add reusable Selenium interaction helpers:

```text
open_url()
find_visible()
find_clickable()
click()
type_text()
get_text()
is_visible()
```

Use:

```text
WebDriverWait
expected_conditions
locator tuples
```

Avoid:

```text
time.sleep()
overly clever locator resolution
giant BasePage
assertion-heavy page methods
```

---

## 19. Planned BasePage Direction

Recommended design:

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def open_url(self, url):
        self.driver.get(url)

    def find_visible(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def find_clickable(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator):
        self.find_clickable(locator).click()

    def type_text(self, locator, text):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_visible(locator).text

    def is_visible(self, locator):
        try:
            self.find_visible(locator)
            return True
        except Exception:
            return False
```

Potential improvement to discuss in PR3:

```text
Should BasePage receive timeout from config?
Should is_visible catch broad Exception or TimeoutException specifically?
Should we add custom assertion messages later or keep BasePage neutral?
```

Do not decide too much ahead of PR3; discuss while implementing.

---

## 20. Old BasePage vs V2 BasePage Direction

### Previous framework style

The previous framework used dynamic locator-name suffix parsing:

```python
self.type_into_element(email, "email_address_field_id", self.email_address_field_id)
```

Then BasePage resolved the locator based on names ending with:

```text
_id
_name
_xpath
_css
_link_text
```

This was educational and worked, but V2 will likely move to standard Selenium locator tuples:

```python
USERNAME_INPUT = (By.ID, "user-name")
```

Then page methods can call:

```python
self.type_text(self.USERNAME_INPUT, username)
```

Why this is cleaner:

- less string magic
- easier for reviewers
- closer to common Selenium/POM convention
- locators are explicit
- fewer hidden failure points

---

## 21. PR3 Interview Explanation Target

After PR3, user should be able to say:

> I added a `BasePage` class to centralize common Selenium operations such as opening URLs, waiting for visible/clickable elements, clicking, typing, and reading text. This keeps Page Objects smaller and prevents repeated raw `driver.find_element` calls across the framework. I used explicit waits through `WebDriverWait` and expected conditions instead of hard sleeps, which improves reliability and reduces flaky timing issues.

---

## 22. PR3 Review Checklist

When reviewing PR3 as maintainer, check:

```text
[ ] Is BasePage small and readable?
[ ] Are explicit waits used?
[ ] Is time.sleep avoided?
[ ] Are method names clear?
[ ] Are methods generic but not too abstract?
[ ] Does BasePage avoid test assertions?
[ ] Does BasePage avoid app-specific locators?
[ ] Is locator tuple style used?
[ ] Is exception handling reasonable?
[ ] Does pytest --collect-only still pass?
```

---

## 23. Important Interview Narratives Preserved

### Why Gitea?

> I used local Gitea to simulate a GitHub-like team workflow with multiple contributors, protected main, PRs, reviews, approvals, merges, and branch cleanup. This helped me practice not just automation coding, but maintainable collaboration and review habits.

### Why protected main?

> Protected main prevents direct pushes and ensures changes go through review before entering the shared branch.

### Why small PRs?

> Small PRs are easier to review, easier to debug, and safer to merge. They also help contributors learn one framework concept at a time.

### Why fixtures?

> Fixtures separate setup and teardown from test logic. Browser lifecycle and config loading should not be repeated inside every test.

### Why POM?

> Page Object Model separates page interaction logic from test scenario logic. Tests describe what behavior is validated; page classes describe how to interact with the UI.

### Why explicit waits?

> Explicit waits wait for meaningful UI states like visibility or clickability instead of blindly pausing execution.

### Why function-based tests now?

> Function-based tests with direct fixture injection make dependencies visible in the test signature, which is helpful for readability and contributors. Page Objects remain class-based.

---

## 24. Prompt for Next Thread

Use this in the next chat thread:

```text
I am continuing my Mozilla Firefox interview prep Framework V2 project. Please read the uploaded context documents and implementation guide before answering.

Current state: Gitea workflow is set up. PR1 framework skeleton was completed by qa-contractor-1 and merged. PR2 browser fixture + config reader was completed by qa-contractor-2 and merged. All dev clones are synced to latest main. The project currently has root-level conftest.py, config/config.json, utils/config_reader.py, and tests/test_smoke_setup.py. pytest --collect-only collects 1 test and pytest tests/test_smoke_setup.py -v passes.

I want to start PR3: feature/add-base-page, preferably from qa-contractor-1. Please help me implement BasePage step by step, compare with my previous framework’s BasePage where relevant, and explain the Selenium/Pytest/POM concepts as we go.
```

---

## 25. Final Current Status Summary

```text
Current milestone: PR2 completed and merged.
Current framework ability: launch browser from fixture, read JSON config, open SauceDemo, pass setup smoke test.
Current workflow ability: multi-contributor Gitea PR workflow with protected main is operational.
Next milestone: PR3 BasePage.
Next contributor recommended: qa-contractor-1.
Next branch: feature/add-base-page.
```
