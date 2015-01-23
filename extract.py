#!/usr/bin/env python3

import sys
from exifread import process_file

def extract_exif_data(filename):
    try:
        print("opening file:", filename)
        f = open(filename, 'rb')
    except IOError:
        print("Could not open file")
        return

    tags = process_file(f, True)

    if "Image GPSInfo" in tags.keys():
        print(tags["Image GPSInfo"])
    else:
        print("no data found")

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        extract_exif_data(arg)
