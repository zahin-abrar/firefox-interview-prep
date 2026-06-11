# Framework V2 Current Context — PR18 Completed, Ready for PR19

**Project:** Mozilla Firefox Round 2 Technical Prep  
**Sub-project:** SauceDemo Selenium/Pytest Framework V2 + Gitea PR Review Lab  
**Current handoff purpose:** Use this file as the memory/context file for the next chat thread, starting with **PR19**.  
**Current state:** PR1–PR18 are completed and merged into `main`.  
**Latest validation:** `pytest -v` passed with **21 tests** after PR18 merge.  
**Next milestone:** PR19 — Add project documentation: PR review checklist, test strategy, and interview explanation notes.

---

## 1. Why This Project Exists

This project supports preparation for the **Mozilla Firefox Software Test Engineering Student Worker** technical deep-dive. It is intentionally more than a Selenium practice repository.

It practices:

- Python/Selenium/Pytest automation
- Page Object Model design
- Pytest fixtures and fixture composition
- explicit waits and stable Selenium interactions
- parametrization and readable Pytest case IDs
- JSON and Excel data-driven testing
- screenshot-on-failure support
- framework logging
- basic Allure report generation
- smoke/regression/negative/e2e marker strategy
- local Gitea protected-branch workflow
- contributor/contractor simulation
- PR review mindset
- Git mistake recovery
- interview explanation under pressure
- maintainable incremental framework development

The local Gitea workflow simulates:

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

This matches the Mozilla role context: reviewing automation PRs, supporting a contractor/manual QA team transitioning into automation, contributing to automation suites, and investigating/debugging automation failures.

---

## 2. Source Documents That Should Continue to Be Considered

The next thread should continue considering:

```text
mozilla_round2_technical_prep_roadmap.md
mozilla_firefox_interview_thread_knowledge_context.md
framework_v2_implementation_guide.md
gitea_workflow_progress_context.md
current_selenium_pytest_framework_context.md
framework_v2_remaining_pr11_pr20_roadmap.md
framework_v2_current_context_pr14_ready_for_pr15.md
```

Document roles:

| Document | Purpose |
|---|---|
| `mozilla_round2_technical_prep_roadmap.md` | Overall Mozilla Round 2 prep plan: Python, Selenium/Pytest, PR review, CI/CD, interview fluency. |
| `mozilla_firefox_interview_thread_knowledge_context.md` | Mozilla role/interview context, Round 1 questions, role expectations, answer narratives. |
| `framework_v2_implementation_guide.md` | Main implementation plan for SauceDemo Selenium/Pytest + Gitea PR review lab. |
| `gitea_workflow_progress_context.md` | Local Gitea setup, multi-developer workflow, permissions, branch protection, PR simulation. |
| `current_selenium_pytest_framework_context.md` | Snapshot of older Selenium Python Hybrid Framework for comparison and familiarity. |
| `framework_v2_remaining_pr11_pr20_roadmap.md` | Remaining roadmap from PR11 to PR20. |
| `framework_v2_current_context_pr14_ready_for_pr15.md` | Previous handoff file; superseded by this PR18-ready context file. |

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
| PR1–PR18 | `qa-contractor-1` handles odd PRs, `qa-contractor-2` handles even PRs. |
| Next PR | PR19 should be handled by `qa-contractor-1`. |

### Identity lesson to preserve

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

Reminder from previous debugging:

- Check PyCharm/terminal interpreter so each clone uses the intended `.venv`.
- A previous issue involved terminal execution path and `.venv` path belonging to different contractor clones.

---

## 6. Current Git Workflow for Future PRs

For each new PR:

```powershell
git checkout main
git pull origin main
git fetch --prune origin
git checkout -b feature-or-docs-branch-name
```

Implement and validate:

```powershell
pytest --collect-only
pytest -v
```

Commit and push:

```powershell
git status
git status --ignored
git add .
git commit -m "Clear meaningful commit message"
git push origin branch-name
```

