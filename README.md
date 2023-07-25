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
              names on the map and also display them on the graph. Use the matplotlib library.

Realization:  two python modules: 1 - meteor.py (fetching data by json format, saving certain data into postgresql table, clearing data)
                                  2 - clearing, sorting and visualizing data

                                

