# Day 1 — Block 2 Python Warm-Up Interview Notes

**Preparation context:** Mozilla Firefox Software Test Engineering Student Worker — Round 2 technical deep-dive preparation  
**Block focus:** Python warm-up through small, interview-style problems  
**Goal:** Build calm Python fluency, explain reasoning clearly, connect coding exercises to QA automation work

---

## 1. Why This Block Matters

This block was not meant to be heavy DSA practice. The goal was practical coding fluency for QA automation interviews.

The problems focused on:

- loops
- conditions
- functions
- strings
- lists
- dictionaries
- sets
- edge cases
- early return
- simple optimization
- explaining code clearly

For a Mozilla-style technical deep dive, the important part is not only solving the problem, but explaining:

1. what the function receives,
2. what it returns,
3. the main logic,
4. edge cases,
5. why the approach is useful in QA automation.

---

## 2. Problem 1 — Check if a Number Is Prime

### Problem

Write a function that returns `True` if a number is prime and `False` otherwise.

```python
def is_prime(num):
    ...
```

Example expected outputs:

```python
is_prime(1)   # False
is_prime(2)   # True
is_prime(3)   # True
is_prime(4)   # False
is_prime(9)   # False
is_prime(11)  # True
```

---

### Concepts Discussed

#### Prime number

A prime number:

- is greater than 1,
- is divisible only by 1 and itself.

Important edge case:

```python
1
```

is **not** prime.

---

#### Modulus operator `%`

The modulus operator gives the remainder after division.

```python
10 % 2 == 0
```

means 10 is divisible by 2.

For prime checking:

```python
num % i == 0
```

means:

> `num` is divisible by `i`, so it is not prime.

---

#### Python `for` loop

Basic structure:

```python
for item in collection:
    # do something
```

For prime checking:

```python
for i in range(2, num):
```

means:

> Try every possible divisor from 2 up to `num - 1`.

---

#### `range()`

```python
range(2, 11)
```

produces:

```python
2, 3, 4, 5, 6, 7, 8, 9, 10
```

Important:

> `range()` includes the start value but excludes the stop value.

---

#### Factors

A factor is a number that divides another number evenly.

Example: factors of 12:

```text
1, 2, 3, 4, 6, 12
```

Because:

```python
12 % 1 == 0
12 % 2 == 0
12 % 3 == 0
12 % 4 == 0
12 % 6 == 0
12 % 12 == 0
```

---

#### Why check only up to square root?

For 36, factor pairs are:

```text
1 × 36
2 × 18
3 × 12
4 × 9
6 × 6
```

After `6 × 6`, the pairs repeat in reverse:

```text
9 × 4
12 × 3
18 × 2
36 × 1
```

So if a number has a divisor larger than its square root, it must also have a paired divisor smaller than the square root.

Therefore:

> If no divisor is found up to `sqrt(num)`, no later divisor is needed.

---

#### Exponent operator `**`

In Python:

```python
2 ** 3
```

means:

```text
2 × 2 × 2 = 8
```

So:

```python
num ** 0.5
```

means square root of `num`.

Examples:

```python
36 ** 0.5  # 6.0
25 ** 0.5  # 5.0
11 ** 0.5  # 3.316...
```

---

#### Why `+1` is needed

Because `range()` excludes the stop value.

If:

```python
sqrt(36) = 6
```

then:

```python
range(2, 6)
```

checks only:

```python
2, 3, 4, 5
```

It misses 6.

So we use:

```python
range(2, int(num ** 0.5) + 1)
```

This includes the square-root boundary.

---

#### Early return / early exit

If we find one divisor, we immediately know the number is not prime.

So we can return immediately:

```python
if num % i == 0:
    return False
```

This avoids unnecessary checks.

Interview explanation:

> Once I find that the number is divisible by another number, I do not need to check further. I can return `False` immediately.

---

### Mistakes / Questions From Practice

#### Initial edge case issue

At first, `is_prime(1)` was considered `True`, but it should be `False`.

Learning:

> 1 is not prime because a prime number must be greater than 1 and have exactly two divisors: 1 and itself.

---

#### Loop variable mistake

Initial code used:

```python
if num % 2 == 0:
```

inside the loop.

But it should use the loop variable:

```python
if num % i == 0:
```

Learning:

> Inside the loop, `i` changes each iteration, so `num % i` checks each possible divisor.

