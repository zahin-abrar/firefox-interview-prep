# Framework V2 Current Context — PR14 Completed, Ready for PR15

**Project:** Mozilla Firefox Round 2 Technical Prep  
**Sub-project:** SauceDemo Selenium/Pytest Framework V2 + Gitea PR Review Lab  
**Current handoff purpose:** Use this document as the memory/context file for the next chat thread, starting with **PR15**.  
**Current state:** PR1–PR14 are completed and merged into `main`.  
**Next milestone:** PR15 — Add CheckoutPage and successful checkout E2E flow.

---

## 1. Why This Project Exists

This project supports preparation for the **Mozilla Firefox Software Test Engineering Student Worker** technical deep-dive. It is intentionally more than a Selenium script collection.

The project practices:

- Python/Selenium/Pytest automation
- Page Object Model design
- reusable fixtures and fixture composition
- explicit waits and stable Selenium interaction patterns
- parametrization
- JSON and Excel data-driven testing
- screenshot-on-failure support
- framework logging
- basic Allure report generation
- PR review mindset
- protected-branch workflow
- contributor/contractor simulation
- Git mistake recovery
- interview explanation under pressure
- maintainable incremental framework development

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

## 2. Active Source Documents to Continue Considering

The next thread should keep these uploaded source/context documents in mind:

```text
mozilla_round2_technical_prep_roadmap.md
mozilla_firefox_interview_thread_knowledge_context.md
framework_v2_implementation_guide.md
gitea_workflow_progress_context.md
current_selenium_pytest_framework_context.md
framework_v2_remaining_pr11_pr20_roadmap.md
framework_v2_current_context_pr10_ready_for_pr11.md
```

### Source document roles

| Document | Purpose |
|---|---|
| `mozilla_round2_technical_prep_roadmap.md` | Overall Mozilla Round 2 prep plan: Python, Selenium/Pytest, PR review, CI/CD, interview fluency. |
| `mozilla_firefox_interview_thread_knowledge_context.md` | Mozilla role/interview context, Round 1 questions, role expectations, answer narratives. |
| `framework_v2_implementation_guide.md` | Main implementation plan for SauceDemo Selenium/Pytest + Gitea PR review lab. |
| `gitea_workflow_progress_context.md` | Local Gitea setup, multi-developer workflow, permissions, branch protection, PR simulation. |
| `current_selenium_pytest_framework_context.md` | Snapshot of older Selenium Python Hybrid Framework for comparison and familiarity. |
| `framework_v2_remaining_pr11_pr20_roadmap.md` | Remaining roadmap from PR11 to PR20. |
| `framework_v2_current_context_pr10_ready_for_pr11.md` | Previous handoff file from PR10, now superseded by this PR14-ready context. |

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
| `qa-contractor-1` | Contributor | Handles odd-numbered PRs in the current rotation. |
| `qa-contractor-2` | Contributor | Handles even-numbered PRs in the current rotation. |

### Contributor rotation so far

| PR range | Rotation pattern |
|---|---|
| PR1–PR14 | `qa-contractor-1` generally handles odd PRs and `qa-contractor-2` handles even PRs. |
| Next PR | PR15 should be handled by `qa-contractor-1`. |

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

Important reminder from earlier debugging:

- PyCharm/terminal interpreter should be checked so each clone ideally uses its own `.venv`.
- Previous context noted a situation where terminal execution path and `.venv` path belonged to different contractor clones.

---

## 6. Current Git Workflow for Future PRs

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

### Sync all clones after PR14 merge

Run in each clone:

```powershell
git checkout main
git pull origin main
git fetch --prune origin
pytest -v
```

For the contributor that created PR14 (`qa-contractor-2`), delete the local PR14 branch after merge if safe:

```powershell
git branch -d feature/add-remove-cart-item-test
```

---

## 7. Completed PRs So Far

