import pygame
import os
import time 
import py_cui
from Music import Music
from PlaySetting import PlaySetting
from MusicList import MusicList
from AllSongsList import AllSongsList 
from SystemSetting import SystemSetting
from PlayList import PlayList
#from MusicPlayer import MusicPlayer

class PlayTitleScreen:
    screen : py_cui 
    mode_list : list
    vol : int 
    speed : int 

    def __init__(self, music_player):
        self.player = music_player
        self.screen = py_cui.PyCUI(18,32)
        self.screen.set_title("Music Player")
        self.vol = music_player.play_setting.play_volume 
        self.speed = music_player.play_setting.play_speed 
        self.mode_list = ["all_song","play_list"]

        #mode select tab
        self.screen.add_button(title="all_song",row=0,column=0,column_span=4)
        self.screen.add_button(title="play_list",row=0,column=4,column_span=4)

        #for test 
        self.screen.add_button(title="update",row=0,column=8,column_span=4,command=self._update_play_info)

        #music list
        self.menu = self.screen.add_scroll_menu(title="All Songs", row=1, column=0, row_span=14, column_span=12) 

        self.menu.add_key_command(97, self._update_play_info) 

        #player
        self.play_title_label = self.screen.add_label(title="title", row=0, column=14, column_span=8)
        self.progress_bar = self.screen.add_slider(title="progress", row=2, column=14, column_span=8, min_val=0, max_val=100)

        self.start_button = self.screen.add_button(title="start", row=4, column=14,column_span=2, command=self._start_music)
        self.stop_button = self.screen.add_button(title="stop", row=4, column=16,column_span=2, command=self._stop_music)
        self.move_previous_button = self.screen.add_button(title="<- 5sec", row=4, column=18,column_span=2)
        self.move_next_button = self.screen.add_button(title="5sec ->", row=4, column=20,column_span=2)
        self.skip_next_button = self.screen.add_button("skip->", row=6, column=20,column_span=2,command=self._skip_to_next)
        self.skip_previous_button = self.screen.add_button("<-skip",row=6, column=14,column_span=2,command=self._skip_to_previous)

        #content
        self.content = self.screen.add_scroll_menu(title="Content", row=8,column=14,row_span=7 ,column_span=8)
    
        #status bar
        self.volume_label = self.screen.add_label(title="vol:"+str(self.vol), row=16, column=0,column_span=4)
        #self.speed_label = self.screen.add_label(title="speed:"+str(self.speed), row=8, column=1, column_span=1)
        #self.shuffle_label = self.screen.add_label(title="shuffle: OFF", row=8, column=2, column_span=1)
      
        #control button
        self.volume_up_button = self.screen.add_button(title="up", row=16,column=4,column_span=2,command=self._volume_up)
        self.volume_up_button = self.screen.add_button(title="down", row=16,column=6,column_span=2,command=self._volume_down) 

        #toggle 
        self.play_title_label.toggle_border()

        #initialize list
        self.menu.add_item_list(self.player.all_songs.music_list)
        self.content.add_item(self.menu.get())
        self._update_play_info()
        self.volume_label.toggle_border()
        #self.speed_label.toggle_border()
        #self.shuffle_label.toggle_border()
        
    def _update_play_info(self):
        self.content.clear() 
        self.content.add_item(self.menu.get())
        self.play_title_label.set_title(self.menu.get())

    def _update_all_song_list(self,list_item:list):
        pass

    def _start_music(self):
        self.player.play_title(self.play_title_label.get_title())

    def _stop_music(self):
        self.player.play_info.stop()

    def _skip_to_next(self):
        self.player.skip_song(True)
        self.menu.set_selected_item_index(self.player.play_index)
        self._update_play_info()

    def _skip_to_previous(self):
        self.player.skip_song(False)
        self.menu.set_selected_item_index(self.player.play_index)
        self._update_play_info()

    def _volume_up(self):
        self.player.volume_control(True)
        self.volume_label.set_title("vol:"+str(self.player.play_setting.play_volume))

    def  _volume_down(self):
        self.player.volume_control(False)
        self.volume_label.set_title("vol:"+str(self.player.play_setting.play_volume))

if __name__ == "__main__":
    #create object
    player = MusicPlayer()
    play_title_screen = PlayTitleScreen(player)

    #start
    play_title_screen.screen.start()


