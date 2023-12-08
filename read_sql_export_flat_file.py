# -*- coding: utf-8 -*-
"""
Created on Wed Dec 6 09:35:34 2023

@author: dindraatmadja

This script is used to handle line breaks within fields in exported SQL tables.
During the SQL export, we specify a custom delimiter and line_terminator and
replace those values in this script.

"""
import chardet

path_to_file = 'test_chunk_read.txt'  # Path to SQL table flat file export
line_terminator = "#^#"  # Line terminator used in SQL export
delimiter = "#|#"  # Delimiter used in SQL export

new_path_to_file = "./outputs/output.txt"  # Output file name and path
new_delimiter = ","  # New delimiter to be used in output
new_encoding = "utf-8"  # New encoding to be used in output

# Detect file encoding
with open(path_to_file, 'rb') as file:
    encoding = chardet.detect(file.read(1024 * 1024))['encoding']  # Read only the first 1 MB for encoding detection

# Function to process chunks
def process_chunk(chunk):
    return chunk.replace('\n', '').replace(line_terminator, '\n').replace(new_delimiter, '').replace(delimiter, new_delimiter)

# Read, process, and write the file in chunks
chunk_size = 5  # 1 MB
with open(path_to_file, 'r', encoding=encoding) as file:
    with open(new_path_to_file, 'w', encoding=new_encoding) as output_file:
        carry_over = ''
        while True:
            chunk = carry_over + file.read(chunk_size)            
            # Extend the read to include the next part of line_terminator
            extension = file.read(max(len(line_terminator), len(delimiter))-1)
            
            # if delimiter/line_terminator rfind on chunk + extension is different from delimiter/line_terminator rfind on chunk
            delim_rfind_ch = (chunk).rfind(delimiter)
            lineterm_rfind_ch = (chunk).rfind(line_terminator)
            delim_rfind_ch_ex = (chunk + extension).rfind(delimiter)
            lineterm_rfind_ch_ex = (chunk + extension).rfind(line_terminator)
            if (lineterm_rfind_ch_ex > lineterm_rfind_ch) or (delim_rfind_ch_ex > delim_rfind_ch):
                
            
            print(chunk)
            print(extension)
            next_terminator_start = (chunk + extension).find(line_terminator[0])
            if next_terminator_start != -1:
                chunk += extension[:next_terminator_start]
                carry_over = extension[next_terminator_start:]
            else:
                chunk += extension
                carry_over = ''

            if not chunk:
                break

            processed_chunk = process_chunk(chunk)
            output_file.write(processed_chunk)

        # Process and write any remaining carry_over
        if carry_over:
            processed_carry_over = process_chunk(carry_over)
            output_file.write(processed_carry_over)