import random
from collections import defaultdict
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from tinydb import Query, TinyDB

from palavreco.utils import LetterPosition, remove_accents


class Termo:
    def __init__(self, size: int = 6):
        self.console = Console()
        self.size = size
        self.db = TinyDB(Path(__file__).resolve().parent / "db.json")

    def _get_random_word(self) -> str:
        return random.choice(self.db.table("initial_words").all())["word"]

    def _is_valid(self, word: str) -> bool:
        no_accent_word = remove_accents(word).lower().strip()
        return len(no_accent_word) == 5 and self.db.table("words").search(
            Query()[no_accent_word].exists()
        )

    def get_input_word(self) -> str:
        while True:
            try:
                word = input("Digite uma palavra: ")
                if self._is_valid(word):
                    return word
                elif len(word) != 5:
                    self.console.print(
                        "Por favor digite uma palavra com 5 letras!", style="yellow"
                    )
                else:
                    self.console.print(
                        "Por favor digite uma palavra existente!", style="yellow"
                    )
            except (KeyboardInterrupt, EOFError):
                exit()

    def compare_word(self, word) -> list[LetterPosition]:
        result = [LetterPosition.wrong] * 5
        found_letters_counter = defaultdict(int)

        for idx in range(5):
            if word[idx] == self.secret_word_unaccentuated[idx]:
                result[idx] = LetterPosition.correct
                found_letters_counter[word[idx]] += 1

        for idx in range(5):
            if (
                word[idx] in self.secret_word_unaccentuated
                and result[idx] != LetterPosition.correct
            ):
                if found_letters_counter[
                    word[idx]
                ] < self.secret_word_unaccentuated.count(word[idx]):
                    result[idx] = LetterPosition.almost
                    found_letters_counter[word[idx]] += 1

        return result

    def _get_accent_word(self, word):
        if word == "_____":
            return word
        word = remove_accents(word)
        return self.db.table("words").search(Query()[word].exists())[0][word]

    @property
    def winner(self):
        for _, result in self.board:
            if all(letter == LetterPosition.correct for letter in result):
                return True
        return False

    @property
    def game_is_over(self):
        return self.winner or self.board[-1][0] != "_____"

    def print_board(self, border=""):
        self.console.rule("TERMO")
        board = self._get_formated_board(self.board, border)
        self.console.print(board, justify="center")

    def _get_formated_board(self, board, border):
        text = Text()
        for word, result in board:
            accented_word = self._get_accent_word(word)
            for idx in range(4):
                text.append(f"{accented_word[idx]} ", style=result[idx].value)
            text.append(f"{accented_word[-1]}\n", style=result[-1].value)
        text.rstrip()
        board = Panel.fit(text, border_style=border)

        return board

    def new_game(self):
        self.secret_word = self._get_random_word()
        self.secret_word_unaccentuated = remove_accents(self.secret_word)
        self.board = [("_____", [LetterPosition.empty] * 5)] * self.size

    def end(self):
        with self.console.screen():
            if self.winner:
                final_txt = Text("Parabéns você ganhou! A palavra era: ")
                border = "green"
            else:
                final_txt = Text("Que pena, você perdeu. A palavra era: ")
                border = "red"
            final_txt.append(Text(self.secret_word, style="green"))
            self.print_board(border)
            self.console.print(final_txt)
            try:
                input()  # wait for enter
            except (KeyboardInterrupt, EOFError):
                exit()

    def run(self):
        self.new_game()
        for move in range(self.size):
            with self.console.screen():
                self.print_board()

                word = self.get_input_word()
                result = self.compare_word(word)
                self.board[move] = (word, result)

                if self.game_is_over:
                    break
        self.end()
