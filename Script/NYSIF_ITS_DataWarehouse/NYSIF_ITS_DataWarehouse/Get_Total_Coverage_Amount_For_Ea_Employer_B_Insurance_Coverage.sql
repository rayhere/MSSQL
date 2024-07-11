USE NYSIFDB
GO
--Calculate the total coverage amount for each employer based on their insurance coverage details.
SELECT E.EmployerName, SUM(CD.CoverageAmount) AS TotalCoverageAmount
FROM Employers E
JOIN CoverageDetails CD ON E.EmployerID = CD.EmployerID
GROUP BY E.EmployerName;