Create PR in Gitea, review as `abrar`, merge, delete branch, and sync all clones.

After merge, run in all clones:

```powershell
git checkout main
git pull origin main
git fetch --prune origin
pytest -v
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
| PR15 | `feature/add-checkout-success-flow` | `qa-contractor-1` | Merged | Added CheckoutPage and successful checkout E2E flow. |
| PR16 | `feature/add-checkout-negative-tests` | `qa-contractor-2` | Merged | Added parametrized checkout form validation tests. |
| PR17 | `feature/add-inventory-sorting-tests` | `qa-contractor-1` | Merged | Added inventory sorting assertions for name A→Z and price low→high. |
| PR18 | `feature/add-logout-smoke-test` | `qa-contractor-2` | Merged | Added logout smoke/regression test. |

---

## 8. Current Expected Test Counts After PR18

Confirmed by user after PR18 merge:

```text
pytest -v → 21 passed
```

Expected marker behavior approximately:

```text
pytest -m smoke -v        → includes setup/login/inventory/cart/logout smoke tests
pytest -m regression -v   → broad suite including most framework tests
pytest -m negative -v     → login negative tests + checkout negative tests
pytest -m data_driven -v  → JSON + Excel login data-driven tests
pytest -m e2e -v          → successful checkout E2E test
```

Exact selected counts should be confirmed in the repo.

---

## 9. Expected Current Folder Structure After PR18

The exact folder tree should be verified in the repo, but after PR18 the project should roughly contain:

```text
saucedemo-pytest-automation/
├── config/
│   └── config.json
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── __init__.py
│   ├── test_smoke_setup.py
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_logout.py
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

Not yet implemented before PR19:

```text
docs/PR_REVIEW_CHECKLIST.md
docs/TEST_STRATEGY.md
docs/INTERVIEW_EXPLANATION_NOTES.md
```

Optional later but intentionally not added yet:

```text
pages/menu_component.py
```

---

## 10. Important Current Framework Capabilities

After PR18, the framework can:

- launch browser from fixture
- read JSON config
- open SauceDemo
- use `BasePage` explicit waits
- log in with standard user
- return `InventoryPage` after successful login
- use `login_page` fixture
- use `logged_in_inventory_page` fixture
- verify inventory list/product count
- add backpack to cart and verify cart badge
- open cart through `InventoryPage.go_to_cart()`
- validate item appears in cart through `CartPage`
- remove backpack from cart and verify it is gone
- start checkout from cart
- complete checkout successfully
- validate final checkout success message
- validate missing checkout fields with parametrization
- sort inventory by name A→Z
- sort inventory by price low→high
- log out from inventory page menu
- verify login page after logout
- run negative login tests with parametrization
- load negative login data from JSON
- load negative login data from Excel
- show readable parametrized case IDs in Pytest output
- capture screenshots automatically on test failure
- write framework logs to `reports/logs/test_run.log`
- generate basic Allure result files using `allure-pytest`

---

## 11. PR15 Summary — CheckoutPage and Successful Checkout Flow

### Contributor

```text
qa-contractor-1
```

### Branch

```text
feature/add-checkout-success-flow
```

### Status

```text
Merged
```

### Files touched

```text
pages/cart_page.py
pages/checkout_page.py
tests/test_checkout.py
```

### Purpose

Add a successful checkout end-to-end flow.

Flow:

```text
log in
→ add Sauce Labs Backpack
→ open cart
→ verify cart is loaded
→ verify product exists in cart
→ click checkout
→ enter first name, last name, postal code
→ continue
→ verify overview page
→ finish
→ verify checkout complete page and success message
```

### Marker decision

```python
@pytest.mark.e2e
@pytest.mark.regression
```

Not smoke by default, because checkout is longer than the smallest build-validation path.

### Important design choices

