ALTER TABLE participant
	ADD FOREIGN KEY (client) -- in participants table
REFERENCES client(client_id) -- primary key on client table
ON DELETE SET NULL;