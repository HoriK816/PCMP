import pygame
import time 
from Music import Music
from PlaySetting import PlaySetting
from MusicList import MusicList
from AllSongsList import AllSongsList
from SystemSetting import SystemSetting

class MusicPlayer:
    key_input : str
    all_songs : AllSongsList
    play_info : Music
    play_index : int #consider it !!
    play_setting : PlaySetting
    system_setting : SystemSetting

    def __init__(self):
        self.system_setting = SystemSetting()
        self.all_songs = AllSongsList(self.system_setting.search_path)
        self.play_info = None
        self.play_setting = PlaySetting()
        #print(self.all_songs.music_list)  
        self.skip_direction = True # for test 

    def play_title(self,title:str) -> None :
        for i in range(len(self.all_songs.music_list)):
            if(title ==  self.all_songs.music_list[i]):
                self.play_info = Music("materials/"+title)
                self.play_index = i 
               
                #for test
                self.play_info.play(self.play_setting)  
                counter = 0
                while(counter < 5):
                    time.sleep(1)
                    counter += 1



    def skip_song(self,direction:bool) -> None:

        if(direction):
            ret_val = self.all_songs.skip_song_to_next(self.play_index)
            self.play_index = ret_val[0] 
            self.play_info = ret_val[1]

            print("skip the song!")
            print("index=" + str(self.play_index))
            print(self.play_info.file_name)

            self.play_title(self.play_info.file_name) 
        else:
            ret_val = self.all_songs.skip_song_to_previous(self.play_index)
            self.play_index = ret_val[0]
            self.play_info = ret_val[1]
            print("skip the song!")
            print("index=" + str(self.play_index))
            print(self.play_info.file_name)

            self.play_title(self.play_info.file_name)
 
    def move_5seconds(self,direction:bool) -> None:
        pass

    def volume_control(self,direction:bool) -> None:
        pass

    def change_dir(self,new_path:str) -> None:
        new_dir = input()
        system_setting.change_search_path(new_dir)

    def change_sort_method(self) -> None:
        pass

    def main(self) -> None: # main loop
        pass

if __name__ == "__main__":
    player = MusicPlayer()
    player.play_title("kibou.mp3")
    player.skip_song(False)
    player.skip_song(False)
    player.skip_song(False)
    player.skip_song(False)
    player.skip_song(False)
 
