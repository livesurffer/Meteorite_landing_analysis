#!/usr/bin/python
import psycopg2
import requests
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

#Connect to PostgreSQL and retrieve data
connection = psycopg2.connect(
    host="127.0.0.1",
    database="postgres",
    user="barmin",
    password="barmin",
    port="5432"
)
cursor = connection.cursor()

query = "SELECT latitude, longitude, count_duplicates FROM (SELECT latitude, longitude, COUNT(*) AS count_duplicates FROM meteoritedata WHERE latitude IS NOT NULL AND longitude IS NOT NULL AND latitude <>0 AND longitude <>0 GROUP BY latitude,longitude HAVING COUNT(*) > 20) as data;"

cursor.execute(query)
data = cursor.fetchall()

cursor.close()
connection.close()

# Get address from coordinates. No google maps api key now.
def get_mapsname(lat, lng):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key=YOUR_GOOGLE_MAPS_API_KEY"
    response = requests.get(url)
    data = response.json()
    if data["results"]:
        return data["results"][0]["formatted_address"]
    return "Unknown"

location_data = []
for lat, lng, counts in data:
    location_name = get_mapsname(lat, lng)
    location_data.append((location_name, counts))

#Data Visualization - Histogram
location_names, counts = zip(*location_data)
plt.bar(location_names, counts)
plt.xticks(rotation=90)
plt.xlabel('Location Names')
plt.ylabel('Counts')
plt.title('Histogram of Counts for Different Location Names')
plt.tight_layout()
plt.savefig('/home/acronym/meteorite_land/meteorite_project/histogram.png')

