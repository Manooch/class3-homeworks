#!/usr/bin/env python

import os

myfilename = "housing.data.txt"


with open(myfilename, 'r') as file_handle:
    transpos = []
    for line in file_handle.readlines():
        line_clean = line.replace('   ', ' ').replace('  ', ' ')
        line_clean = line_clean.strip()
        values = line_clean.split(' ')
        cast = []
        print("Original file:")
        print(values)
#Convert to proper data type
        print("Convert to proper datatype:")
        for value in values:
             if '.' in value:
                cast.append(float(value))
             else:
                cast.append(int(value))
        print(cast)
#Transpose the list
        transpos.append(cast)
    print("Transpose columns to rows:")
    final = list(map(list, zip(*transpos)))
    for value in final:
        print(value)

    print('finished!')
