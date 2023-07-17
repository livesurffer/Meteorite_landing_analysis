#!/usr/bin/python

import requests
import pandas as pd

r = requests.get('https://data.nasa.gov/resource/gh4g-9sfh.json?$limit=50000')
meteor_data = r.json()
df = pd.DataFrame(meteor_data)
print(df.shape)
##print(meteor_data)
