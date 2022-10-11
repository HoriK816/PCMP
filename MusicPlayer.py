import pygame
import os
import sys
import time 
from music import Music
from PlaySetting import PlaySetting
from MusicList import MusicList
from AllSongsList import AllSongsList
from SystemSetting import SystemSetting
from PlayList import PlayList
from PlayTitleScreen import PlayTitleScreen 

class MusicPlayer:

    def __init__(self):

        #setting 
        self.system_setting = SystemSetting()
        self.play_setting = PlaySetting()

        #music all song 
        self.all_songs = AllSongsList(self.system_setting.search_path)

        #load all playlist
        self.all_playlist = []
        self.load_all_playlist("playlist/")

        #information about the song
        self.play_info = None

    def play_title(self,title:str) -> None :
        """ play the music that the name was given """
        # At the first time, player be sure to lead music.
        # if the music had already loaded, player don't load again 
        
        if (self.play_info == None):
            # load music which user selected
            self.play_index, self.play_info = self._get_selected_music(title)

        elif(self.play_info.file_name != ("materials/"+title)): 
            # load music which user selected
            self.play_index, self.play_info = self._get_selected_music(title)
                     
        # play music
        self.play_info.play(self.play_setting)  


    def skip_song(self,direction:bool) -> None:
        """ skip to next song or previous song """ 
    
        # stop current song
        self.play_info.stop()

        # when the direction is true, skip to next song
        if(direction):

            # get the information about next song 
            ret_val = self.all_songs.skip_song_to_next(self.play_index)
            self.play_index = ret_val[0] 
            self.play_info = ret_val[1]

        # when the direction is false, skip to previous song
        else:

            # get the information about previous song
            ret_val = self.all_songs.skip_song_to_previous(self.play_index)
            self.play_index = ret_val[0]
            self.play_info = ret_val[1]

        # start next song
        self.play_title(self.play_info.file_name)

   
    def move_five_seconds(self,direction:bool) -> None:
        """ I was going to use this method to move playing position thought..."""
        if(direction):
            self.play_info.move_five_seconds_to_next()
        else:
            self.play_info.move_five_seconds_to_previous() 

    def volume_control(self,direction:bool) -> None:
        """ change volume """ 
        
        current_volume = self.play_setting.play_volume 

        # when the direction is true, turn the volume up
        if(direction): 
            new_volume = current_volume + 0.2

            if(new_volume <= 1.0): # max is 1.0
                new_volume = round(new_volume,1)
                self.play_setting.change_volume(new_volume) 
            else:
                self.play_setting.change_volume(1.0)

        # when the direction is false, turn the volume down
        else: 
            new_volume = current_volume - 0.2

            if(new_volume >= 0.0): # min is 0.0
                new_volume = round(new_volume,1)
                self.play_setting.change_volume(new_volume)
            else:
                self.play_setting.change_volume(0.0)

    def change_dir(self,new_path:str) -> None:
        """ change the path of music directory """

        new_dir = input()
        system_setting.change_search_path(new_dir)

    def change_sort_method(self) -> None:
        """ change the order of music """
        pass            

    '''
    def play_playlist(self, tmp_playlist_name,index) -> None:
        is this method necessary ??  

        for i in range(len(self.all_playlist)):
            if(tmp_playlist_name == self.all_playlist[i].playlist_name):
                for j in range(len(self.all_playlist[i].music_list)):
                    self.play_title(self.all_playlist[i].music_list[j])

                    
    '''

    def load_all_playlist(self, search_dir) -> list:
        """ load all music from search_dir """

        files = os.listdir(search_dir) 
        for i in range(len(files)):
            tmp_line = files[i].split(".")
            if(tmp_line[1] == "csv"):
                self.all_playlist.append(PlayList(tmp_line[0]))
                self.all_playlist[i].load_playlist(files[i])


    def _get_selected_music(self,title:str) -> (int,Music):
        """ seek the title from list of songs """

        for i in range(len(self.all_songs.music_list)):
            if(title == self.all_songs.music_list[i]):
                return i, Music("materials/"+title)
 
if __name__ == "__main__":
   
    #create object
    player = MusicPlayer()
    play_screen = PlayTitleScreen(player)

    #start
    play_screen.screen.start()


