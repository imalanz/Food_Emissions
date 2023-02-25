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

# adding a column with the year and in the rows the cuantity of production in ton.
def adding_yearcolumns (df, year):
    # iteration to create a dictionary getting the values in the column year.
    _1999 = {index:row[4] for index, row in df.iterrows() if row[2] == year}
    df1999 = pd.DataFrame.from_dict(_1999, orient="index")
    df1999.rename(columns= {0: 1999}, inplace = True)
    # return df.
    return pd.concat([df, df1999], axis = 1)