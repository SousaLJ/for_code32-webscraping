import pandas as pd
from model import Vagas
from scraping import get_vagas

email = "estagiosforcode@gmail.com"
senha = "F0rC0d3Estagio5"

lista_vagas = get_vagas(email, senha)

data = pd.DataFrame.from_records([v.to_dict() for v in lista_vagas])
data.to_excel('vagas.xlsx')