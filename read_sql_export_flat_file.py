# -*- coding: utf-8 -*-
"""
Created on Wed Dec 6 09:35:34 2023

@author: dindraatmadja

This script is used to handle line breaks within fields in exported SQL tables.
During the SQL export, we specify a custom delimiter and line_terminator and
replace those values in this script.

"""
import chardet  # Used to detect file encoding

path_to_file = '3 char delim and line ending.txt'  # Path to SQL table flat file export
line_terminator = "#^#"  # Line terminator used in SQL export
delimiter = "#|#"  # Delimiter used in SQL export

new_path_to_file = "./outputs/output.txt"  # Output file name and path
new_delimiter = ","  # New delimiter to be used in output
new_encoding = "utf-8"  # New encoding to be used in output

# Detect file encoding
encoding = chardet.detect(open(path_to_file, 'rb').read())['encoding']

# Open, read, and close text file
opened_file = open(path_to_file, 'r', encoding=encoding)
read_file = opened_file.read()
opened_file.close()

# Clean linebreaks from data and replace line terminator and delimiter characters
read_file = read_file.replace('\n', '').replace(line_terminator, '\n').replace(new_delimiter, '').replace(delimiter, new_delimiter)

# Write cleaned table data to output file
with open(new_path_to_file, 'w', encoding=new_encoding) as f:
    f.write(read_file)
