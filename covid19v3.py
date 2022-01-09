############################################
#
# Filter by country
# Author : MS
# Date : 16/03/2020
# Update : 09/01/2022
#
# Replace the "___" by appropriate code
#
###########################################

import urllib.request as urllib2
import csv
from covid19v1 import *
from covid19v2 import *

def data_for_country(data, state = "", country = ""):
    # for each country in data
    for pays in ___:
        # if 'Province/State' key match with state given in argument
        # and if 'Country/Region' key match with country given in argument
        if pays[___] == ___ and pays[___] == ___:
            return pays


# here the main code
if __name__ == '__main__':

  # File name of datas
  file = "time_series_covid19_confirmed_global.csv"
  # where datas are located
  url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

  if download_file(url,file):
      print(f'Téléchargement du fichier {file} terminé avec succès')
      countries = read_CSV(file)
      print("liste des pays et régions recencés")
      print("----------------------------------")
      # for row in coutries:
      #    print(row['Province/State'], row['Country/Region'])
      france = data_for_country(countries, '', 'France')
      print(france)

  else:
      print(f'Téléchargement du fichier {file} impossible')
