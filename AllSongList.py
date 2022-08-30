import os
import Music
from MusicList import MusicList 

class AllSongsList(MusicList):
    music_list:list 

    def __init__(self, search_dir:str):
        self.music_list = []
        
        tmp_line:str
        files = os.listdir(search_dir)

        for i in range(len(files)):
            tmp_line = files[i].split(".")
            if(tmp_line[1] == "mp3" or tmp_line[1] == "wav" or tmp_line[1] == "ogg"):
                self.music_list.append(files[i])

        #self.music_list =  os.listdir(search_dir) 

    def seach_title(self, title:str) -> Music:
        pass

if __name__ == "__main__":
    tmp_list = AllSongsList("./materials")
    print(tmp_list.music_list)

