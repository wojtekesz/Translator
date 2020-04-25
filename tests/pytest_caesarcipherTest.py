import pytest
from pytest import fail

from caesarcipher.caesarcipher import CaesarCipher

# zbiór testów w postaci skryptu pytest

# fixture, czyli wcześniej przygotowany kawałek kodu do wielokrotnego uzycia
@pytest.fixture
def translator():
    translator = CaesarCipher()
    return translator

# test właściwy
def test_test_should_translate(translator):
    # given
    msg = "lokok"
    shift = 2

    # when
    result = translator.translate(msg, shift)

    # then
    assert result == "nqmqm"


def test_should_translate2(translator):
    # given
    msg = "whatever"
    shift = 3

    # when
    result = translator.translate(msg, shift)

    # then
    assert result == "zkdwhyhu"


def test_should_throw_exception(translator):
    # given

    # when
    with pytest.raises(Exception):
        translator.translate(None, None)

    # then


def test_should_translate_ignore(translator):
    # given
    msg = "KOT"
    shift = 2

    # when
    result = translator.translate_ignore_case(msg, shift)

    # then
    assert result == "mqv"


def test_should_check_not_translatable(translator):
    # given
    c = "#"

    # when
    result = translator.is_translatable(c)

    # then
    assert not result


def test_should_check_translatable(translator):
    # given
    c = "g"

    # when
    result = translator.is_translatable(c)

    # then
    assert result == True


def test_should_check_code_length(translator):
    # given

    # when
    size = translator.get_code_length()

    # then
    assert size == 26