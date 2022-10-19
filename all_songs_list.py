import os
import music
from music_list import MusicList 

class AllSongsList(MusicList):

    def __init__(self, search_dir:str):
        super().__init__()

        tmp_line:str
        files = os.listdir(search_dir)

        for i in range(len(files)):
            tmp_line = files[i].split(".")
            if(tmp_line[1] == "mp3" or tmp_line[1] == "wav" \
                    or tmp_line[1] == "ogg"):
                self.music_list.append(files[i])

if __name__ == "__main__":
    tmp_list = AllSongsList("./materials")
    print(tmp_list.music_list)

