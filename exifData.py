#!/usr/bin/env python3
# -*- coding: utf8 -*-

import re
from exifread import process_file

class TagError(Exception):
    def __init__(self, value="Tag not found"):
        self.value = value

    def __str__(self):
        return repr(self.value)


class ExifData:
    def __init__(self, path, details=False):
        self.path = path
        self.rePatterns = {
            'GPS': re.compile('EXIF GPS GPS[A-Za-z]+'),
            'Date': None
        }
        self.coordKeys = {
            'latRef': 'EXIF GPS GPSLatitudeRef',
            'lat': 'EXIF GPS GPSLatitude',
            'lonRef': 'EXIF GPS GPSLongitudeRef',
            'lon': 'EXIF GPS GPSLongitude'
        }

        try:
            self.fo = open(self.path, 'rb')
        except IOError:
            print('Could not open file')
            return

        self.tags = process_file(self.fo, details=details)

    def __filter(self, name):
        for tag in self.tags.keys():
            match = self.rePatterns[name].search(tag)

            if match:
                yield match.string

    def __fromDMStoDD(self, DMSCoord):
        """
        translate DMS (degrees, minutes, seconds) exifread form to readable DD
        """

    def dump(self, name='GPS'):
        """
        dump any values that could be found in exifread's returned data
        related to name (by default GPS)
        """
        for tag in self.__filter(name):
            print(tag + ':', self.tags[tag])

    def filter(self):
        """
        return every name that could be passed to dump
        """
        return [k for k in self.rePatterns.keys()]

    def coordinates(self):
        """
        return longitude and latitude from DMS notation
        to a tuple based on following tags' keys defined in self.coordKeys dict:
        EXIF GPS GPSLatitudeRef
        EXIF GPS GPSLatitude
        EXIF GPS GPSLatitudeRef
        EXIF GPS GPSLongitude
        """
        value = lambda t: None if t not in self.tags.keys() else self.tags[t]

        lat = str(value(self.coordKeys['latRef'])) + ' ' +\
            self.__fromDMStoDD(str(value(self.coordKeys['lat'])))
        lon = str(value(self.coordKeys['lonRef'])) + ' ' +\
            self.__fromDMStoDD(str(value(self.coordKeys['lon'])))


        print((lat, lon))

        return (lat, lon)

