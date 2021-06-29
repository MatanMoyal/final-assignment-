from classes.abstracts_files import File, MediaFile
from classes.abstracts_files import IAsMail_Mixin
import json
from classes.regular_file import PDFFile, WordFile, PictureFile, SongFile
from classes.PART2 import FileSystem

with open('thefile.txt', mode='r') as file:
    content = json.load(file)

file_system = FileSystem()
for file in content:
    file_system.add_file(file)

# Print all Correct Files
print('-' * 50, '\nAll Correct Files\n', '-' * 15)
for file in file_system.files:
    print(file)
print('-' * 50)

# delete file
print('-' * 50, '\nDelete Method\n', '-' * 15)
file_system.delete_file("file1.pdf")
print('-' * 50)

# get file
print('-' * 50, '\nGet Files Method\n', '-' * 15)
for file in file_system.getFiles("PDFFile"):
    print(file)
print('-' * 50)

# clone file
print('-' * 50, '\nClone Method\n', '-' * 15)
file_system.cloneFile('file2.pdf')
for file in file_system.files:
    print(file)
print('-' * 50)

# concat files
print('-' * 50, '\nConcat Method\n', '-' * 15)
file_system.concatFiles('file2.pdf', 'file3.pdf')
for file in file_system.files:
    print(file)
print('-' * 50)


