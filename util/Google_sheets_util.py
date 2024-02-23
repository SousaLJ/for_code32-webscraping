import pandas as pd
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow,Flow
from google.auth.transport.requests import Request
import os
import pickle
class google_sheets_util:

    #todo config account to use api (ref: https://developers.google.com/sheets/api/quickstart/python?hl=pt-br)
    def main():
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
