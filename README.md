# DSCI 510 Final Project

## Description: 
I created two python files, scrape.py and plot.py. Scrape.py is a .py file with scraping the data, the primary python file, and plot.py is a .py file with getting analysis graphs for this project.
As for scrape.py, I identify some countries (USA, Brazil, India, Russia, Mexico, France, UK, Peru, Bulgaria, Bosnia and Herzegovina, Hungary, Georgia) based on the high number of death rate, 
death number, and total number of cases on the url, then I have created the dataset cases_and_deaths_dataset.csv with each country's death rate, 
death number, total number of confirmed cases of covid-19, and the date "by 3/29/2022' on each row; based on the countries from dataset named cases_and_deaths_dataset.csv, 
then I created the dataset covid_vaccine_dataset.csv with each country's vaccination rate, vaccination number, and the date "by 3/29/2022' on each row; 
another dataset titled population_and_recovered_dataset.csv with each country's population, the number of recovered, and the date 'by 3/29/2022' on each row; 
meanwhile, in terms of plot.py, I make four bar graphs based on each country's death number, population, dose number, and recovered number: 
Bar Graph for Death Number of Each Country by 3/29/2022, Bar Graph for Population of Each Country by 3/29/2022, Bar Graph for Dose Number of Each Country by 3/29/2022, 
Bar Graph for Recovered Number of Each Country by 3/29/2022; and one line plot graph based on the each country's population and recovered number: Plot for Recovered Rate in Each Country by 3/29/2022. 

## Requirements: 
Following requirements are needed to be satisfied to run all the codes:
Packages to be installed:
1.bs4
2.requests
3.pandas
4.matplotlib
To install above packages use the following command: pip install -r requirements.txt
'requirements.txt' file has a list of all the necessary packages required to run this code.



## Data Sources:
1.Number of Total Cases, Death Rate, and Deaths by Country Over the World(https://www.bbc.com/news/world-51235105)
One data table from this URL shows the total number of confirmed cases, death rate, and deaths from over 100 different countries respectively by 
March 29th, 2022 after covid-19 outbreak. I will use top 5 countries (US, Brazil, India, Russia, and Mexico) based on the highest number of covid-19 death 
cases during this covid-19 outbreak, other 5 top countries (US, India, Brazil, France, and UK) in terms of highest cases of covid-19, and other top 5 countries 
(Peru, Bulgaria, Bosnia and Herzegovina, Hungary, and Georgia) with regard to highest death rates for this covid-19 outbreak into my analysis dataset 1.

2.Number of Vaccination and Vaccination Rate By Country Around the World(https://www.bbc.com/news/world-51235105)
Another data table from this website reflects the total number of fully vaccinations and vaccination rates from over 100 different countries respectively 
by March 29th, 2022 after covid-19 outbreak. Based on dataset 1, I will track the number of doses of vaccination and vaccination rates from countries of 
dataset 1 around the world during this covid-19 outbreak and put these data into my analysis dataset 2. 

3.API about Detailed Information of Different Countries Related to Covid-19(https://about-corona.net/documentation)
Json Link: https://corona-api.com/countries
Based on dataset 1 and dataset 2, I will use this API to identify the countries which I choose from dataset 1 and dataset 2 to get the overall number of 
recovered cases and population of each country by March 29th, 2022 in my analysis dataset 3.



## Running the code file named scrape.py:
The code can be run in three modes:default, scrape, and static

Default mode: To run the code in default mode, type command - python3 Weiqian_Zhang_HW4_DSCI510.py
In this mode, I make one list of these countries (US, Brazil, India, Russia, Mexico, US, India, Brazil, France, UK, Peru, Bulgaria, Bosnia and Herzegovina, Hungary, 
and Georgia) to scrape the data information from BBC News link(https://www.bbc.com/news/world-51235105) and make another country list(USA, Brazil, India, Russia, 
Mexico, US, India, Brazil, France, UK, Peru, Bulgaria, Bosnia and Herzegovina, Hungary, and Georgia) to scrape information from API, finally this mode will print out 
all the information that I scrape list by list.
(Note:US and USA represents the United States, these two country lists could help me easier scrape the data information that I need.)

Scrape mode: To run the code in scrape mode, type command - python3 Weiqian_Zhang_HW4_DSCI510.py --scrape
In this mode, I make 3 datasets based on the data of default mode, print out first 5 rows of each dataset and return the 3 datasets in the scrape function.

Static mode: To run the code in scrape mode, type command - python3 Weiqian_Zhang_HW4_DSCI510.py --static
In this mode, I print out the 3 datasets from the returning output of scrape mode, make these datasets into three csv files(cases_and_deaths_dataset.csv,covid_vaccine_dataset.csv,and
population_and_recovered_dataset.csv), and I move these csv files into the folder named dataset in python. 
(Note: in order to make sure the csv files can be put in the folder named dataset when you run in the command line of the code, you have to delete all the files from the folder named dataset and 
run in the command line of the code again).



## Running the code file named plot.py:
First, I just import the scrape.py, then write some codes which you can just run the code directly, and finally you can get the graphs which can be used to be analyzed. 
