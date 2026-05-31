# Mozilla Firefox Round 2 Prep — Day 2 Part 1 Interview Notes

**Topic:** Python Coding Practice Warm-Up  
**Context:** Firefox Software Test Engineering Student Worker — Round 2 technical preparation  
**Focus:** Practical Python for QA automation, test result processing, data normalization, duplicate detection, and interview explanation fluency.

---

## 1. Why This Part Matters

The Day 2 warm-up was intentionally started with practical Python problems to shift into implementation mode before Selenium/Pytest framework work.

The goal was not advanced DSA. The goal was to build confidence in:

- writing small Python utilities,
- explaining logic clearly,
- handling edge cases,
- debugging simple mistakes,
- connecting code to QA automation scenarios,
- thinking like someone who can maintain an automation framework.

This matters for the Mozilla Firefox role because the likely Round 2 technical deep dive may evaluate practical Python, Selenium/Pytest reasoning, automation framework maintainability, and communication under pressure.

---

## 2. Coding Practice Pattern Used

For each problem, the intended solving pattern was:

1. Restate the problem.
2. Identify input/output examples.
3. Mention edge cases.
4. Write pseudocode or mental steps.
5. Implement.
6. Run manual tests.
7. Explain how it relates to QA automation.
8. Add a small PR-review/maintainability reflection.

### Key Interview Habit

Before coding, spend 30 seconds confirming the problem requirement.

This became especially important during the duplicate-values problem, where the initial confusion was about whether the first occurrence should be appended or only the repeated occurrence.

---

# Problem 1 — Normalize Strings Before Comparison

## Problem Statement

Write a function that compares two strings after normalizing them.

Normalization means:

- trim leading/trailing spaces,
- convert to lowercase,
- collapse repeated internal spaces into one space.

Example:

```python
normalize_and_compare("  Login   Successful ", "login successful")
# True
```

---

## Concepts Discussed

### Useful Python String Cleaning Methods

```python
text.strip()        # removes leading/trailing spaces
text.lower()        # converts to lowercase
text.upper()        # converts to uppercase
text.casefold()     # stronger lowercase, useful for international text
text.split()        # splits by whitespace and removes repeated spaces
" ".join(words)     # joins strings with a single space separator
text.replace(a, b)  # replaces characters/substrings
```

### Important Note About `split()`

```python
text.split()
```

without arguments splits on any whitespace and automatically handles:

- multiple spaces,
- tabs,
- newlines.

Example:

```python
text = "  Login   Successful "
text.split()
# ["Login", "Successful"]
```

---

## Explanation of `" ".join(...)`

`" ".join(...)` takes a list of strings and joins them using a single space as the separator.

Example:

```python
words = ["login", "successful"]
result = " ".join(words)

print(result)
# login successful
```

Other separators are also possible:

```python
"-".join(["a", "b", "c"])
# "a-b-c"

",".join(["a", "b", "c"])
# "a,b,c"
```

For normalization:

```python
text = "  Login   Successful "
cleaned = " ".join(text.strip().lower().split())

print(cleaned)
# login successful
```

---

## User's Initial Solution

```python
def normalize_string(str1, str2):
    cleaned_str1 = " ".join(str1.strip().lower().split())
    cleaned_str2 = " ".join(str2.strip().lower().split())

    if cleaned_str1 == cleaned_str2:
        return True
    else:
        return False

print(normalize_string("   hello", "hello       1"))
```

This correctly returns:

```python
False
```

because:

```python
"hello" != "hello 1"
```

---

## Polished Version

```python
def normalize_and_compare(str1, str2):
    cleaned_str1 = " ".join(str1.strip().lower().split())
    cleaned_str2 = " ".join(str2.strip().lower().split())

    return cleaned_str1 == cleaned_str2
```

### Why This Is Cleaner

The comparison itself already returns `True` or `False`, so this is unnecessary:

```python
if condition:
    return True
else:
    return False
```

---

## Manual Tests

```python
print(normalize_and_compare("   Hello   World ", "hello world"))
# True

print(normalize_and_compare("Login   Successful", " login successful "))
# True

print(normalize_and_compare("hello", "hello 1"))
# False
```

---

## QA Automation Connection

In UI automation, direct text comparison can be brittle when the application introduces harmless formatting differences.

Example:

```python
"Login   Successful"
```

versus:

```python
"login successful"
```

The actual content is the same, but raw comparison may fail.

Normalization helps reduce false failures caused by:

- extra spaces,
- inconsistent casing,
- formatting variation.

---

## Interview Explanation

