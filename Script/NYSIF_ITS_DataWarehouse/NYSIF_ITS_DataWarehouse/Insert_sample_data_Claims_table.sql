USE NYSIFDB;
GO

-- Insert sample data into Claims table
INSERT INTO Claims (ClaimID, EmployerID, EmployeeID, ClaimDate, ClaimDescription, ClaimStatus, ResolutionDate)
VALUES
(1, 1, 1, '2023-02-05', 'Employee slipped and fell at workplace', 'Pending', NULL),
(2, 1, 2, '2023-03-10', 'Employee reported back injury from lifting', 'Approved', '2023-03-15'),
(3, 2, 3, '2023-01-20', 'Employee vehicle accident during business trip', 'Denied', NULL),
(4, 2, 4, '2023-04-12', 'Employee illness requiring hospitalization', 'Pending', NULL),
(5, 3, 5, '2023-05-03', 'Employee injury from malfunctioning equipment', 'Approved', '2023-05-10');
-- Add more INSERT INTO statements as needed for additional data

-- Verify data insertion
SELECT * FROM Claims;
