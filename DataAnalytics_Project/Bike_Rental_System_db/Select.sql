use bikeproject;
SELECT UserID,Address
FROM Users 

# Write a SQL query to retrieve the total number of rentals made by each user.
SELECT UserID, COUNT(*) AS TotalRentals
FROM Rental
GROUP BY UserID;

# Create a view named LateRentals that displays information about rentals where the end time is later than the expected return time.
CREATE VIEW LateRentals AS
SELECT *
FROM Rental
WHERE EndTime > ContractEndDate;
SELECT * FROM LateRentals;

# Write a SQL query to find the average rental cost per bike for each partner.
SELECT PartnerID, AVG(TotalCost) AS AverageRentalCost
FROM Rental
WHERE PartnerID IS NOT NULL
GROUP BY PartnerID;

# List the usernames and the number of rentals made by users who have rented bikes more than five times.
SELECT UserID, COUNT(*) AS NumRentals
FROM Rental
WHERE UserID IS NOT NULL
GROUP BY UserID
HAVING COUNT(*) > 1;



