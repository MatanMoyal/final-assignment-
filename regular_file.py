from classes.abstracts_files import File, MediaFile
from classes.abstracts_files import IAsMail_Mixin


class WordFile(File, IAsMail_Mixin):
    def __init__(self, file_name, file_content, created_by, file_size):
        File.__init__(self, file_name, file_content, created_by, file_size)

    def __str__(self):
        return str(self.file_name + " " + self.file_content + self.created_by + " " + str(self.file_size))

    def send(self, sender_mail, email_address=list):
        pass

    def as_email_format(self):
        print(f"{self.file_name},{self.file_content}_by_@{self.created_by}.{self.file_size} ")




class PDFFile(WordFile):
    def __init__(self, file_name, file_content, created_by, file_size, is_writable=True):
        self.is_writable = is_writable
        self.__file_content = file_content
        WordFile.__init__(self, file_name, file_content, created_by, file_size)

    def __str__(self):
        return str(self.file_name + " " + self.file_content + " " + self.created_by + " " +
                   str(self.file_size) + " " + str(self.is_writable))

        @property
        def is_writeable(self):
            return self.__file_content

        @is_writeable.setter
        def is_writeable(self, file_content):
            if self.is_writable:
                self.__file_content = file_content
            else:
                print("not allowed to change file content")


class PictureFile(File):
    def __init__(self, file_name, file_content, created_by, file_size, dim_width, dim_height):
        super().__init__(file_name, file_content, created_by, file_size)
        self.dim_width = dim_width
        self.dim_height = dim_height

    def __str__(self):
        return str(
            self.file_name + " " + self.file_content + " " + self.created_by + " " + str(self.file_size) + " " +
            str(self.dim_width) + " " + str(self.dim_height))

    def show_picture(self):
        for i in range(self.dim_height):
            for j in range(self.dim_width):
                print("x", end='')
            print()


class SongFile(MediaFile):

    def __init__(self, file_name, file_content, created_by, file_size, duration, song_name, artist):
        super().__init__(file_name, file_content, created_by, file_size, duration)
        self.song_name = song_name
        self.artist = artist



    def __str__(self):
        return str(
            self.file_name + " " + self.file_content + " " + self.created_by + " " + str(self.file_size) + " " +
            str(self.volume) + " " + str(self.duration) + " " + self.song_name + " " + self.artist)

    def play(self):
        print(f"song name:{self.song_name} \n artist:{self.artist} \n duration:")
        super().play()


class MovieFile(MediaFile):
    def __init__(self, file_name, file_content, created_by, file_size, duration, movie_name, director):
        super().__init__(file_name, file_content, created_by, file_size, duration)
        self.movie_name = movie_name
        self.director = director

        

    def __str__(self):
        return str(self.file_name + " " + self.file_content + " " + self.created_by + " " + str(self.file_size) + " " +
                   str(self.volume) + " " + str(self.duration) + " " + self.movie_name + " " + self.director)

    def play(self):
        print(f"movie name:{self.movie_name} \n director:{self.director} \n duration:")

        super().play()






