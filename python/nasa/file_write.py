#!/usr/bin/env python3

import os, os.path

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

d = '2020-05-10'
image = '/home/nick/project/devops/python/nasa/nasa_test.txt'

def save_image(d, image):

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
# 2020/05/2020-05-10.jpg

f = save_image(d, image)

print(f)
