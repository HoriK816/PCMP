import py_cui

class EditPlayListScreen:

    def __init__(self, music_player):
        self.player = music_player
        self.screen = py_cui.PyCUI(18,32)
        self.screen.set_title("Edit Playlist")
        self.vol = music_player.play_setting.play_volume
        self.speed = music_player.play_setting.play_speed
        
        # is this necessary ??? 
        #self.mode_list = ["all_song","play_list"] 

        self._create_widgets()

        # load playlists and music
        self._update_all_playlists() 
        self._update_playlist_contents()
        self._update_all_songs_list()
        self._update_selected_music_label()

    def _update_all_playlists(self):
        """ reload all playlist information """

        # clear playlist
        self.player.all_playlist = []
        self.player.load_all_playlist("playlist/")
        self.list_menu.clear()

        # reload all playlist information
        for i in range(len(self.player.all_playlist)):
            self.list_menu.add_item(self.player.all_playlist[i].playlist_name)

    def _update_playlist_contents(self):
        """ show musics of selected playlist """

        self.elements_menu.clear()
    
        # get index
        playlist_index = self.list_menu.get_selected_item_index()

        # update the information about selected playlist on list_menu 
        self.elements_menu.add_item_list(self.player.
                all_playlist[playlist_index].music_list)

        # update the title
        if(self.list_menu.get() != None):
            self.selected_playlist_label.set_title(self.list_menu.get())
            self._update_selected_music_label()

    def _update_selected_music_label(self):
        """ show selected title """

        if(self.elements_menu.get() != None):
            self.selected_music_label_for_elements_menu.set_title(
                    self.elements_menu.get())        

        if(self.all_songs_menu.get() != None):
            self.selected_music_label_for_all_songs_menu.set_title(
                    self.all_songs_menu.get())


    def _update_all_songs_list(self):
        """ reload the list of all music """ 

        self.all_songs_menu.clear()
    
        # initialize music list
        self.all_songs_menu.add_item_list(self.player.all_songs.music_list)

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

    def _create_widgets(self):
        
        # tabs to select play mode
        self.screen.add_button(title="all_song", row=0,
                column=0, column_span=4)
        self.screen.add_button(title="play_list", row=0,
                column=4, column_span=4)

        # the button to exit system
        self.screen.add_button(title="quit", row=0,
                column=8, column_span=2, command=self._exit_system)

        # the button to create new playlist
        self.create_list_button = self.screen.add_button(
                title="Create New PlayList",
                row=2,column=0,row_span=1,column_span=5,
                command=self._create_empty_playlist)

        # the button to delete selected playlist
        self.delete_list_button = self.screen.add_button(
                title="Delete the PlayList",
                row=2,column=5,row_span=1,column_span=5)
        
        # the label to give information about current playlist
        self.selected_playlist_label = self.screen.add_label(
                title="",row=1,column=0,row_span=1,
                column_span=10)

        # the button to delete selected music
        self.delete_music_button = self.screen.add_button(
                title="Delete the music",row=2,column=10,row_span=1,
                column_span=10,command=self._delete_music_from_playlist)
    
        # the label to give information about current music
        self.selected_music_label_for_elements_menu = self.screen.add_label(
                title="",row=1,column=10,row_span=1,
                column_span=10)

        # the list of playlist title 
        self.list_menu = self.screen.add_scroll_menu(title="PlayList",
                row=3,column=0,row_span=13,column_span=10)
        
        self.list_menu.add_key_command(10, self._update_playlist_contents)


        # the list of elements in the playlist
        self.elements_menu = self.screen.add_scroll_menu(title="Elements",
                row=3,column=10,row_span=13,column_span=10)
        self.elements_menu.add_key_command(10, 
                self._update_selected_music_label)


        # the label to give information about current music
        self.selected_music_label_for_all_songs_menu = self.screen.add_label(
                title="",row=1,column=20,row_span=1,
                column_span=10)

        self.add_music_button = self.screen.add_button(
                title="<<- add music",row=2,column=20,row_span=1,
                column_span=10,command=self._add_music_to_playlist)

        # the list of all songs
        self.all_songs_menu = self.screen.add_scroll_menu(title="All Songs",
                row=3,column=20,row_span=13,column_span=10)

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
        self.volume_label.toggle_border()        
        self.selected_playlist_label.toggle_border()
        self.selected_music_label_for_elements_menu.toggle_border()
        self.selected_music_label_for_all_songs_menu.toggle_border()

    def _create_empty_playlist(self):
        #self.player.create_playlist()
        
        self.screen.show_text_box_popup(
                title="input new playlist name",
                command=self._reflect_to_playlist,
                initial_text="") 

    def _reflect_to_playlist(self,text:str):
        #consider the method name !!!!!

        self.player.create_playlist(text)
        self._update_all_playlists()

    def _add_music_to_playlist(self):
        """ add music to playlist from all_songs """
        selected_title = self.all_songs_menu.get()
        selected_list = self.player.all_playlist[
                self.list_menu.get_selected_item_index()]
        selected_list.music_list.append(selected_title)
        self._update_playlist_contents()

    def _delete_music_from_playlist(self):

        selected_title_index = self.elements_menu.get_selected_item_index()
        selected_list = self.player.all_playlist[
                self.list_menu.get_selected_item_index()]

        if (len(selected_list.music_list) != 0):
            del selected_list.music_list[selected_title_index]
            self._update_playlist_contents()


    def _exit_system(self):
        """ exit this music player""" 

        self.player.is_exit = True
        self.screen.stop()


if __name__ == "__main__":
    
    player = MusicPlayer()

    edit_screen = EditPlayListScreen(player)

    edit_screen.screen.start()

