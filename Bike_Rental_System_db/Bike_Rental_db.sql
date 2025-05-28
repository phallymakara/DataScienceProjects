use bikeproject;
CREATE TABLE Users (
  UserID VARCHAR(255) PRIMARY KEY,
  Username VARCHAR(255) NOT NULL,
  Email VARCHAR(255) UNIQUE,
  Phone VARCHAR(255) NOT NULL,
  Address VARCHAR(255)
);

CREATE TABLE Bike (
  BikeID VARCHAR(255) PRIMARY KEY,
  Model VARCHAR(255) NOT NULL,
  Years INT NOT NULL,
  Conditions VARCHAR(255), 
  Availability VARCHAR(255) NOT NULL,
  PhotoURL VARCHAR(255)
);

CREATE TABLE Partner (
  PartnerID VARCHAR(255) PRIMARY KEY,
  Username VARCHAR(255) NOT NULL,
  ContactEmail VARCHAR(255) UNIQUE,
  ContactPhone VARCHAR(255),
  StreetAddress VARCHAR(255),
  PartnerName VARCHAR(255),
  District VARCHAR(255),
  Province VARCHAR(255),
  PostalCode VARCHAR(255)
);

CREATE TABLE AuthenticationForUser (
  AuthID VARCHAR(255) PRIMARY KEY,
  UserID VARCHAR(255) NOT NULL UNIQUE,
  PasswordHash VARCHAR(255) NOT NULL,
  Salt VARCHAR(255),
  FOREIGN KEY (UserID) REFERENCES Users (UserID)
);

CREATE TABLE Rental (
  RentalID VARCHAR(255) PRIMARY KEY,
  UserID VARCHAR(255) NOT NULL,
  PartnerID VARCHAR(255) NOT NULL,
  BikeID VARCHAR(255) NOT NULL,
  Dates DATE,
  StartTime TIMESTAMP,
  EndTime TIMESTAMP,
  TotalCost DECIMAL(10, 2),
  PricePerHour DECIMAL(10, 2),
  LateFeeStructure VARCHAR(255),
  WebsiteURL VARCHAR(255),
  DamageReport TEXT,
  ContractStartDate DATE,
  ContractEndDate DATE,
  FOREIGN KEY (UserID) REFERENCES Users (UserID),
  FOREIGN KEY (BikeID) REFERENCES Bike (BikeID),
  FOREIGN KEY (PartnerID) REFERENCES Partner (PartnerID)
);

CREATE TABLE Payment (
  PaymentID VARCHAR(255) PRIMARY KEY,
  RentalID VARCHAR(255) NOT NULL,
  Descriptions VARCHAR(255),
  PaymentMethod VARCHAR(255),
  Dates DATE,
  TransactionID VARCHAR(255) UNIQUE,
  Currency VARCHAR(3),
  Fees DECIMAL(10, 2),
  FOREIGN KEY (RentalID) REFERENCES Rental (RentalID)
);

CREATE TABLE RequiredDocuments (
  TypeID VARCHAR(255) PRIMARY KEY,
  DocumentName VARCHAR(255),
  Purpose VARCHAR(255),
  PartnerID VARCHAR(255) NOT NULL,
  FOREIGN KEY (PartnerID) REFERENCES Partner (PartnerID)
);

CREATE TABLE AuthenticationForPartner (
  AuthID VARCHAR(255) PRIMARY KEY,
  PartnerID VARCHAR(255) NOT NULL UNIQUE,
  Username VARCHAR(255) NOT NULL,
  PasswordHash VARCHAR(255) NOT NULL,
  Salt VARCHAR(255),
  FOREIGN KEY (PartnerID) REFERENCES Partner (PartnerID)
);
