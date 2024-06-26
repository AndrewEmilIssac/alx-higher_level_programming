-- creates the database hbtn_0d_usa and the table cities on your MySQL server.
   -- name VARCHAR(256) - can't be null
   -- If the table hbtn_0d_usa already exists, script should not fail
   -- If the table cities already exists, script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
       id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
       state_id INT NOT NULL,
       FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id),
       name VARCHAR(256) NOT NULL);
