USE NYSIFDB;
GO

-- Insert sample data into ComplianceInfo table
INSERT INTO ComplianceInfo (ComplianceID, EmployerID, ComplianceType, ComplianceStatus, ComplianceDate)
VALUES
(1, 1, 'Safety Training', 'Complete', '2023-02-10'),
(2, 1, 'Tax Filing', 'Pending', NULL),
(3, 2, 'Environmental Review', 'Complete', '2023-01-15'),
(4, 2, 'Licenses Renewal', 'Complete', '2023-03-20'),
(5, 3, 'Workplace Inspections', 'Pending', NULL);
-- Add more INSERT INTO statements as needed for additional data

-- Verify data insertion
SELECT * FROM ComplianceInfo;
