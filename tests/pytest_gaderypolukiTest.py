import pytest
from pytest import fail

from gaderypoluki.gaderypoluki import GaDeRyPoLuKi

# zbiór testów w postaci skryptu pytest

# fixture, czyli wcześniej przygotowany kawałek kodu do wielokrotnego uzycia
@pytest.fixture
def translator():
    translator = GaDeRyPoLuKi()
    return translator

# test właściwy
def test_test_should_translate(translator):
    # given
    msg = "lok"

    # when
    result = translator.translate(msg)

    # then
    assert result == "upi"

# uwaga na klauzulę wyłączającą test

def test_should_stay_not_translated(translator):
    # given
    msg = "LOK"

    # when
    result = translator.translate(msg)

    # then
    assert result == "LOK"


def test_should_translate2(translator):
    # given
    msg = "whatever"

    # when
    result = translator.translate(msg)

    # then
    assert result == "whgtdvdy"


def test_should_throw_exception(translator):
    # given

    # when
    with pytest.raises(Exception):
        translator.translate(None)

    # then


def test_should_translate_ignore(translator):
    # given
    msg = "KOT"

    # when
    result = translator.translate_ignore_case(msg)

    # then
    assert result == "ipt"


def test_should_check_not_translatable(translator):
    # given
    c = "Z"

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
    assert size == 12
