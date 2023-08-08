"""This script is not complete.
It is an excerpt of code from the command history."""

import requests
import time
import pickle

import pandas as pd
import googlemaps

import sql_helper as sql

key = "thisisnotmycode"

gmaps = googlemaps.Client(key=key)
#
db = sql.Database()
geo = db.easy_merge({"city": ["citiy"], "country": ["country"]})

response = requests.get('https://restcountries.com/v3.1/all').json()



countries = [{"name": r["name"]["common"], "region": r["region"], "subregion": r["subregion"] if "subregion" in r else r["region"]} for r in response]
df = pd.DataFrame(countries)
geo2 = geo.merge(df, left_on="country_country", right_on="name", how="left")
countries = [{"name": r["name"]["official"], "region": r["region"], "subregion": r["subregion"] if "subregion" in r else r["region"]} for r in response]
df = pd.DataFrame(countries)
geo3 = geo.merge(df, left_on="country_country", right_on="name", how="left")
countries = [{"name": r["altSpellings"][1] if len(r["altSpellings"])>1 else "", "region": r["region"], "subregion": r["subregion"] if "subregion" in r else r["region"]} for r in response]
df = pd.DataFrame(countries)
geo4 = geo.merge(df, left_on="country_country", right_on="name", how="left")
geo5 = geo2.combine_first(geo3).combine_first(geo4)
geo5.to_excel(file_prefix+"countries.xlsx")


countries = pd.read_excel("countries.xlsx")


geocode_results = []
locations = list(countries.city + ", "+ countries.country)
for location in locations:
    geocode_results.append(gmaps.geocode(location))
    time.sleep(0.02)



with open('geocodes.pkl', 'wb') as f:
    pickle.dump(geocode_results, f)
