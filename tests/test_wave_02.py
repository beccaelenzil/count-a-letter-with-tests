import pytest
from count.count import count_a_letter

def test_string_with_no_matches_returns_0():
    test_sentence = "hello world"
    test_letter = "q"

    result = count_a_letter(test_sentence, test_letter)

    assert result == 0

def test_list_with_no_matches_returns_0():
    test_sentence = list("hello world")
    test_letter = "q"

    result = count_a_letter(test_sentence, test_letter)

    assert result == 0

def test_string_with_one_match_returns_1():
    test_sentence = "hello world"
    test_letter = "w"

    result = count_a_letter(test_sentence, test_letter)

    assert result == 1

def test_list_with_one_match_returns_1():
    test_sentence = list("hello world")
    test_letter = "w"

    result = count_a_letter(test_sentence, test_letter)

    assert result == 1

def test_string_with_multiple_matches_returns_count():
    test_sentence = "hello world"
    test_letter = "l"

    result = count_a_letter(test_sentence, test_letter)

    assert result == 3

def test_list_with_multiple_matches_returns_count():
    test_sentence = list("hello world")
    test_letter = "l"

    result = count_a_letter(test_sentence, test_letter)

    assert result == 3

def test_string_with_substring_returns_0():
    test_sentence = "hello world"
    test_letter = "ello"

    result = count_a_letter(test_sentence, test_letter)

    assert result == 0

def test_list_with_substring_returns_0():
    test_sentence = list("hello world")
    test_letter = "ello"

    result = count_a_letter(test_sentence, test_letter)

    assert result == 0
