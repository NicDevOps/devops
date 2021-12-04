import sqlite3

connection = sqlite3.connect("fiftyville.db")

cursor = connection.cursor()

# Fiftyville
# Who the thief is,
# What city the thief escaped to, and
# Who the thief’s accomplice is who helped them escape
# All you know is that the theft took place on July 28, 2020 and that it took place on Chamberlin Street.

# sql_query = '''
# SELECT * 
# FROM crime_scene_reports 
# WHERE year = 2020 AND month = 7 AND day = 28
# '''

# 295, 2020, 7, 28, 'Chamberlin Street', 
# Theft of the CS50 duck took place at 10:15am at the Chamberlin Street courthouse. 
# Interviews were conducted today with three witnesses who were present at the time 
# — each of their interview transcripts mentions the courthouse.

# sql_query = '''
# SELECT *
# FROM interviews
# WHERE year = 2020 AND month = 7 AND day = 28
# '''

# 161, 'Ruth', 2020, 7, 28, Sometime within ten minutes of the theft, 
# I saw the thief get into a car in the courthouse parking lot and drive away. 
# If you have security footage from the courthouse parking lot, 
# you might want to look for cars that left the parking lot in that time frame.

# sql_query = '''
# SELECT license_plate FROM courthouse_security_logs
# WHERE year = 2020 AND month = 7 AND day = 28 AND hour BETWEEN 8 AND 11 AND activity = 'exit'
# '''

# sql_query = '''
# SELECT name, people.license_plate
# FROM people
# JOIN courthouse_security_logs ON people.license_plate = courthouse_security_logs.license_plate
# WHERE year = 2020 AND month = 7 AND day = 28 AND hour BETWEEN 10 AND 11 AND activity = 'exit'
# '''

# ('Patrick', '5P2BI95'), ('Ernest', '94KL13X'), ('Amber', '6P58WS2'),
# ('Danielle', '4328GD8'), ('Roger', 'G412CB7'), ('Elizabeth', 'L93JTIZ'), 
# ('Russell', '322W7JE'), ('Evelyn', '0NTHK55'), ('Madison', '1106N58')

# 162, 'Eugene', 2020, 7, 28, I don't know the thief's name, 
# but it was someone I recognized. Earlier this morning, before I arrived at the courthouse, 
# I was walking by the ATM on Fifer Street and saw the thief there withdrawing some money.

# sql_query = '''
# SELECT * FROM atm_transactions
# WHERE year = 2020 AND month = 7 AND day = 28 AND atm_location = 'Fifer Street'
# '''

# sql_query = '''
# SELECT name, people.license_plate
# FROM people
# JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
# JOIN bank_accounts ON people.id = person_id
# WHERE year = 2020 AND month = 7 AND day = 28 AND atm_location = 'Fifer Street'
# '''

# ('Ernest', '94KL13X'), ('Robert', 'I449449'), ('Russell', '322W7JE'), ('Roy', 'QX4YZN3'), 
# ('Bobby', '30G67EN'), ('Elizabeth', 'L93JTIZ'), ('Danielle', '4328GD8'), 
# ('Madison', '1106N58'), ('Victoria', '8X428L0')

# 163, 'Raymond', 2020, 7, 28, As the thief was leaving the courthouse, 
# they called someone who talked to them for less than a minute. In the call, 
# I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. 
# The thief then asked the person on the other end of the phone to purchase the flight ticket.

# sql_query = '''
# SELECT * 
# FROM phone_calls
# WHERE year = 2020 AND month = 7 AND day = 28 AND duration < 60
# '''

# sql_query = '''
# SELECT name, people.license_plate
# FROM people
# JOIN phone_calls ON people.phone_number = phone_calls.receiver
# WHERE year = 2020 AND month = 7 AND day = 28 AND duration < 60
# '''

# phone receiver
# x('Jack', '52R0Y8U'), x('Larry', 'O268ZZ0'), ('Berthold', '4V16VO0'), 
# x('Melissa', None), x('James', 'Q13SVG6'), x('Philip', 'GW362R6'), 
# ('Jacqueline', '43V0R5D'), x('Doris', 'M51FA04'), ('Anna', None)

