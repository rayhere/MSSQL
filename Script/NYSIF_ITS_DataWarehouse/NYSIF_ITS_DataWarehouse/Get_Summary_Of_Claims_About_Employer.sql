--To retrieve a summary of claims by employer and their statuses.

USE NYSIFDB;
GO

-- Your SELECT query here
SELECT
   E.EmployerName,
   COUNT(C.ClaimID) AS TotalClaims,
   SUM(CASE WHEN C.ClaimStatus = 'Pending' THEN 1 ELSE 0 END) AS PendingClaims,
   SUM(CASE WHEN C.ClaimStatus = 'Approved' THEN 1 ELSE 0 END) AS ApprovedClaims,
   SUM(CASE WHEN C.ClaimStatus = 'Denied' THEN 1 ELSE 0 END) AS DeniedClaims
FROM
   Employers E
JOIN
   Claims C ON E.EmployerID = C.EmployerID
GROUP BY
   E.EmployerName
ORDER BY
   TotalClaims DESC;