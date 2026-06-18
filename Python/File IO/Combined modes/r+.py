"""
The argument mode points to a string beginning with one of the following
sequences (Additional characters may follow these sequences.):

r : Open text file for reading. The stream is positioned at the
    beginning of the file.

r+: Open for reading and writing. The stream is positioned at the
    beginning of the file.

w : Truncate file to zero length or create text file for writing.
    The stream is positioned at the beginning of the file.

w+ :Open for reading and writing. The file is created if it does not
    exist, otherwise it is truncated. The stream is positioned at
    the beginning of the file.

a : Open for writing. The file is created if it does not exist. The
    stream is positioned at the end of the file. Subsequent writes
    to the file will always end up at the then current end of file,
    irrespective of any intervening fseek(3) or similar.

a+ Open for reading and writing. The file is created if it does not
   exist. The stream is positioned at the end of the filel Subse-
   quent writes to the file will always end up at the then current
   end of file, irrespective of any intervening fseek(3) or similar.

w+ *.
"""



f = open("E:\Material\Coding\Python\File IO\demo.txt","r+")
f.write("abc") # cursor reach at override word till c 
print(f.read()) # thus prints words aper c
f.close()