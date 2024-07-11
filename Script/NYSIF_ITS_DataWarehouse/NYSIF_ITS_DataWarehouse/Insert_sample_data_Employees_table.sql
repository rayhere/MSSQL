USE NYSIFDB;
GO

-- Insert sample data into Employees table
INSERT INTO Employees (EmployeeID, EmployerID, FirstName, LastName, DateOfBirth, SSN, JobTitle, Department, IsActive)
VALUES
(1, 1, 'Michael', 'Smith', '1990-05-15', '123-45-6789', 'Software Engineer', 'IT Department', 1),
(2, 1, 'Emily', 'Johnson', '1988-09-20', '987-65-4321', 'Business Analyst', 'Finance Department', 1),
(3, 2, 'David', 'Williams', '1995-03-10', '456-78-9012', 'Marketing Specialist', 'Marketing Department', 1),
(4, 2, 'Sarah', 'Brown', '1992-11-25', '654-32-1098', 'HR Manager', 'Human Resources', 1),
(5, 3, 'Daniel', 'Davis', '1987-07-08', '789-01-2345', 'Project Manager', 'Project Management', 1);
-- Add more INSERT INTO statements as needed for additional data

-- Verify data insertion
SELECT * FROM Employees;
