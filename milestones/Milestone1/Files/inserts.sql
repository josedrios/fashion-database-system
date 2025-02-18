-- Script name: inserts.sql
-- Author:      Jose Rios
-- Purpose:     insert sample data to test the integrity of this database system
   
-- the database used to insert the data into.
USE FashionDesignDB; 

-- for copy and past purposes, delete later:
-- INSERT INTO User (user_id, email, full_name) VALUES (,,), (,,), (,,);
   
-- User table inserts
INSERT INTO User (user_id, email, full_name) VALUES (1, 'jr@email.com', 'Jose Rios'), (2, 'js@email.com', 'John Smith'), (3, 'bc@email.com', 'Betty Carter');

-- Account table inserts
INSERT INTO Account (account_id, password, user_id) VALUES (1, 'hidden123',  1), (2, 'password123', 2), (3, 'passcode@241', 3);

-- Region table inserts
INSERT INTO Region (region_id, country, state) VALUES (1, 'United State of America',  'California'), (2, 'Mexico', 'Jalisco'), (3, 'Italy', 'Sicily');

-- Language table inserts
INSERT INTO Language (language_id, name, dialect) VALUES (1, 'English',  'Standard'), (2, 'Spanish', 'Spain'), (3, 'Chinese', 'Hokkien');

-- Company table inserts
INSERT INTO Company (company_id, description, employee_count, team_count, project_count, name) VALUES (1, 'Welcome to our company', 12, 3, 2, 'Punk Models'), (2, 'This is our new company', 8, 3, 1, 'Cool Models'), (3, 'Hello, we have a big diverse company', 80, 10, 10,'Diverse Models');

-- Fashion Genre table inserts
INSERT INTO `Fashion Genre` (genre_id, name, description) VALUES (1, 'Old Money',  'Influenced by old, comfortable clothing'), (2, 'Punk', 'Contains darker, spiker clothing'), (3, 'Professional', 'Containg suits and dresses');

-- Registered Viewer table inserts
INSERT INTO `Registered Viewer` (viewer_id, full_name, biography, gender, username, account_id, language_id, region_id) VALUES (1, 'Jose Rios',  'This is my account', 'male', 'MyUser123', 1,1, 1), (2, 'John Smith',  'Welcome to my account', 'male', 'Account12', 2,2, 2), (3, 'Betty Carter',  'This is my account, welcome', 'female', 'Carter23', 3,3, 3);

-- Model table inserts
INSERT INTO Model (model_id, height, weight, gender, full_name, biography, account_id, fashiongenre_id, language_id, region_id, team_id) VALUES (1, 175,  185, 'male', 'Jose Rios', 'Welcome to my model account',1, 1, 1, 1, 1), (2, 185,  175, 'male', 'John Smith', 'Welcome to my modeling page',2, 2, 2, 2, 1), (3, 165,  140, 'female', 'Betty Carter', 'This is my model account',3, 3, 3, 3, 1);

-- Team table inserts
INSERT INTO Team (team_id, name, description, employee_count, project_count, company_id) VALUES (1, 'Cali Show Team',  'This is the team for the cali show', 10, 2, 1), (2, 'NYC Show Team',  'This is the team for the NYC show', 10, 2, 1), (3, 'Texas Show Team',  'This is the team for the texas show', 10, 2, 1);

-- Employer table inserts
INSERT INTO Employer (employer_id, full_name, gender, biography, account_id, fashiongenre_id, language_id, region_id, team_id) VALUES (1, 'Jose Rios', 'male', 'this is my bio', 1, 1, 1, 1, 1), (2, 'John Smith' , 'male', 'my bio', 2, 1, 1, 1, 1), (3, 'Betty Carter', 'female', 'my bio is right here', 3, 1, 1, 1, 1);

-- Project table inserts
INSERT INTO Project (project_id, name, description, employee_count, team_id) VALUES (1, 'Cali Morning Project',  'This is the morning project', 5, 1), (2, 'NYC Night Project',  'NYC Night Project', 2, 1), (3, 'Texas Afternoon Project',  'Afternoon project', 3, 1);

-- Model Inquiry table inserts
INSERT INTO `Model Inquirys` (inquiry_id, model_id, Model_team_id, employer_id) VALUES (1, 1, 1, 2), (2, 2, 1 ,3), (3,3, 1, 3);

-- Payment Information table inserts
INSERT INTO `Payment Information` (payment_id, cardholder_name, card_number, billing_address, modelinquiry_id) VALUES (1, 'Joseph Rios', 1234, 'Apartment 1', 1), (2, 'Johnathon Smith', 2341, 'Apartment 2', 2), (3, 'Beatrice Carter', 4321, 'Apartment 3', 3);



