import random
from enum import Enum
from collections import defaultdict

from rich import print
from rich.text import Text
from rich.panel import Panel
from rich.console import Console, Group
from rich.live import Live
from rich.align import Align
from rich.columns import Columns
from rich.rule import Rule
from rich.traceback import install; install()

from palavras import palavras
from dicionario import dicionario
from utils import remove_accents, get_click, LetterPosition



class Termo():
    def __init__(self):
        self.console = Console()

    def _get_random_word(self) -> str:
        return "areal"
        return random.choice(palavras)

    def _is_valid(self, word: str) -> bool:
        no_accent_word = remove_accents(word).lower().strip()
        return len(no_accent_word) == 5 and no_accent_word in dicionario

    def get_input_word(self) -> str:
        while True:
            word = input("Digite uma palavra: ")
            if self._is_valid(word):
                return word
            elif len(word) != 5:
                self.console.print("Por favor digite uma palavra com 5 letras!", style="yellow")
            else:
                self.console.print("Por favor digite uma palavra existente!", style="yellow")

    def compare_words(self, word, secret_word):

        result = [LetterPosition.wrong] * 5
        found_letters_counter = defaultdict(int)

        for idx in range(5):
            if word[idx] == secret_word[idx]:
                result[idx] = LetterPosition.correct
                found_letters_counter[word[idx]] += 1

        for idx in range(5):
            if word[idx] in secret_word and result[idx] != LetterPosition.correct:
                if found_letters_counter[word[idx]] < secret_word.count(word[idx]):
                    result[idx] = LetterPosition.almost
                    found_letters_counter[word[idx]] += 1

        return result

    def _get_accent_word(self, word):
        return word

    @property
    def winner(self):
        for _, result in self.board:
            if all(letter == LetterPosition.correct for letter in result):
                return True
        return False
    
    @property
    def game_is_over(self):
        if self.winner:
            return True
        elif self.board[-1][0] != "_____":
            return True
        return False

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
            text.append(f"{accented_word[4]}\n", style=result[idx].value)
        text.rstrip()
        board = Panel.fit(text, border_style=border)
        
        return board

    def new_game(self):
        self.secret_word = self._get_random_word()
        self.secret_word_unaccentuated = remove_accents(self.secret_word)
        self.board = [("_____", [LetterPosition.empty]*5)] * 6

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
            input()

    def run(self):
        self.new_game()

        for move in range(6):
            with self.console.screen():
                self.print_board()

                word = self.get_input_word()
                result = self.compare_words(word, self.secret_word_unaccentuated)
                self.board[move] = (word, result)

                if self.game_is_over:
                    break

        self.end()

