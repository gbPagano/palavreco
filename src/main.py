from rich.console import Console
from rich.rule import Rule
from rich.text import Text
from rich_menu import Menu

from src.dueto import Dueto
from src.termo import Termo


class Palavreco:
    def __init__(self):
        self.console = Console()
        self.termo = Termo()
        self.dueto = Dueto()
        self.main_menu = Menu(
            "Termo",
            "Dueto",
            "Tutorial",
            rule_title="Palavreco",
        )

    def tutorial(self):
        with self.console.screen():
            self.console.print(Rule("TUTORIAL", style="yellow"))
            text = Text()
            text.append("\nNo ")
            text.append("Termo ", style="green")
            text.append("você deve acertar uma palavra em 6 tentativas. ")
            text.append("No ")
            text.append("Dueto ", style="red")
            text.append("são duas palavras em 7 tentativas.")
            text.append(
                "\n\nA palavra sempre terá 5 letras, e será gerada de forma aleatória a partir de uma lista pré-estabelecida."
            )
            text.append(
                "\nDepois de cada tentativa, as letras recebem cores para mostrar o quão perto você está da solução."
            )
            text.append("\nSomente palavras existentes são aceitas por tentativa.")
            text.append("\n\nCaso a letra fique ")
            text.append("vermelha", style="red")
            text.append(", significa que ela ")
            text.append("não faz parte da solução.", style="red")
            text.append("\nCaso a letra fique ")
            text.append("verde", style="green")
            text.append(", significa que ela ")
            text.append(
                "faz parte da solução e está na posição correta.", style="green"
            )
            text.append("\nCaso a letra fique ")
            text.append("amarela", style="yellow")
            text.append(", significa que ela ")
            text.append("faz parte da solução porém em outra posição.", style="yellow")
            text.append("\n\nAs palavras podem possuir letras repetidas.")
            text.append(
                "\nAo observar as cores das letras você pode verificar se uma mesma letra se repete na palavra ou não."
            )
            text.append(
                "\n\nOs acentos são preenchidos automaticamente e não são considerados nas dicas."
            )
            text.append("\n\nPressione enter para continuar.")
            self.console.print(text, justify="center")
            input()

    def run(self):
        while True:
            try:
                match self.main_menu.ask():
                    case "Termo":
                        self.termo.run()
                    case "Dueto":
                        self.dueto.run()
                    case "Tutorial":
                        self.tutorial()
            except (KeyboardInterrupt, EOFError):
                exit()


def main():
    app = Palavreco()
    app.run()


if __name__ == "__main__":
    main()
