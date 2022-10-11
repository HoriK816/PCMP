import pygame
import os
import time 
import py_cui
from music import Music
from PlaySetting import PlaySetting
from MusicList import MusicList
from AllSongsList import AllSongsList 
from SystemSetting import SystemSetting
from PlayList import PlayList
from MusicPlayer import MusicPlayer


class PlayListScreen:

    def __init__(self, music_player):
        self.player = music_player
        self.screen = py_cui.PyCUI(18,32)
        self.screen.set_title("Music Player")
        self.vol = music_player.play_setting.play_volume 
        self.speed = music_player.play_setting.play_speed 
        self.mode_list = ["all_song","play_list"]
        #is the attribute necessary ???  
        self.music_index = 0

        self._create_widges()

        #load playlists and music
        self._update_all_song_list()
        self.content.add_item(self.menu.get())
        self._update_play_info()
        self.volume_label.toggle_border()
        
    def _update_play_info(self):
        """ show music of selected playlist """
        
        self.content.clear() 

        # get index
        playlist_index = self.menu.get_selected_item_index() 

        # update the information about selected playlist on the content menu 
        self.content.add_item_list(self.player.
                all_playlist[playlist_index].music_list)
    
        # update the title 
        if(self.content.get() != None):
            self.play_title_label.set_title(self.content.get())

    def _update_all_song_list(self):
        """ reload all playlist information """ 
        
        # clear playlist
        self.player.all_playlist = []
        player.load_all_playlist("playlist/")
        self.menu.clear()

        # reload all playlist information
        for i in range(len(self.player.all_playlist)):
            self.menu.add_item(self.player.all_playlist[i].playlist_name)



    def _start_music(self):
        """ start music """
        self.player.play_playlist(self.menu.get(), self.music_index)

    def _stop_music(self):
        """ stop music """ 
        self.player.play_info.stop()

    def _skip_to_next(self):
        """ skip to next song in current playlist """
        #get index of the selected playlist
        selected_list_index = self.menu.get_selected_item_index()
        selected_music_index = self.content.get_selected_item_index()
        #play next song
        self.player.skip_song_on_playlist(True, selected_list_index, 
                selected_music_index)

    def _skip_to_previous(self):
        """ skip to previous song in current playlist """ 
        #get index of the selected playlist and the selected music
        selected_list_index = self.menu.get_selected_item_index()
        selected_music_index = self.content.get_selected_item_index()
        # play previous song
        self.player.skip_song_on_playlist(False, selected_list_index,
                selected_music_index)

    def _volume_up(self):
        """ turn the volume up """
        self.player.volume_control(True)
        self.volume_label.set_title("vol:"+str(self.player
            .play_setting.play_volume))

    def  _volume_down(self):
        """ turn the volume down """
        self.player.volume_control(False)
        self.volume_label.set_title("vol:"+str(self.player
            .play_setting.play_volume))

    def _create_widges(self):

        # tabs to select play mode
        self.screen.add_button(title="all_song", row=0,
                column=0, column_span=4)
        self.screen.add_button(title="play_list", row=0, 
                column=4, column_span=4)

        # the list of created playlist
        self.menu = self.screen.add_scroll_menu(title="PlayList", 
                row=1, column=0, row_span=14, column_span=12) 

        self.menu.add_key_command(97, self._update_play_info) 

        # the label to give information about current playlist
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
            row=4, column=20,column_span=2)
        '''
        
        # the button to skip to next song
        self.skip_next_button = self.screen.add_button("skip->", row=6,
                column=20,column_span=2,command=self._skip_to_next)
        
        # the button to skip to previous song
        self.skip_previous_button = self.screen.add_button("<-skip",row=6,
                column=14,column_span=2,command=self._skip_to_previous)

        # the list of music included in current playlist 
        self.content = self.screen.add_scroll_menu(title="Content", row=8,
                column=14, row_span=7 ,column_span=8)
    
        # the label to give information about current volume 
        self.volume_label = self.screen.add_label(title="vol:"+str(self.vol),
                row=16, column=0, column_span=4)

        # the button to turn the volume up
        self.volume_up_button = self.screen.add_button(title="up", row=16,
                column=4, column_span=2, command=self._volume_up)

        # the button to turn the volume down
        self.volume_up_button = self.screen.add_button(title="down", row=16,
                column=6, column_span=2, command=self._volume_down) 

        # draw border line 
        self.play_title_label.toggle_border()

if __name__ == "__main__":
    #create object
    player = MusicPlayer()
    play_list_screen = PlayListScreen(player)

    #start
    play_list_screen.screen.start()