- `CartPage.checkout()` returns `CheckoutPage`, following the page-transition style already used by `LoginPage -> InventoryPage` and `InventoryPage -> CartPage`.
- `CheckoutPage` owns checkout-specific locators/actions.
- Assertions remain in the test layer.
- The helper `add_backpack_and_start_checkout()` was used to avoid repeating setup while keeping tests independent.

### Interview explanation

> In PR15, I added the first successful end-to-end checkout flow. The test starts from a logged-in inventory state, adds a product to the cart, verifies the cart precondition, enters checkout information, continues to the overview page, finishes the order, and validates the final success message. I kept checkout-specific locators and actions inside CheckoutPage, cart navigation inside CartPage, and assertions in the test layer so the scenario remains readable and maintainable.

---

## 12. PR16 Summary — Negative Checkout Validation Tests

### Contributor

```text
qa-contractor-2
```

### Branch

```text
feature/add-checkout-negative-tests
```

### Status

```text
Merged
```

### Files touched

```text
pages/checkout_page.py
tests/test_checkout.py
```

### Purpose

Add parametrized validation for required checkout customer information fields:

```text
missing first name
missing last name
missing postal code
```

### Marker decision

```python
@pytest.mark.negative
@pytest.mark.regression
```

Not `e2e`, because the purpose is checkout form validation, not successful full purchase flow.

### Implementation differences from original plan

The original plan suggested:

```python
ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
```

But the implemented version uses:

```python
ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")
```

Reason:

- User could not find `[data-test='error']` during implementation.
- `error-message-container` was available and used instead.

The original plan also suggested adding a wrapper method:

```python
submit_customer_information(...)
```

But this was **not implemented**.

Reason:

- `enter_customer_information(...)` and `continue_checkout()` already express the flow clearly.
- The test remains explicit and readable.
- Avoids premature abstraction.

Current test flow shape:

```python
def test_checkout_requires_customer_information(
    logged_in_inventory_page,
    first_name,
    last_name,
    postal_code,
    expected_error
):
    checkout_page = add_backpack_and_start_checkout(logged_in_inventory_page)

    checkout_page.enter_customer_information(
        first_name=first_name,
        last_name=last_name,
        postal_code=postal_code
    )

    checkout_page.continue_checkout()

    actual_error = checkout_page.get_error_message()

    assert actual_error == expected_error
```

### Parametrize IDs

The test uses:

```python
ids=[
    "missing-first-name",
    "missing-last-name",
    "missing-postal-code",
]
```

These IDs appear in Pytest output:

```text
test_checkout_requires_customer_information[missing-first-name]
test_checkout_requires_customer_information[missing-last-name]
test_checkout_requires_customer_information[missing-postal-code]
```

### Interview explanation

> In PR16, I added parametrized negative checkout validation for missing customer information fields. I kept the test data inline because there are only three cases. The test reuses the checkout setup from PR15, enters each missing-field combination, continues checkout, and verifies the exact validation message. I intentionally did not add a submit wrapper because the existing enter and continue methods already keep the flow clear.

---

## 13. PR17 Summary — Inventory Sorting Tests

### Contributor

```text
qa-contractor-1
```

### Branch

```text
feature/add-inventory-sorting-tests
```

### Status

```text
Merged
```

### Files touched

```text
pages/inventory_page.py
tests/test_inventory.py
```

### Purpose

Add regression coverage for inventory sorting:

```text
name A to Z
price low to high
```

### Marker decision

```python
@pytest.mark.regression
```

Not smoke, because sorting is useful regression coverage but not a critical build-validation path.

### Main implementation concepts

`InventoryPage` added methods/locators for:

```text
sort dropdown
product names
product prices
selecting sort option
extracting product names
extracting product prices
```

Likely locator/method pattern:

