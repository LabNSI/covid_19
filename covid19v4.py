############################################
#
# Trace graphs
# Author : MS
# Date : 16/03/2020
#
# Replace the "___" by appropriate code
#
###########################################

import urllib.request as urllib2
import csv
import matplotlib.pyplot as plt

def download_file(url, file_name):
    '''
    Download a file from url and copy it localy with file_name as name
    '''
    try:
        # open url get in argument
        file = urllib2.urlopen(url)
        # open file for writing in binary mode
        # https://docs.python.org/3/library/functions.html#open
        with open(file_name, 'wb') as output:
            # write in output the file read
            output.write(file.read())
        # OK : return true
        return True
    except:
        # Somthing is wrong : return false
        return False

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
        reader = csv.DictReader(csvfile)
        # each row in reader is a dictionary by country
        for row in reader:
            # add row in datas list
            datas.append(row)
        # return the list of dictionaries by countries
        return datas

def data_for_country(data, state = "", country = ""):
    # for each country in data
    for pays in data:
        # if 'Province\State' key match with state given in argument
        # and if 'Country/Region' key match with country given in argument
        if pays['Province/State'] == state and pays['Country/Region'] == country:
            return pays

def trace_data_for_country(country):
    '''
    Prepare lists of datas for x and y axis
    '''
    # x is an empty list
    x = ___
    # y is an empty list
    y = ___
    # browse through the country dictionary to get datas.
    # - Keys contain datas for x axis (dates)
    # - Values contain datas for y axis (number of daily cases)
    #for key, value in country.___():
    for key, value in country.items():
        # Filter inappropriate keys
        if key != 'Province/State' and key !='___' and key != '___' and key != '___':
            # Add key to the x list
            x.___(___)
            # add value to the y list.
            # value must be an integer
            y.___(int(___))
    # return a tuple of lists x,y
    return x,y

        
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
        chine = data_for_country(countries, 'Hubei', 'China')
        france = data_for_country(countries, 'France', 'France')
        italie = data_for_country(countries, '', 'Italy')
        
        print(chine)
        print(france)
        print(italie)

        # Figure dimensions
        plt.figure(figsize=(10, 7))

        # Rotate ticks and labels of the x-axis
        plt.xticks(rotation=90)

        # Plot datas for China
        x , y = trace_data_for_country(chine)
        plt.plot(x, y, label="Chine")

        # Plot datas for France
        ___
        ___

        # Plot datas for Italy
        ___
        ___

        # Add title to graph : "Infectés"
        ___

        # Add legend to graph
        plt.___()
        # Show graph
        plt.___()
        # Save the figure as '19-covid-Confimed.png'
        plt.___('9-covid-Confimed.png')
        # Close graph
        plt.___()
        
    else:
        print(f'Téléchargement du fichier {file} impossible')

    
    




    





