import pygame
import os
import time 
from Music import Music
from PlaySetting import PlaySetting
from MusicList import MusicList
from AllSongsList import AllSongsList
from SystemSetting import SystemSetting
from PlayList import PlayList

class MusicPlayer:
    key_input : str
    all_songs : AllSongsList
    play_info : Music
    play_index : int #consider it !!
    play_setting : PlaySetting
    system_setting : SystemSetting
    all_playlist : list
    playlist_name : str

    def __init__(self):

        #setting 
        self.system_setting = SystemSetting()
        self.play_setting = PlaySetting()
        self.skip_direction = True # for test 

        #music all song 
        self.all_songs = AllSongsList(self.system_setting.search_path)

        #load all playlist
        self.all_playlist = []
        self.load_all_playlist("playlist/")

        #self.list_of_playlist.append(PlayList("test_list")) #for test

        #information about the song
        self.play_info = None

    def play_title(self,title:str) -> None :
        """ play the music that the name was given """

        for i in range(len(self.all_songs.music_list)):
            if(title ==  self.all_songs.music_list[i]):
                self.play_info = Music("materials/"+title)
                self.play_index = i 
               
                #for test of skip_song method
                self.play_info.play(self.play_setting)  
                counter = 0
                while(counter < 5):
                    time.sleep(1)
                    counter += 1
                self.play_info.stop()  
 
    def skip_song(self,direction:bool) -> None:
        """ skip to next song or previous song """ 

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
        """ to control volume """ 

        new_volume = self.play_setting.play_volume 

        if(direction): #up
            new_volume += 0.2
            if(new_volume <= 1.0):
                new_volume = round(new_volume,1)
                self.play_setting.change_volume(new_volume) 
            else:
                self.play_setting.change_volume(1.0)
        else: #down
            new_volume -= 0.2
            if(new_volume >= 0.0):
                new_volume = round(new_volume,1)
                self.play_setting.change_volume(new_volume)
            else:
                self.play_setting.change_volume(0.0)

    def change_dir(self,new_path:str) -> None:
        new_dir = input()
        system_setting.change_search_path(new_dir)

    def change_sort_method(self) -> None:
        pass            

    def play_playlist(self, name) -> None:
        '''
        
        # rewrite this part.


        self.list_of_playlist[0].load_playlist("test_list.csv") #for test
        print(self.list_of_playlist[0].music_list)

        for i in range(len(self.list_of_playlist[0].music_list)):
            self.play_title(self.list_of_playlist[0].music_list[i])

        '''
    def main(self) -> None: # main loop
        pass


    def load_all_playlist(self, search_dir) -> list:
        files = os.listdir(search_dir) 

        for i in range(len(files)):
            tmp_line = files[i].split(".")
            if(tmp_line[1] == "csv"):
                self.all_playlist.append(PlayList(tmp_line))
                self.all_playlist[i].load_playlist(files[i])
    

if __name__ == "__main__":

    player = MusicPlayer()
    player.play_playlist(0) 

    '''
    #test for playlist
    player = MusicPlayer()
    player.play_playlist()
    #print(player.all_songs.music_list)
    exit_flag = False
    #for test
    while(True):
        print("1-10 : select songs")
        print(" sn : skip to next")
        print(" sp : skip to previous")
        print(" vu : volume up")
        print(" vd : volume down")
        print("voluem = " + str(player.play_setting.play_volume))
        select = input()
        if(select == "sn"):
            player.skip_song(True) 
        elif(select == "sp"):
            player.skip_song(False) 
        elif(select == "vu"):
            player.volume_control(True)
        elif(select == "vd"):
            player.volume_control(False)
        else:
            number = int(select)
            player.play_title(player.all_songs.music_list[number])
    '''
