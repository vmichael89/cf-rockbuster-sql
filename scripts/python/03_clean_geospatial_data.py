"""This script is not complete.
It is an excerpt of code from the command history."""

import requests
import time
import pickle

import pandas as pd
import googlemaps

import sql_helper as sql

# connect to Rockbuster database
db = sql.Database()
# select city and country columns which need to be cleaned
geo = db.easy_merge({"city": ["city"], "country": ["country"]})


# first look at the countries
# get countries and meta date from a public API
response = requests.get('https://restcountries.com/v3.1/all').json()

# use various metadata from the API to identify the countries and additionally get its region and subregion
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
geo5.to_excel("countries.xlsx")


# load data with cleaned country data
countries = pd.read_excel("countries.xlsx")

# intialize google maps API
gmaps = googlemaps.Client(key="thisisnotmykey")

# loop over city and country to get the location (lat, lng) for each city
# this takes a while
geocode_results = []
locations = list(countries.city + ", "+ countries.country)
for location in locations:
    geocode_results.append(gmaps.geocode(location))
    # API calls are limited to 50 per second
    time.sleep(0.02)

# store the results to file
with open('geocodes.pkl', 'wb') as f:
    pickle.dump(geocode_results, f)


# MISSING
# the part that saves the data to countries_geo.xlsx