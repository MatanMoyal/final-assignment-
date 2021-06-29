from abc import ABC, abstractmethod
from time import sleep


class File(ABC):
    @abstractmethod
    def __init__(self, file_name, file_content, created_by, file_size):
        self.file_name = file_name
        self.file_content = file_content
        self.created_by = created_by
        self.file_size = file_size


class IAsMail_Mixin(ABC):

    @abstractmethod
    def as_email_format(self):
        pass

    @abstractmethod
    def send(self, sender_mail, email_address):
        pass


class PlayableFile_Mixin(ABC):

    @abstractmethod
    def __init__(self, volume=0):
        self.volume = volume

    def volume_up(self):
        self.volume += 5

    def volume_down(self):
        self.volume =- 5

    def play(self):
        print(self.volume)


class MediaFile(File, PlayableFile_Mixin):

    def __init__(self, file_name, file_content, created_by, file_size, duration):
        File.__init__(self, file_name, file_content, created_by, file_size)
        PlayableFile_Mixin.__init__(self)
        self.duration = duration

    @abstractmethod
    def play(self):
        super().play()
        for i in range(self.duration):
            print(i + 1)
            sleep(0.5)


