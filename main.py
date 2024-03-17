
import pytest

# Тесты для структуры данных str:

def test_string_uppercase():
    test_string = "hello"
    assert test_string.upper() == "HELLO"

@pytest.mark.parametrize("test_string, expected_result", [("Hello", True), ("Hello123", False), ("123", False)])
def test_string_isalpha(test_string, expected_result):
    try:
        assert test_string.isalpha() == expected_result
    except AttributeError as e:
        pytest.fail(f"AttributeError: {e}")

@pytest.mark.parametrize("test_string, expected_result", [("   Hello   ", "Hello"), ("   World", "World"), ("Space   ", "Space")])
def test_string_strip(test_string, expected_result):
    assert test_string.strip() == expected_result@pytest.mark.parametrize("test_string, to_replace, replacement, expected_result", [("Hello, World!", "Hello", "Hi", "Hi, World!")])

def test_string_replace(test_string, to_replace, replacement, expected_result):
    assert test_string.replace(to_replace, replacement) == expected_result

# Тесты для структуры данных set:

@pytest.mark.parametrize("set1, set2, expected_result", [({1, 2, 3}, {3, 4, 5}, {1, 2, 3, 4, 5}), ({1, 2, 3}, {3, 4, 5, 6}, {1, 2, 3, 4, 5, 6})])
def test_set_union(set1, set2, expected_result):
    assert set1.union(set2) == expected_result@pytest.mark.parametrize("set1, set2, expected_result", [({1, 2, 3, 4, 5}, {2, 3}, True), ({1, 2, 3, 4, 5}, {6, 7}, False)])

def test_set_subset(set1, set2, expected_result):
    assert set2.issubset(set1) == expected_result@pytest.mark.parametrize("set1, set2, expected_result", [({1, 2, 3, 4, 5}, {2, 3}, True), ({2, 3}, {1, 2, 3, 4, 5}, False)])

def test_set_superset(set1, set2, expected_result):
    assert set1.issuperset(set2) == expected_result