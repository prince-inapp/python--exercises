create database hospital

create table patients(
	patientId int primary key,
	name varchar(20),
	gender varchar(10),
	age int,
	bloodGroup varchar(20)
	)
select * from patients