This is similar to automation bugs where a value is accidentally hardcoded instead of using a variable.

---

### Final Naive Version

```python
def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True
```

---

### Final Optimized Version

```python
def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True
```

---

### Interview Explanation

> I first handle numbers less than or equal to 1 because they are not prime. Then I check divisibility from 2 up to the square root of the number. If any divisor gives remainder 0, I return `False` immediately. If the loop completes without finding any divisor, I return `True`. I only check up to the square root because any larger factor would already have a smaller paired factor.

---

### QA Automation Relevance

This problem practices:

- loop logic,
- condition checking,
- early return,
- edge-case handling,
- optimization reasoning.

QA examples:

- stop a retry loop once an action succeeds,
- stop validation once a critical failure is found,
- avoid unnecessary checks in test utilities,
- classify data quickly based on conditions.

---

## 3. Problem 2 — Reverse a String Manually

### Problem

Reverse a string without using slicing like `[::-1]`.

Example:

```python
reverse_string("hello")
```

Expected result:

```python
"olleh"
```

---

### Manual Thinking

The intuitive idea was:

> Start from the last character and put one letter after another.

For `"hello"`, the building process is:

```text
o
ol
oll
olle
olleh
```

---

### Concepts Discussed

#### Strings are iterable

Python can loop through a string character by character.

```python
word = "hello"

for char in word:
    print(char)
```

Output:

```text
h
e
l
l
o
```

---

#### Indexing

Each character in a string has a position.

For:

```python
word = "hello"
```

indexes are:

```text
h -> 0
e -> 1
l -> 2
l -> 3
o -> 4
```

Important:

> Python indexing starts at 0.

---

#### `len()`

```python
len("hello")
```

returns:

```python
5
```

The last index is:

```python
len(word) - 1
```

For `"hello"`:

```python
5 - 1 = 4
```

---

#### `range(start, stop, step)`

For reverse looping:

```python
range(len(val) - 1, -1, -1)
```

For `"hello"`, this gives indexes:

```python
4, 3, 2, 1, 0
```

---

#### Why stop value is `-1`

Because `range()` excludes the stop value.

To include index `0`, the stop value must be one less than 0:

```python
-1
```

---

#### Step `-1`

```python
step = -1
```

means:

> go backward one step each time.

---

### Final Version

```python
def reverse_string(val):
    new_str = ""

    for i in range(len(val) - 1, -1, -1):
        new_str += val[i]

    return new_str


print(reverse_string("hello"))
```

Expected output:

```text
olleh
```

---

### Important Improvement: Return Instead of Print

Initial version printed the reversed string inside the function.

Better interview/utility style:

```python
return new_str
```

Why?

Because returned values can be reused:

```python
result = reverse_string("hello")
assert result == "olleh"
```

This is closer to QA automation utility design.

---

### Interview Explanation

> I create an empty result string. Then I loop from the last index of the input string down to index 0 using `range(start, stop, step)`. In each iteration, I add the current character to the result. Finally, I return the reversed string.

---

### QA Automation Relevance

This problem practices:

- string indexing,
- reverse iteration,
- building output step by step,
- utility function design,
- returning values for assertions.

QA examples:

- UI text manipulation,
- validating transformed strings,
- checking formatting logic,
- writing reusable helper functions,
- preparing values before assertions.

---

## 4. Problem 3 — Count Character Frequency

### Problem

Count how many times each character appears in a string.

Example:

```python
count_char_frequency("hello")
```

Expected result:

```python
{
    "h": 1,
    "e": 1,
    "l": 2,
    "o": 1
}
```

For:

```python
"banana"
```

Expected result:

```python
{
    "b": 1,
    "a": 3,
    "n": 2
}
```

---

### Concepts Discussed

#### Dictionary

A dictionary stores key-value pairs.

Example:

```python
student = {
    "name": "Abrar",
    "age": 28
}
```

Here:

- `"name"` is a key,
- `"Abrar"` is a value.

For character frequency:

- character = key,
- count = value.

Example:

```python
{
    "a": 3
}
```

means:

> character `"a"` appeared 3 times.

---

#### Empty dictionary

```python
freq = {}
```

This starts with an empty dictionary.

---

#### Checking if a key exists

```python
if char in freq:
```

means:

> Does this character already exist as a key in the dictionary?

Example:

