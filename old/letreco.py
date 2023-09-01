import os
from random import choice
from palavras import palavras
from unidecode import unidecode
from dicionario import dicionario

def main():
    ligar = True
    while ligar:
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")    
        print("┌","─"*9,"┐""\n│ Letreco │\n└","─"*9,"┘\n",sep= "")
        continuar = True
        print("Para \033[033maprender\033[m a jogar, digite \033[033m0\033[m")
        while continuar:
            print("Para jogar \033[032mTermo\033[m, digite \033[032m1\033[m\nPara jogar \033[031mDueto\033[m, digite \033[031m2\033[m\n")
            jogo = input("O que deseja jogar: ")
            if jogo not in "123" or len(jogo) != 1:
                while jogo not in "012" or len(jogo) != 1:
                    if os.name == 'nt':
                        os.system("cls")
                    else:
                        os.system("clear")
                    print("\033[33mPor favor digite uma opção disponível.\033[m\n")
                    print("Para \033[033maprender\033[m a jogar, digite \033[033m0\033[m")
                    print("Para jogar \033[032mTermo\033[m, digite \033[032m1\033[m\nPara jogar \033[031mDueto\033[m, digite \033[031m2\033[m\n")
                    jogo = input("O que deseja jogar: ")
            if jogo == "1":
                if termo():
                    continuar = True
                    if os.name == 'nt':
                        os.system("cls")
                    else:
                        os.system("clear")
                else:
                    continuar = False
                    if os.name == 'nt':
                        os.system("cls")
                    else:
                        os.system("clear")
            elif jogo == "2":
                if dueto():
                    continuar = True
                    if os.name == 'nt':
                        os.system("cls")
                    else:
                        os.system("clear")
                else:
                    continuar = False
                    if os.name == 'nt':
                        os.system("cls")
                    else:
                        os.system("clear")
            else:
                regras()
                if os.name == 'nt':
                    os.system("cls")
                else:
                    os.system("clear")
        
        print("fim")
        ligar = False

def termo():
    ligar = True
    while ligar:
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")    
        print("\033[032m┌","─"*7,"┐""\n│\033[m \033[032mTermo\033[m \033[032m│\n└","─"*7,"┘\033[m",sep= "")
        palavra = choice(palavras)
        palavra_sem_acentos = unidecode(palavra)
        todas = [[],[],[],[],[],[]]
        vidas = 6
        contador=0
        while vidas != 0:
            if vidas > 3:
                print("\nVocê tem \033[32m{}\033[m tentativas restantes.\n".format(vidas))
            elif vidas >1:
                print("\nVocê tem \033[33m{}\033[m tentativas restantes.\n".format(vidas))
            else:
                print("\nVocê tem \033[31m{}\033[m tentativas restantes.\n".format(vidas))
            tentativa = receber_palavra().upper()
            tentativa_sem_acentos = unidecode(tentativa).lower()
            if comparar_palavra(tentativa_sem_acentos, palavra_sem_acentos,tentativa, contador, todas, vidas):
                vidas = 0
                resultado = 1
            else:
                vidas -= 1
                resultado = 0
                contador+=1
        palavra = palavra.capitalize()
        if resultado == 1: print("\033[0;32mParabéns você ganhou! A palavra era:\033[m \033[032m{}\033[m".format(palavra))
        else: print("\033[0;31mQue pena, você perdeu. A palavra era:\033[m \033[32m{}\033[m".format(palavra))
        continuar =  input("Deseja continuar jogando? (\033[032ms\033[m/\033[031mn\033[m): ")
        if continuar not in "sn" or len(continuar) != 1:
            while continuar not in "sn" or len(continuar) != 1:
                if os.name == 'nt':
                    os.system("cls")
                else:
                    os.system("clear")
                print("\033[33mPor favor digite uma opção disponível.\033[m\n")
                continuar =  input("Deseja continuar jogando? (\033[032ms\033[m/\033[031mn\033[m): ")
        if continuar == "s":
            ligar = False
            return True
        else:
            ligar = False
            return False 
        
def receber_palavra():
    palavra = "errado"
    while palavra == "errado":
        palavra = unidecode(input("Digite a palavra: ").lower().replace("#","xyz").replace("&","xyz").strip())
        while len(palavra) != 5:
            print("\033[33mPor favor digite uma palavra com\033[m \033[33m5 letras\033[m.\n")
            palavra = unidecode(input("Digite a palavra: ").lower().replace("#","xyz").replace("&","xyz").strip())

        if palavra not in dicionario:
            print ("\033[33mPor favor digite uma\033[m \033[33mpalavra existente\033[m.\n")    
            palavra = "errado"
        else:
            palavra_acentuada = dicionario[palavra]
         
    return palavra_acentuada

