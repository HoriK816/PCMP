import pygame
import time 
from Music import Music
from PlaySetting import PlaySetting
from MusicList import MusicList
from AllSongsList import AllSongsList
from SystemSetting import SystemSetting

class MusicPlayer:
    key_input : str

    def __init__(self):
        self.system_setting = SystemSetting()
        self.all_songs = AllSongsList(self.system_setting.search_path)

    def play_title(self,title:str) -> None :
        for i in range(len(self.all_songs.music_list)):
            print(self.all_songs.music_list[i])
        self.key_input = input() 
         

if __name__ == "__main__":
    player = MusicPlayer()
    player.play_title("materials/music_for_programming_1-datassette.mp3")

