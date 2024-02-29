from model import Vagas
from util import google_sheets_util as gs
import pandas as pd

lista_vagas = []

#Criação de objetos vaga
vaga1 = Vagas.Vagas("Estágio de Engenharia Química", "Esta é a descrição da vaga", "UFRJ", "http://ufrj.br")

lista_vagas.append(vaga1)

vaga2 = Vagas.Vagas("Estágio de Química Industrial", "Esta é a descrição da vaga2", "UFRJ", "http://ufrj.br")

lista_vagas.append(vaga2)

data = pd.DataFrame.from_records([v.to_dict() for v in lista_vagas])

gs.writeToSheets(data)