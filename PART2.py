import json

from classes.regular_file import PDFFile, WordFile, PictureFile, SongFile, MovieFile
from copy import copy


class FileSystem:
    types = ["doc", "docx", "pdf", "png", "jpeg", "jpg", "mp3", "wav", "mp4", "avi"]

    # attributes_Movie = ['movie_name', 'director', 'duration', 'file_name', 'created_by', "volume", 'file_size',
    #                     'file_content']
    # attributes_Song = ['song_name', 'artist', 'duration', 'file_name', 'created_by', "volume", 'file_size',
    #                    'file_content']
    # attributes_Picture = ['file_name', 'created_by', 'file_size', 'file_content', "dim_width", "dim_height"]
    # attributes_Pdf = ['file_name', 'created_by', 'file_size', 'file_content', "is_writable"]
    # attributes_Word = ['file_name', 'created_by', 'file_size', 'file_content']

    def __init__(self):
        self.max_size = 50
        self.files = []

    # יצירת האובייקטים ע"פ סוג הקובץ
    def to_pdf(self, file_json):

        file = PDFFile(
            file_json['file_name'],
            file_json['file_content'],
            file_json['created_by'],
            file_json['file_size'],
            file_json['is_writable'])

        return file

    def to_word(self, file_json):
        file = WordFile(
            file_json['file_name'],
            file_json['file_content'],
            file_json['created_by'],
            file_json['file_size']
        )
        return file

    def to_picture(self, file_json):
        file = PictureFile(

            file_json['file_name'],
            file_json['file_content'],
            file_json['created_by'],
            file_json['file_size'],
            file_json['dim_width'],
            file_json['dim_height']
        )
        return file

    def to_song(self, file_json):
        file = SongFile(
            file_json['file_name'],
            file_json['file_content'],
            file_json['created_by'],
            file_json['file_size'],
            file_json['duration'],
            file_json['song_name'],
            file_json['artist']
        )
        return file

    def to_movie(self, file_json):

        file = MovieFile(

            file_json['file_name'],
            file_json['file_content'],
            file_json['created_by'],
            file_json['file_size'],
            file_json['duration'],
            file_json['movie_name'],
            file_json['director']
        )
        return file


# פונקציות שבודקות האם כל התכונות קיימות בקובץ הנבדק ומוסיפה אותו לרשימה הסופית
    def Movie_check_att(self, file_json):

        attributes_Movie = ['movie_name', 'director', 'duration', 'file_name', 'created_by', 'file_size',
                            'file_content']

        temp = True
        for key in attributes_Movie:
            if key not in file_json.keys():
                temp = False
                break
            else:
                continue
        if temp == True:

            good_file = self.to_movie(file_json)
            self.files.append(good_file)

        else:
            print("cant add this file not exist attribute")

    def Pdf_check_att(self, file_json):

        attributes_Pdf = ['file_name', 'created_by', 'file_size', 'file_content', "is_writable"]

        temp = True
        for key in attributes_Pdf:
            if key not in file_json.keys():
                temp = False
                break
            else:
                continue
        if temp == True:

            good_file = self.to_pdf(file_json)
            self.files.append(good_file)

        else:
            return ("cant add this file not exist attribute")

    def Song_check_att(self, file_json):

        attributes_Song = ['song_name', 'artist', 'duration', 'file_name', 'created_by', 'file_size',
                           'file_content']

        temp = True
        for key in attributes_Song:
            if key not in file_json.keys():
                temp = False
                break
            else:
                continue
        if temp == True:

            good_file = self.to_song(file_json)
            self.files.append(good_file)

        else:
            return ("cant add this file not exist attribute")

    def Word_check_att(self, file_json):

        attributes_Word = ['file_name', 'created_by', 'file_size', 'file_content']

        temp = True
        for key in attributes_Word:
            if key not in file_json.keys():
                temp = False
                break
            else:
                continue
        if temp == True:

            good_file = self.to_word(file_json)
            self.files.append(good_file)

        else:
            return ("cant add this file not exist attribute")

    def Picture_check_att(self, file_json):

        attributes_Picture = ['file_name', 'created_by', 'file_size', 'file_content', "dim_width", "dim_height"]

        temp = True
        for key in attributes_Picture:
            if key not in file_json.keys():
                temp = False
                break
            else:
                continue
        if temp == True:

            good_file = self.to_picture(file_json)
            self.files.append(good_file)

        else:
            print("cant add this file not exist attribute: ",key)

