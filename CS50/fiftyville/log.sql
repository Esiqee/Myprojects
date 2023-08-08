-- Keep a log of any SQL queries you execute as you solve the mystery.
-- All you know is that the theft took place on July 28, 2021 and that it took place on Humphrey Street.
-- sqlite3 fiftyville.db
.schema
.tables
select * from crime_scene_reports where street = "Humphrey Street";
/*Humphrey Street | Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.*/
select * from interviews where transcript like "%bakery%";
/*Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security
footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.*/
/*I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking
by the ATM on Leggett Street and saw the thief there withdrawing some money.*/
/*As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that
they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to
purchase the flight ticket.*/
select * from bakery_security_logs where year = 2021 and month = 7 and day = 28;
select name, license_plate from people where license_plate = "5P2BI95" or license_plate = "94KL13X" or license_plate = "6P58WS2" or license_plate = "4328GD8"
or license_plate = "G412CB7" or license_plate = "L93JTIZ" or license_plate = "322W7JE" or license_plate = "0NTHK55";
/*possibilities : 5P2BI95 94KL13X 6P58WS2 4328GD8 G412CB7 L93JTIZ 322W7JE 0NTHK55 */
/*possibilities : Vanessa Bruce   Barry   Luca    Sofia   Iman    Diana   Kelsey */
select phone_calls.caller, people.name from phone_calls
join people on phone_calls.caller = people.phone_number
where phone_calls.year =2021 and phone_calls.month = 7 and phone_calls.day = 28 and phone_calls.duration < 60;
select phone_calls.receiver, people.name from phone_calls
join people on phone_calls.receiver = people.phone_number
where phone_calls.year =2021 and phone_calls.month = 7 and phone_calls.day = 28 and phone_calls.duration < 60;
-- caller - receiver included only suspects
/*sofia-jack kelsey-larry bruce-robin kelsey-melissa diana- philip*/
select name from bank_accounts
join people on bank_accounts.person_id = people.id
join atm_transactions on bank_accounts.account_number = atm_transactions.account_number
where year = 2021 and month = 7 and day = 28 and atm_location = "Leggett Street" and transaction_type = "withdraw";
/*who withdrew money at morning - including only suspects*/
/*bruce-pass 5773159633 diana-pass 3592750733*/
select name, passport_number from people where name = "Bruce";
select name, passport_number from people where name = "Diana";
/*Now search for earliest plane tomorrow */
select * from flights
join airports on destination_airport_id = airports.id
where year = 2021 and month = 7 and day = 29;
/*first flight has id 36 @ 8:20 to LaGuardia NY*/
select passport_number from passengers
join flights on flight_id = flights.id
where flight_id = 36;

-- bruce-pass 5773159633 found on board! robin is accomplice! Objective complete