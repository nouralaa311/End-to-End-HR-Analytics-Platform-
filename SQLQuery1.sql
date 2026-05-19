CREATE DATABASE HR_Analytics;
USE HR_Analytics;

CREATE TABLE Departments (
    department_id INT IDENTITY(1,1) PRIMARY KEY,
    department VARCHAR(100),
    region VARCHAR(100)
);
CREATE VIEW v_Departments_Load AS
SELECT department, region
FROM Departments;
CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    department VARCHAR(100),
    education VARCHAR(100),
    region VARCHAR(100),
    gender VARCHAR(10),
    recruitment_channel VARCHAR(100),
    age INT CHECK (age >= 18),
    length_of_service INT,
    is_senior_employee INT CHECK (is_senior_employee IN (0, 1)),
    department_id INT FOREIGN KEY REFERENCES Departments (department_id)
);
CREATE VIEW v_Employees_Load AS
SELECT
    employee_id,
    department,
    education,
    region,
    gender,
    recruitment_channel,
    age,
    length_of_service,
    is_senior_employee
FROM Employees;
CREATE TABLE Performance (
    performance_id INT IDENTITY(1,1) PRIMARY KEY,
    employee_id INT FOREIGN KEY REFERENCES Employees(employee_id),
    previous_year_rating INT CHECK (previous_year_rating BETWEEN 1 AND 5),
    KPIs_met_more_than_80 INT CHECK (KPIs_met_more_than_80 IN (0, 1)),
    avg_training_score INT,
    no_of_trainings INT,
    training_level NVARCHAR(50)
);
CREATE VIEW v_Performance_Load AS 
SELECT employee_id, previous_year_rating, KPIs_met_more_than_80, avg_training_score, no_of_trainings, training_level 
FROM Performance;
CREATE TABLE Salaries (
    salary_id INT IDENTITY(1,1) PRIMARY KEY,
    employee_id INT FOREIGN KEY REFERENCES Employees(employee_id),
    awards_won INT
);
CREATE VIEW v_Salaries_Load AS 
SELECT employee_id, awards_won 
FROM Salaries;
CREATE TABLE Promotions (
    promotion_id INT IDENTITY(1,1) PRIMARY KEY,
    employee_id INT FOREIGN KEY REFERENCES Employees(employee_id),
    is_promoted INT
);
CREATE VIEW v_Promotions_Load AS 
SELECT employee_id, is_promoted 
FROM Promotions;
BULK INSERT  v_Departments_Load
FROM "C:\Users\asus\Nour's Projects\Data Analysis Project\departments_table.csv"
WITH (FIELDTERMINATOR = ',', ROWTERMINATOR = '\n');
BULK INSERT v_Employees_Load
FROM "C:\Users\asus\Nour's Projects\Data Analysis Project\employees_table.csv"
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2,
    CODEPAGE = '65001'
);
BULK INSERT v_Performance_Load 
FROM "C:\Users\asus\Nour's Projects\Data Analysis Project\performance_table.csv"
WITH (FIELDTERMINATOR = ',', ROWTERMINATOR = '\n');
BULK INSERT v_Salaries_Load
FROM "C:\Users\asus\Nour's Projects\Data Analysis Project\salaries_table.csv" 
WITH (FIELDTERMINATOR = ',', ROWTERMINATOR = '\n');
BULK INSERT v_Promotions_Load 
FROM "C:\Users\asus\Nour's Projects\Data Analysis Project\promotions.csv"
WITH (FIELDTERMINATOR = ',', ROWTERMINATOR = '\n');
SELECT * 
FROM Employees
UPDATE E
SET department_id = D.department_id
FROM Employees E
JOIN Departments D
  ON E.department = D.department
 AND E.region = D.region;
 SELECT * 
FROM Employees

SELECT department, region, COUNT(*) AS num_employees
FROM Employees
GROUP BY department, region;

SELECT 
    Employees.department,
    AVG(Performance.previous_year_rating) AS avg_rating
FROM Employees
JOIN Performance ON Employees.employee_id = Performance.employee_id
GROUP BY Employees.department
ORDER BY Employees.department;

SELECT Employees.department, SUM(Performance.KPIs_met_more_than_80) AS num_high_KPI
FROM Employees 
JOIN Performance ON Employees.employee_id = Performance.employee_id
GROUP BY Employees.department;