> I normalized both strings by trimming whitespace, lowercasing, and collapsing repeated spaces before comparison. This avoids false failures when UI text has harmless formatting differences but the meaningful content is the same.

---

## PR Review Reflection

If this utility appeared in an automation framework PR, check:

- Is the function name clear?
- Does it return a boolean consistently?
- Is normalization logic easy to understand?
- Should it handle `None` defensively?
- Is this function reusable in UI/API text assertions?

---

# Problem 2 — Check If Two Strings Are Anagrams

## Problem Statement

Write a function that returns `True` if two strings are anagrams.

An anagram means two words or strings contain the same letters with the same frequency, but in a different order.

Examples:

| String 1 | String 2 | Anagram? | Reason |
|---|---|---:|---|
| `listen` | `silent` | Yes | same letters |
| `evil` | `vile` | Yes | same letters |
| `triangle` | `integral` | Yes | same letters |
| `hello` | `world` | No | different letters |
| `apple` | `apply` | No | different letters/frequency |

---

## Concepts Discussed

### Step 1 — Clean Both Strings

For anagram checking, remove spaces completely and lowercase:

```python
cleaned = "".join(text.lower().split())
```

### Why `"" .join(...)` Instead of `" ".join(...)`?

For normalized text comparison, spaces should be collapsed into one space:

```python
" ".join(...)
```

For anagram checking, spaces should be removed completely:

```python
"".join(...)
```

Example:

```python
text = "Rail Safety"
cleaned = "".join(text.lower().split())

print(cleaned)
# railsafety
```

---

## Dictionary Comparison in Python

Two dictionaries are equal if:

- they have the same keys,
- and the same values for those keys.

Order does not matter.

Example:

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 2, "a": 1}

print(dict1 == dict2)
# True
```

This makes dictionaries useful for frequency-map comparison.

---

## First Attempt and Debugging Moment

Initial logic was mostly correct, but the second loop accidentally iterated over the empty dictionary instead of the second cleaned string:

```python
for c in char_count_2:
```

Since `char_count_2` was empty, the loop never executed.

Correct loop:

```python
for c in cleaned_str2:
```

### Lesson

This was a realistic debugging issue: the algorithm was right, but the wrong variable was used in a loop.

Interviewers often care less about writing perfect code instantly and more about whether you can understand and fix bugs calmly.

---

## Refactored Final Version With Helper Function

```python
def dict_builder(val):
    freq = {}

    for c in val:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

    return freq


def check_anagram(str1, str2):
    cleaned_str1 = "".join(str1.lower().split())
    cleaned_str2 = "".join(str2.lower().split())

    if len(cleaned_str1) != len(cleaned_str2):
        return False

    return dict_builder(cleaned_str1) == dict_builder(cleaned_str2)


print(check_anagram("rail safety", "fairy tales"))
# True
```

---

## Why the Helper Function Is Good

The helper function avoids duplicating the frequency-map building logic.

This improves:

- readability,
- maintainability,
- reusability,
- PR-review quality.

---

## QA Automation Connection

Anagram checking itself may not be a common QA task, but the underlying skill is very useful:

- building frequency maps,
- comparing transformed data,
- checking expected vs actual content where order may not matter,
- validating generated or transformed test data.

---

## Interview Explanation

> I first normalized both strings by removing spaces and converting them to lowercase. Then I checked if their lengths were equal. If not, they cannot be anagrams. After that, I built frequency dictionaries for both strings and compared the dictionaries. If the character counts match, the strings are anagrams.

---

## PR Review Reflection

Good points:

- normalization handled,
- length check avoids unnecessary work,
- helper function removes duplication,
- dictionary comparison is clean.

Possible improvements:

- function name `dict_builder` could be more specific, such as `build_frequency_map`,
- optional defensive handling for `None`,
- optional handling of punctuation if required.

Suggested naming improvement:

```python
def build_frequency_map(text):
    ...
```

---

# Problem 3 — Find Duplicate Values in a List

## Problem Statement

Given a list, return duplicate values only once.

Example:

```python
find_duplicates(["login", "search", "login", "cart", "search"])
# ["login", "search"]
```

Important: The first occurrence is not returned. A value is added to the result only when it appears again.

---

## Concepts Discussed

### List Syntax

Lists use square brackets:

```python
items = [1, 2, 3]
empty_list = []
```

### Curly Braces

Curly braces are used for dictionaries and sets.

Dictionary:

```python
person = {
    "name": "Abrar",
    "role": "QA"
}
```

Set:

```python
unique_values = {"a", "b", "c"}
```

Important gotcha:

```python
{}
```

creates an empty dictionary, not an empty set.

Empty set:

```python
set()
```

---

## Checking If a List Is Empty

```python
if not items:
    return []