| PR | Branch | Contributor | Status | Main purpose |
|---:|---|---|---|---|
| PR1 | `feature/framework-skeleton` | `qa-contractor-1` | Merged | Framework skeleton, folders, pytest config, requirements, config placeholder. |
| PR2 | `feature/add-browser-fixture` | `qa-contractor-2` | Merged | Browser fixture, config reader, expanded config, smoke setup test. |
| PR3 | `feature/add-base-page` | `qa-contractor-1` | Merged | BasePage with explicit wait helpers and reusable Selenium actions. |
| PR4 | `feature/add-login-page-and-smoke-test` | `qa-contractor-2` | Merged | LoginPage + first valid login smoke/regression test. |
| PR5 | `feature/add-inventory-page-smoke-test` | `qa-contractor-1` | Merged | InventoryPage, logged-in inventory fixture, inventory product-list test, LoginPage returns InventoryPage. |
| PR6 | `feature/add-cart-badge-smoke-test` | `qa-contractor-2` | Merged | Cart badge smoke test: add one inventory item and verify badge count is `1`. |
| PR7 | `feature/add-negative-login-parametrization` | `qa-contractor-1` | Merged | Added `login_page` fixture, refactored login flow, negative login parametrization. |
| PR8 | `feature/add-json-login-data` | `qa-contractor-2` | Merged | Moved negative login cases to JSON and used readable parametrized case IDs. |
| PR9 | `feature/add-screenshot-on-failure` | `qa-contractor-1` | Merged | Added screenshot utility and Pytest hook/fixture teardown integration for failed tests. |
| PR10 | `feature/add-basic-logging` | `qa-contractor-2` | Merged | Added basic framework logging to `reports/logs/test_run.log`. |
| PR11 | `feature/add-allure-reporting` | `qa-contractor-1` | Merged | Added minimal Allure reporting support via `allure-pytest`. |
| PR12 | `feature/add-excel-data-provider` | `qa-contractor-2` | Merged | Added Excel data provider and Excel-driven negative login tests. |
| PR13 | `feature/add-cart-page-validation` | `qa-contractor-1` | Merged | Added CartPage and cart item validation. |
| PR14 | `feature/add-remove-cart-item-test` | `qa-contractor-2` | Merged | Added remove item from cart test. |

---

## 8. Current Expected Test Counts After PR14

Exact counts should be confirmed by running the commands, but based on the current PR additions:

```text
pytest -v                 → expected around 14 passed
pytest -m smoke -v        → expected around 4 selected
pytest -m regression -v   → expected around 13 selected
pytest -m negative -v     → expected around 8 selected
pytest -m data_driven -v  → expected around 8 selected
pytest -m e2e -v          → expected 0 selected until PR15
```

Reasoning:

- PR10 baseline had 8 tests.
- PR12 added 4 Excel-driven negative login cases.
- PR13 added 1 cart item visibility test.
- PR14 added 1 cart removal test.

So the expected total is approximately:

```text
8 + 4 + 1 + 1 = 14 tests
```

---

## 9. Expected Current Folder Structure After PR14

The exact folder tree should be verified in the repo, but after PR14 the project should roughly contain:

```text
saucedemo-pytest-automation/
├── config/
│   └── config.json
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
├── tests/
│   ├── __init__.py
│   ├── test_smoke_setup.py
│   ├── test_login.py
│   ├── test_inventory.py
│   └── test_cart.py
├── test_data/
│   ├── login_data.json
│   └── login_data.xlsx
├── utils/
│   ├── __init__.py
│   ├── config_reader.py
│   ├── json_reader.py
│   ├── excel_reader.py
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

Not yet implemented:

```text
pages/checkout_page.py
tests/test_checkout.py
pages/menu_component.py
docs/PR_REVIEW_CHECKLIST.md
docs/TEST_STRATEGY.md
docs/INTERVIEW_EXPLANATION_NOTES.md
```

---

## 10. Important Current Files and Code Shape

### 10.1 `utils/excel_reader.py` — added in PR12

Expected shape:

```python
from pathlib import Path

