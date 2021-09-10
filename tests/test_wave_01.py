import pytest
from count.count import count_a_letter

def test_non_alpha_letter_returns_none():
    test_sentence = "hello world"
    test_letter = "3"

    result = count_a_letter(test_sentence, test_letter)

    assert result is None

def test_empty_string_sentence_returns_none():
    test_sentence = ""
    test_letter = "e"

    result = count_a_letter(test_sentence, test_letter)

    assert result is None

def test_empty_list_sentence_returns_none():
    test_sentence = []
    test_letter = "e"

    result = count_a_letter(test_sentence, test_letter)

    assert result is None

