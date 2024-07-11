--List all active employers and their compliance status.

SELECT E.EmployerName, CI.ComplianceType, CI.ComplianceStatus
FROM Employers E
LEFT JOIN ComplianceInfo CI ON E.EmployerID = CI.EmployerID
WHERE E.IsActive = 1;