```

Why it works:

- empty lists are falsy,
- non-empty lists are truthy.

Examples:

```python
bool([])
# False

bool(["a"])
# True
```

For this problem, an empty list should return an empty duplicate list:

```python
find_duplicates([])
# []
```

However, an explicit empty-list check is not strictly necessary because if the loop does not run, the result stays empty.

---

## Why Use `seen`, `duplicates`, and `result`?

```python
seen = set()
duplicates = set()
result = []
```

Each has a different purpose.

| Variable | Purpose |
|---|---|
| `seen` | tracks values encountered at least once |
| `duplicates` | tracks values already reported as duplicates |
| `result` | preserves ordered output |

---

## Key Conceptual Clarification

At first, it seemed like `seen` might be enough.

But consider:

```python
items = ["login", "login", "login"]
```

Using only `seen` could produce:

```python
["login", "login"]
```

because the second and third `"login"` are both already seen.

But the desired result is:

```python
["login"]
```

So `duplicates` prevents adding the same duplicate multiple times.

---

## Difference Between `seen` and `duplicates`

```text
seen = item appeared at least once
duplicates = item appeared at least twice and was already added to result
```

Example:

```python
items = ["a", "b", "a"]
```

After processing first `"a"`:

```python
seen = {"a"}
duplicates = set()
result = []
```

At this point:

```python
"a" in seen        # True
"a" in duplicates  # False
```

When second `"a"` appears:

```python
"a" in seen        # True
"a" not in duplicates # True
```

So we append `"a"` and record it as already reported.

---

## Set Behavior

A set cannot store duplicate values.

Example:

```python
items = set()

items.add("login")
items.add("login")
items.add("login")

print(items)
# {"login"}
```

If a value already exists in a set, adding it again is simply ignored. It does not replace anything.

---

## Time Complexity Discussion

### List Membership

```python
if item in result:
```

For a list, Python may scan the whole list.

Average/worst-case lookup:

```text
O(n)
```

If used inside a loop, total can become:

```text
O(n²)
```

### Set Membership

```python
if item in seen:
```

Set lookup is average:

```text
O(1)
```

Looping through all items gives:

```text
O(n)
```

Space complexity is:

```text
O(n)
```

because seen/duplicates may store values.

---

## Final User Solution

```python
def find_duplicate(items):
    result = []
    seen = set()
    duplicates = set()

    if not items:
        return items
    else:
        for i in items:
            if i in seen:
                if i not in duplicates:
                    result.append(i)
                    duplicates.add(i)
            else:
                seen.add(i)
        return result

print(find_duplicate(["a", "b", "a", "a", "b", "c", "d", "e", "e"]))
```

Expected output:

```python
["a", "b", "e"]
```

---

## Polished Version

```python
def find_duplicates(items):
    result = []
    seen = set()
    duplicates = set()

    for item in items:
        if item in seen:
            if item not in duplicates:
                result.append(item)
                duplicates.add(item)
        else:
            seen.add(item)

    return result


print(find_duplicates(["a", "b", "a", "a", "b", "c", "d", "e", "e"]))
# ["a", "b", "e"]
```

### Why This Version Is Cleaner

No explicit empty-list check is needed.

For:

```python
[]
```

the loop does not run and `result` remains:

```python
[]
```

---

## QA Automation Connection

This type of helper is useful for:

- detecting duplicate test data,
- finding duplicate IDs in API responses,
- validating repeated UI labels,
- checking duplicate test names,
- validating configuration lists.

---

## Interview Explanation

> I used a `seen` set to track values already encountered, a `duplicates` set to avoid adding the same duplicate more than once, and a result list to preserve the order of duplicate detection. This keeps membership checks efficient and returns each duplicate only once.

---

## PR Review Reflection

Review points:

- Does the function name clearly describe the output?
- Does it consistently return a list?
- Is the output order meaningful?
- Does the implementation avoid unnecessary nested complexity?
- Are sets used appropriately for efficient lookup?

Possible improvement:

```python
def find_duplicates(items):
```

is a better name than:

```python
def find_duplicate(items):
```

because the function may return multiple duplicates.

---

# Problem 4 — Count Failed Test Statuses

## Problem Statement

Given a list of test result dictionaries, count how many tests failed.

Example:

```python
results = [
    {"name": "test_login", "status": "passed"},
    {"name": "test_search", "status": "failed"},
    {"name": "test_checkout", "status": "failed"},
]

