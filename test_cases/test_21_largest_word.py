import importlib.util
from pathlib import Path

file_path = Path(__file__).parent.parent / "codes" / "21_largest_word.py"
spec = importlib.util.spec_from_file_location("largest_word_module", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
largest_word = module.largest_word

def test_simple_sentence():
    assert largest_word("I love programming") == "programming"


def test_single_word():
    assert largest_word("Python") == "Python"


def test_empty_sentence():
    assert largest_word("") == ""


def test_punctuation():
    assert largest_word("Hello, beautiful world!") == "beautiful"


def test_first_longest_word():
    assert largest_word("apple mango") == "apple"