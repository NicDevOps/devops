#!/usr/bin/env python3

# python/nasa/nasa_api.py

import argparse
from datetime import date
from random import randint
import os, os.path


def parse_command_line():
    """
    Parse the command line arguments and return the argparse object.
        
    There should be no positional arguments and 4 optional arguments.
    The help message generated by the parser should look like:
    usage: apod.py [-h] [-d month day year] [-s] [-k API_KEY] [-v]

    optional arguments:
      -h, --help            show this help message and exit
      -d month day year, --date month day year
                            formatted date (i.e. 03 28 1998)
      -s, --surprise        select a random date for a surprise image
      -k API_KEY, --api_key API_KEY
                            NASA developer key
      -v, --verbose         verbose mode


    HINT: for the --date optional argument, use a tuple: metavar = ("month", "day", "year")

    args:
        None
        
    returns:
        args: generated argparse object with all the parsed command line arguments      
    """
    parser = argparse.ArgumentParser()
    
    API_KEY = "cZX0zRDveiz7AfGfOW23typMH3NCnS3uvQJc0ZNS"

    parser.add_argument('-d', '--date',metavar = ("month", "day", "year"), nargs = 3, type = int, help = 'formatted date (i.e. 03 28 1998)')

    parser.add_argument('-s', '--surprise', action = 'store_true', help = 'select a random date for a surprise image')

    parser.add_argument('-k', '--api_key',metavar = API_KEY, default = API_KEY)

    parser.add_argument('-v', '--verbose', action = 'store_true', help = 'verbose mode') 

    return parser.parse_args()

def create_date(datelist, surprise):
    """
    Create a valid date object.
    
    If datelist is not an empty list, create a date object using the data in the list [month day year].
    If datelist is empty, and surprise is True, create a random date object between June 16 1995 and today.
    If datelist is empty and surprise is False, create a date object using yesterday's date
    
    If the datelist contain invalid information (i.e. month = 1323), the function should return None
    If the created date is invalid (i.e. earlier than June 16 1995 or later than today), the function should return None
    
    HINTS: 
        - Use exception handling to validate the info in the datelist
        - Use timedelta objects to generate a surprise date
    
    args:
        d: list containing the [month, day, year] or an empty list []
        surprise: Boolean, if True and datelist is empty, generate a random date 
                  the earliest valid date is June 16 1995
    
    returns:
        created valid date object or None when date selected by user is invalid (i.e. in the future)
    """
    
    early = date(day = 16, month = 6, year = 1995)
    today = date.today()

    if datelist:

        date_object = date(month = datelist[0], day = datelist[1], year = datelist[2])

        if date_object >= early:
            return date_object
        
    if not datelist and surprise:

        d = randint(1, 31)
        m = randint(1, 12)
        y = randint(1995, today.year)
        
        random_date = date(month = m, day = d, year = y)
        
        try:
            if random_date >= early:
                return random_date
        
        except ValueError:
            return None

def query_url(d, api_key):
    """
    Create a URL to fetch an image metadata (not the image itself).
    
    The base URL is https://api.nasa.gov/planetary/apod?
    For a complete URL, the api_key and the date (d) (formatted as YYYY-MM-DD) should be added to the base.
    For example, if date object (d) represents July 5 2016 and api_key is DEMO_KEY, the complete URL is:
    
    https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=2016-07-05
    
    HINTS: 
        - Use strftime to format the date object (d) as necessary
    
    args:
        d: date object containing a valid date
        api_key: string containing "DEMO_KEY" or your valid NASA developer key for higher request rate limits
        
    returns:
        complete url as a string
        
    examples:
        d is a date object representing Sep 24 2017
        query_url(d, "DEMO_KEY") ==> returns https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=2017-09-24
        
        d is a date object representing Jul 19 1999
        query_url(d, "ABCDEFG") ==> returns https://api.nasa.gov/planetary/apod?api_key=ABCDEFG&date=1999-07-19
    """
    
    http_nasa = 'https://api.nasa.gov/planetary/apod?api_key='
    
    new_string = http_nasa + api_key + '&date=' + str(d)

    return new_string


def save_image(d, image):
    """
    Save binary image on disk.
    
    Use the date of the image (d) to create a directory structure (year/month) if it doesn't exist already,
    then save the binary image under its corresponding year and month using the date (d) + '.jpg' as a file name
    
    HINT: Binary data can be written to files in a similar way to how strings are written to files.
          Use 'wb' (write binary) instead of 'w' in the file open clause (i.e. open(file_path, 'wb'))

    args:
        d: date object containing image date
        image: binary image itself
    
    returns:
        file_path: where the image was saved
        
    examples:
        if d = 2017-8-21, the image will be saved as: 2017/8/2017-8-21.jpg
        if d = 1998-4-15, the image will be saved as: 1998/4/1998-4-15.jpg
    """
    year = d[0:4]
    month = d[5:7]

    new_image = d + '.jpg'

    os.chdir('/home/nick/project/devops/python/nasa')

    if not os.path.isdir(year):
        os.mkdir(year)
        os.chdir('/home/nick/project/devops/python/nasa' + '/' + year)
        os.mkdir(month)
        os.chdir(month)
    
        with open(new_image, 'w') as new_image:
            new_image.write(image)

        new_image = d + '.jpg'
        file_path = os.path.abspath(new_image)
    
        if(os.path.exists(file_path)):
            new_path = file_path[-22:]
            return new_path

    else:
        os.chdir('/home/nick/project/devops/python/nasa' + '/' + year)
        if not os.path.isdir(month):
            os.mkdir(month)
            os.chdir(month)
            with open(new_image, 'w') as new_image:
                new_image.write(image)
        
            new_image = d + '.jpg'
            file_path = os.path.abspath(new_image)
    
            if(os.path.exists(file_path)):
                new_path = file_path[-22:]
                return new_path

        else:
            os.chdir(month)
            with open(new_image, 'w') as new_image:
                new_image.write(image)

            new_image = d + '.jpg'
            file_path = os.path.abspath(new_image)
    
            if(os.path.exists(file_path)):
                new_path = file_path[-22:]
                return new_path
  
  


# python/nasa/nasa_api.py -d 05 17 2020

r =  parse_command_line()
print(r)
d = create_date(r.date, r.surprise)
print(d)
q = query_url(d, r.api_key)


print(q)