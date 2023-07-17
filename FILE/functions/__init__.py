def cabecalho(txt):
    print(f"\033[1:34m{'-'}\033[m" * 42)
    print(f'{txt:^42}')
    print(f"\033[1:34m{'-'}\033[m"*42)

def leiaint(msg):
    while True:
        try:
            nu = int(input(msg))
        except (ValueError,TypeError):
            print("-"*42)
            print(f"\033[1:31m{'ERRO DE DIGITAÇÃO!':^42}\033[m")
            print(f"{'--------------------':^42}")
            print('Tente novamente... ')
            print("-" * 42)

        else:
            return nu

def menu(lista):
    cabecalho(f"{'==   ELEIÇÕES 2022   == ':^42}")
    for x in range (1,len(lista)+1):
        print(f'[\033[1:34m{x}\033[m] - {lista[x-1]}')

    b = leiaint(f"Sua opção\033[1:34m{':'}\033[m ")
    print(f"{'=-='*14}")
    return b


class Candidato(object):

    def __init__(self, nome, votos):
        self.__nome = nome
        self.__votos = votos

    def __repr__(self):
        return "nome:%s valor:%s" % (self.__nome, self.__votos)

    def get_nome(self):
        return self.__nome

    def get_valor(self):
        return self.__votos



