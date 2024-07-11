--Delete Inactive Employers and Their Related Data.
--Delete employers who are no longer active and their associated employees, claims, coverage details, and compliance information.

BEGIN TRANSACTION;

-- Delete claims related to inactive employers
DELETE FROM Claims
WHERE EmployerID IN (
    SELECT EmployerID
    FROM Employers
    WHERE IsActive = 0
);

-- Delete coverage details related to inactive employers
DELETE FROM CoverageDetails
WHERE EmployerID IN (
    SELECT EmployerID
    FROM Employers
    WHERE IsActive = 0
);

-- Delete compliance information related to inactive employers
DELETE FROM ComplianceInfo
WHERE EmployerID IN (
    SELECT EmployerID
    FROM Employers
    WHERE IsActive = 0
);

-- Delete employees of inactive employers
DELETE FROM Employees
WHERE EmployerID IN (
    SELECT EmployerID
    FROM Employers
    WHERE IsActive = 0
);

-- Delete inactive employers
DELETE FROM Employers
WHERE IsActive = 0;

COMMIT TRANSACTION;