```python
freq = {
    "a": 2,
    "b": 1
}

print("a" in freq)  # True
print("x" in freq)  # False
```

---

#### Increasing a count

```python
freq[char] += 1
```

means:

```python
freq[char] = freq[char] + 1
```

---

### Logic

For each character:

```python
if character already exists in dictionary:
    increase count
else:
    add character with count 1
```

---

### Final Version

```python
def check_frequency(val):
    freq = {}

    for c in val:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

    return freq


print(check_frequency("banana"))
```

Expected output:

```python
{'b': 1, 'a': 3, 'n': 2}
```

---

### Interview Explanation

> I use a dictionary where each character is the key and its frequency is the value. I loop through the string. If the character already exists in the dictionary, I increment its count. If it does not exist, I add it with count 1. At the end, I return the dictionary.

---

### Questions From Practice

#### Question

How do we check whether a character already exists in a dictionary?

#### Answer

Use:

```python
if char in freq:
```

This checks whether `char` exists as a key in the dictionary.

---

### QA Automation Relevance

This problem is highly useful for QA automation because dictionaries are common in:

- JSON/API response validation,
- test result summaries,
- counting pass/fail statuses,
- log analysis,
- error frequency reports,
- configuration handling,
- data-driven testing.

QA examples:

```python
{
    "passed": 42,
    "failed": 3,
    "skipped": 5
}
```

or:

```python
{
    "ERROR": 12,
    "WARN": 7,
    "INFO": 31
}
```

---

## 5. Problem 4 — Remove Duplicates While Preserving Order

### Problem

Remove duplicate values from a list while keeping the first occurrence order.

Example:

```python
remove_duplicates([1, 2, 2, 3, 1, 4])
```

Expected result:

```python
[1, 2, 3, 4]
```

Another example:

```python
["apple", "banana", "apple", "orange", "banana"]
```

Expected result:

```python
["apple", "banana", "orange"]
```

---

### Initial Intuitive Solution

The initial idea was:

```python
new_list = []

for i in values:
    if i not in new_list:
        new_list.append(i)
```

This is valid.

It works because:

- `new_list` stores the final result,
- before adding an item, we check whether it is already there.

---

### Simple Version

```python
def remove_duplicates(values):
    new_list = []

    for i in values:
        if i not in new_list:
            new_list.append(i)

    return new_list
```

This is easy to understand and acceptable for small lists.

---

### Optimized Version With `set()`

```python
def remove_duplicate(values):
    result = []
    seen = set()

    for i in values:
        if i not in seen:
            result.append(i)
            seen.add(i)

    return result


print(remove_duplicate([1, 2, 2, 3, 1, 4]))
```

Expected output:

```python
[1, 2, 3, 4]
```

---

### Concepts Discussed

#### Why two structures?

The optimized version uses two structures:

```python
result = []
seen = set()
```

#### `result`

Purpose:

> Keep the final output in the original order.

Example:

```python
[1, 2, 3, 4]
```

#### `seen`

Purpose:

> Quickly remember what has already appeared.

Example:

```python
{1, 2, 3, 4}
```

---

#### What is `set()`?

A set is a collection, but unlike a list:

| Feature | List | Set |
|---|---|---|
| Keeps order for output use | Yes | Not something to rely on here |
| Allows duplicates | Yes | No |
| Access by index | Yes | No |
| Lookup speed | Slower | Faster |

Example:

```python
my_list = [1, 2, 2, 3]
print(my_list)
```

Output:

```python
[1, 2, 2, 3]
```

But:

```python
my_set = {1, 2, 2, 3}
print(my_set)
```

Output:

```python
{1, 2, 3}
```

Duplicate `2` is removed automatically.

---

#### Set does not support index access

This works:

```python
my_list[0]
```

This does not work:

```python
my_set[0]
```

So for this problem:

```python
result = []     # preserves order
seen = set()    # fast duplicate lookup
```

---

### Interview Explanation

> I can solve this in a simple way using only a result list and checking whether each item already exists in that list. For better performance, I use a set called `seen` to track items that already appeared, because set lookup is faster. I still use a list called `result` to preserve the original order of first occurrences.

---

### QA Automation Relevance

This problem practices:

- list handling,
- duplicate detection,
- set usage,
- preserving order,
- performance-aware thinking.

QA examples:

