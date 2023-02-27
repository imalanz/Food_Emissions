# Analysis.
import pandas as pd


from getpass import getpass

# clean first df.
def clean_df (df):
    # Drop columns.
    df.drop(columns=["Domain", "Domain Code", "Element Code", "Element", "Year Code"],inplace=True)
    # Change columns names
    df.rename(columns={"Area Code (M49)":"Country_Code", "Item Code (CPC)": "Food_Code",
                     "Area":"Country", "Item":"Food"}, inplace= True)
    return df

# clean first df in price db.
def clean_df_price (df):
    # Drop columns.
    df.drop(columns=["Domain", "Months Code", "Months", "Domain Code", "Element Code", "Element", "Year Code"],inplace=True)
    # Change columns names
    df.rename(columns={"Area Code (M49)":"Country_Code", "Item Code (CPC)": "Food_Code",
                     "Area":"Country", "Item":"Food"}, inplace= True)
    return df

# iterate trhow column years to pass each year with its oun column with values.
def iterate_column_years (df, year):
    x = {index:[row[0],row[1],row[2],row[3],row[6]] for index, row in df.iterrows() if row[4] == year}
    y = pd.DataFrame.from_dict(x, orient="index")
    y.rename(columns= {0: "Country_Code", 1:"Country", 2:"Food_Code", 3:"Food", 4:year}, inplace = True)
    y["Food"] = y["Food"].astype (object)
    y["Country"] = y["Country"].astype(object)
    y[year] = y[year].astype(object)
    
    return y.drop_duplicates(subset=['Country_Code', 'Food_Code'], keep='last')

# Second type of cleaning after new year dataframes.
def clean2_df (df):
    df.drop(columns=["Year", "Value"],inplace=True)
    df["Food_Code"] = df["Food_Code"].astype(object)
    df["Country_Code"] = df["Country_Code"].astype(object)
    # drop duplicates.
    df.drop_duplicates(inplace=True)
    return df

# Merging all years df to main. 2010 - 2021
def merging_production_area (df, df2010, df2011, df2012, df2013, df2014, df2015, df2016, df2017, df2018, df2019, df2020, df2021):
    z = pd.merge(df, df2010, how="left").merge(df2011, how="left").merge(df2012, how="left")
    z = pd.merge(z, df2013, how="left").merge(df2014, how="left").merge(df2015, how="left")
    z = pd.merge(z, df2016, how="left").merge(df2017, how="left").merge(df2018, how="left")        
    z = pd.merge(z, df2019, how="left").merge(df2020, how="left").merge(df2021, how="left")  
    return z

# Merging all years df to main in price db, no 2021 year.
def merging_price (df, df2010, df2011, df2012, df2013, df2014, df2015, df2016, df2017, df2018, df2019, df2020):
    z = pd.merge(df, df2010, how="left").merge(df2011, how="left").merge(df2012, how="left")
    z = pd.merge(z, df2013, how="left").merge(df2014, how="left").merge(df2015, how="left")
    z = pd.merge(z, df2016, how="left").merge(df2017, how="left").merge(df2018, how="left")        
    z = pd.merge(z, df2019, how="left").merge(df2020, how="left") 
    return z

