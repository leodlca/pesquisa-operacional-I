# -*- coding: utf-8 -*-

import os
import statistics
from pprint import pprint
from table import tabulate
from sys import exit


def clear(): 
    if os.name == 'nt': 
        os.system('cls')
    else: 
        os.system('clear')


def hold():
    input('> Pressione ENTER para continuar... ')


def sepbar():
    print('*'*50)


def center(_str):
    print('{:^50}'.format(_str))


def bcenter(_str):
    print('*{:^48}*'.format(_str))


def bcentertitle(_str):
    sepbar()
    bcenter('')
    bcenter(_str)
    bcenter('')
    sepbar()
    print()


def error(message):
    clear()
    sepbar()
    bcenter('ERRO')
    bcenter('')
    bcenter(message)
    sepbar()
    print()
    input('> Pressione ENTER para fechar o programa... ')
    clear()
    exit(0)


def header(mode=''):
    clear()
    sepbar()
    bcenter('TRABALHO DE PESQUISA OPERACIONAL I')
    bcenter('Feito por Leonardo Amorim')
    if mode != '':
        bcenter('')
        bcenter(mode)
    sepbar()
    print()


def welcome():
    header()
    hold()
    clear()


def get_file_read(_str):
    header(mode='Leitura do Arquivo')
    print('* OPCIONAL')
    print()
    print(('* Caso você já tenha executado o programa anteriormente e queira executar o arquivo salvo, '
           'insira o nome escolhido para o arquivo.'))
    print(('* Caso você ainda nao tenha executado o programa ou queira resolver um novo problema, '
            'simplesmente aperte ENTER.'))
    print('* O arquivo deve estar no mesmo diretorio do script')
    print()
    _ = input('> ' + _str)
    clear()
    return _.strip()


def get_file_creation_clear(_str):
    header(mode='Criacao do Arquivo')
    print('* Vamos salvar as configuracoes em um arquivo para facilitar o acesso numa proxima vez!')
    print()
    _ = input('> ' + _str)
    clear()
    return _.strip()


def get_file_creation(_str):
    header(mode='Criacao do Arquivo')
    print('* Vamos salvar as configuracoes em um arquivo para facilitar o acesso numa proxima vez!')
    print()
    _ = input('> ' + _str)
    return _.strip()


def get_input_nl(_str):
    _ = input('> ' + _str)
    print()
    return _.strip()


def get_input(_str):
    _ = input('> ' + _str)
    return _.strip()


def println(_str):
    print('* ' + _str)


def success_message(_str):
    header(mode='Sucesso!')
    bcentertitle(_str)
    hold()
    clear()


def print_file(problem):
    header(mode='Exibindo configuracoes do problema')
    pprint(problem)
    print()
    hold()
    clear()
    

def get_end():
    header(mode='Fim')
    _ = input('> Para recomecar, pressione ENTER. Para sair, digite "q" e pressione ENTER... ')
    clear()
    return _.strip()
    

def print_table_iter(m, bv, title, pivot=None):
    M = []
    h = ['Base'] + ['x' + str(x) for x in range(len(m[0])-1)] + ['Solucao']

    for i in range(len(m)):
        if i == 0:
            M.append(['z'])
        else:
            M.append(['x' + str(bv[i-1] + 1)])
        for j in range(len(m[i])):
            M[i].append(float(m[i][j]))

    sepbar()
    bcenter(title)
    sepbar()
    if pivot is not None:
        print()
        print('* Pivo: {}, linha: {}, coluna: {}'.format(pivot[0], pivot[1]+1, pivot[2]+1))
    print()
    print(tabulate(M, headers=h))
    print()

def print_final_results(solution, optimal):
    sepbar()
    bcenter('')
    for k, v in solution.items():
        bcenter('{} = {:.5f}'.format(k.replace('_', ''), float(v)))
    bcenter('')
    bcenter('Solucao Otima = {:.5f}'.format(float(optimal)))
    bcenter('')
    sepbar()

    print()
    hold()

