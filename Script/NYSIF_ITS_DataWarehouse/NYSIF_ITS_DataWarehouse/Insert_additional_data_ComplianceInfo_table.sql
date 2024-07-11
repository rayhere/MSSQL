USE NYSIFDB;
GO


-- Insert more sample data into ComplianceInfo table
INSERT INTO ComplianceInfo (ComplianceID, EmployerID, ComplianceType, ComplianceStatus, ComplianceDate)
VALUES
(6, 1, 'Annual Report Submission', 'Pending', NULL),
(7, 2, 'Employee Training Records', 'Complete', '2023-04-05'),
(8, 2, 'Fire Safety Inspection', 'Pending', NULL),
(9, 3, 'Health Code Compliance', 'Complete', '2023-05-15'),
(10, 3, 'Insurance Coverage Verification', 'Pending', NULL);


-- Verify data insertion
SELECT * FROM ComplianceInfo;