USE NYSIFDB;
GO

-- Insert sample data into CoverageDetails table
INSERT INTO CoverageDetails (CoverageID, EmployerID, CoverageType, CoverageAmount, CoverageStartDate, CoverageEndDate)
VALUES
(1, 1, 'Health Insurance', 1500.00, '2023-01-01', '2023-12-31'),
(2, 1, 'Life Insurance', 500000.00, '2023-02-15', '2024-02-14'),
(3, 2, 'Dental Insurance', 1000.00, '2023-03-01', '2023-12-31'),
(4, 2, 'Disability Insurance', 2000.00, '2023-01-01', '2023-12-31'),
(5, 3, 'Vision Insurance', 800.00, '2023-04-01', '2023-12-31');
-- Add more INSERT INTO statements as needed for additional data

-- Verify data insertion
SELECT * FROM CoverageDetails;
