# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can find my tasks among all my notes
I want to check if a line from my notes includes the string `#TODO`.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def is_task(note):
    """Extracts uppercase words from a string

    Parameters:
        note: a string containing words (e.g. "hello WORLD")

    Returns:
        a boolean, True or False

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Test that an empty string will throw an error
"""
is_task("") => RAISES ERROR ("I need a string to check!")

"""
Given a non-string (e.g. integer) throw an error
"""
is_task(1) => RAISES ERROR ("I need a string to check!")

"""
Given string contains "#TODO", returns TRUE
"""
is_task("#TODO buy milk") => TRUE

"""
Given string doesn't contain "#TODO", returns FALSE
"""
is_task("hello WoRLD") => FALSE

"""
Given a string that contains 'todo', returns FALSE
"""
is_task("todo buy milk") => FALSE

"""
Given a string that contains '#todo', returns FALSE
"""
is_task("#todo buy milk") => FALSE

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
