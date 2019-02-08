#!/usr/bin/env python

import os

myfilename = "housing.data.txt"

with open(myfilename, 'r') as file_handle:
    for line in file_handle.readlines():
        line_clean = line.replace('   ', ' ').replace('  ', ' ')
        line_clean = line_clean.strip()
        values = line_clean.split(' ')
        cast = []
        print(values)
        for value in values:
             if '.' in value:
                cast.append(float(value))
             else:
                cast.append(int(value))
        print (cast)
    print('finished!')