from openpyxl import load_workbook


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def read_excel_as_dicts(file_path: str | Path, sheet_name: str) -> list[dict]:
    """
    Read an Excel sheet and return rows as dictionaries.

    The first row is treated as the header row.
    Empty cells are converted to empty strings for easier test usage.
    """
    workbook_path = PROJECT_ROOT / file_path
    workbook = load_workbook(workbook_path)
    sheet = workbook[sheet_name]

    rows = list(sheet.iter_rows(values_only=True))
    headers = rows[0]

    data = []
    for row in rows[1:]:
        row_data = {
            header: "" if value is None else value
            for header, value in zip(headers, row)
        }
        data.append(row_data)

    return data
```

Key design choices:

- Excel file does **not** need to be converted into an Excel Table.
- The first row is treated as the header row by our reader function.
- Empty Excel cells are returned by `openpyxl` as `None`, so the reader converts `None` to `""`.
- This prevents Selenium `send_keys()` issues when negative login cases intentionally use empty username/password values.

---

### 10.2 `tests/test_login.py` — updated in PR12

PR12 added Excel-based negative login testing inside the existing `tests/test_login.py`, rather than creating a separate `tests/test_login_excel.py` file.

Expected pattern:

```python
from utils.excel_reader import read_excel_as_dicts


NEGATIVE_LOGIN_EXCEL_DATA = read_excel_as_dicts(
    "test_data/login_data.xlsx",
    "negative_login"
)
```

Example Excel-driven test shape:

```python
@pytest.mark.data_driven
@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.parametrize(
    "login_case",
    NEGATIVE_LOGIN_EXCEL_DATA,
    ids=[case["case_id"] for case in NEGATIVE_LOGIN_EXCEL_DATA]
)
def test_invalid_login_from_excel_shows_error(login_page, login_case):
    login_page.attempt_login(
        login_case["username"],
        login_case["password"]
    )

    actual_error = login_page.get_error_message()

    assert login_case["expected_error"] in actual_error
```

Discussion decision:

- Keep JSON negative login tests and Excel negative login tests separate test functions.
- Do not combine success and negative cases into one Excel test with branching.
- Avoid test logic like `if expected_result == "success"` in PR12 because it makes the parametrized test less clean.

---

### 10.3 `pages/cart_page.py` — added in PR13 and updated in PR14

Expected shape after PR14:

```python
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

    CART_CONTAINER = (By.ID, "cart_contents_container")
    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BACKPACK_BUTTON = (By.ID, "remove-sauce-labs-backpack")

    def is_loaded(self) -> bool:
        return self.is_visible(self.CART_CONTAINER)

    def get_cart_item_names(self) -> list[str]:
        items = self.driver.find_elements(*self.CART_ITEM_NAMES)
        return [item.text for item in items]

    def has_product(self, product_name: str) -> bool:
        return product_name in self.get_cart_item_names()

    def remove_backpack(self):
        self.click(self.REMOVE_BACKPACK_BUTTON)
```

Important PR13 lesson:

```python
return [items.text for item in items]
```

is incorrect because `items` is a list and a list has no `.text` attribute.

Correct:

```python
return [item.text for item in items]
```

Here:

- `items` = list of WebElements.
- `item` = one WebElement inside the loop.
- `item.text` extracts visible text from each element.

---

### 10.4 `pages/inventory_page.py` — updated in PR13

PR13 added navigation from InventoryPage to CartPage.

Expected pattern:

```python
from pages.cart_page import CartPage
```

Expected method:

```python
def go_to_cart(self):
    self.click(self.SHOPPING_CART_LINK)
    return CartPage(self.driver, timeout=self.timeout)
```

Important design choice:

- `go_to_cart()` returns `CartPage` because clicking the cart link transitions the user to the cart page.
- This follows the same page-object transition idea as `LoginPage.login() -> InventoryPage`.

---

### 10.5 `tests/test_cart.py` — updated in PR13 and PR14

Expected current shape:

```python
import pytest

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage


BACKPACK_PRODUCT_NAME = "Sauce Labs Backpack"


def add_backpack_and_open_cart(
    logged_in_inventory_page: InventoryPage
) -> CartPage:
    logged_in_inventory_page.add_backpack_to_cart()
    cart_page = logged_in_inventory_page.go_to_cart()

    assert cart_page.is_loaded()

    return cart_page


