############################################
#
# Read a csv file
# Author : MS
# Date : 16/03/2020
#
# Replace the "___" by appropriate code
#
###########################################

import urllib.request as urllib2
from covid19v1 import *
import csv



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

        
# here the main code
if __name__ == '__main__':

    # File name of datas
    file = "time_series_covid19_confirmed_global.csv"
    # where datas are located
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

    if download_file(url,file):
        print(f'Téléchargement du fichier {file} terminé avec succès')
        coutries = read_CSV(file)
        print("liste des pays et régions recencés")
        print("----------------------------------")
        for row in coutries:
            print(row['Province/State'], row['Country/Region'])
    else:
        print(f'Téléchargement du fichier {file} impossible')

    
    




    





