############################################
#
# Trace graphs
# Author : MS
# Date : 16/03/2020
# Update : 09/01/2022
#
# Replace the "___" by appropriate code
#
###########################################

import urllib.request as urllib2
import csv
import matplotlib.pyplot as plt
from covid19v1 import *
from covid19v2 import *
from covid19v3 import *


def trace_data_for_country(country):
    '''
    Prepare lists of datas for x and y axis
    '''
    # x is an empty list
    x = ___
    # y is an empty list
    y = ___
    # browse through the country dictionary to get datas.
    # - Keys contain dates
    # - Values contain datas for y axis (number of daily cases)
    # x axis contains the number of days since the beginning of pandemic
    day = 0

    #for key, value in the country dictionnary
    for key, value in ___:
        # Filter inappropriate keys
        if key != 'Province/State' and key !='___' and key != '___' and key != '___':
            # Add day number to the x list
            x.___(___)
            # Prepare for the next day
            day = ___
            # add value to the y list.
            # value must be a number
            y.___(float(___))
    # return a tuple of lists x,y
    return x,y

        
# here the main code
if __name__ == '__main__':

    # File name of datas
    file = "time_series_19-covid-Confirmed.csv"
    # where datas are located
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

    if download_file(url,file):
        print(f'Téléchargement du fichier {file} terminé avec succès')
        countries = read_CSV(file)
        
        chine = data_for_country(countries, 'Hubei', 'China')
        france = data_for_country(countries, '', 'France')
        italie = data_for_country(countries, '', 'Italy')
        
        print(chine)
        print(france)
        print(italie)

        # Figure dimensions
        plt.figure(figsize=(10, 7))


        # Plot datas for China
        x , y = trace_data_for_country(chine)
        plt.plot(x, y, label="Chine")

        # Plot datas for France
        ___
        ___

        # Plot datas for Italy
        ___
        ___

        # Add title to graph : "Infectés COVID-19 depuis le 22/01/2020"
        ___

        # Add label on x axis : 'Nombre de jours'
        ___

        # Add label on y axis : 'Nombre de contaminés'
        ___

        # Add legend to graph
        plt.___()

        # Save the figure as an image
        plt.___('covid19-Confimed.png')
        
        # Show graph
        plt.___()
        
        # Close graph
        plt.___()
        
    else:
        print(f'Téléchargement du fichier {file} impossible')

    
    




    





