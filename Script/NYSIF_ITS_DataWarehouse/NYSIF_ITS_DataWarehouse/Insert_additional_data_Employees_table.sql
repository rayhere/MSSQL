USE NYSIFDB;
GO

-- Insert more sample data into Employees table
INSERT INTO Employees (EmployeeID, EmployerID, FirstName, LastName, DateOfBirth, SSN, JobTitle, Department, IsActive)
VALUES
(6, 3, 'Jessica', 'Wilson', '1993-04-18', '111-22-3333', 'Software Developer', 'IT Department', 1),
(7, 1, 'Matthew', 'Anderson', '1985-12-30', '444-55-6666', 'Sales Manager', 'Sales Department', 1),
(8, 2, 'Emma', 'Martinez', '1990-08-05', '777-88-9999', 'Financial Analyst', 'Finance Department', 1),
(9, 3, 'Christopher', 'Garcia', '1989-06-25', '222-33-4444', 'Operations Manager', 'Operations Department', 1),
(10, 1, 'Olivia', 'Lopez', '1991-02-14', '888-99-0000', 'Product Manager', 'Product Management', 1);

-- Verify data insertion
SELECT * FROM Employees;
