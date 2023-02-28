USE Food_emissions;

-- Create primary key in table food.
ALTER TABLE food
	ADD PRIMARY KEY (food_id);

-- create primary key in table country.
ALTER TABLE Country
	ADD PRIMARY KEY (Country_id);

-- Create foreign key to area_harvested table. 
ALTER TABLE area_harvested
	ADD FOREIGN KEY (food_id)
	REFERENCES Food (Food_id)
		ON DELETE SET NULL;

ALTER TABLE area_harvested	
	ADD FOREIGN KEY (Country_id)
	REFERENCES Country (Country_id)
		ON DELETE SET NULL;

-- Create foreign key to emissions table.
ALTER TABLE emissions
	ADD FOREIGN KEY (food_id)
	REFERENCES Food (food_id)
		ON DELETE SET NULL;

ALTER TABLE emissions	
	ADD FOREIGN KEY (Country_id)
	REFERENCES Country (Country_id)
		ON DELETE SET NULL;		

-- Create foreign key to producer_price table.
ALTER TABLE producer_price
	ADD FOREIGN KEY (food_id)
	REFERENCES Food (food_id)
		ON DELETE SET NULL;

ALTER TABLE producer_price	
	ADD FOREIGN KEY (Country_id)
	REFERENCES Country (Country_id)
		ON DELETE SET NULL;	

-- Create foreign key to production_quantity table.
ALTER TABLE production_quantity
	ADD FOREIGN KEY (food_id)
	REFERENCES Food (food_id)
		ON DELETE SET NULL;

ALTER TABLE production_quantity	
	ADD FOREIGN KEY (Country_id)
	REFERENCES Country (Country_id)
		ON DELETE SET NULL;	