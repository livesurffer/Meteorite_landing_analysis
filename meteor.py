#!/usr/bin/python

import requests
import  psycopg2

r = requests.get('https://data.nasa.gov/resource/gh4g-9sfh.json?$limit=50000')
print(r.status_code)
meteor_data = r.json()
con=psycopg2.connect(
	database="postgres",
	user="barmin",
	password="barmin",
	host="127.0.0.1",
	port="5432"
)

cursor=con.cursor()


for item in meteor_data:
	place=item['name']
	nametype=item['nametype']
	recclass=item['recclass']
	fall=item['fall']

	if 'mass' in item and item['mass'] is not None:
		meteor_mass = item['mass']

	else:
		meteor_mass = None

	if 'year' in item and item['year'] is not None:
		date=item['year']
		short_date=date[0:10]+' 00:00:00'
	else:
		short_date=None

	if 'reclat' in item and item['reclat'] is not None:
		latitude=item['reclat']
	else:
		latitude=None

	if 'reclong' in item and item['reclong'] is not None:
		longitude=item['reclong']
	else:
		longitude=None

	cursor.execute('insert into meteoritedata(place,nametype,recclass,"mass g",fall,date,latitude,longitude)values(%s,%s,%s,%s,%s,%s,%s,%s)',
	(place,nametype,recclass,meteor_mass,fall,short_date,latitude,longitude))
	con.commit()
con.close()
