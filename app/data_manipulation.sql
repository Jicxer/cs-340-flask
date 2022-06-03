--The following queires represent user inputs as :Input_tablecolumn
SELECT id from members where first_name = :Insert_first_name;
INSERT into members(title, first_name, last_name, dob, location) values (:Insert_title, :Insert_first_name, :Insert_last_name, :Insert_dob, :Insert_location);
UPDATE members set title=:Insert_title where first_name=:Insert_first_name;
DELETE from members where first_name=:Insert_first_name;

SELECT id from clubs where name = :Insert_club_name;
INSERT into clubs(name, address, email, phonenumber) values (:Insert_club_name, :Insert_address, :Insert_email, :Insert_phonenumber);
UPDATE clubs set phonenumber=:Insert_phonenumber where name=:Insert_club_name;
DELETE from clubs where name=:Insert_club_name;

SELECT id from Events where event_name = :Insert_event_name;
INSERT into Events(event_name, event_location, start_date, end_date, private_or_public) values (:Insert_event_name, :Insert_event_location, :Insert_start_date, :Insert_end_date, :Insert_public_or_private);
UPDATE Events set start_date=:Insert_start_date where event_name=:Insert_event_name;
DELETE from Events where event_name=:Insert_event_name;

SELECT id from sponsors where name = :Insert_name;
INSERT into sponsors(name, email, phonenumber) values (:Insert_name, :Insert_email, :Insert_phonenumber);
UPDATE sponsors set email=:Insert_email where name = :Insert_name;
DELETE from sponsors where name=:Insert_name;


--The queries below are examples of what the inputs would look like
SELECT first_name from members where id = "274187248";
INSERT into members(title, first_name, last_name, dob, location) values ('General members', 'Tom', 'Wagner', '1/01/2001', '97330');
INSERT into members(title, first_name, last_name, dob, location) values ('General members', 'Ivan', 'Chan', '1/02/2002', '97330');
UPDATE members set title='Captain' where first_name='Ivan';
DELETE from members where first_name='Tom';

SELECT name from clubs where id = "224287248";
INSERT into clubs(name, address, email, phonenumber) values ('Sunset Club', 'NW A113 Street', 'sunsetclub@gmail.com', '503000001');
INSERT into clubs(name, address, email, phonenumber) values ('Box Club', 'SW 36th Street', 'sunsetclub@gmail.com', '503034001');
UPDATE clubs set phonenumber='5046666969' where name='Sunset Club';
DELETE from clubs where name='Box Club';

SELECT event_name from Events where id = "274187248"
INSERT into Events(event_name, event_location, start_date, end_date, private_or_public) values ('Barrack\'s dob Party', 'Sunset Club', '12/25/2016', '12/27/2016', 'public');
INSERT into Events(event_name, event_location, start_date, end_date, private_or_public) values ('Free Pizza Event', 'Box Club', '5/25/2017', '5/26/2017', 'private');
UPDATE Events set start_date='11/25/2016' where event_name='Barrack\'s dob Party';
DELETE from Events where event_name='Free Pizza Event';

SELECT name from sponsors where id = "2742324432"
INSERT into sponsors(name, email, phonenumber) values ('Barack Obama', barrack@gmail.com, '2024561111');
INSERT into sponsors(name, email, phonenumber) values ('Mario Pasta', mario@gmail.com, '2434521111');
UPDATE sponsors set email='obama@gmail.com' where name = 'Barack Obama';
DELETE from sponsors where name='Mario Pasta';







  


