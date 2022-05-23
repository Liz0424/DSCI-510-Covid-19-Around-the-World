import sys
from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import shutil


def default_function():
    # default mode
    # add the functions/code you need to scrape all your data
    # print all the data you scrape/request but and if it's huge, show the dimensions and a sample
    url_scrape = 'https://www.bbc.com/news/world-51235105'
    content = requests.get(url_scrape)
    soup = BeautifulSoup(content.content, 'html.parser')

    #create dataset 1 and dataset 2
    countries_1_2 = ['US', 'Brazil', 'India', 'Russia', 'Mexico', 'France', 'UK', 'Peru',
                   'Bulgaria', 'Bosnia and Herzegovina', 'Hungary', 'Georgia']
    death_list = []
    death_rate_list = []
    cases_list = []
    dose_rate_list = []
    dose_total_list = []
    for country in countries_1_2:
        name_countries_cases = soup.find_all('tr', attrs={'data-country': country})
        for country_cases in name_countries_cases:
            death = country_cases.get('data-deaths')
            death_list.append(float(death))
            death_rate = country_cases.get('data-death_rate')
            death_rate_list.append(float(death_rate))
            case = country_cases.get('data-cases')
            cases_list.append(case)
        name_countries_vaccine = soup.find_all('tr', attrs={'data-location': country})
        for country_vaccine in name_countries_vaccine:
            dose_rate = country_vaccine.get('data-doses')
            dose_rate_list.append(float(dose_rate))
            dose_total = country_vaccine.get('data-total')
            dose_total_list.append(float(dose_total))
    countries = ['USA', 'Brazil', 'India', 'Russia', 'Mexico', 'France', 'UK', 'Peru',
                 'Bulgaria', 'Bosnia and Herzegovina', 'Hungary', 'Georgia']
    url_api = 'https://corona-api.com/countries'
    response = requests.get(url_api)
    js = response.json()
    population_list = []
    country_list = []
    recovered_list = []
    for i in js['data']:
        for country in countries:
            if i['name'] == country:
                country_list.append(country)
                population = i['population']
                population_list.append(population)
                recovered_data = i["latest_data"]['recovered']
                recovered_list.append(recovered_data)
    return countries_1_2,cases_list,death_list,death_rate_list,dose_rate_list,dose_total_list,country_list,population_list,recovered_list


def scrape_function():
    # scrape mode
    # add the functions/code you need to scrape SOME (5 rows per dataset) of your data and print
    # this might be very similar to the default mode
    # you can hard code inputs if need be
    countries_1_2,cases_list,death_list,death_rate_list,dose_rate_list,dose_total_list,country_list,population_list,recovered_list=default_function()

    data_1 = {
        'date':'by 3/29/2022',
        'country': countries_1_2,
        'cases': cases_list,
        'deaths': death_list,
        'death_rate': death_rate_list
    }
    df1 = pd.DataFrame(data_1, index=[i + 1 for i in range(len(countries_1_2))])
    # dose dataset
    data_2 = {
        'date': 'by 3/29/2022',
        'country': countries_1_2,
        'dose_rate': dose_rate_list,
        'dose_total': dose_total_list
    }
    df2 = pd.DataFrame(data_2, index=[i + 1 for i in range(len(countries_1_2))])
    data_3 = {
        'date': 'by 3/29/2022',
        'country': country_list,
        'population': population_list,
        'recovered': recovered_list
    }
    df3 = pd.DataFrame(data_3, index=[i + 1 for i in range(len(country_list))])
    return df1,df2,df3


d1,d2,d3=scrape_function()
def static_function(file_1,file_2,file_3):
    # static mode
    # add the functions/code you need to open and print the static copies of your data
    # you can use the path provided in the command line argument to open the data
    print(d1)
    print(d2)
    print(d3)
    file_1 = 'cases_and_deaths_dataset.csv'
    file_2 = 'covid_vaccine_dataset.csv'
    file_3 = 'population_and_recovered_dataset.csv'
    d1.to_csv(file_1)
    d2.to_csv(file_2)
    d3.to_csv(file_3)
    shutil.move(file_1,'dataset')
    shutil.move(file_2,'dataset')
    shutil.move(file_3,'dataset')






if __name__ == '__main__':  # for your purpose, you can think of this line as the saying "run this chunk of code first"
    if len(sys.argv) == 1:  # this is basically if you don't pass any additional arguments to the command line
        # default mode
        # print eveything or the dimensions and a sample
        print('this is default mode and this is all data that I scrape:')
        print('the following lists are countries for dataset 1 and 2,cases,deaths,death rates,'
              'dose rate,dose total,countries for dataset 3,population,recovered number respectively')
        print(default_function())

    elif sys.argv[1] == '--scrape':  # if you pass '--scrape' to the command line
        # scrape mode
        # print a sample of the data you retrieve from your sources
        print('this is the scrape mode and I return first 5 rows of each dataset:')
        print(d1[:5])
        print(d2[:5])
        print(d3[:5])

    elif sys.argv[1]=='--static':  # if you pass '--static' to the command line
        # static mode
        # print a sample of the static datasets you have built from your scraping
        print('this is the static mode:')
        path_1=sys.argv[1]
        path_2=sys.argv[1]
        path_3=sys.argv[1]
        static_function(path_1,path_2,path_3)




