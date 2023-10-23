import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt


# Definindo os universos de discurso para as variáveis de entrada
nivel_sujeira = ctrl.Antecedent(np.arange(0, 11, 1), 'nivel_sujeira')
numero_de_roupas = ctrl.Antecedent(np.arange(0, 11, 1), 'numero_de_roupas')
material_tecido = ctrl.Antecedent(np.arange(0, 11, 1), 'material_tecido')

# Definindo os universos de discurso para as variáveis de saída
tempo_lavagem = ctrl.Consequent(np.arange(0, 101, 1), 'tempo_lavagem')
gasto_de_agua = ctrl.Consequent(np.arange(0, 101, 1), 'gasto_de_agua')
gasto_de_eletricidade = ctrl.Consequent(np.arange(0, 101, 1), 'gasto_de_eletricidade')
consumo_detergente = ctrl.Consequent(np.arange(0, 101, 1), 'consumo_detergente')
tempo_secagem = ctrl.Consequent(np.arange(0, 101, 1), 'tempo_secagem')

# Definindo as funções de pertinência para as variáveis de saída
tempo_lavagem['curto'] = fuzz.trimf(tempo_lavagem.universe, [0, 0, 50])
tempo_lavagem['médio'] = fuzz.trimf(tempo_lavagem.universe, [0, 50, 100])
tempo_lavagem['longo'] = fuzz.trimf(tempo_lavagem.universe, [50, 100, 100])

#Definindo as funções de pertinência para Tempo de Secagem
tempo_secagem['curto'] = fuzz.trimf(tempo_secagem.universe, [0, 0, 50])
tempo_secagem['médio'] = fuzz.trimf(tempo_secagem.universe, [0, 50, 100])
tempo_secagem['longo'] = fuzz.trimf(tempo_secagem.universe, [50, 100, 100])

# Definindo as funções de pertinência para Número de Roupas
numero_de_roupas['pequena'] = fuzz.trimf(numero_de_roupas.universe, [0, 0, 5])
numero_de_roupas['média'] = fuzz.trimf(numero_de_roupas.universe, [0, 5, 10])
numero_de_roupas['grande'] = fuzz.trimf(numero_de_roupas.universe, [5, 10, 10])

# Definindo as funções de pertinência para Material do Tecido
material_tecido['delicado'] = fuzz.trimf(material_tecido.universe, [0, 0, 5])
material_tecido['algodão'] = fuzz.trimf(material_tecido.universe, [0, 5, 10])
material_tecido['sintético'] = fuzz.trimf(material_tecido.universe, [5, 10, 10])

# Definindo as funções de pertinência para Nivel de Sujeira
nivel_sujeira['baixo'] = fuzz.trimf(nivel_sujeira.universe, [0, 0, 5])
nivel_sujeira['médio'] = fuzz.trimf(nivel_sujeira.universe, [0, 5, 10])
nivel_sujeira['alto'] = fuzz.trimf(nivel_sujeira.universe, [5, 10, 10])


#Definindo as funções de pertinência para Gasto de Água
gasto_de_agua['baixo'] = fuzz.trimf(gasto_de_agua.universe, [0, 0, 50])
gasto_de_agua['médio'] = fuzz.trimf(gasto_de_agua.universe, [0, 50, 100])
gasto_de_agua['alto'] = fuzz.trimf(gasto_de_agua.universe, [50, 100, 100])


#Definindo as funções de pertinência para Gasto de Eletricidade

gasto_de_eletricidade['baixo'] = fuzz.trimf(gasto_de_eletricidade.universe, [0, 0, 50])
gasto_de_eletricidade['médio'] = fuzz.trimf(gasto_de_eletricidade.universe, [0, 50, 100])
gasto_de_eletricidade['alto'] = fuzz.trimf(gasto_de_eletricidade.universe, [50, 100, 100])

#Definindo as funções de pertinência para Gasto de Detergente
consumo_detergente['baixo'] = fuzz.trimf(consumo_detergente.universe, [0, 0, 50])
consumo_detergente['médio'] = fuzz.trimf(consumo_detergente.universe, [0, 50, 100])
consumo_detergente['alto'] = fuzz.trimf(consumo_detergente.universe, [50, 100, 100])


# Definindo as regras fuzzy
regra1 = ctrl.Rule(nivel_sujeira['baixo'] & numero_de_roupas['pequena'] & material_tecido['delicado'], 
                   [tempo_lavagem['curto'], gasto_de_agua['baixo'], gasto_de_eletricidade['baixo'], consumo_detergente['baixo'], tempo_secagem['curto']])
regra2 = ctrl.Rule(nivel_sujeira['baixo'] & numero_de_roupas['pequena'] & material_tecido['algodão'], 
                   [tempo_lavagem['curto'], gasto_de_agua['baixo'], gasto_de_eletricidade['baixo'], consumo_detergente['baixo'], tempo_secagem['curto']])
regra3 = ctrl.Rule(nivel_sujeira['baixo'] & numero_de_roupas['média'] & material_tecido['delicado'], 
                   [tempo_lavagem['curto'], gasto_de_agua['baixo'], gasto_de_eletricidade['baixo'], consumo_detergente['baixo'], tempo_secagem['curto']])
