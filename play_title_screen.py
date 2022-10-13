import pygame
import os
import time 
import py_cui
from music import Music
from play_setting import PlaySetting
from music_list import MusicList
from all_songs_list import AllSongsList 
from system_setting import SystemSetting
from playlist import PlayList

class PlayTitleScreen:

    def __init__(self, music_player):
        self.player = music_player
        self.screen = py_cui.PyCUI(18,32)
        self.screen.set_title("Music Player")
        self.vol = music_player.play_setting.play_volume 
        self.speed = music_player.play_setting.play_speed 
        self.mode_list = ["all_song","play_list"]
        
        self._create_widges()
    
        # update music list
        self._update_all_song_list()
       
        # load the name of selected music
        self._update_play_info()


    def _create_widges(self):

        # tabs to select play mode
        self.screen.add_button(title="all_song",row=0,
                column=0,column_span=4)
        self.screen.add_button(title="play_list",row=0,
                column=4,column_span=4)

        # all music list
        self.menu = self.screen.add_scroll_menu(title="All Songs",
                row=1, column=0, row_span=14, column_span=12) 

        self.menu.add_key_command(97, self._update_play_info) 

        # the label to give information about current song
        self.play_title_label = self.screen.add_label(title="title",
                row=0, column=14, column_span=8)
        self.progress_bar = self.screen.add_slider(title="progress",
                row=2, column=14, column_span=8, min_val=0, max_val=100)

        # the button to make current music started
        self.start_button = self.screen.add_button(title="start",
                row=4, column=16,column_span=2, command=self._start_music)

        # the button to make current music stopped
        self.stop_button = self.screen.add_button(title="stop",
                row=4, column=18,column_span=2, command=self._stop_music)
        
        '''
        unimplemented

        self.move_previous_button = self.screen.add_button(title="<- 5sec",
                row=4, column=14,column_span=2)

        self.move_next_button = self.screen.add_button(title="5sec ->",
                row=4, column=20,column_span=2, command=self._move_to_next_five_sec)
       
        '''
        # the button to skip to next song 
        self.skip_next_button = self.screen.add_button("skip->", row=4,
                column=20,column_span=2,command=self._skip_to_next)

        # the button to skip to previous song
        self.skip_previous_button = self.screen.add_button("<-skip",row=4,
                column=14,column_span=2,command=self._skip_to_previous)

        # the label to give information about current volume
        self.volume_label = self.screen.add_label(title="vol:"+str(self.vol),
                row=16, column=0,column_span=4)

        # the button to turn the volume up
        self.volume_up_button = self.screen.add_button(title="up", row=16,
                column=4,column_span=2,command=self._volume_up)

        # the button to turn the volume down
        self.volume_up_button = self.screen.add_button(title="down", row=16,
                column=6,column_span=2,command=self._volume_down) 

        # draw border line
        self.play_title_label.toggle_border()
        self.volume_label.toggle_border()

    def _update_play_info(self):
        """ reflect the title of selected song to the title bar """
        if(self.menu.get() != None):
            self.play_title_label.set_title(self.menu.get())

    def _update_all_song_list(self):
        """ reload music directory """
        
        self.menu.clear()

        #initialize music list
        self.menu.add_item_list(self.player.all_songs.music_list)


    def _start_music(self):
        """ start current music """ 
        self.player.play_title(self.play_title_label.get_title())

    def _stop_music(self):
        """ stop current music """ 
        self.player.play_info.stop()

    def _skip_to_next(self):
        """ skip to next song in all music list"""
        self.player.skip_song(True)
        self.menu.set_selected_item_index(self.player.play_index)
        self._update_play_info()

    def _skip_to_previous(self):
        """ skip to previous song in all music list """
        self.player.skip_song(False)
        self.menu.set_selected_item_index(self.player.play_index)
        self._update_play_info()

    '''
    maybe, I won't use these methods forever ...

    def _move_to_next_five_sec(self):
        self.player.move_five_seconds(True)

    def _move_to_previous_five_sec(self):
        self.player.move_five_seconds(False)

    '''

    def _volume_up(self):
        """ turn the volume up"""
        self.player.volume_control(True)
        self.volume_label.set_title("vol:"+str(self.player.play_setting
            .play_volume))

    def  _volume_down(self):
        """ turn the volume down """
        self.player.volume_control(False)
        self.volume_label.set_title("vol:"+str(self.player.play_setting
            .play_volume))

if __name__ == "__main__":

    #create object
    player = MusicPlayer()
    play_title_screen = PlayTitleScreen(player)

    #start
    play_title_screen.screen.start()


