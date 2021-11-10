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
# WHERE year = 2020 AND month = 7 AND day = 28 AND hour BETWEEN 8 AND 11 AND activity = 'exit'
# '''

# ('Alice', '1M92998'), ('Peter', 'N507616'), ('Rachel', '7Z8B130'), ('Debra', '47MEFVA'), 
# ('Wayne', 'D965M59'), ('Jordan', 'HW0488P'), ('Michael', 'HOD8639'), ('George', 'L68E5I0'), 
# ('Andrew', 'W2CT78U'), ('Ralph', '3933NUH'), ('Joshua', '1FBL6TH'), ('Carolyn', 'P14PE2Q'), 
# ('Berthold', '4V16VO0'), ('Donna', '8LLB02B'), ('Martha', 'O784M2U'), ('Patrick', '5P2BI95'), 
# ('Ernest', '94KL13X'), ('Amber', '6P58WS2'), ('Danielle', '4328GD8'), ('Roger', 'G412CB7'), 
# ('Elizabeth', 'L93JTIZ'), ('Russell', '322W7JE'), ('Evelyn', '0NTHK55'), ('Madison', '1106N58')

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
# JOIN phone_calls ON people.phone_number = phone_calls.caller
# WHERE year = 2020 AND month = 7 AND day = 28 AND duration < 60
# '''

# ('Roger', 'G412CB7'), ('Evelyn', '0NTHK55'), ('Ernest', '94KL13X'), 
# ('Evelyn', '0NTHK55'), ('Madison', '1106N58'), ('Russell', '322W7JE'), 
# ('Kimberly', 'Q12B3Z3'), ('Bobby', '30G67EN'), ('Victoria', '8X428L0')

sql_query = '''
SELECT DISTINCT name, people.license_plate
FROM people
JOIN airports ON flights.origin_airport_id = airports.id
JOIN flights ON airports.id = flights.origin_airport_id
JOIN passengers AS p1 ON flights.id = p1.flight_id
JOIN passengers AS p2 ON people.passport_number = p2.passport_number
WHERE year = 2020 AND month = 7 AND day = 29 
AND airports.city = 'Fiftyville'
'''

rows = cursor.execute(sql_query).fetchall()
print(rows)
print(len(rows))