def comparar_palavra(tentativa, palavra, tentativa_com_acentos, c, t,vidas):

    certo = []
    achadas = []
    resultado = ["","","","",""]

    for i in range (5):
        
        if tentativa[i] not in palavra:
            resultado[i] = "\033[31m{} \033[m".format(tentativa_com_acentos[i])
            achadas.append(tentativa[i])

        if tentativa[i] == palavra[i]:
            resultado[i] = "\033[32m{} \033[m".format(tentativa_com_acentos[i])
            achadas.append(palavra[i])
            certo.append(palavra[i])
                
    for i in range (5):
        
        if tentativa[i] != palavra[i] and tentativa[i] in palavra and achadas.count(tentativa[i]) < palavra.count(tentativa[i]):
            resultado[i] = "\033[33m{} \033[m".format(tentativa_com_acentos[i])
            achadas.append(tentativa[i])
        elif tentativa[i] != palavra[i] and tentativa[i] in palavra:
            resultado[i] = "\033[31m{} \033[m".format(tentativa_com_acentos[i])
                    
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
    for i in range(5):
        t[c].append(resultado[i])
    for i in range (c+1):
        print(t[i][0],t[i][1],t[i][2],t[i][3],t[i][4], sep="")
    
    for i in range(vidas-1):
        print ("_ _ _ _ _")       

    if len(certo) == 5:
        return True

def dueto():
    ligar = True
    while ligar:
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")    
        print("\033[031m┌","─"*7,"┐""\n│\033[m \033[031mDueto\033[m \033[031m│\n└","─"*7,"┘\033[m",sep= "")
        palavra = choice(palavras)
        palavra2 = choice(palavras)
        while palavra2 == palavra:
            palavra2 = choice(palavras)
        palavra_sem_acentos = unidecode(palavra)
        palavra_sem_acentos2 = unidecode(palavra2)
        todas = [[],[],[],[],[],[],[]]
        todas2 = [[],[],[],[],[],[],[]]
        vidas = 7
        contador = 0
        verificador1 = [0]
        verificador2 = [0]
        while vidas != 0:
            if vidas > 3:
                print("\nVocê tem \033[32m{}\033[m tentativas restantes.\n".format(vidas))
            elif vidas >2:
                print("\nVocê tem \033[33m{}\033[m tentativas restantes.\n".format(vidas))
            else:
                print("\nVocê tem \033[31m{}\033[m tentativas restantes.\n".format(vidas))
            tentativa = receber_palavra().upper()
            tentativa_sem_acentos = unidecode(tentativa).lower()
            if comparar_2palavras(tentativa_sem_acentos, palavra_sem_acentos,palavra_sem_acentos2, tentativa, contador, todas, todas2, verificador1, verificador2, vidas):
                vidas = 0
                resultado = 1
            else:
                vidas -= 1 
                resultado = 0
                contador+=1
        palavra = palavra.capitalize()
        palavra2 = palavra2.capitalize()
        if resultado == 1: print("\033[32mParabéns você ganhou! As palavras eram:\033[m \033[032m{} e {}\033[m".format(palavra,palavra2))
        else: print("\033[31mQue pena, você perdeu. As palavras eram:\033[m \033[32m{} e {}\033[m".format(palavra,palavra2))
        continuar =  input("Deseja continuar jogando? (\033[032ms\033[m/\033[031mn\033[m): ")
        if continuar not in "sn" or len(continuar) != 1:
            while continuar not in "sn" or len(continuar) != 1:
                if os.name == 'nt':
                    os.system("cls")
                else:
                    os.system("clear")
                print("\033[033mPor favor digite uma opção disponível.\033[m\n")
                continuar =  input("Deseja continuar jogando? (\033[032ms\033[m/\033[031mn\033[m): ")
        if continuar == "s":
            ligar = False
            return True
        else:
            ligar = False
            return False 

