USE NYSIFDB;
GO


-- Insert more sample data into CoverageDetails table
INSERT INTO CoverageDetails (CoverageID, EmployerID, CoverageType, CoverageAmount, CoverageStartDate, CoverageEndDate)
VALUES
(6, 1, 'Accidental Death Insurance', 250000.00, '2023-05-10', '2024-05-09'),
(7, 2, '401(k) Plan', 0.00, '2023-06-01', '2023-12-31'),
(8, 3, 'Flexible Spending Account', 1500.00, '2023-07-01', '2023-12-31'),
(9, 1, 'Workers Compensation', 100000.00, '2023-08-01', '2024-07-31'),
(10, 2, 'Employee Assistance Program', 0.00, '2023-09-01', '2023-12-31');


-- Verify data insertion
SELECT * FROM CoverageDetails;