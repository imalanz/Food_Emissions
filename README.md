# Food_Emissions_Proy4

![portada](https://github.com/imalanz/_proy4/blob/main/images/a.jpg?raw=true)

## Introduction
Food industry is a crucial part of our lives, but we seldom realize how much it contributes to polluting the environment. In this project, we aimed to calculate the emissions produced by the most consumed foods and predict the future of the food industry and its impact on our planet.

### Process.
To achieve our goal, we extracted data from various sources such as the Food and Agriculture Organization of the United Nations and Kaggle. We transformed the data into a database and analyzed it by cleaning and matching it to make new columns with relevant information. We then imported the data into a SQL structure and used Tableau for better graphic analysis of the data.

![portada](https://github.com/imalanz/_proy4/blob/main/images/b.jpg?raw=true)

## Data Bases.

We obtained most of the data from the Food and Agriculture Organization of the United Nations and Kaggle. We collected information related to production, quantity, area harvested, and pollution.

### Emissions DB.

We obtained data related to emissions from Kaggle, which provided technical information about the quantity of pollution for each type of food. The data included Eutrophying emissions, Water withdrawals, Greenhouse gases, Scarcity-weighted water use, and Land use. 

- "Eutrophying emissions": Eutrophying emissions represent runoff of excessnutrients into the surrounding environment andwaterways, which affect and pollute ecosystems.
- "Water withdrawals": or water abstractions, are defined as freshwater taken from ground or surface water sources, either permanently or temporarily, and conveyed to a place of use.
- "Greenhouse gases": (also known as GHGs) are gases in the earth's atmosphere that trap heat.
- "Scarcity-weighted water use": represents freshwater useweighted by local water scarcity. This is measured in litersper kilogram of food product.
- "Land use": the total amount of hectars that the production of each food ocupy.

### Area harvested DB.

We created a database to detect how many hectares of land each type of food needs for their production. The data included information for each year.

### Production quantity DB.
This database provided information about the amount of tonnes produced for each food item each year.
### Producer Price.
The Producer Price table provided insights into the cost of producing each type of food. With this information, we could determine the most recommended business for the producers and make assumptions about the future of the industry.


## SQL structure.
We passed all the new data frames into a SQL structure with primary keys as items ID and connected to each other for better comprehension.

![portada](https://github.com/imalanz/_proy4/blob/main/images/f.png?raw=true)
## Graphic exploration.

We created Geo-spatial graphs to visualize the data related to Area Harvested, Production Quantity, and Producer Prices. These graphs helped us gain better insight into the data and understand the variations across different countries.
### Area harvested.
- Geo spatial graph to see the quantity of area in Hectaries that each contry uses.

![area](https://github.com/imalanz/FoodEmissions_proy4/blob/main/images/area.jpg?raw=true)

### Production quantity.
- Geo spatial graph for a better comprehention in the quantity of production in tonnes of different types of food.

![production](https://github.com/imalanz/FoodEmissions_proy4/blob/main/images/production.jpg?raw=true)

### Producer prices USD.
- Graph of differences in costs of the acumulated foods per country.

![price](https://github.com/imalanz/FoodEmissions_proy4/blob/main/images/price.jpg?raw=true)


[For the complete graphic study](https://public.tableau.com/app/profile/imanol.lanzagorta.diaz/viz/FoodEmissions_16775259232060/Story3?publish=yes)


## Conclution.
The project highlights the significant impact of the food industry on the environment. Every food item we consume contributes to pollution, which can have a long-term impact on the planet. We need to take care of ourselves and our planet by being more conscious of our food choices and reducing our carbon footprint.



![portada](https://github.com/imalanz/_proy4/blob/main/images/s.jpg?raw=true)






