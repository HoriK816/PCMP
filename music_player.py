import pygame
import os
import sys
import time 
from music import Music
from play_setting import PlaySetting
from music_list import MusicList
from all_songs_list import AllSongsList
from system_setting import SystemSetting
from playlist import PlayList
from play_title_screen import PlayTitleScreen 
from playlist_screen import PlayListScreen
from setting_screen import SettingScreen

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
        self.play_index = 0

        self.is_exit = False

        self.mode_list = ["all_song","play_list","setting"]
        self.mode = "all_song" 

    def main(self):
        #create object
        player = MusicPlayer()

        while True:
            if player.is_exit:
                sys.exit()
            else:
                # set play_screen to match play mode
                if player.mode == "all_song": 
                    play_screen = PlayTitleScreen(player)
                elif player.mode == "playlist":
                    play_screen = PlayListScreen(player)
                elif player.mode ==  "setting":
                    play_screen = SettingScreen(player)
                
                # start
                play_screen.screen.start()


    def play_title(self,title:str) -> None :
        """ play the music that the name was given """

        # At the first time, player be sure to load music.
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
        is_busy = pygame.mixer.get_busy() 
        if is_busy:
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

    def skip_song_on_playlist(self,direction:bool,playlist_index:int) -> None:
        """ skip to next song or previous song on playlist """

        # stop current song
        is_busy = pygame.mixer.get_busy()
        if is_busy:
            self.play_info.stop()

        # get the target playlist
        target_list = self.all_playlist[playlist_index]

        # when the direction is true, skip to next song
        if(direction):

            # get the information about next song
            ret_val = target_list.skip_song_to_next(self.play_index_on_list)
            self.play_index_on_list = ret_val[0]
            self.play_info = ret_val[1]

            print(ret_val[0])
            print(ret_val[1].file_name)
            
        else:

            # get the information about previous song
            ret_val = target_list.skip_song_to_previous(self.play_index_on_list)
            self.play_index_on_list = ret_val[0]
            self.play_info = ret_val[1]
        
        self.play_title(self.play_info.file_name)

   
    def move_five_seconds(self,direction:bool) -> None:
        """ I was going to use this method to move playing position thought..."""

        if(direction):
            self.play_info.move_five_seconds_to_next()
        else:
            self.play_info.move_five_seconds_to_previous() 


    def _get_selected_music(self,title:str) -> (int,Music):
        """ seek the title from list of songs """

        for i in range(len(self.all_songs.music_list)):
            if(title == self.all_songs.music_list[i]):
                return i, Music("materials/"+title)
 
    def change_dir(self,new_path:str) -> None:
        """ change the path of music directory """

        new_dir = input()
        system_setting.change_search_path(new_dir)

    def change_sort_method(self) -> None:
        """ change the order of music """
        pass            

    def volume_control(self,direction:bool) -> None:
        """ change volume """ 

        is_stop = False
       
        if (self.play_info is not None):
            self.play_info.stop()
            is_stop = True

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

            if(new_volume > 0.0): # min is 0.0
                new_volume = round(new_volume,1)
                self.play_setting.change_volume(new_volume)
            else:
                self.play_setting.change_volume(0.0)

        if is_stop: 
            self.play_info.play(self.play_setting)

    def load_all_playlist(self, search_dir) -> None:
        """ load all music from search_dir """

        files = os.listdir(search_dir) 
        for i in range(len(files)):
            tmp_line = files[i].split(".")
            if(tmp_line[1] == "csv"):
                self.all_playlist.append(PlayList(tmp_line[0]))
                self.all_playlist[i].load_playlist(files[i])

    def create_playlist(self, playlist_name:str) -> None:
        """ create an empty playlist"""
        
        # create new playlist
        new_playlist = PlayList(playlist_name)
        # add it to the list of all playlist
        self.all_playlist.append(new_playlist)
        # create new file to handle the playlist 
        with open("./playlist/"+new_playlist.playlist_name+".csv","w") as f:
            f.write("")

    def delete_playlist(self, playlist_name:str) -> None:
        """ delete selected playlist"""
        pass 

if __name__ == "__main__":
    music_player = MusicPlayer()
    music_player.main()