def comparar_2palavras(tentativa, palavra,palavra2, tentativa_com_acentos, c, t,t2, verificador1, verificador2, vidas):

    certo = []
    achadas = []
    resultado = ["","","","",""]
    certo2 = []
    achadas2 = []
    resultado2 = ["","","","",""]
    #primeira palavra:
    if verificador1[0] == 0:
        for i in range (5):
            
            if tentativa[i] not in palavra:
                resultado[i] = "\033[31m{} \033[m".format(tentativa_com_acentos[i])
                achadas.append(tentativa[i])

            if tentativa[i] == palavra[i]:
                resultado[i] = "\033[32m{} \033[m".format(tentativa_com_acentos[i])
                achadas.append(palavra[i])
                certo.append(palavra[i])
                    
        for i in range (5):
            
            if tentativa[i] != palavra[i] and tentativa[i] in palavra and achadas.count(tentativa[i]) < palavra.count(tentativa[i]):
                resultado[i] = "\033[33m{} \033[m".format(tentativa_com_acentos[i])
                achadas.append(tentativa[i])
            elif tentativa[i] != palavra[i] and tentativa[i] in palavra:
                resultado[i] = "\033[31m{} \033[m".format(tentativa_com_acentos[i])
    else:
        for i in range (5):
            resultado[i] = t[verificador1[1]][i]

    #segunda palavra:
    if verificador2[0] == 0:
        for i in range (5):
            
            if tentativa[i] not in palavra2:
                resultado2[i] = "\033[31m{} \033[m".format(tentativa_com_acentos[i])
                achadas2.append(tentativa[i])

            if tentativa[i] == palavra2[i]:
                resultado2[i] = "\033[32m{} \033[m".format(tentativa_com_acentos[i])
                achadas2.append(palavra2[i])
                certo2.append(palavra2[i])
                    
        for i in range (5):
            
            if tentativa[i] != palavra2[i] and tentativa[i] in palavra2 and achadas2.count(tentativa[i]) < palavra2.count(tentativa[i]):
                resultado2[i] = "\033[33m{} \033[m".format(tentativa_com_acentos[i])
                achadas2.append(tentativa[i])
            elif tentativa[i] != palavra2[i] and tentativa[i] in palavra2:
                resultado2[i] = "\033[31m{} \033[m".format(tentativa_com_acentos[i])
    else:
        for i in range (5):
            resultado2[i] = t2[verificador2[1]][i]
    
    if len(certo) == 5:
        verificador1[0] = 1
        verificador1.append(c)
    if len(certo2) == 5:
        verificador2[0] = 1
        verificador2.append(c)

    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
    for i in range(5):
        t[c].append(resultado[i])
        t2[c].append(resultado2[i])

    for i in range (c+1):
        print(t[i][0],t[i][1],t[i][2],t[i][3],t[i][4],"     ",t2[i][0],t2[i][1],t2[i][2],t2[i][3],t2[i][4], sep="")
    for i in range(vidas-1):
        print ("_ _ _ _ _      _ _ _ _ _")    
    if verificador1[0] == 1 and verificador2[0] == 1:
        return True

def regras():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
    print("\033[033m┌","─"*12,"┐""\n│\033[m \033[033mComo Jogar\033[m \033[033m│\n└","─"*12,"┘\033[m\n",sep= "")
    print("\033[033m>\033[m No \033[032mTermo\033[m você deve acertar uma palavra em 6 tentativas. No \033[031mDueto\033[m são duas palavras em 7 tentativas.")
    print("\033[033m>\033[m A palavra sempre terá 5 letras, e será gerada de forma aleatória a partir de uma lista pré-estabelecida.")
    print("\033[033m>\033[m Depois de cada tentativa, as letras recebem cores para mostrar o quão perto você está da solução.")
    print("\033[033m>\033[m Somente palavras existentes são aceitas por tentativa.\n")
    print("\033[033m>\033[m Caso a letra fique \033[031mvermelha\033[m, significa que ela \033[031mnão faz parte da solução\033[m.")
    print("\033[033m>\033[m Caso a letra fique \033[032mverde\033[m, significa que ela \033[032mfaz parte da solução e está na posição correta\033[m.")
    print("\033[033m>\033[m Caso a letra fique \033[033mamarela\033[m, siginifica que ela \033[033mfaz parte da solução porém em outra posição\033[m.\n")
    print("\033[033m>\033[m As palavras podem possuir letras repetidas.")
    print("\033[033m>\033[m Ao observar as cores das letras você pode verificar se uma mesma letra se repete na palavra ou não.\n")
    print("\033[033m>\033[m Os acentos são preenchidos automaticamente e não são considerados nas dicas.\n")
    input("Digite enter para continuar: ")

if __name__ == '__main__':
    main()  