count_failed_tests(results)
# 2
```

---

## Concepts Discussed

### The Input Is a List of Dictionaries

The attempted loop caused this error:

```text
TypeError: list indices must be integers or slices, not str
```

because the outer structure was a list, not a dictionary.

Input:

```python
[
    {"name": "test_login", "status": "passed"},
    {"name": "test_search", "status": "failed"},
    {"name": "test_checkout", "status": "failed"},
]
```

Correct approach:

```python
for item in results:
    print(item["name"], ":", item["status"])
```

Each `item` is one dictionary.

---

## Looping Through a Dictionary

If working with one dictionary:

```python
test = {"name": "test_login", "status": "passed"}
```

You can loop through keys:

```python
for key in test:
    print(key, test[key])
```

Or key-value pairs:

```python
for key, value in test.items():
    print(key, value)
```

But for this problem, the first loop must be over the list:

```python
for item in results:
    status = item.get("status", "").lower()
```

---

## Why Use `.get("status", "")`?

```python
item.get("status", "")
```

means:

> Get the value for `"status"`. If `"status"` does not exist, return an empty string instead of crashing.

Example:

```python
item = {"name": "test_login"}

print(item.get("status", ""))
# ""
```

Without `.get()`:

```python
item["status"]
```

would raise:

```text
KeyError: 'status'
```

The empty string default is useful because:

```python
status = item.get("status", "").lower()
```

Even if `"status"` is missing:

```python
"".lower()
```

is safe.

---

## Final User Solution

```python
def count_failed_test(result):
    count = 0

    for i in result:
        status = i.get("status", "").lower()

        if status == "failed":
            count += 1

    return count

print(count_failed_test([
    {"name": "test_login", "status": "passed"},
    {"name": "test_search", "status": "failed"},
    {"name": "test_checkout", "status": "failed"},
]))
```

Expected output:

```python
2
```

---

## Polished Version

```python
def count_failed_tests(results):
    count = 0

    for item in results:
        status = item.get("status", "").lower()

        if status == "failed":
            count += 1

    return count
```

### Naming Note

Use plural names when the input contains multiple items:

```python
results
```

instead of:

```python
result
```

---

## QA Automation Connection

This is directly related to:

- CI result summarization,
- test report parsing,
- automation dashboards,
- quick failure statistics,
- build health checks.

---

## Interview Explanation

> I loop through each test result dictionary, safely read the status using `.get()`, normalize it to lowercase, and increment the count when the status is failed. This is useful for summarizing CI or automation report results.

---

# Bonus Problem — Return Failed Test Names

## Problem Statement

Return the names of failed tests from a list of test result dictionaries.

Example:

```python
results = [
    {"name": "test_login", "status": "passed"},
    {"name": "test_search", "status": "failed"},
    {"name": "test_checkout", "status": "failed"},
]

get_failed_test_names(results)
# ["test_search", "test_checkout"]
```

---

## User's Combined Solution

The solution returned both count and failed test names.

```python
def count_failed_test(result):
    count = 0
    failed_test_case_names = []

    for i in result:
        status = i.get("status", "").lower()

        if status == "failed":
            count += 1
            failed_test_case_names.append(i.get("name"))

    return count, failed_test_case_names

print(count_failed_test([
    {"name": "test_login", "status": "passed"},
    {"name": "test_search", "status": "failed"},
    {"name": "test_checkout", "status": "failed"},
]))
```

Expected output:

```python
(2, ["test_search", "test_checkout"])
```

---

## Polished Version

```python
def summarize_failed_tests(results):
    count = 0
    failed_test_case_names = []

    for item in results:
        status = item.get("status", "").lower()

        if status == "failed":
            count += 1
            failed_test_case_names.append(item.get("name", "unknown_test"))

    return count, failed_test_case_names
```

### Why Use `"unknown_test"`?

```python
item.get("name", "unknown_test")
```

prevents `None` from appearing in the output if a failed test dictionary has no name.

---

## QA Automation Connection

Returning both count and failed names is practical because:

- the count gives a quick summary,
- the names tell the team where to investigate,
- this resembles CI failure summaries or monitoring dashboards.

---

## Interview Explanation

> I return both the failed count and failed test names because in automation reporting, the count gives a quick health summary while the names help the team immediately identify which tests need investigation.

---

# Python Concepts Covered in Part 1

## String Methods

| Method | Purpose |
|---|---|
| `strip()` | remove leading/trailing whitespace |
| `lower()` | convert to lowercase |
| `upper()` | convert to uppercase |
| `casefold()` | stronger lowercase for international text |
| `split()` | split text into words/parts |
| `join()` | join list items into a string |
| `replace()` | replace substring/characters |

---

## Collections

| Type | Syntax | Use |
|---|---|---|
| List | `[]` | ordered collection, allows duplicates |
| Dictionary | `{key: value}` | key-value mapping |
| Set | `{"a", "b"}` or `set()` | unique values, fast membership checks |

---

## Common Python Patterns Practiced

### Direct Boolean Return

```python
return cleaned_str1 == cleaned_str2
```

instead of:

```python
if cleaned_str1 == cleaned_str2:
    return True