#פונקציה שבודקת האם הקבצים תקינים(גודל קובץ,כפילויות,תקינות)
    def add_file(self, file_json):
#לולאה שבודקת האם השם של הקובץ קיים כבר
        for file in self.files:
            if (file.file_name == file_json['file_name']):
                print("File is Exist:", file.file_name)
                return None

        if file_json["file_name"].split(".")[1] == "pdf":

            if file_json["file_size"] <= self.max_size:
                self.Pdf_check_att(file_json)
            else:
                print("cant add this file size / duplicate")

        elif file_json["file_name"].split(".")[1] == "doc" or file_json["file_name"].split(".")[1] == "docx":
            if file_json["file_size"] <= self.max_size:
                self.Word_check_att(file_json)
            else:
                print("cant add this file size / duplicate")


        elif file_json["file_name"].split(".")[1] == "png" or file_json["file_name"].split(".")[1] == "jpeg" or \
 \
                file_json["file_name"].split(".")[1] == "jpg":
            if file_json["file_size"] <= self.max_size:
                self.Picture_check_att(file_json)
            else:
                print("cant add this file size / duplicate")


        elif file_json["file_name"].split(".")[1] == "mp3" or file_json["file_name"].split(".")[1] == "wav":
            if file_json["file_size"] <= self.max_size:
                self.Song_check_att(file_json)
            else:
                print("cant add this file size / duplicate")


        elif file_json["file_name"].split(".")[1] == "mp4" or file_json["file_name"].split(".")[1] == "avi":
            if file_json["file_size"] <= self.max_size:
                self.Movie_check_att(file_json)
            else:
                print("cant add this file size / duplicate")

        else:
            print("cant add this file not exist type")

        return self.files


    def delete_file(self, file_name):
        for file in self.files:
            if (file.file_name == file_name):
                print('File is Deleted: \n', file)
                self.files.remove(file)


    def getFiles(self, type_file=None):
        if (type_file):
            temp = []
            for file in self.files:
                if (type_file in type(file).__name__):
                    temp.append(file)
            return temp
        return self.files



    def cloneFile(self, file_name):
        for file in self.files:
            if (file.file_name == file_name):
                newFile = copy(file)
                newFile.file_name = 'CLONE_' + file_name
                self.files.append(newFile)



    def concatFiles(self, file_name1, file_name2):
        temp = []
        for file in self.files:
            if (file.file_name == file_name1 or file.file_name == file_name2):
                temp.append(file)

            if (len(temp) == 2):
                break
        if (len(temp) == 2):
            temp[0] = copy(temp[0])
            if (type(temp[0]).__name__ == type(temp[1]).__name__):
                temp[0].file_name = temp[0].file_name.split('.')[0] + '_' + temp[1].file_name.split('.')[0] + '.' + \
                                    temp[0].file_name.split('.')[1]
                temp[0].file_content = '(' + temp[0].file_content + "_" + temp[1].file_content + ')'
                temp[0].file_size = temp[0].file_size + temp[1].file_size
                temp[0].created_by = temp[0].created_by + "_" + temp[1].created_by

                if (type(temp[0]).__name__ == 'SongFile'):

                    print(type(temp[0]).__name__)
                    temp[0].duration = temp[0].duration + temp[1].duration
                    temp[0].artist = temp[0].artist + "_" + temp[1].artist
                    temp[0].song_name = temp[0].song_name + "_" + temp[1].song_name

                elif (type(temp[0]).__name__ == 'MovieFile'):
                    temp[0].director = temp[0].director + "_" + temp[1].director
                    temp[0].movie_name = temp[0].movie_name + "_" + temp[1].movie_name
                    temp[0].duration = temp[0].duration + temp[1].duration

                elif (type(temp[0]).__name__ == 'PictureFile'):
                    temp[0].dim_width = temp[0].dim_width + temp[1].dim_width
                    temp[0].dim_height = temp[0].dim_height + temp[1].dim_height
                else:
                    temp[0].is_writable = str(temp[0].is_writable) + "_" + str(temp[1].is_writable)
                self.files.append(temp[0])