# Cleaning and replacing the food names for matching other df.
def replace_items (df):
    import re
    # Clean with regex column "Items" to match other Data Frames.
    df["Food"] = df["Food"].str.replace("n\.e\.c\.", "", regex=True)
    df["Food"] = df["Food"].str.replace(".*Other berries and fruits of the genus vaccinium.*", 'Berries & Grapes', regex=True)
    df["Food"] = df["Food"].str.replace('.*Onions and shallots, green*.', 'Onions & Leeks', regex=True)
    df["Food"] = df["Food"].str.replace(".*Beer of barley, malted*.", 'Beer', regex=True)
    df["Food"] = df["Food"].str.replace(".*Barley*.", 'Beer', regex=True)
    df["Food"] = df["Food"].str.replace('.*Brazil nuts, in shell*.', "Nuts", regex=True)
    df["Food"] = df["Food"].str.replace(".*Cocoa beans*.", "Chocolate", regex=True)
    df["Food"] = df["Food"].str.replace('.*Coffee, green*.', "Coffee", regex=True)
    df["Food"] = df["Food"].str.replace('.*Groundnuts, excluding shelled*.', "Groundnuts", regex=True)
    df["Food"] = df["Food"].str.replace('.*Edible roots and tubers with high starch or inulin content, , fresh*.', 'Root Vegetables', regex=True)
    df["Food"] = df["Food"].str.replace('.*Oats*.', "Oatmeal", regex=True)
    df["Food"] = df["Food"].str.replace('.*Other citrus fruit,*.', 'Citrus Fruit', regex=True)
    df["Food"] = df["Food"].str.replace('.*Other fruits*.', 'Other Fruit', regex=True)
    df["Food"] = df["Food"].str.replace('.*Meat of pig with the bome, fresh or chilled', "Pig Meat", regex=True)
    df["Food"] = df["Food"].str.replace('.*Meat of cattle with the bone, fresh or chilled', 'Beef', regex=True)
    df["Food"] = df["Food"].str.replace('.*Walnuts, in shell*.', 'Nuts', regex=True)
    df["Food"] = df["Food"].str.replace('.*Hazelnuts, in shell*.', 'Nuts', regex=True)
    df["Food"] = df["Food"].str.replace('.*Peas, dry*.', 'Peas', regex=True)
    df["Food"] = df["Food"].str.replace('.*Sugar beet*.', 'Beet Sugar', regex=True)
    df["Food"] = df["Food"].str.replace('.*Soya beans*.', 'Beet Sugar', regex=True)
    df["Food"] = df["Food"].str.replace('.*Other vegetables, fresh *.', 'Other Vegetables', regex=True)
    df["Food"] = df["Food"].str.replace('.*Hen eggs in shell, fresh*.', 'Eggs', regex=True)
    df["Food"] = df["Food"].str.replace('.*Gooseberries*.', 'Berries & Grapes', regex=True)
    df["Food"] = df["Food"].str.replace('.*Raw hides and skins of sheep or lambs*.', 'Lamb & Mutton', regex=True)
    df["Food"] = df["Food"].str.replace('.*Strawberries*.', 'Berries & Grapes', regex=True)
    df["Food"] = df["Food"].str.replace('.*Cranberries*.', 'Berries & Grapes', regex=True)
    df["Food"] = df["Food"].str.replace('.*Raw milk of cattle*.', 'Milk', regex=True)
    df["Food"] = df["Food"].str.replace('.*Cassava, fresh*.', 'Cassava', regex=True)
    df["Food"] = df["Food"].str.replace('.*Meat of pig with the bone, fresh or chilled*.', 'Pig Meat', regex=True)
    df["Food"] = df["Food"].str.replace('.*Chick peas, dry*.', 'Peas', regex=True)
    df["Food"] = df["Food"].str.replace('.*Sunflower-seed oil, crude*.', 'Sunflower Oil', regex=True)
    df["Food"] = df["Food"].str.replace('.*Meat of chickens, fresh or chilled*.', 'Poultry Meat', regex=True)
    df["Food"] = df["Food"].str.replace('.*Rapeseed or canola oil, crude*.', 'Rapeseed Oil', regex=True)
    df["Food"] = df["Food"].str.replace('.*Peas, green*.', 'Peas', regex=True)
    df["Food"] = df["Food"].str.replace('.*Cow peas, dry*.', 'Peas', regex=True)
    df["Food"] = df["Food"].str.replace('.*Raspberries*.', 'Berries & Grapes', regex=True)
    df["Food"] = df["Food"].str.replace('.*Blueberries*.', 'Berries & Grapes', regex=True)
    df["Food"] = df["Food"].str.replace('.*Cheese from whole cow milk*.', 'Cheese', regex=True)
    df["Food"] = df["Food"].str.title()
    df["Food"] = df["Food"].str.strip()
    return df


# For emissions DB.
#Cleaning raw db.
 
def cleaning_emissions (df): 
    # Drop not necesary columns.   
    df = df.drop(columns=["Eutrophying emissions per 1000kcal (gPO₄eq per 1000kcal)", "Eutrophying emissions per 100g protein (gPO₄eq per 100 grams protein)",
    "Freshwater withdrawals per 1000kcal (liters per 1000kcal)", "Freshwater withdrawals per 100g protein (liters per 100g protein)",
    "Greenhouse gas emissions per 100g protein (kgCO₂eq per 100g protein)", "Land use per 1000kcal (m² per 1000kcal)", "Land use per 100g protein (m² per 100g protein)",
    "Scarcity-weighted water use per 100g protein (liters per 100g protein)", "Scarcity-weighted water use per 1000kcal (liters per 1000 kilocalories)",
    "Land use change", "Animal Feed", "Farm", "Processing", "Transport", 
    "Packging", "Retail", "Total_emissions"])
    #Change names of columns.
    df.rename(columns= {"Eutrophying emissions per 1000kcal (gPO₄eq per 1000kcal)": "Eutrophying emissions (gPO₄eq per 1000kcal)", 
                "Freshwater withdrawals per kilogram (liters per kilogram)":"Freshwater withdrawals (liters per kilogram)", 
                "Greenhouse gas emissions per 1000kcal (kgCO₂eq per 1000kcal)":"Greenhouse gas emissions (kgCO₂eq per 1000kcal)",
                "Land use per kilogram (m² per kilogram)":"Land use (m² per kilogram)", 
                "Scarcity-weighted water use per kilogram (liters per kilogram)":"Scarcity-weighted water use (liters per kilogram)",
                "Food product": "Food"}, inplace = True)       
    return df

# Clean with regex column "Items" to match other Data Frames.
def cleaning_item_column_emissions (df):
    df["Food"] = df["Food"].str.strip()
    df["Food"] = df["Food"].str.replace('Beef (dairy herd)', "dairy", regex=True)

    df["Food"] = df["Food"].str.replace('([\(\[]).*?([\)\]])', "", regex=True)

    df["Food"] = df["Food"].str.replace('.*Wheat & Rye*.', "Wheat", regex=True)
    df["Food"] = df["Food"].str.replace('.*Barley*.', "Beer", regex=True)
    df["Food"] = df["Food"].str.replace('.*Soymilk*.', "Soya beans", regex=True)
    df["Food"] = df["Food"].str.replace('.*Dark Chocolate*.', "Chocolate", regex=True)
    df["Food"] = df["Food"].str.replace('.*Cane Sugar*.', "Sugar cane", regex=True)

    return df