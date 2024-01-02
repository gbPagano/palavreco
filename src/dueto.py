import random
from collections import defaultdict
from enum import Enum

from rich import print
from rich.align import Align
from rich.columns import Columns
from rich.console import Console, Group
from rich.live import Live
from rich.panel import Panel
from rich.rule import Rule
from rich.text import Text
from rich.traceback import install

install()

from termo import Termo
from utils import LetterPosition, get_click, remove_accents


class Dueto(Termo):
    def __init__(self):
        self.console = Console()

    @property
    def winner(self):
        board_1, board_2 = False, False
        for _, result in self.board_1:
            if all(letter == LetterPosition.correct for letter in result):
                board_1 = True
        for _, result in self.board_2:
            if all(letter == LetterPosition.correct for letter in result):
                board_2 = True

        self.borders[0] = "green" if board_1 else ""
        self.borders[1] = "green" if board_2 else ""
        return board_1 and board_2

    @property
    def game_is_over(self):
        if self.winner:
            return True
        elif (
            LetterPosition.empty not in self.board_1[-1][1]
            and LetterPosition.empty not in self.board_2[-1][1]
        ):
            return True
        return False

    def print_board(self, borders):
        self.console.rule("DUETO", style="red")
        board_1 = self._get_formated_board(self.board_1, borders[0])
        board_2 = self._get_formated_board(self.board_2, borders[1])

        self.console.print(Columns([board_1, board_2]), justify="center")

    def new_game(self):
        self.secret_words = self._get_random_word(), self._get_random_word()
        self.secret_words_unaccentuated = (
            remove_accents(
                self.secret_words[0]
            ),  # remove_accents(self.secret_words[1])
            "termo",
        )
        self.board_1 = [("_____", [LetterPosition.empty] * 5)] * 7
        self.board_2 = [("_____", [LetterPosition.empty] * 5)] * 7
        self.borders = ["", ""]

    def end(self):
        with self.console.screen():
            if self.winner:
                final_txt = Text("Parabéns você ganhou! As palavras eram: ")
            else:
                final_txt = Text("Que pena, você perdeu. As palavras eram: ")
                self.borders = ["red", "red"]

            final_txt.append(Text(self.secret_words[0], style="green"))
            final_txt.append(Text(" e "))
            final_txt.append(Text(self.secret_words[1], style="green"))
            self.print_board(self.borders)
            self.console.print(final_txt)
            input()

    def run(self):
        self.new_game()

        for move in range(7):
            with self.console.screen():
                self.print_board(self.borders)

                word = self.get_input_word()
                print(self.secret_words_unaccentuated[0])
                result = self.compare_words(word, self.secret_words_unaccentuated[0])
                result_2 = self.compare_words(word, self.secret_words_unaccentuated[1])
                if self.borders[0] != "green":
                    self.board_1[move] = (word, result)

                if self.borders[1] != "green":
                    self.board_2[move] = (word, result_2)

                if self.winner:
                    break

        self.end()