@pytest.mark.smoke
@pytest.mark.regression
def test_add_one_item_to_cart_updates_badge(logged_in_inventory_page):
    logged_in_inventory_page.add_backpack_to_cart()

    cart_badge_count = logged_in_inventory_page.get_cart_badge_count()

    assert cart_badge_count == "1", (
        f"Expected cart badge count to be '1' after adding one item, "
        f"but found '{cart_badge_count}'."
    )


@pytest.mark.smoke
@pytest.mark.regression
def test_added_item_is_visible_in_cart(logged_in_inventory_page):
    cart_page = add_backpack_and_open_cart(logged_in_inventory_page)

    assert cart_page.has_product(BACKPACK_PRODUCT_NAME)


@pytest.mark.regression
def test_remove_item_from_cart_removes_product(logged_in_inventory_page):
    cart_page = add_backpack_and_open_cart(logged_in_inventory_page)

    assert cart_page.has_product(BACKPACK_PRODUCT_NAME)

    cart_page.remove_backpack()

    assert not cart_page.has_product(BACKPACK_PRODUCT_NAME)
```

Important PR14 decision:

- Do **not** call one test function from another test function.
- Extract repeated setup flow into a small helper function instead.
- This keeps tests independent while avoiding duplication.

Important PyCharm lesson:

- PyCharm autocomplete was weak inside helper function because the fixture parameter looked like a plain untyped object.
- Adding type hints helped:

```python
def add_backpack_and_open_cart(
    logged_in_inventory_page: InventoryPage
) -> CartPage:
```

Benefits:

- better IDE autocomplete
- better static analysis
- improved readability for future reviewers

---

### 10.6 `requirements.txt` — updated in PR11 and maybe PR12

Expected current dependency set should include at least:

```text
selenium
pytest
openpyxl
allure-pytest
```

Notes:

- `allure-pytest` enables Pytest to generate Allure result files when running with `--alluredir`.
- `allure-pytest` does **not** automatically generate reports for normal `pytest -v` runs.
- Allure CLI is separately required to render/serve the visual report.

Basic Allure commands:

```powershell
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

`conftest.py` is not needed for basic Allure report generation. It is only needed for custom attachments/metadata such as screenshots, logs, labels, or dynamic metadata.

---

## 11. PR11 Summary — Minimal Allure Reporting Support

### Contributor

```text
qa-contractor-1
```

### Branch

```text
feature/add-allure-reporting
```

### Status

```text
Merged
```

### Purpose

Add minimal Allure reporting support.

### Main discussion decisions

- Basic Allure reporting does **not** require code in `conftest.py`.
- Adding `allure-pytest` enables Pytest to generate Allure result files when run with `--alluredir`.
- `pytest -v` alone does not generate Allure result files.
- `pytest --alluredir=reports/allure-results` generates result files.
- `allure serve reports/allure-results` requires Allure CLI and opens the browser report.
- Screenshot attachments are not part of PR11.
- README update was considered optional because README is planned for major rewrite in PR20.

### Validation

```powershell
pytest -v
pytest --alluredir=reports/allure-results
```

Expected result after PR11 baseline:

```text
8 passed
```

### Interview explanation

> In PR11, I added basic Allure reporting support by adding the Allure Pytest plugin. I kept the PR minimal because Allure can generate structured test results without custom framework code. Screenshot attachments can be added later as a separate focused enhancement.

---

## 12. PR12 Summary — Excel Data Provider

### Contributor

```text
qa-contractor-2
```

### Branch

```text
feature/add-excel-data-provider
```

### Status

```text
Merged
```

### Files likely touched

```text
utils/excel_reader.py
test_data/login_data.xlsx
tests/test_login.py
requirements.txt  # only if openpyxl was missing
```

### Purpose

Add Excel-based data-driven negative login testing.

### Important decisions

