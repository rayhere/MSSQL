USE NYSIFDB;
GO
-- Insert more sample data into Employers table
BEGIN TRY
    INSERT INTO Employers (EmployerID, EmployerName, Address, City, State, ZipCode, ContactPerson, Phone, Email, RegistrationDate, IsActive)
    VALUES (1, 'Duplicate Company', '789 Oak St', 'Seattle', 'WA', '98101', 'Sam Johnson', '555-777-8888', 'sam@duplicate.com', '2023-05-25', 1);
END TRY
BEGIN CATCH
    PRINT 'Error inserting record: ' + ERROR_MESSAGE();
END CATCH;
-- Verify data insertion
SELECT * FROM Employers;