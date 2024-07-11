--Retrieve the latest compliance status update for each employer.

WITH LatestCompliance AS (
    SELECT CI.EmployerID, CI.ComplianceType, CI.ComplianceStatus, CI.ComplianceDate,
           ROW_NUMBER() OVER (PARTITION BY CI.EmployerID ORDER BY CI.ComplianceDate DESC) AS rn
    FROM ComplianceInfo CI
)
SELECT E.EmployerName, LC.ComplianceType, LC.ComplianceStatus, LC.ComplianceDate
FROM Employers E
LEFT JOIN LatestCompliance LC ON E.EmployerID = LC.EmployerID AND LC.rn = 1;