USE master;
GO

-- Drop existing database if it exists
IF EXISTS (SELECT * FROM sys.databases WHERE name = 'NYSIFDB')
BEGIN
    ALTER DATABASE NYSIFDB SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE NYSIFDB;
END
GO

-- Create database
CREATE DATABASE NYSIFDB;
GO

-- Set recovery mode to full (adjust as needed based on backup strategy)
ALTER DATABASE NYSIFDB
SET RECOVERY FULL;
GO

-- Set database options (adjust as needed)
ALTER DATABASE NYSIFDB
SET ANSI_NULL_DEFAULT OFF,
    ANSI_NULLS OFF,
    ANSI_PADDING OFF,
    ANSI_WARNINGS OFF,
    ARITHABORT OFF,
    AUTO_CLOSE OFF,
    AUTO_CREATE_STATISTICS ON,
    AUTO_UPDATE_STATISTICS ON,
    CURSOR_CLOSE_ON_COMMIT OFF,
    CURSOR_DEFAULT GLOBAL,
    CONCAT_NULL_YIELDS_NULL OFF,
    NUMERIC_ROUNDABORT OFF,
    QUOTED_IDENTIFIER OFF,
    RECURSIVE_TRIGGERS OFF,
    DISABLE_BROKER;
GO

-- Optionally, set compatibility level (adjust as needed)
ALTER DATABASE NYSIFDB
SET COMPATIBILITY_LEVEL = 150; -- SQL Server 2019 compatibility level
GO

-- Define file locations and sizes (adjust paths and sizes as needed)
ALTER DATABASE NYSIFDB
MODIFY FILE (NAME = NYSIFDB, FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL16.SQL1\MSSQL\DATA\NYSIFDB.mdf', SIZE = 100MB, MAXSIZE = UNLIMITED, FILEGROWTH = 10%)
GO

ALTER DATABASE NYSIFDB
MODIFY FILE (NAME = NYSIFDB_Log, FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL16.SQL1\MSSQL\DATA\NYSIFDB.ldf', SIZE = 50MB, MAXSIZE = UNLIMITED, FILEGROWTH = 5MB);
GO

-- Verify database creation
USE NYSIFDB;
GO

-- Create tables for employer use (sample tables, adjust as per actual schema requirements)

-- Employers table
CREATE TABLE Employers (
    EmployerID INT PRIMARY KEY,
    EmployerName VARCHAR(100) NOT NULL,
    Address VARCHAR(200),
    City VARCHAR(50),
    State VARCHAR(50),
    ZipCode VARCHAR(20),
    ContactPerson VARCHAR(100),
    Phone VARCHAR(20),
    Email VARCHAR(100),
    RegistrationDate DATE,
    IsActive BIT
);
GO

-- Employees table
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    EmployerID INT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    DateOfBirth DATE,
    SSN VARCHAR(20),
    JobTitle VARCHAR(100),
    Department VARCHAR(100),
    IsActive BIT,
    CONSTRAINT FK_Employees_Employers FOREIGN KEY (EmployerID) REFERENCES Employers(EmployerID)
);
GO

-- Coverage details table
CREATE TABLE CoverageDetails (
    CoverageID INT PRIMARY KEY,
    EmployerID INT,
    CoverageType VARCHAR(50),
    CoverageAmount DECIMAL(18, 2),
    CoverageStartDate DATE,
    CoverageEndDate DATE,
    CONSTRAINT FK_CoverageDetails_Employers FOREIGN KEY (EmployerID) REFERENCES Employers(EmployerID)
);
GO

-- Claims table
CREATE TABLE Claims (
    ClaimID INT PRIMARY KEY,
    EmployerID INT,
    EmployeeID INT,
    ClaimDate DATE,
    ClaimDescription VARCHAR(MAX),
    ClaimStatus VARCHAR(50),
    ResolutionDate DATE,
    CONSTRAINT FK_Claims_Employers FOREIGN KEY (EmployerID) REFERENCES Employers(EmployerID),
    CONSTRAINT FK_Claims_Employees FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);
GO

-- Compliance information table (sample)
CREATE TABLE ComplianceInfo (
    ComplianceID INT PRIMARY KEY,
    EmployerID INT,
    ComplianceType VARCHAR(50),
    ComplianceStatus VARCHAR(50),
    ComplianceDate DATE,
    CONSTRAINT FK_ComplianceInfo_Employers FOREIGN KEY (EmployerID) REFERENCES Employers(EmployerID)
);
GO
