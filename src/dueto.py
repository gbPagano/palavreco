from rich.columns import Columns
from rich.text import Text

from src.termo import Termo


class Dueto(Termo):
    def __init__(self, size=7):
        super().__init__(size)
        self.termo_a = Termo(size)
        self.termo_b = Termo(size)

    def new_game(self):
        self.termo_a.new_game()
        self.termo_b.new_game()

    def print_board(self):
        self.console.rule("DUETO", style="red")
        border_a, border_b = self.get_borders()
        board_a = self._get_formated_board(self.termo_a.board, border_a)
        board_b = self._get_formated_board(self.termo_b.board, border_b)
        self.console.print(Columns([board_a, board_b]), justify="center")

    @property
    def game_is_over(self):
        return self.termo_a.game_is_over and self.termo_b.game_is_over

    @property
    def winner(self):
        return self.termo_a.winner and self.termo_b.winner

    def get_borders(self):
        border_a = ""
        if self.termo_a.game_is_over and self.termo_a.winner:
            border_a = "green"
        elif self.termo_a.game_is_over:
            border_a = "red"

        border_b = ""
        if self.termo_b.game_is_over and self.termo_b.winner:
            border_b = "green"
        elif self.termo_b.game_is_over:
            border_b = "red"
        
        return border_a, border_b

    def end(self):
        with self.console.screen():
            final_txt = Text("Que pena, você perdeu. As palavras eram: ")
            if self.winner:
                final_txt = Text("Parabéns você ganhou! A palavras eram: ")

            final_txt.append(Text(self.termo_a.secret_word, style="green"))
            final_txt.append(Text(" e "))
            final_txt.append(Text(self.termo_b.secret_word, style="green"))
            self.print_board()
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
                result_a = self.termo_a.compare_word(word)
                result_b = self.termo_b.compare_word(word)
                if not self.termo_a.game_is_over:
                    self.termo_a.board[move] = (word, result_a)
                if not self.termo_b.game_is_over:
                    self.termo_b.board[move] = (word, result_b)

                if self.game_is_over:
                    break

        self.end()
