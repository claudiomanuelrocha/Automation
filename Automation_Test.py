# content of test_verbosity_example.py
def test_1_ok():
    pass

def test_2_words_fail():
    fruits1 = ["banana", "apple", "grapes", "melon", "kiwi"]
    fruits2 = ["banana", "apple", "orange", "melon", "kiwi"]
    assert fruits1 == fruits2

def test_3_numbers_fail():
    number_to_text1 = {str(x): x for x in range(5)}
    number_to_text2 = {str(x * 10): x * 10 for x in range(5)}
    assert number_to_text1 == number_to_text2

def test_4_long_text_fail():
    long_text = "Lorem ipsum dolor sit amet " * 10
    assert "hello world" in long_text

####Adding a final line