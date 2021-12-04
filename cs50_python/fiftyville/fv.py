import sqlite3
from pprint import pprint

connection = sqlite3.connect("fiftyville.db")

cursor = connection.cursor()

# sql_query = '''
# SELECT description
# FROM crime_scene_reports 
# WHERE year = 2020 AND month = 7 AND day = 28 AND street = 'Chamberlin Street'
# '''

# Theft of the CS50 duck took place at 10:15am at the Chamberlin Street courthouse. 
# Interviews were conducted today with three witnesses who were present at the time
# — each of their interview transcripts mentions the courthouse.

# sql_query = '''
# SELECT transcript
# FROM interviews
# WHERE year = 2020 AND month = 7 AND day = 28 AND transcript LIKE '%courthouse%'
# '''


# Sometime within ten minutes of the theft, 
# I saw the thief get into a car in the courthouse parking lot and drive away. 
# If you have security footage from the courthouse parking lot, 
# you might want to look for cars that left the parking lot in that time frame.

    # sql_query = '''
    # SELECT name, people.license_plate
    # FROM people
    # JOIN courthouse_security_logs ON people.license_plate = courthouse_security_logs.license_plate
    # WHERE year = 2020 AND month = 7 AND day = 28 AND hour = 10 AND minute BETWEEN 0 AND 30 
    # AND activity = 'exit'
    # '''

    # [('Patrick', '5P2BI95'),
    #  ('Ernest', '94KL13X'),
    #  ('Amber', '6P58WS2'),
    #  ('Danielle', '4328GD8'),
    #  ('Roger', 'G412CB7'),
    #  ('Elizabeth', 'L93JTIZ'),
    #  ('Russell', '322W7JE'),
    #  ('Evelyn', '0NTHK55')]

# I don't know the thief's name, but it was someone I recognized. 
# Earlier this morning, before I arrived at the courthouse, 
# I was walking by the ATM on Fifer Street and saw the thief there withdrawing some money.


    # sql_query = '''
    # SELECT a.amount, p.name
    # FROM atm_transactions AS a
    # JOIN bank_accounts AS b ON a.account_number = b.account_number
    # JOIN people AS p ON b.person_id = p.id
    # WHERE a.year = 2020 AND a.month = 7 AND a.day = 28 AND a.atm_location = 'Fifer Street'
    # AND a.transaction_type = 'withdraw'
    # '''

    # [(50, 'Ernest'),
    #  (35, 'Russell'),
    #  (80, 'Roy'),
    #  (20, 'Bobby'),
    #  (20, 'Elizabeth'),
    #  (48, 'Danielle'),
    #  (60, 'Madison'),
    #  (30, 'Victoria')]

# As the thief was leaving the courthouse, they called someone who talked to them for less than a minute. 
# In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville 
# tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket.

    # sql_query = '''
    # SELECT c.caller, c.receiver, p1.name, p2.name 
    # FROM phone_calls AS c
    # JOIN people AS p1 ON c.caller = p1.phone_number
    # JOIN people AS p2 ON c.receiver = p2.phone_number
    # WHERE c.year = 2020 AND c.month = 7 AND c.day = 28 AND c.duration < 60
    # '''

    # [('(130) 555-0289', '(996) 555-8899', 'Roger', 'Jack'),
    #  ('(499) 555-9472', '(892) 555-8872', 'Evelyn', 'Larry'),
    #  ('(367) 555-5533', '(375) 555-8161', 'Ernest', 'Berthold'),
    #  ('(499) 555-9472', '(717) 555-1342', 'Evelyn', 'Melissa'),
    #  ('(286) 555-6063', '(676) 555-6554', 'Madison', 'James'),
    #  ('(770) 555-1861', '(725) 555-3243', 'Russell', 'Philip'),
    #  ('(031) 555-6622', '(910) 555-3251', 'Kimberly', 'Jacqueline'),
    #  ('(826) 555-1652', '(066) 555-9701', 'Bobby', 'Doris'),
    #  ('(338) 555-6650', '(704) 555-2131', 'Victoria', 'Anna')]


sql_query = '''
SELECT p.name, f.hour, a1.city, a2.city
FROM flights AS f
JOIN airports AS a1 ON f.origin_airport_id = a1.id
JOIN airports AS a2 ON f.destination_airport_id = a2.id
JOIN passengers AS p1 ON f.id = p1.flight_id
JOIN people AS p ON p1.passport_number = p.passport_number
WHERE a1.city = 'Fiftyville' 
AND p1.passport_number = 5773159633 
AND f.year = 2020 
AND f.month = 7 
AND f.day = 29
'''

# [('Ernest', 8, 'Fiftyville', 'London')] & (50, 'Ernest')

# [(686048, 'Ernest', '(367) 555-5533', 5773159633, '94KL13X')]
# [(514354, 'Russell', '(770) 555-1861', 3592750733, '322W7JE')]

rows = cursor.execute(sql_query).fetchall()
pprint(rows)
print(len(rows))