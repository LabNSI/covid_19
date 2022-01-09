############################################
#
# Filter by country
# Author : MS
# Date : 16/03/2020
#
# Replace the "___" by appropriate code
#
###########################################

import urllib.request as urllib2
import csv


def download_file(url, file_name):
    '''
    Download a file from url and copy it localy with file_name as name
    '''
    try:
        # open url passed in argument
        file = urllib2.urlopen(___)
        # open file for writing in binary mode
        # https://docs.python.org/3/library/functions.html#open
        with open(___, '___') as output:
            # write in output the file read
            output.___(file.___())
        # OK : return true
        return ___
    except:
        # Something is wrong : return false
        return ___


def read_CSV(file):
    '''
    Read a csv file and return :
    - fields name as string in a list
    - datas dictionary  by countries in a list
    '''
    # datas is an empty list
    datas = []
    # open the file passed in argument as csvfile
    # https://docs.python.org/3/library/csv.html#csv.reader
    with open(file) as csvfile:
        # Create a dictionnary with all datas
        reader = csv.DictReader(____)
        # each row in reader is a dictionary by country
        for row in reader:
            # add row in datas list
            datas.___(___)
        # return the list of dictionaries by countries
        return datas

def data_for_country(data, state = "", country = ""):
    # for each country in data
    for pays in ___:
        # if 'Province\State' key match with state given in argument
        # and if 'Country/Region' key match with country given in argument
        if pays[___] == ___ and pays[___] == ___:
            return pays


# here the main code
if __name__ == '__main__':

  # File name of datas
  file = "time_series_19-covid-Confirmed.csv"
  # where datas are located
  url = "https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"

  if download_file(url,file):
      print(f'Téléchargement du fichier {file} terminé avec succès')
      countries = read_CSV(file)
      print("liste des pays et régions recencés")
      print("----------------------------------")
      # for row in coutries:
      #    print(row['Province/State'], row['Country/Region'])
      france = data_for_country(countries, 'France', 'France')
      print(france)

  else:
      print(f'Téléchargement du fichier {file} impossible')
