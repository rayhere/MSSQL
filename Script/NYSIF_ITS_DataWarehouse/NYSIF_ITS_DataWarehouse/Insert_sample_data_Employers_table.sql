USE NYSIFDB;
GO

-- Insert sample data into Employers table
INSERT INTO Employers (EmployerID, EmployerName, Address, City, State, ZipCode, ContactPerson, Phone, Email, RegistrationDate, IsActive)
VALUES
(1, 'ABC Company', '123 Main St', 'New York', 'NY', '10001', 'John Doe', '555-123-4567', 'john.doe@abccompany.com', '2023-01-15', 1),
(2, 'XYZ Corporation', '456 Oak Ave', 'Albany', 'NY', '12205', 'Jane Smith', '555-987-6543', 'jane.smith@xyzcorp.com', '2022-12-05', 1),
(3, '123 Enterprises', '789 Elm Rd', 'Buffalo', 'NY', '14202', 'Mike Johnson', '555-555-5555', 'mike.johnson@123ent.com', '2023-02-28', 1),
(4, 'New Company', '123 Elm St', 'Los Angeles', 'CA', '90001', 'Alice Brown', '555-111-2222', 'alice@newcompany.com', '2023-03-15', 1),
(5, 'Another Company', '456 Pine Ave', 'Chicago', 'IL', '60601', 'Bob Green', '555-333-4444', 'bob@anothercompany.com', '2023-04-20', 1);
-- Add more INSERT INTO statements as needed for additional data

-- Verify data insertion
SELECT * FROM Employers;
