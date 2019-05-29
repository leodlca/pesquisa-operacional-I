# -*- coding: utf-8 -*-

import statistics
import math
import os
import view
import pickle
from simplex import Simplex


DECIMAL_SIGNIFICANCE = 3


def round_decimal(n, decimals=DECIMAL_SIGNIFICANCE):
    if n > 0:
        return round_up(n, decimals=decimals)
    else:
        return round_down(n, decimals=decimals)


def round_up(n, decimals=2):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier


def round_down(n, decimals=2):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier


def read_file(filename):
    with open(filename, 'rb') as f:
        problem = pickle.load(f)

    return problem


def equation_to_str(coefs, operation=None, indep=None):
    if operation is not None:
        map_operator = {
            '==': '=',
            '>=': '>=',
            '<=': '<='
        }
    equation_str = ''

    for i in range(len(coefs)):
        equation_str += '{:.3f}x_{} '.format(coefs[i], i+1)
    if indep is None:
        return equation_str.strip()

    equation_str += ' {} {:.3f}'.format(map_operator[operation], indep)
    return equation_str.strip()


def solver(problem):
    map_objective = {
        'max': 'maximize',
        'min': 'minimize'
    }

    objective = (map_objective[problem['type']], equation_to_str(problem['coef_obj']))
    constraints = [equation_to_str(x['coefs'], x['type'], x['independent']) for x in problem['restrictions']]
    system = Simplex(num_vars=problem['n_var'], constraints=constraints, objective_function=objective)

    return system.solution, system.optimize_val

while True:
    #########
    # INPUT #
    #########

    view.welcome()
    filename = view.get_file_read('Por favor insira o nome do arquivo de texto contendo os dados (com a extensao): ')

    if filename == '' or not os.path.isfile(filename):
        filename = view.get_file_creation_clear('Insira o nome desejado para o arquivo (com a extensao): ')

        if filename == '':
            view.error('Nome do arquivo vazio')
        if os.path.isfile(filename):
            view.error('Esse arquivo ja existe')

        n_var = int(view.get_file_creation('Numero de variaveis (ilimitado): '))
        if 0 >= n_var:
            view.error('Numero menor ou igual a 0')

        n_rest = int(view.get_input_nl('Numero de restricoes (ilimitado): '))
        if 0 >= n_rest:
            view.error('Numero menor ou igual a 0')

        ptype = view.get_input_nl('Tipo de problema (max/min): ').lower()
        if ptype not in ['max', 'min']:
            view.error('Tipos de problemas suportados: max, min')

        view.println('Funcao Objetivo')
        coef_obj = []
        for i in range(n_var):
            coef_obj.append(float(view.get_input('Coeficiente da variavel x{}: '.format(str(i)))))
            if i == n_var-1:
                print()

        restrictions = []

        for nr in range(n_rest):
            view.println('Restricao {}:'.format(str(nr + 1)))
            _restriction = {
                'coefs': []
            }
            for i in range(n_var):
                _restriction['coefs'].append(float(view.get_input('Coeficiente da variavel x{}: '.format(str(i)))))

            _restriction['type'] = view.get_input('Tipo de Restricao (==, <=, >=): ')
            if _restriction['type'] not in ['==', '<=', '>=']:
                view.error('Tipo de restricao invalida')

            _restriction['independent'] = float(view.get_input_nl('Termo independente: '))

            restrictions.append(_restriction)
        
        with open(filename, 'wb') as f:
            problem = {
                'n_var': n_var,
                'n_rest': n_rest,
                'type': ptype,
                'coef_obj': coef_obj,
                'restrictions': restrictions
            }
            pickle.dump(problem, f)

        view.success_message('Arquivo criado com sucesso!')

    problem = read_file(filename)
    view.print_file(problem)

    solution = solver(problem)
    view.print_final_results(solution[0], solution[1])

    if 'q' in view.get_end().lower():
        break