regra4 = ctrl.Rule(nivel_sujeira['baixo'] & numero_de_roupas['média'] & material_tecido['algodão'], 
                   [tempo_lavagem['médio'], gasto_de_agua['médio'], gasto_de_eletricidade['médio'], consumo_detergente['médio'], tempo_secagem['médio']])
regra5 = ctrl.Rule(nivel_sujeira['médio'] & numero_de_roupas['pequena'] & material_tecido['delicado'], 
                   [tempo_lavagem['curto'], gasto_de_agua['baixo'], gasto_de_eletricidade['baixo'], consumo_detergente['baixo'], tempo_secagem['curto']])
regra6 = ctrl.Rule(nivel_sujeira['médio'] & numero_de_roupas['pequena'] & material_tecido['algodão'], 
                   [tempo_lavagem['médio'], gasto_de_agua['médio'], gasto_de_eletricidade['médio'], consumo_detergente['médio'], tempo_secagem['médio']])
regra7 = ctrl.Rule(nivel_sujeira['médio'] & numero_de_roupas['média'] & material_tecido['delicado'], 
                   [tempo_lavagem['médio'], gasto_de_agua['médio'], gasto_de_eletricidade['médio'], consumo_detergente['médio'], tempo_secagem['médio']])
regra8 = ctrl.Rule(nivel_sujeira['médio'] & numero_de_roupas['média'] & material_tecido['algodão'], 
                   [tempo_lavagem['médio'], gasto_de_agua['médio'], gasto_de_eletricidade['médio'], consumo_detergente['médio'], tempo_secagem['médio']])
regra9 = ctrl.Rule(nivel_sujeira['alto'] & numero_de_roupas['pequena'] & material_tecido['delicado'], 
                   [tempo_lavagem['médio'], gasto_de_agua['alto'], gasto_de_eletricidade['alto'], consumo_detergente['alto'], tempo_secagem['médio']])
regra10 = ctrl.Rule(nivel_sujeira['alto'] & numero_de_roupas['pequena'] & material_tecido['algodão'], 
                    [tempo_lavagem['longo'], gasto_de_agua['alto'], gasto_de_eletricidade['alto'], consumo_detergente['alto'], tempo_secagem['longo']])
regra11 = ctrl.Rule(nivel_sujeira['alto'] & numero_de_roupas['média'] & material_tecido['delicado'], 
                    [tempo_lavagem['longo'], gasto_de_agua['alto'], gasto_de_eletricidade['alto'], consumo_detergente['alto'], tempo_secagem['longo']])
regra12 = ctrl.Rule(nivel_sujeira['alto'] & numero_de_roupas['média'] & material_tecido['algodão'], 
                    [tempo_lavagem['longo'], gasto_de_agua['alto'], gasto_de_eletricidade['alto'], consumo_detergente['alto'], tempo_secagem['longo']])
regra13 = ctrl.Rule(nivel_sujeira['baixo'] & numero_de_roupas['grande'] & material_tecido['delicado'], 
                    [tempo_lavagem['médio'], gasto_de_agua['médio'], gasto_de_eletricidade['médio'], consumo_detergente['médio'], tempo_secagem['médio']])
regra14 = ctrl.Rule(nivel_sujeira['baixo'] & numero_de_roupas['grande'] & material_tecido['algodão'], 
                    [tempo_lavagem['médio'], gasto_de_agua['médio'], gasto_de_eletricidade['médio'], consumo_detergente['médio'], tempo_secagem['médio']])
regra15 = ctrl.Rule(nivel_sujeira['médio'] & numero_de_roupas['grande'] & material_tecido['delicado'], 
                    [tempo_lavagem['médio'], gasto_de_agua['alto'], gasto_de_eletricidade['médio'], consumo_detergente['alto'], tempo_secagem['médio']])
regra16 = ctrl.Rule(nivel_sujeira['médio'] & numero_de_roupas['grande'] & material_tecido['algodão'], 
                    [tempo_lavagem['longo'], gasto_de_agua['alto'], gasto_de_eletricidade['alto'], consumo_detergente['alto'], tempo_secagem['longo']])

# Criando o sistema de controle fuzzy
sistema_fuzzy = ctrl.ControlSystem([regra1, regra2, regra3, regra4, regra5, regra6, regra7, regra8, regra9, regra10, regra11, regra12, regra13, regra14, regra15, regra16])

# Criando a simulação
simulacao = ctrl.ControlSystemSimulation(sistema_fuzzy)

# Definindo os valores de entrada
simulacao.input['nivel_sujeira'] = 4
simulacao.input['numero_de_roupas'] = 3
simulacao.input['material_tecido'] = 5

# Realizando a inferência
simulacao.compute()

# Obtendo os valores de saída
tempo_de_lavagem = simulacao.output['tempo_lavagem']
consumo_de_agua = simulacao.output['gasto_de_agua']
consumo_de_eletricidade = simulacao.output['gasto_de_eletricidade']
consumo_de_detergente = simulacao.output['consumo_detergente']
tempo_de_secagem = simulacao.output['tempo_secagem']

print("Tempo de lavagem recomendado:", tempo_de_lavagem)
print("Gasto de água recomendado:", consumo_de_agua)
print("Gasto de eletricidade recomendado:", consumo_de_eletricidade)
print("Gasto de detergente recomendado:", consumo_de_detergente)
print("Tempo de secagem recomendado:", tempo_de_secagem)