```python
from selenium.webdriver.support.ui import Select

SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")

def select_sort_option(self, value: str):
    sort_dropdown = self.find_visible(self.SORT_DROPDOWN)
    Select(sort_dropdown).select_by_value(value)

def sort_by_name_ascending(self):
    self.select_sort_option("az")

def sort_by_price_low_to_high(self):
    self.select_sort_option("lohi")

def get_product_names(self) -> list[str]:
    products = self.driver.find_elements(*self.PRODUCT_NAMES)
    return [product.text for product in products]

def get_product_prices(self) -> list[float]:
    prices = self.driver.find_elements(*self.PRODUCT_PRICES)
    return [
        float(price.text.replace("$", ""))
        for price in prices
    ]
```

### `Select` helper detail

The SauceDemo sort control is an HTML `<select>` element. Selenium’s `Select` helper is designed for this type of dropdown.

Example:

```python
sort_dropdown = self.find_visible(self.SORT_DROPDOWN)
Select(sort_dropdown).select_by_value("az")
```

Meaning:

- `find_visible(...)` waits until the dropdown is visible and returns the WebElement.
- `Select(sort_dropdown)` wraps the WebElement in Selenium’s dropdown helper.
- `select_by_value("az")` chooses the `<option>` whose `value` attribute is `"az"`.

For SauceDemo:

```text
az   → Name (A to Z)
za   → Name (Z to A)
lohi → Price (low to high)
hilo → Price (high to low)
```

### `sorted()` assertion detail

The tests use:

```python
assert actual_product_prices == sorted(actual_product_prices)
```

Meaning:

- `actual_product_prices` is the order shown in the UI.
- `sorted(actual_product_prices)` creates a new list sorted in ascending order.
- If both lists match, the UI is already sorted low to high.

`sorted()` is ascending by default.

For descending order, use:

```python
sorted(actual_product_prices, reverse=True)
```

### Interview explanation

> In PR17, I added inventory sorting validation to cover list-based UI behavior. The page object handles selecting sort options and extracting product names or prices, while the test layer asserts whether the displayed data is actually sorted. For prices, I remove the dollar sign and convert text into floats so the assertion checks numeric order instead of string order.

---

## 14. PR18 Summary — Logout Smoke Test

### Contributor

```text
qa-contractor-2
```

### Branch

```text
feature/add-logout-smoke-test
```

### Status

```text
Merged
```

### Final validation

```text
pytest -v → 21 passed
```

### Files touched

```text
pages/inventory_page.py
pages/login_page.py
tests/test_logout.py
```

### Purpose

Add logout coverage to complete the basic authenticated session lifecycle.

Flow:

```text
log in
→ inventory page
→ open side menu
→ click logout
→ verify login page is visible again
```

### Marker decision

```python
@pytest.mark.smoke
@pytest.mark.regression
```

### Design decision

Logout was kept inside `InventoryPage`, not moved into `menu_component.py`.

Reason:

- The menu is currently only used for logout.
- Creating `menu_component.py` now would be premature abstraction.
- It can be introduced later if more tests need the menu.

### Expected implementation shape

In `InventoryPage`:

```python
MENU_BUTTON = (By.ID, "react-burger-menu-btn")
LOGOUT_LINK = (By.ID, "logout_sidebar_link")

def open_menu(self):
    self.click(self.MENU_BUTTON)

def logout(self):
    self.open_menu()
    self.click(self.LOGOUT_LINK)
```

In `LoginPage`:

```python
def is_loaded(self) -> bool:
    return (
        self.is_visible(self.USERNAME_INPUT)
        and self.is_visible(self.PASSWORD_INPUT)
        and self.is_visible(self.LOGIN_BUTTON)
    )
```

In `tests/test_logout.py`:

```python
@pytest.mark.smoke
@pytest.mark.regression
def test_standard_user_can_logout(logged_in_inventory_page, driver, base_url):
    logged_in_inventory_page.logout()

    login_page = LoginPage(driver, base_url)

    assert login_page.is_loaded()
```

If the actual `LoginPage.__init__` does not require `base_url`, use `LoginPage(driver)`.