- Excel tests were added inside existing `tests/test_login.py` instead of creating a separate `tests/test_login_excel.py`.
- This keeps related login tests together.
- Excel file does not need to be converted into an Excel Table.
- The first row is treated as the header row by our reader function.
- Empty Excel cells are normalized from `None` to `""`.

### Key code explained

```python
row_data = {
    header: "" if value is None else value
    for header, value in zip(headers, row)
}
```

Meaning:

- `zip(headers, row)` pairs each header with the corresponding cell value.
- `header` becomes the dictionary key.
- `value` becomes the dictionary value.
- If the Excel cell is empty and openpyxl returns `None`, store `""` instead.

Equivalent beginner-friendly version:

```python
row_data = {}

for header, value in zip(headers, row):
    if value is None:
        row_data[header] = ""
    else:
        row_data[header] = value
```

### Validation

```powershell
pytest tests/test_login.py -v
pytest -m data_driven -v
pytest -m negative -v
pytest -v
```

Expected after PR12:

```text
pytest -v                → around 12 passed
pytest -m data_driven -v → around 8 selected
pytest -m negative -v    → around 8 selected
```

### Interview explanation

> In PR12, I added Excel-based data-driven login validation inside the existing login test file. I kept it as a separate test function from the JSON-driven negative login test, so the two data-source approaches are easy to compare. Excel is useful because many QA teams are comfortable maintaining tabular test data, while JSON remains cleaner for developer-oriented review.

---

## 13. PR13 Summary — CartPage and Cart Item Validation

### Contributor

```text
qa-contractor-1
```

### Branch

```text
feature/add-cart-page-validation
```

### Status

```text
Merged
```

### Files touched

```text
pages/inventory_page.py
pages/cart_page.py
tests/test_cart.py
```

### Purpose

Move beyond badge-only validation and verify that the actual product appears in the cart.

Flow added:

```text
log in
→ add Sauce Labs Backpack
→ go to cart
→ verify CartPage is loaded
→ verify Sauce Labs Backpack is present
```

### Key implementation points

- Added `CartPage`.
- Added `InventoryPage.go_to_cart()`.
- `go_to_cart()` returns a `CartPage` object.
- `CartPage` explicitly calls `super().__init__(driver, timeout)` for consistency with the framework’s page object pattern.
- `get_cart_item_names()` returns text from WebElements.

### Git mistake and recovery

During PR13, development accidentally started on local `main` and the PR13 commit was created on `main`.

Recovery approach:

```powershell
git checkout -b feature/add-cart-page-validation
git log --oneline --decorate --graph -5
git checkout main
git reset --hard origin/main
git checkout feature/add-cart-page-validation
git push origin feature/add-cart-page-validation
```

Why this works:

- Branches are pointers to commits.
- Creating the feature branch first preserves the accidental commit.
- Resetting local `main` back to `origin/main` cleans `main` without deleting the feature branch commit.

### Interview explanation

> Earlier, the framework only validated that the cart badge updated. In PR13, I added a CartPage so the test can verify the actual cart contents. This is a stronger user-flow assertion because it confirms the selected product is really present in the cart. I kept cart-specific locators and actions inside CartPage, while the test remains readable as a user scenario.

---

## 14. PR14 Summary — Remove Item from Cart Test

### Contributor

```text
qa-contractor-2
```

### Branch

```text
feature/add-remove-cart-item-test
```

### Status

```text
Merged
```

### Files touched

```text
pages/cart_page.py
tests/test_cart.py
```

### Purpose

Add regression coverage for removing an item from the cart.

Flow added:

```text
log in
→ add Sauce Labs Backpack
→ go to cart
→ verify backpack exists
→ remove backpack
→ verify backpack no longer exists
```

### Main design decision

The remove test reused much of the setup from `test_added_item_is_visible_in_cart`. Instead of calling one test from another, the repeated setup flow was extracted into a helper function:

```python
def add_backpack_and_open_cart(
    logged_in_inventory_page: InventoryPage
) -> CartPage:
    logged_in_inventory_page.add_backpack_to_cart()
    cart_page = logged_in_inventory_page.go_to_cart()

    assert cart_page.is_loaded()

    return cart_page
```

