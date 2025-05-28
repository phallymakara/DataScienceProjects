# Retrieve rental information along with the corresponding user details (username, email) for each rental.
SELECT Rental.*, Users.Username, Users.Email
FROM Rental
INNER JOIN Users ON Rental.UserID = Users.UserID;

# Get a list of rentals made by each partner, including partner details (name,phone).
SELECT Rental.*, Partner.PartnerName, Partner.ContactPhone
FROM Rental
INNER JOIN Partner ON Rental.PartnerID = Partner.PartnerID;

# Display rental details along with the bike information (year, model) for each rental.
SELECT Rental.*, Bike.Years, Bike.Model
FROM Rental
INNER JOIN Bike ON Rental.BikeID = Bike.BikeID;

# Retrieve payments made for each rental, including payment details (payment method, transaction ID).
SELECT Payment.*, Rental.TotalCost, Rental.RentalID
FROM Payment
INNER JOIN Rental ON Payment.RentalID = Rental.RentalID;


