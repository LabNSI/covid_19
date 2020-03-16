import urllib.request as urllib2
import csv

############################################
#
# Read a csv file
# Author : MS
# Date : 16/03/2020
#
# Replace the "___" by appropriate code
#
###########################################

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
            output.(file.___())
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

        
# here the main code
if __name__ == '__main__':

    # File name of datas
    file = "time_series_19-covid-Confirmed.csv"
    # where datas are located
    url = "https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"

    if download_file(url,file):
        print(f'Téléchargement du fichier {file} terminé avec succès')
        coutries = read_CSV(file)
        print("liste des pays et régions recencés")
        print("----------------------------------")
        for row in coutries:
            print(row['Province/State'], row['Country/Region'])
    else:
        print(f'Téléchargement du fichier {file} impossible')

    
    




    





