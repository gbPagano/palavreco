# Wordle Game for Terminal
## Introdução
### Este é um jogo para terminal baseado no [Wordle][link-wordle], [Termo][link-termo] e [Letreco][link-letreco].
> O programa e o código fonte estão em português
## Requisitos
* Ter o Python instalado na versão 3.10.4 (durante o desenvolvimento, utilizei a versão 3.10.4, então não garanto que versões anteriores funcionem);
    * Ter as seguintes bibliotecas no Python:
        * Unidecode==1.3.4
* O programa não funciona bem no Windows 7 ou inferior.
## Como utilizar
### Instalando as bibliotecas necessárias
```bash
$ git clone https://github.com/gbPagano/wordle-game-for-terminal
$ cd wordle-game-for-terminal
$ pip install -r requirements.txt
```
### Executando o jogo
```bash
$ python letreco.py
```
No **Termo** você deve acertar uma palavra em **6** tentativas. No **Dueto** são duas palavras em **7** tentativas.

A palavra sempre terá 5 letras, e será gerada de forma aleatória a partir de uma lista pré-estabelecida.

Depois de cada tentativa, as letras recebem cores para mostrar o quão perto você está da solução.
Somente palavras existentes são aceitas por tentativa.

>Caso a letra fique **vermelha**, significa que ela **não faz parte da solução**.

>Caso a letra fique **verde**, significa que ela **faz parte da solução e está na posição correta**.

>Caso a letra fique **amarela**, siginifica que ela **faz parte da solução porém em outra posição**.

As palavras podem possuir letras repetidas.
Ao observar as cores das letras você pode verificar se uma mesma letra se repete na palavra ou não.

Os acentos são preenchidos automaticamente e não são considerados nas dicas.

![menu](./assets/menu.png)

Exemplo no modo termo:

![termo](./assets/termo.png)

Exemplo no modo dueto:

![dueto](./assets/dueto.png)
## Como funciona
As palavras selecionadas para as partidas foram escolhidas manualmente por mim e colocadas em uma lista no python. A cada início de partida uma nova palavra é escolhida aleatoriamente a partir dessa lista.

Para verificar se a palavra existe ou não, filtrei uma lista publica de palavras que pode ser encontrada [aqui][link-palavras], e coloquei essas palavras em um dicionário no python, com cada palavra acentuada e desacentuada.

Para verificar a existência de cada palavra realizei requests no [dicio.com][link-dicio], onde fiz um script em python para automatizar o processo.

[link-wordle]: https://www.nytimes.com/games/wordle/index.html
[link-termo]: https://term.ooo/
[link-letreco]: https://www.gabtoschi.com/letreco/
[link-palavras]: https://github.com/fserb/pt-br
[link-dicio]: https://www.dicio.com.br/