from src.termo import Termo
from src.utils import LetterPosition


def test_correct():
    termo = Termo()
    termo.secret_word_unaccentuated = "termo"
    result = termo.compare_word("termo")

    assert result == [LetterPosition.correct] * 5


def test_wrong():
    termo = Termo()
    termo.secret_word_unaccentuated = "termo"
    result = termo.compare_word("busca")

    assert result == [LetterPosition.wrong] * 5


def test_mixed():
    termo = Termo()
    termo.secret_word_unaccentuated = "termo"
    result = termo.compare_word("dueto")

    assert result == [
        LetterPosition.wrong,
        LetterPosition.wrong,
        LetterPosition.almost,
        LetterPosition.almost,
        LetterPosition.correct,
    ]


def test_amora_arara():
    termo = Termo()
    termo.secret_word_unaccentuated = "amora"
    result = termo.compare_word("arara")

    assert result == [
        LetterPosition.correct,
        LetterPosition.wrong,
        LetterPosition.wrong,
        LetterPosition.correct,
        LetterPosition.correct,
    ]


def test_sagaz_arara():
    termo = Termo()
    termo.secret_word_unaccentuated = "sagaz"
    result = termo.compare_word("arara")

    assert result == [
        LetterPosition.almost,
        LetterPosition.wrong,
        LetterPosition.almost,
        LetterPosition.wrong,
        LetterPosition.wrong,
    ]