else:
    return False
```

### Safe Dictionary Access

```python
status = item.get("status", "").lower()
```

### Empty List Handling

```python
if not items:
    return []
```

or simply return the initialized result after loop.

### Frequency Map

```python
freq = {}

for c in text:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1
```

### Duplicate Detection

```python
seen = set()
duplicates = set()
result = []
```

---

# Main Strengths Observed

## 1. Strong Questioning

Good questions were asked about:

- why `join()` works,
- how dictionary comparison works,
- why two sets are needed,
- whether list membership has worse complexity,
- how sets behave when adding duplicate values,
- why `.get()` uses a default value.

This is good interview behavior because it shows curiosity and reasoning.

---

## 2. Debugging Awareness

The anagram bug was caused by iterating over the wrong variable:

```python
for c in char_count_2:
```

Instead of:

```python
for c in cleaned_str2:
```

The issue was identified and fixed. This shows the ability to debug implementation mistakes calmly.

---

## 3. Maintainability Instinct

The anagram solution was refactored with a helper function.

This is relevant to framework design and PR review because automation code should avoid duplication and be readable for teammates.

---

## 4. QA Automation Framing

Each problem was connected back to practical QA use cases:

- normalized string comparison → UI assertion reliability,
- anagram/frequency maps → transformed data comparison,
- duplicate detection → test data/API validation,
- failed test count/name summary → CI/reporting.

---

# Improvement Areas

## 1. Restate the Problem Before Coding

The duplicate-values problem initially caused confusion because the requirement was not fully internalized.

Recommended habit:

> Before coding, say: “The first occurrence is only remembered. The value is returned only when it appears again.”

This prevents solving the wrong problem.

---

## 2. Use More Descriptive Names

Examples:

Instead of:

```python
def dict_builder(val):
```

Prefer:

```python
def build_frequency_map(text):
```

Instead of:

```python
def count_failed_test(result):
```

Prefer:

```python
def count_failed_tests(results):
```

Descriptive names are especially important in automation framework PRs.

---

## 3. Keep Return Types Consistent

For helper functions, consistent return types make framework code easier to use.

Example:

```python
find_duplicates([])
# []
```

not:

```python
None
```

or an error.

---

## 4. Consider Defensive Input Handling Later

For interview warm-up, normal inputs are fine.

For production-quality framework utilities, consider:

- `None` inputs,
- missing keys,
- unexpected types,
- malformed data.

Example:

```python
def normalize_and_compare(str1, str2):
    if str1 is None or str2 is None:
        return False

    ...
```

Do not over-engineer unless the requirement asks for it.

---

# Interview-Ready Mini Answers

## Normalize Strings

> I normalize both strings by trimming spaces, converting to lowercase, and collapsing repeated whitespace. This avoids false failures in UI assertions when formatting changes but the meaningful content stays the same.

## Anagram

> I clean both strings by lowercasing and removing spaces. Then I build character frequency dictionaries and compare them. If the dictionaries match, the strings contain the same characters with the same counts.

## Duplicate Values

> I use a `seen` set to remember values already encountered, a `duplicates` set to avoid reporting the same duplicate multiple times, and a result list to preserve output order.

## Count Failed Tests

> I loop through the list of test result dictionaries, safely read the status using `.get()`, normalize it to lowercase, and count the entries where the status is failed.

## Return Failed Test Names

> I collect failed test names into a list while counting failures, which gives both a quick summary and actionable details for CI/debugging.

---

# Final Part 1 Summary

Day 2 Part 1 successfully covered practical Python coding for QA automation. The warm-up included string normalization, frequency-map comparison, duplicate detection with sets, and test-result summarization with dictionaries.

The most valuable outcomes were:

- stronger practical Python fluency,
- better understanding of lists/dicts/sets,
- improved defensive coding with `.get()`,
- awareness of time complexity with sets vs lists,
- debugging a wrong-loop-variable issue,
- refactoring with helper functions,
- connecting each coding task to automation framework/reporting scenarios.

The next section should build on this momentum by moving into the Selenium-Pytest framework walkthrough, especially `conftest.py`, BasePage, browser setup/teardown, waits, config handling, and failure artifacts.
