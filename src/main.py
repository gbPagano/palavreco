import random
from enum import Enum
from collections import defaultdict

from rich import print
from rich.text import Text

from palavras import palavras
from dicionario import dicionario
from utils import remove_accents


class LetterPosition(Enum):
    wrong = "red"
    correct = "green"
    almost = "yellow"


class Letreco():
    def __init__(self):
        # self.random_word = self._get_random_word()
        self.random_word = "areal"

    def _get_random_word(self) -> str:
        return random.choice(palavras)

    def _is_valid(self, word: str) -> bool:
        no_accent_word = remove_accents(word).lower().strip()
        return len(no_accent_word) == 5 and no_accent_word in dicionario

    def get_input_word(self) -> str:
        while True:
            word = input("Digite uma palavra: ")
            if self._is_valid(word):
                return word
            else:
                print("Palavra inválida!")

    def compare_words(self, word):

        result = [LetterPosition.wrong] * 5
        found_letters_counter = defaultdict(int)

        for idx in range(5):
            if word[idx] == self.random_word[idx]:
                result[idx] = LetterPosition.correct
                found_letters_counter[word[idx]] += 1

        for idx in range(5):
            if word[idx] in self.random_word and result[idx] != LetterPosition.correct:
                if found_letters_counter[word[idx]] < self.random_word.count(word[idx]):
                    result[idx] = LetterPosition.almost
                    found_letters_counter[word[idx]] += 1

        return result

    def is_correct(self, result):
        return all(letter == LetterPosition.correct for letter in result)


    def run(self):
        tentatives = 6
        while tentatives:
            word = self.get_input_word()
            result = self.compare_words(word)
            print_result(word, result)
            if self.is_correct(result):
                break
            tentatives -= 1



def print_result(word: str, result: list[LetterPosition]):
    text = Text()
    for idx in range(5):
        text.append(word[idx], style=result[idx].value)

    print(text)





if __name__ == "__main__":
    app = Letreco()
    app.run()