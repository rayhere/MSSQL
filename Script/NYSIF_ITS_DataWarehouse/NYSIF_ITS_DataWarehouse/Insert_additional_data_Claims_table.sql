USE NYSIFDB;
GO


-- Insert more sample data into Claims table
INSERT INTO Claims (ClaimID, EmployerID, EmployeeID, ClaimDate, ClaimDescription, ClaimStatus, ResolutionDate)
VALUES
(6, 1, 1, '2023-06-08', 'Employee slip and fall injury in cafeteria', 'Pending', NULL),
(7, 2, 2, '2023-07-15', 'Employee vehicle damage in parking lot', 'Denied', NULL),
(8, 3, 3, '2023-08-20', 'Employee work-related stress leave request', 'Pending', NULL),
(9, 1, 4, '2023-09-25', 'Employee eye injury from workplace debris', 'Approved', '2023-09-30'),
(10, 2, 5, '2023-10-10', 'Employee discrimination complaint', 'Pending', NULL);


-- Verify data insertion
SELECT * FROM Claims;