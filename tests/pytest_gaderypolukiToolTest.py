import pytest

from gaderypoluki.gaderypoluki import GaDeRyPoLuKi


@pytest.fixture
def translator():
    translator = GaDeRyPoLuKi()
    return translator


# iteracja i kolejne wywołania testów
@pytest.mark.parametrize("test_input, expected", [
    ("ala", "gug"),
    ("gala", "agug"),
    ("kot", "ipt"),
    ("wonsz", "wpnsz"),
])
def test_should_translate(translator, test_input, expected):
    assert translator.translate(test_input) == expected
