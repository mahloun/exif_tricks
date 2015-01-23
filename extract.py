#/usr/bin/env python2

import sys
from exifread import process_file

def extract_exif_data(filename):
    try:
        f = open(filename, 'rb')
    except IOError:
        print("Could not open file")
        return

    tags = process_file(f)

    if tags.has_key("Image GPSInfo"):
        print(tags["Image GPSInfo"])

if __name__ == "main":
    for arg in sys.argv[1:]:
        extract_exif_data(arg)
