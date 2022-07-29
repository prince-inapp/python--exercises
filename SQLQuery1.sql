create database RailwayReservation
use RailwayReservation
go

CREATE TABLE Trains
( train_id INT PRIMARY KEY,
  train_name VARCHAR(20),
  destination INT,
  booked_seats INT,
  waiting_list INT
  );
go

INSERT INTO Trains VALUES
(101, 'TVM-ALP', 1, 0, 0),
(102, 'TVM-ERN', 2, 0, 0),
(103, 'TVM-KZK', 3, 0, 0);
go

SELECT * FROM Trains;
GO

CREATE TABLE Stations (
	s_id INT PRIMARY KEY,
	s_name VARCHAR(20),
	);
GO
INSERT INTO Stations VALUES (1, 'ALP'),(2, 'ERN'),(3, 'KZK');
GO

SELECT * FROM Stations;
GO

ALTER TABLE Trains
ADD FOREIGN KEY(destination) REFERENCES Stations(s_id);
go

CREATE TABLE Passengers
( 
  p_name VARCHAR(20),
  p_dest INT,
  P_train_id INT,
 );
GO

select * from Passengers

alter table 

select booked_seats from Trains where train_id = 101

update Trains set booked_seats = 0 where train_id = 102

select * from Trains
select booked_seats from Trains where train_id = 101

select * from Passengers
truncate Passengers
