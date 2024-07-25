from model import Vagas
from util import google_sheets_util as gs
import pandas as pd
from scraping import get_vagas

email = ""
senha = ""

lista_vagas = get_vagas(email, senha)

data = pd.DataFrame.from_records([v.to_dict() for v in lista_vagas])
data.to_excel('vagas.xlsx')