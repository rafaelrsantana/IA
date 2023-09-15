import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import sklearn.tree
import matplotlib.pyplot as plt
import numpy as np


nome_arquivo = input("Digite o nome ou caminho do arquivo CSV: ")

try:
    df = pd.read_csv(nome_arquivo)
    print("Arquivo CSV lido com sucesso!")
except FileNotFoundError:
    print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo CSV: {e}")


perguntas = list(df.columns[1:].values)
coluna = df.columns[0]
resposta = df[coluna].tolist()
dados = df[df.columns[1:]].to_numpy()

modelo = DecisionTreeClassifier(random_state=0)
modelo.fit(dados, resposta)



nodes = modelo.tree_.feature
no_esquerda = [x for x in modelo.tree_.children_left if x != -1 ]
no_direita = [x for x in modelo.tree_.children_right if x != -1 ]
i = 0
prox_no = 0
no_atual = 0
perguntas_respondidas_com_s = []
perguntas_respondidas_com_n = []

while nodes[no_atual] != -2:
  resp = input(f"{perguntas[nodes[no_atual]]} (Responda com Sim (s) ou Não (n))?\n").strip().lower()

  if resp == 'n':
    pergunta_respondida = perguntas[nodes[no_atual]].rstrip('?')
    perguntas_respondidas_com_n.append(pergunta_respondida)
    prox_no = no_esquerda[i]
    while prox_no <= no_atual:
      i+=1
      prox_no = no_esquerda[i]
      

  if resp == 's':
    pergunta_respondida = perguntas[nodes[no_atual]].rstrip('?')
    perguntas_respondidas_com_s.append(pergunta_respondida)
    prox_no = no_direita[i]
    while prox_no <= no_atual:
      i+=1
      prox_no = no_direita[i]
      
  i+=1

  no_atual = prox_no


adivinhado = (modelo.tree_.value[no_atual])
indice = adivinhado.argmax()

if perguntas_respondidas_com_s:
    print("\nComo a(s) resposta(s) negativa(s) obtida(s) foram:\n")
    for pergunta in perguntas_respondidas_com_n:
        print(f"{pergunta}? - Não\n")
    print("\nE a(s) resposta(s) afirmativa(s) obtida(s) foram:")
    for pergunta in perguntas_respondidas_com_s:
        print(f"{pergunta}? - Sim\n")

print(f"Por isso, a melhor opção é: {modelo.classes_[indice]}!\n")

if modelo.classes_[indice] == "Receitar analgesico":
    print(
        f"Como o paciente não está se sentindo bem, mas os sintomas não são de outras doenças, a melhor escolha é {modelo.classes_[indice]}"
    )