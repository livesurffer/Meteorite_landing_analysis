# Meteorite_landing_analysis
On this project I used dataset named "meteorite landings" from Nasa.com  
https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh #dataset

About dataset:
This comprehensive data set from The Meteoritical Society contains information on all of the known meteorite landings.
34,513 meteorites and includes info: 
type_of_meteorite
mass_g
fell_found
year
database
coordinate_1
coordinates_2
cartodb_id
created_at
updated_at
year_date
longitude
latitude
geojson

PROJECT GOAL: Goal: Create a graph that displays the locations where meteorites have fallen most frequently, 
              starting from 20 occurrences. Convert the coordinates into geographical locations with their 
              names on the map and also display them on a chart.

Realization:  two Python modules: 1 - meteor.py (fetching data by json format, clearing data and saving certain data into postgresql table)
                                  2 - clearing, sorting and visualizing data.

python libraries: requests, psycopg2, matplotlib


#В этом проекте я использовал набор данных "meteorite landings" с веб-сайта Nasa.com
https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh

О наборе данных: 
Этот набор данных от The Meteoritical Society содержит информацию о всех известных местах падения метеоритов. 
В набор входит 34,513 метеоритов c информацией о них: 
- тип метеорита
- масса в граммах
- год падения/обнаружения
- координата 1, координата 2
- cartodb_id
- created_at
- updated_at
- year_date
- долгота
- широта,
- geojson.

Цель проекта: Создать график, который показывает места, где метеориты падали наиболее часто, начиная с 20 случаев. 
Преобразовать координаты в географические местоположения с их названиями на карте, а также отобразить их на графике. 

Реализация: два модуля на языке Python: 1 - meteor.py (получение данных в формате json, обработка и загрузка данных в таблице postgresql) 2 - обработка, сортировка и визуальное представление данные в виде графика.

Библиотеки Python: requests, psycopg2, matplotlib