- removing duplicate test cases from a selected suite,
- detecting duplicate IDs in API responses,
- cleaning repeated test data,
- summarizing unique error messages,
- avoiding duplicate bug reports,
- validating uniqueness constraints.

---

## 6. Key Python Concepts Learned Today

### Loops

Used to process items one by one.

```python
for item in values:
```

---

### `range()`

Used to generate number sequences.

```python
range(start, stop, step)
```

Important:

> stop value is excluded.

---

### Modulus `%`

Used to check divisibility.

```python
num % i == 0
```

---

### Early Return

Return as soon as the answer is known.

```python
return False
```

inside a loop can avoid unnecessary work.

---

### Strings and Indexes

Strings can be accessed by index.

```python
word[0]
```

---

### `len()`

Returns the length of a string/list.

```python
len("hello")  # 5
```

---

### Dictionaries

Store key-value pairs.

```python
freq = {
    "a": 3
}
```

---

### Checking Dictionary Keys

```python
if key in dictionary:
```

---

### Sets

Useful for fast lookup and duplicate tracking.

```python
seen = set()
```

---

### `append()`

Adds an item to a list.

```python
result.append(item)
```

---

### `add()`

Adds an item to a set.

```python
seen.add(item)
```

---

## 7. Personal Questions and Confusions Captured

These are valuable because they show exactly where concepts became clear.

### Question 1

> What are factors?

Learning:

> Factors are numbers that divide another number evenly without remainder.

---

### Question 2

> What does `**` represent in Python?

Learning:

> `**` means exponent/power. `num ** 0.5` means square root.

---

### Question 3

> Why is `+1` needed in `range()`?

Learning:

> Because `range()` excludes the stop value, so `+1` is needed when we want to include the square-root boundary.

---

### Question 4

> How does a Python `for` loop work?

Learning:

> A `for` loop takes each item from a collection one by one and performs logic on it.

---

### Question 5

> How do we check if a key exists in a dictionary?

Learning:

> Use `if key in dictionary:`.

---

### Question 6

> Is `set()` like a list?

Learning:

> A set is a collection like a list, but it does not allow duplicates, does not support index access, and is useful for fast lookup.

---

## 8. Interview Patterns to Use

### Pattern for Explaining a Coding Problem

Use this structure:

1. Restate the problem.
2. Mention input and output.
3. Explain edge cases.
4. Explain the main logic.
5. Write code.
6. Test with examples.
7. Connect to QA automation if relevant.

---

### Good Phrase for Simple-to-Optimized Progression

> I would first write a simple correct version, then optimize it once the logic is clear.

This is useful for prime checking and duplicate removal.

---

### Good Phrase for Mistakes During Coding

> I noticed I accidentally hardcoded a value instead of using the loop variable. I would correct it by using the variable that changes in each iteration.

This is a healthy debugging response.

---

### Good Phrase for QA Connection

> This small coding exercise is useful for QA automation because similar logic appears in test utilities, report parsing, data validation, retry handling, and result summarization.

---

## 9. Day 1 Block 2 Summary

Completed problems:

1. Prime number check
2. Reverse string manually
3. Count character frequency
4. Remove duplicates while preserving order

Main concepts learned:

- `for` loops
- `range()`
- modulo `%`
- factors
- square-root optimization
- exponent operator `**`
- string indexing
- `len()`
- dictionaries
- key existence checks
- sets
- duplicate tracking
- early return
- returning values from utility functions

Most important improvement:

> The focus shifted from just writing code to explaining logic, edge cases, tradeoffs, and QA automation relevance.

That is exactly the type of communication needed for a practical QA automation technical deep dive.

---

## 10. Quick Revision Checklist

Before the next session, review these questions:

- Why is 1 not prime?
- Why can prime checking stop at the square root?
- What does `%` do?
- What does `**` do?
- Why does `range()` need `+1` sometimes?
- Why does `range(len(word) - 1, -1, -1)` include index 0?
- What is a dictionary?
- How do you check if a key exists in a dictionary?
- What is a set?
- Why use both `result` and `seen` for duplicate removal?
- Why should utility functions return values instead of only printing?

---

## 11. Practice Again Later

Re-solve these without looking:

```python
def is_prime(num):
    pass


def reverse_string(val):
    pass


def check_frequency(val):
    pass


def remove_duplicate(values):
    pass
```

Then explain each function aloud in 60 seconds.
