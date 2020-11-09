#!/usr/bin/env python3

#usage:  python/nasa/nasa_final.py -d 7 04 2004


import argparse
from datetime import date, timedelta
from random import randint
import os
import urllib.request

def parse_command_line():
    
    parser = argparse.ArgumentParser()

    # NASA developer key (You can hardcode yours for higher request rate limits!)
    API_KEY = "cZX0zRDveiz7AfGfOW23typMH3NCnS3uvQJc0ZNS"

    parser.add_argument('-d', '--date', metavar = ("month", "day", "year"), nargs = 3, type = int, help = 'formatted date (i.e. 03 28 1998)')

    parser.add_argument('-s', '--surprise', action = 'store_true', help = 'select a random date for a surprise image')

    parser.add_argument('-k', '--api_key', metavar = 'API_KEY', default = API_KEY)

    parser.add_argument('-v', '--verbose', action = 'store_true', help = 'verbose mode') 

    return parser.parse_args()


def create_date(datelist, surprise):
    
    early = date(day = 16, month = 6, year = 1995)
    today = date.today()
    yesterday = date(day = today.day - 1, month = today.month, year = today.year)

    if datelist:

        date_object = date(month = datelist[0], day = datelist[1], year = datelist[2])

        if date_object >= early:
            return date_object
        
    elif not datelist and surprise:

        d = randint(1, 31)
        m = randint(1, 12)
        y = randint(1995, today.year)
        
        random_date = date(month = m, day = d, year = y)
        
        try:
            if random_date >= early:
                return random_date
        
        except ValueError:
            return None
    else:
        return yesterday
    
def query_url(d, api_key):
    
    http_nasa = 'https://api.nasa.gov/planetary/apod?api_key='
    
    new_string = http_nasa + api_key + '&date=' + str(d)

    return new_string

    
def save_image(d, image):
    
    year = str(d.year)
    month = str(d.month)

    new_image = str(d) + '.jpg'

    os.chdir('/home/nick/project/devops/python/nasa')

    if not os.path.isdir(year):
        os.mkdir(year)
        os.chdir('/home/nick/project/devops/python/nasa' + '/' + year)
        os.mkdir(month)
        os.chdir(month)
    
        with open(new_image, 'wb') as new_image:
            new_image.write(image)

        new_image = str(d) + '.jpg'
        file_path = os.path.abspath(new_image)
    
        if(os.path.exists(file_path)):
            new_path = file_path[-22:]
            return new_path

    else:
        os.chdir('/home/nick/project/devops/python/nasa' + '/' + year)
        if not os.path.isdir(month):
            os.mkdir(month)
            os.chdir(month)
            with open(new_image, 'wb') as new_image:
                new_image.write(image)
        
            new_image = str(d) + '.jpg'
            file_path = os.path.abspath(new_image)
    
            if(os.path.exists(file_path)):
                new_path = file_path[-22:]
                return new_path

        else:
            os.chdir(month)
            with open(new_image, 'wb') as new_image:
                new_image.write(image)

            new_image = str(d) + '.jpg'
            file_path = os.path.abspath(new_image)
    
            if(os.path.exists(file_path)):
                new_path = file_path[-22:]
                return new_path

    
    
def request(url):
    """
    Download the metadata located at url and return it as a dictionary.
     
    args:
        url: to request image metadata for a specific date
    
    returns:
        dictionary of the metadata downloaded from url
        
    examples:
        if url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=2017-09-24"
        url_request(url) ==> returns dictionary:
        
        {
          "copyright": "The League of Lost Causes", 
          "date": "2017-09-24", 
          "explanation": "What is that light in the sky? Perhaps one of humanity's more common questions, an answer may result from a few quick observations.  For example -- is it moving or blinking? If so, and if you live near a city, the answer is typically an airplane, since planes are so numerous and so few stars and satellites are bright enough to be seen over the din of artificial city lights. If not, and if you live far from a city, that bright light is likely a planet such as Venus or Mars -- the former of which is constrained to appear near the horizon just before dawn or after dusk.  Sometimes the low apparent motion of a distant airplane near the horizon makes it hard to tell from a bright planet, but even this can usually be discerned by the plane's motion over a few minutes. Still unsure?   The featured chart gives a sometimes-humorous but mostly-accurate assessment.  Dedicated sky enthusiasts will likely note -- and are encouraged to provide -- polite corrections.   Chart translations: Spanish, Italian, Polish, Tamil, Kannada, Latvian, and Norwegian", 
          "hdurl": "https://apod.nasa.gov/apod/image/1709/astronomy101_hk_750.jpg", 
          "media_type": "image", 
          "service_version": "v1", 
          "title": "How to Identify that Light in the Sky", 
          "url": "https://apod.nasa.gov/apod/image/1709/astronomy101_hk_960.jpg"
        }
        
    """
    
    # request the content of url and save the retrieved binary data
    with urllib.request.urlopen(url) as response:
        data = response.read()
    
    # convert data from byte to string
    data = data.decode('UTF-8')
    
    # convert data from string to dictionary
    data = eval(data)
    return data

def download_image(url):
    """
    Download the image located at url.
    
    args:
        url: where actual image is located
        
    returns:
        image as binary data
    """
    
    # request the content of url and return the retrieved binary image data
    with urllib.request.urlopen(url) as response:
        image = response.read()
    return image

def main():

    # parse command line arguments
    args = parse_command_line()
    print(args)
    
    # create a request date
    d = create_date(args.date, args.surprise)
    
    # ascertain a valid date was created, otherwise exit program
    if d is None:
        print("No valid date selected!")
        exit()
    
    # verbose mode
    if args.verbose:
        print("Image date: {}".format(d.strftime("%b %d, %Y")))
        
    # generate query url
    url = query_url(d, args.api_key)

    # verbose mode    
    if args.verbose:
        print("Query URL: {}".format(url))
        
    # download the image metadata as a Python dictionary
    metadata = request(url)

    # verbose mode    
    if args.verbose:
        # display image title, other metadata can be shown here
        print("Image title: {}".format(metadata['title']))
    
    # get the url of the image data from the dictionary
    image_url = metadata['url']

    # verbose mode    
    if args.verbose:
        print("Downloading image from:", image_url)
        
    # download the image itself (the returned info is binary)
    image = download_image(image_url)
    
    # save the downloaded image into disk in (year/month)
    # the year and month directories correspond to the date of the image (d)
    # the file name is the date (d) + '.jpg'
    save_image(d, image)

    print("Image saved")

if __name__ == '__main__':
    main()