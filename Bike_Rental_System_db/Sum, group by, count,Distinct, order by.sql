# Sum the total cost of rentals for each partner, ordered by the total cost in descending order.
SELECT Partner.PartnerID, Partner.PartnerName, SUM(Rental.TotalCost) AS TotalCost
FROM Rental
INNER JOIN Partner ON Rental.PartnerID = Partner.PartnerID
GROUP BY Partner.PartnerID, Partner.PartnerName
ORDER BY TotalCost DESC;

# Count the number of rentals made by each user and order the result by the count of rentals in descending order.
SELECT Rental.UserID, Users.Username, COUNT(*) AS NumRentals
FROM Rental
INNER JOIN Users ON Rental.UserID = Users.UserID
GROUP BY Rental.UserID, Users.Username
ORDER BY NumRentals DESC;

# Find the distinct bike models rented by users along with the count of rentals for each model.
SELECT DISTINCT Bike.Model, COUNT(*) AS NumRentals
FROM Rental
INNER JOIN Bike ON Rental.BikeID = Bike.BikeID
GROUP BY Bike.Model;

# Retrieve the total cost of rentals for each user, grouped by the user ID, and ordered by the total cost in ascending order.
SELECT Rental.UserID, Users.Username, SUM(Rental.TotalCost) AS TotalCost
FROM Rental
INNER JOIN Users ON Rental.UserID = Users.UserID
GROUP BY Rental.UserID, Users.Username
ORDER BY TotalCost ASC;


