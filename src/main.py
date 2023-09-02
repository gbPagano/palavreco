import random
from enum import Enum
from collections import defaultdict

from rich import print
from rich.text import Text
from rich.panel import Panel
from rich.console import Console, Group
from rich.live import Live
from rich.align import Align
from rich.rule import Rule
from rich.traceback import install; install()

from palavras import palavras
from dicionario import dicionario
from utils import remove_accents, get_click
from termo import Termo
from dueto import Dueto


          

class Letreco:
    def __init__(self):
        self.console = Console()
        self.termo = Termo()
        self.dueto = Dueto()

    def _gen_menu_group(self, index: int = 0) -> Group:
        menu = Text(justify="left")

        selected = Text("> ", "bold green")
        not_selected = Text("  ")
        options = [not_selected, not_selected, not_selected]
        options[index] = selected

        menu.append(Text.assemble(options[0], "Termo\n"))
        menu.append(Text.assemble(options[1], "Dueto\n"))
        menu.append(Text.assemble(options[2], "Tutorial"))

        panel = Panel.fit(menu)
        group = Group(
            Rule("LETRECO"),
            Align(panel, "center"),
        )
        return group


    def _update_menu_index(self, index: int, key: str, length: int = 3) -> int:
        if key in ["right", "down"]:
            index += 1
        elif key in ["left", "up"]:
            index -= 1

        if index > length - 1:
            index = 0
        elif index < 0:
            index = length - 1

        return index


    def main_menu(self):
        index = 0
        group = self._gen_menu_group()

        with Live(group, auto_refresh=False, screen=True) as live:
            live.update(group, refresh=True)
            while True:
                key = get_click()
                if key == "enter":
                    match index:
                        case 0:
                            return "termo" 
                        case 1:
                            return "dueto" 
                        case 2:
                            return "tutorial" 

                index = self._update_menu_index(index, key)
                group = self._gen_menu_group(index)
                live.update(group, refresh=True)


    def tutorial_menu(self):
        with self.console.screen():
            self.console.print(Rule("TUTORIAL", style="yellow"))
            text = Text()
            text.append("\nNo ") 
            text.append("Termo ", style="green")
            text.append("você deve acertar uma palavra em 6 tentativas. ")
            text.append("No ") 
            text.append("Dueto ", style="red")
            text.append("são duas palavras em 7 tentativas.")
            text.append("\n\nA palavra sempre terá 5 letras, e será gerada de forma aleatória a partir de uma lista pré-estabelecida.")
            text.append("\nDepois de cada tentativa, as letras recebem cores para mostrar o quão perto você está da solução.")
            text.append("\nSomente palavras existentes são aceitas por tentativa.")
            text.append("\n\nCaso a letra fique ")
            text.append("vermelha", style="red")
            text.append(", significa que ela ")
            text.append("não faz parte da solução.", style="red")
            text.append("\nCaso a letra fique ")
            text.append("verde", style="green")
            text.append(", significa que ela ")
            text.append("faz parte da solução e está na posição correta.", style="green")
            text.append("\nCaso a letra fique ")
            text.append("amarela", style="yellow")
            text.append(", significa que ela ")
            text.append("faz parte da solução porém em outra posição.", style="yellow")
            text.append("\n\nAs palavras podem possuir letras repetidas.")
            text.append("\nAo observar as cores das letras você pode verificar se uma mesma letra se repete na palavra ou não.")
            text.append("\n\nOs acentos são preenchidos automaticamente e não são considerados nas dicas.")
            text.append("\n\nPressione enter para continuar.")

            self.console.print(text, justify="center")

            input()

    def run(self):
        while True:
            option = self.main_menu()
            match option:
                case "tutorial":
                    self.tutorial_menu()
                case "termo":
                    self.termo.run()
                case "dueto":
                    self.dueto.run()







if __name__ == "__main__":
    app = Letreco()
    app.run()