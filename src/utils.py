from unicodedata import normalize
from sys import exit
from enum import Enum

import click


class LetterPosition(Enum):
    wrong = "red"
    correct = "green"
    almost = "yellow"
    empty = ""



def get_click() -> str | None:
    match click.getchar():
        case "\r":
            return "enter"
        case "\x1b[B" | "s" | "S":
            return "down"
        case "\x1b[A" | "w" | "W":
            return "up"
        case "\x1b[D" | "a" | "A":
            return "left"
        case "\x1b[C" | "d" | "D":
            return "right"
        case "\x1b" | "q" | "Q":
            exit()
        case _:
            return None

def remove_accents(word: str) -> str:
    return normalize("NFKD", word).encode("ASCII","ignore").decode("ASCII")