"""
Test that an empty string will throw an error
"""

from lib.is_task import *
import pytest

def test_empty_string_raises_error():
    with pytest.raises(Exception) as e:
        is_task("")
    error_message = str(e.value)
    assert error_message == "I need a string to check!"

""""
Given a non-string (e.g. integer) throw an error
"""

# is_task(1) => RAISES ERROR ("I need a string to check!")

def test_non_string_raises_error():
    with pytest.raises(Exception) as e:
        is_task(1)
    error_message = str(e.value)
    assert error_message == "I need a string to check!"

"""""
Given string contains "#TODO", returns TRUE
"""

# is_task("#TODO buy milk") => TRUE

def test_contains_todo_returns_true():
    assert is_task("#TODO buy milk") == True

"""
Given string doesn't contain "#TODO", returns FALSE
"""
# is_task("hello WoRLD") => FALSE

def test_doesnt_contain_todo_returns_false():
     assert is_task("buy milk") == False

"""
Given a string that contains '#todo', returns FALSE
"""
# is_task("todo buy milk") => FALSE

def test_lowercase_returns_false():
        assert is_task("#todo buy milk") == False
