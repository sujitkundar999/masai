import string
from src.utils import clean_text, average

def test_clean_text_basic():
    assert clean_text("Hello, World!") == "hello world"
    assert clean_text("  Spaces   here!! ") == "spaces here"

def test_clean_text_punctuations():
    punct = string.punctuation
    assert clean_text(f"keep words{punct}") == "keep words"

def test_average_numbers():
    assert average([1, 2, 3, 4]) == 2.5
    assert average([10]) == 10

def test_average_empty_list():
    assert average([]) == 0
