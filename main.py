from model import Vagas
from util import google_sheets_util as gs
import pandas as pd
from scraping import get_vagas

lista_vagas = get_vagas()

data = pd.DataFrame.from_records([v.to_dict() for v in lista_vagas])

gs.writeToSheets(data)