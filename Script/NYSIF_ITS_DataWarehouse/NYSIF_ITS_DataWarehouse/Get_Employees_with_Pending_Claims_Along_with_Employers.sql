--Identify employees with pending claims, along with their employers.

USE NYSIFDB;
GO

SELECT E.EmployeeID, E.FirstName, E.LastName, Emp.EmployerName, C.ClaimDate, C.ClaimDescription
FROM Employees E
JOIN Claims C ON E.EmployeeID = C.EmployeeID
JOIN Employers Emp ON E.EmployerID = Emp.EmployerID
WHERE C.ClaimStatus = 'Pending';