### Interview explanation

> In PR18, I added logout coverage as a smoke/regression test to complete the authenticated session lifecycle. The test starts from the logged-in inventory fixture, performs logout through the inventory page menu, and verifies that the login page is visible again. I kept the menu logic inside InventoryPage for now because it is only used in one place, avoiding premature abstraction.

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

- `.gitignore` prevents new matching files from being tracked.
- `.gitignore` does not delete local files.
- Local screenshots/logs/Allure result files may remain after pull/merge.
- Before committing, always run:

```powershell
git status
git status --ignored
```

---

## 16. Recommended Next PR: PR19

### Recommended PR title

```text
Add framework review and strategy documentation
```

### Recommended branch

```text
docs/add-framework-review-docs
```

### Recommended contributor

```text
qa-contractor-1
```

Reason: PR18 was done by `qa-contractor-2`, so rotate back to `qa-contractor-1`.

### Goal

Add documentation that supports interview explanation and PR review practice.

### Files to add

```text
docs/PR_REVIEW_CHECKLIST.md
docs/TEST_STRATEGY.md
docs/INTERVIEW_EXPLANATION_NOTES.md
```

### Scope

PR19 should be documentation-only.

Do not add:

```text
new tests
code changes
dependencies
large README rewrite
CI workflow
parallel execution
```

### Suggested validation

```powershell
git status
pytest -v
```

No test behavior should change.

### PR19 definition of done

```text
[ ] docs folder added if missing.
[ ] PR_REVIEW_CHECKLIST.md added.
[ ] TEST_STRATEGY.md added.
[ ] INTERVIEW_EXPLANATION_NOTES.md added.
[ ] No code behavior changed.
[ ] No generated files committed.
[ ] pytest -v still passes.
```

### PR19 interview explanation target

> I added documentation because framework quality is not only about code. A reviewer or new contributor should understand the test strategy, PR expectations, and design decisions. This is especially relevant when supporting a team that is transitioning from manual QA to automation.

---

## 17. PR19 Suggested Document Contents

### `docs/PR_REVIEW_CHECKLIST.md`

Include review points for:

```text
test value
test readability
Page Object Model structure
Selenium reliability
fixture usage
data/config handling
debug artifacts
maintainability
generated files
markers
assertions
test independence
```

### `docs/TEST_STRATEGY.md`

Include:

```text
why SauceDemo
why this framework exists
smoke vs regression vs negative vs e2e
current automated flows
which tests run in which suite
what is intentionally out of scope
how to choose new tests
future improvements
```

### `docs/INTERVIEW_EXPLANATION_NOTES.md`

Include:

```text
3-minute framework walkthrough
why Gitea
why SauceDemo
why POM
why fixtures
why BasePage
why hooks
why screenshots/logs
why Allure
why JSON and Excel
why markers
why parametrization
why Select helper
why sorted assertions
PR review mindset
how to help manual QA engineers transition to automation
what to improve next
```

---

## 18. Final Current Status Summary

```text
Current milestone:
  PR18 completed and merged.

Current validation:
  pytest -v → 21 passed.

Current framework ability:
  - setup/browser/config
  - POM with BasePage, LoginPage, InventoryPage, CartPage, CheckoutPage
  - login
  - inventory list validation
  - cart badge
  - cart page validation
  - cart item removal
  - successful checkout E2E
  - negative checkout validation
  - inventory sorting validation
  - logout
  - JSON data-driven tests
  - Excel data-driven tests
  - screenshots on failure
  - logs
  - basic Allure result generation
  - markers
  - parametrization
  - Gitea PR workflow simulation

Next milestone:
  PR19 project documentation.

Recommended next contributor:
  qa-contractor-1.

Recommended next branch:
  docs/add-framework-review-docs.

Remaining PRs:
  PR19 — docs
  PR20 — CI-ready cleanup and README finalization.
```
