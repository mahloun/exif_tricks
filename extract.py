#!/usr/bin/env python3

import sys
import re
from exifread import process_file

def getGpsTags(tags):
    pattern = re.compile("GPS GPS[A-Za-z]+")
    gpsTags = []

    for tag in tags:
        match = pattern.search(tag)

        if match:
            gpsTags.append(match.string)

    return gpsTags

def extract_exif_data(filename):
    try:
        print("opening file:", filename)
        f = open(filename, 'rb')
    except IOError:
        print("Could not open file")
        return

    tags = process_file(f, True)
    gpsTags = getGpsTags(tags)

    for gpsTag in gpsTags:
        if gpsTag in tags.keys():
            print('\t'+ gpsTag.replace("EXIF GPS GPS", "") + ':', tags[gpsTag])


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        extract_exif_data(arg)
