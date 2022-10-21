'''
MIT License

Copyright (c) 2022 Gabriel Costa Andrade

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from Uteis import menu
from Uteis import cabecalho

ciro = 0
felipe = 0
bolsonaro = 0
maria = 0
leo = 0
lula = 0
pablo = 0
roberto = 0
simone = 0
sofia = 0
soraya = 0
vera = 0
nulo = 0
branco = 0

while True:

    menuinicial = menu(["Escolher Candidatos","Mostrar Resultado","Sair"])
    if menuinicial == 3:
        break
    if menuinicial == 2:
        cabecalho('** RESULTADOS **')
        print(f"Ciro Gomes (PDT): \033[1:34m{ciro}\033[m")
        print(f"Felipe D’Ávila (Novo):\033[1:34m{felipe}\033[m")
        print(f"Jair Bolsonaro (PL): \033[1:34m{bolsonaro}\033[m")
        print(f"José Maria Eymael (DC): \033[1:34m{maria}\033[m")
        print(f"Léo Péricles (UP): \033[1:34m{leo}\033[m")
        print(f"Lula (PT): \033[1:34m{lula}\033[m")
        print(f"Pablo Marçal (Pros): \033[1:34m{pablo}\033[m")
        print(f"Roberto Jefferson (PTB): \033[1:34m{roberto}\033[m")
        print(f"Simone Tebet (MDB): \033[1:34m{simone}\033[m")
        print(f"Sofia Manzano (PCB):\033[1:34m {sofia}\033[m")
        print(f"Soraya Thronicke (União):\033[1:34m {soraya}\033[m")
        print(f"Vera Lucia (PSTU): \033[1:34m{vera}\033[m")
        print(f"Voto em Branco: \033[1:34m{branco}\033[m")
        print(f"Voto Nulo:\033[1:34m {nulo}\033[m")

        sair = str(input("Aperte \033[1:34m'S'\033[m para voltar ao Menu-Inicial: ")).strip().upper()
        if sair not in "Ss":
            print(f"\033[1:31m{'Opção Inválida!'}\033[m")
            sair = str(input("Aperte ' S ' para voltar ao Menu Inicial: ")).strip().upper()

        if sair == "Ss":
            break


    if menuinicial == 1:

        while True:
            cabecalho("IR PARA VOTAÇÃO ?")
            p = str(input('\033[1:34m[S]\033[m para SIM ou \033[1:34m[N]\033[m para NÃO\033[1:34m:\033[m ')).strip().upper()
            if p not in 'NnSs':
                print(f"-"*42)
                print(f"\033[1:31m{'OPÇÃO INVÁLIDA':^42}\033[m")
                print(f"{'----------------':^42}")
                print("Tente novamente...")
            if p == 'N':
                print(".")
                print(".")
                print("Voltando ao Menu...")
                break
            if p == 'S':
                resposta = menu([
                    "Ciro Gomes (PDT): 12",
                    "Felipe D’Ávila (Novo): 30",
                    "Jair Bolsonaro (PL): 22",
                    "José Maria Eymael (DC): 27",
                    "Léo Péricles (UP): 80",
                    "Lula(PT): 13",
                    "Pablo Marçal (Pros): 90",
                    "Roberto Jefferson (PTB): 14",
                    "Simone Tebet (MDB): 15",
                    "Sofia Manzano (PCB): 21",
                    "Soraya Thronicke (União): 44",
                    "Vera Lucia (PSTU): 16",
                    "NULO",
                    "BRANCO"
                ])

                if resposta == 1:

                    while True:
                        print(f"{'CONFIRMA ?':^42}")
                        print(f"{'-----------':^42}")
                        confirmar = str(input("\033[1:34m[S]\033[m para SIM ou \033[1:34m[N]\033[m para NÃO\033[1:34m:\033[m ")).strip().upper()
                        print(f"{'-'*42}")
                        if confirmar not in "SsNn":
                            print(f"\033[1:31mErro de digitação!\033[m")

                        if confirmar == "S":
                            print(f"-" * 42)
                            print(f"\033[1:34m{'VOTO CONFIRMADO !':^42}\033[m")
                            print(f"-" * 42)
                            ciro = ciro + 1
                            break

                        elif confirmar == "N":
                            print(f"-"*42)
                            print(f"033[1:31m{'VOTO NÃO CONFIRMADO !':^42}\033[m")
                            print(f"-"*42)
                            break

                if resposta == 2:
                    while True:
                        confirmar = str(input("Confirma? [S|N]: ")).strip().upper()
                        if confirmar not in "SsNn":
                            print(f"\033[1:31mErro de digitação!\033[m")

                        if confirmar == "S":
                            print("Confirmado!")
                            felipe = felipe + 1
                            break

                        elif confirmar == "N":
                            print("Voto não confirmado!")
                            break

                if resposta == 3:
                    while True:
                        confirmar = str(input("Confirma? [S|N]: ")).strip().upper()
                        if confirmar not in "SsNn":
                            print(f"\033[1:31mErro de digitação!\033[m")

                        if confirmar == "S":
                            print("Confirmado!")
                            bolsonaro = bolsonaro + 1
                            break

                        elif confirmar == "N":
                            print("Voto não confirmado!")
                            break

                if resposta == 4:
                    while True:
                        confirmar = str(input("Confirma? [S|N]: ")).strip().upper()
                        if confirmar not in "SsNn":
                            print(f"\033[1:31mErro de digitação!\033[m")

                        if confirmar == "S":
                            print("Confirmado!")
                            maria = maria + 1
                            break

                        elif confirmar == "N":
                            print("Voto não confirmado!")
                            break

                if resposta == 5:
                    while True:
                        confirmar = str(input("Confirma? [S|N]: ")).strip().upper()
                        if confirmar not in "SsNn":
                            print(f"\033[1:31mErro de digitação!\033[m")

                        if confirmar == "S":
                            print("Confirmado!")
                            leo = leo + 1
                            break

                        elif confirmar == "N":
                            print("Voto não confirmado!")
                            break

                if resposta == 6:
                    while True:
                        confirmar = str(input("Confirma? [S|N]: ")).strip().upper()
                        if confirmar not in "SsNn":
                            print(f"\033[1:31mErro de digitação!\033[m")

                        if confirmar == "S":
                            print("Confirmado!")
                            lula = lula + 1
                            break

                        elif confirmar == "N":
                            print("Voto não confirmado!")
                            break

                if resposta == 7:
                    while True:
                        confirmar = str(input("Confirma? [S|N]: ")).strip().upper()
                        if confirmar not in "SsNn":
                            print(f"\033[1:31mErro de digitação!\033[m")

                        if confirmar == "S":
                            print("Confirmado!")
                            pablo = pablo + 1
                            break

                        elif confirmar == "N":
                            print("Voto não confirmado!")
                            break

                if resposta == 8:
                    while True:
                        confirmar = str(input("Confirma? [S|N]: ")).strip().upper()
                        if confirmar not in "SsNn":
                            print(f"\033[1:31mErro de digitação!\033[m")

                        if confirmar == "S":
                            print("Confirmado!")
                            roberto = roberto + 1
                            break

                        elif confirmar == "N":
                            print("Voto não confirmado!")
                            break

                if resposta == 9:
                    while True:
                        confirmar = str(input("Confirma? [S|N]: ")).strip().upper()
                        if confirmar not in "SsNn":
                            print(f"\033[1:31mErro de digitação!\033[m")

                        if confirmar == "S":
                            print("Confirmado!")
                            simone = simone + 1
                            break

                        elif confirmar == "N":
                            print("Voto não confirmado!")
                            break

                if resposta == 10:
                    while True:
                        confirmar = str(input("Confirma? [S|N]: ")).strip().upper()
                        if confirmar not in "SsNn":
                            print(f"\033[1:31mErro de digitação!\033[m")

                        if confirmar == "S":
                            print("Confirmado!")
                            sofia = sofia + 1
                            break

                        elif confirmar == "N":
                            print("Voto não confirmado!")
                            break

                if resposta == 11:
                    while True:
                        confirmar = str(input("Confirma? [S|N]: ")).strip().upper()
                        if confirmar not in "SsNn":
                            print(f"\033[1:31mErro de digitação!\033[m")

                        if confirmar == "S":
                            print("Confirmado!")
                            soraya = soraya + 1
                            break

                        elif confirmar == "N":
                            print("Voto não confirmado!")
                            break

                if resposta == 12:
                    while True:
                        confirmar = str(input("Confirma? [S|N]: ")).strip().upper()
                        if confirmar not in "SsNn":
                            print(f"\033[1:31mErro de digitação!\033[m")

                        if confirmar == "S":
                            print("Confirmado!")
                            vera = vera + 1
                            break

                        elif confirmar == "N":
                            print("Voto não confirmado!")
                            break

                if resposta == 13:
                    while True:
                        confirmar = str(input("Confirma? [S|N]: ")).strip().upper()
                        if confirmar not in "SsNn":
                            print(f"\033[1:31mErro de digitação!\033[m")

                        if confirmar == "S":
                            print("Confirmado!")
                            nulo = nulo + 1
                            break

                        elif confirmar == "N":
                            print("Voto não confirmado!")
                            break

                if resposta == 14:
                    while True:
                        confirmar = str(input("Confirma? [S|N]: ")).strip().upper()
                        if confirmar not in "SsNn":
                            print(f"\033[1:31mErro de digitação!\033[m")

                        if confirmar == "S":
                            cabecalho("Confirmado!")
                            branco = branco + 1
                            break

                        elif confirmar == "N":
                            cabecalho("Voto não confirmado!")
                            break

cabecalho("Volte Sempre!")
