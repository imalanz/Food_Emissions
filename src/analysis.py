# Analysis.

from pymongo import MongoClient
import pandas as pd
import time
import importlib
import geopandas as gpd
import json
from cartoframes.viz import Map, Layer, popup_element
from getpass import getpass
import os
import requests
from dotenv import load_dotenv
import pymongo

# PRODUCTION.ipynb

def iterate_column_years (year):
    # iterate 2010
    x = {index:[row[6],row[0],row[2]] for index, row in production.iterrows() if row[4] == year}
    df = pd.DataFrame.from_dict(x, orient="index")
    df.rename(columns= {0: year, 1:"Area", 3:"Item"}, inplace = True)
    df["Item"] = df["Item"].astype(object)
    df["Area"] = df["Area"].astype(object)
    df[year] = df[year].astype(object)
    return df