# phone caller
# ('Roger', 'G412CB7'), ('Evelyn', '0NTHK55'), ('Ernest', '94KL13X'), 
# ('Evelyn', '0NTHK55'), ('Madison', '1106N58'), ('Russell', '322W7JE'), 
# ('Kimberly', 'Q12B3Z3'), ('Bobby', '30G67EN'), ('Victoria', '8X428L0')

# sql_query = '''
# SELECT DISTINCT name, people.license_plate, hour, p1.flight_id, p2.passport_number, flights.destination_airport_id
# FROM people
# JOIN airports ON flights.origin_airport_id = airports.id
# JOIN flights ON airports.id = flights.origin_airport_id
# JOIN passengers AS p1 ON flights.id = p1.flight_id
# JOIN passengers AS p2 ON people.passport_number = p2.passport_number
# WHERE p1.flight_id = 36 AND year = 2020 AND month = 7 AND day = 29 AND hour = 8
# AND airports.city = 'Fiftyville'
# ORDER BY name
# '''
##########################################################################################
sql_query = '''
SELECT flights.id, flights.hour, flights.origin_airport_id, destination_airport_id
FROM flights
JOIN airports ON flights.origin_airport_id = airports.id
JOIN passengers AS p1 ON flights.id = p1.flight_id
WHERE city = 'Fiftyville' AND p1.passport_number = 3592750733 AND year = 2020 AND month = 7 AND day = 29
'''

sql_query = '''
SELECT flights.id, flights.hour, flights.origin_airport_id, destination_airport_id, p1.passport_number
FROM flights
JOIN airports ON flights.origin_airport_id = airports.id
JOIN passengers AS p1 ON flights.id = p1.flight_id
WHERE city = 'Fiftyville' AND year = 2020 AND month = 7 AND day = 29 AND hour = 8
'''

# sql_query = '''
# SELECT city FROM airports
# JOIN flights ON airports.id = destination_airport_id
# WHERE destination_airport_id = 6
# '''

# sql_query = '''
# SELECT city FROM airports
# JOIN flights ON airports.id = origin_airport_id
# WHERE origin_airport_id = 8
# '''
##########################################################################################
# sql_query = '''
# SELECT flights.id, passengers.flight_id, flights.hour 
# FROM flights
# JOIN passengers ON flights.id = passengers.flight_id
# WHERE year = 2020 AND month = 7 AND day = 29
# ORDER BY flights.hour
# '''

# sql_query = '''
# SELECT city FROM airports
# JOIN flights ON airports.id = destination_airport_id
# WHERE destination_airport_id = 4
# '''

# phone receiver
# x('Jack', '52R0Y8U'), x('Larry', 'O268ZZ0'), ('Berthold', '4V16VO0'), 
# x('Melissa', None), x('James', 'Q13SVG6'), x('Philip', 'GW362R6'), 
# ('Jacqueline', '43V0R5D'), x('Doris', 'M51FA04'), ('Anna', None)

# sql_query = '''
# SELECT name, passport_number, license_plate
# FROM people
# WHERE name = 'Doris' AND license_plate = 'M51FA04'
# '''

# seat suspect : are suspect sit next to each other?
# ('Russell', 3592750733)
# ('Jack', 9029462229), ('Larry', 2312901747), 
# ('Melissa', 7834357192), ('James', 2438825627,), ('Philip', 3391710505)
# ('Doris', 7214083635)

# sql_query = '''
# SELECT seat, flight_id
# FROM passengers
# WHERE passport_number = 3592750733
# '''
# sql_query = '''
# SELECT passengers.flight_id, passengers.passport_number, people.passeport_number
# FROM passengers
# JOIN people ON passengers.passport_number = people.passeport_number
# WHERE passengers.flight_id = 36
# '''

# sql_query = '''
# SELECT people.passeport_number
# FROM people
# WHERE people.passeport_number IN(SELECT passengers.passeport_number FROM passengers
# WHERE passengers.flight_id = 36)
# '''

# ('Russell', '322W7JE', 8, 36) ('Elizabeth', 'L93JTIZ', 8, 36) ('Evelyn', '0NTHK55', 8, 36)

rows = cursor.execute(sql_query).fetchall()
print(rows)
print(len(rows))

# they escape at city of 

# Thief 1st suspect: ('Russell', '322W7JE')

# Accomplice suspect : 