Why this is better:

- Tests remain independent.
- No test depends on another test’s execution.
- Duplication is reduced.
- The helper represents setup/precondition, not test behavior.
- Type hints improve PyCharm autocomplete and reviewer readability.

### Marker decision

PR14 test should be:

```python
@pytest.mark.regression
```

It should not be smoke by default because badge and cart visibility already cover the critical cart path. Remove-from-cart is useful regression coverage, not necessarily a build-validation smoke check.

### Interview explanation

> In PR14, I added regression coverage for removing an item from the cart. PR13 verified that an added item appears in the cart; PR14 completes that cart behavior by verifying the user can remove the item and the cart state updates correctly. I avoided calling one test from another and instead extracted the repeated setup into a helper function, keeping the tests independent and readable.

---

## 15. Generated Artifacts and `.gitignore`

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
- Local screenshots/logs/Allure result files may remain on disk after pull/merge.
- Before committing, always run:

```powershell
git status
git status --ignored
```

---

## 16. Recommended Next PR: PR15

### Recommended PR title

```text
Add CheckoutPage and successful checkout flow
```

### Recommended branch

```text
feature/add-checkout-success-flow
```

### Recommended contributor

```text
qa-contractor-1
```

Reason: PR14 was done by `qa-contractor-2`, so rotate back to `qa-contractor-1`.

### Goal

Add a successful checkout end-to-end flow.

### Files likely touched

```text
pages/cart_page.py
pages/checkout_page.py
tests/test_checkout.py
```

Possibly touched:

```text
pages/inventory_page.py
```

### Suggested PR15 tasks

- Add checkout button action to `CartPage`.
- Add `CheckoutPage`.
- Add methods for:
  - entering customer information
  - continuing checkout
  - finishing checkout
  - reading/verifying success message
- Add successful checkout test.

### Suggested validation

```powershell
pytest tests/test_checkout.py -v
pytest -m e2e -v
pytest -v
```

Optional Allure result generation check:

```powershell
pytest --alluredir=reports/allure-results
```

### Marker recommendation

```python
@pytest.mark.e2e
@pytest.mark.regression
```

Possibly smoke if the test remains stable and fast, but the safer recommendation is `e2e` + `regression`.

### Avoid in PR15

```text
negative checkout validation
sorting
logout
Allure screenshot attachments
large checkout abstraction
```

### PR15 definition of done

```text
[ ] CheckoutPage added.
[ ] CartPage can click checkout and return CheckoutPage.
[ ] Successful checkout flow test added.
[ ] Test validates final success message/state.
[ ] `e2e` marker is registered in pytest.ini if not already.
[ ] `pytest tests/test_checkout.py -v` passes.
[ ] `pytest -m e2e -v` passes.
[ ] `pytest -v` passes.
```

### PR15 interview explanation target

> I added the complete checkout flow as an end-to-end regression test. This validates the main SauceDemo purchase journey while keeping the page interactions separated across InventoryPage, CartPage, and CheckoutPage.

---

## 17. Final Current Status Summary

```text
Current milestone: PR14 completed and merged.

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
  - add backpack to cart and verify cart badge
  - verify added item is visible in cart through CartPage
  - remove backpack from cart and verify it is gone
  - run negative login tests with parametrization
  - load negative login data from JSON
  - load negative login data from Excel
  - show readable parametrized case IDs in Pytest output
  - capture screenshots automatically on test failure
  - write framework logs to reports/logs/test_run.log
  - generate basic Allure result files using allure-pytest

Current tests:
  - setup/environment validation
  - standard user login smoke/regression
  - inventory product-list smoke/regression
  - cart badge smoke/regression
  - cart item visibility smoke/regression
  - cart item removal regression
  - JSON-driven negative login regression/data-driven tests
  - Excel-driven negative login regression/data-driven tests

Expected current validation:
  pytest -v → around 14 passed

Next milestone:
  PR15 successful checkout E2E flow.

Recommended next contributor:
  qa-contractor-1.

Recommended next branch:
  feature/add-checkout-success-flow.
```

