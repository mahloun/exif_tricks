#!/usr/bin/env python3

import sys
from exifread import process_file

gpsTags = [
    "EXIF GPS GPSImgDirection",
    "EXIF GPS GPSDate",
    "Image GPSInfo",
    "EXIF GPS GPSImgDirectionRef",
    "EXIF GPS GPSTimeStamp"
]

def extract_exif_data(filename):
    try:
        print("opening file:", filename)
        f = open(filename, 'rb')
    except IOError:
        print("Could not open file")
        return

    tags = process_file(f, True)

    for gpsTag in gpsTags:
        if gpsTag in tags.keys():
            print(gpsTag + ':', tags[gpsTag])

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        extract_exif_data(arg)
