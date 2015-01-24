#!/usr/bin/env python3
# -*- coding: utf8 -*-

import re
from exifread import process_file

class ExifData:
    def __init__(self, path, details=False):
        self.tag = {}
        self.path = path
        self.rePatterns = {
            'GPS': re.compile('GPS GPS[A-Za-z]+'),
            'Date': None
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
