# bonus
def test_non_string_letter_reports_error():
    test_sentence = "hello world"
    test_letter = 3

    with pytest.raises(AttributeError):
        count_a_letter(test_sentence, test_letter)
