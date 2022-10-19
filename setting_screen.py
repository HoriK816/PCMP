import py_cui

class SettingScreen:

    def __init__(self, music_player):
        self.player = music_player
        self.setting = music_player.system_setting
        self.screen = py_cui.PyCUI(18,32)
        self.screen.set_title("Setting Screen")

        self._create_widgets()
       
        self._update_setting_list()

    def _create_widgets(self):
        
        # tabs to select play mode
        self.screen.add_button(title="all_song", row=0,
                column=0, column_span=4, command=self._change_to_all_song_mode)
        self.screen.add_button(title="play_list", row=0,
                column=4, column_span=4, command=self._change_to_playlist_mode)
        
        # the button for setting mode
        self.screen.add_button(title="setting", row=0, column=8, column_span=2)

        # the button to exit system
        self.screen.add_button(title="quit", row=0,
                column=10, column_span=2, command=self._exit_system)

        # the menu 
        self.menu = self.screen.add_scroll_menu(title="Setting",
                row=1, column=0, column_span=30, row_span=10)

        self.menu.add_key_command(10,command=self._select_popup)

    def _select_popup(self):
        """ show a popup depending on user's choice """

        # Search Path -> 0
        # Search Order -> 1
        selected_item_index = self.menu.get_selected_item_index()

        if selected_item_index == 0: 
            # search path
            self._search_path_popup()

        elif selected_item_index == 1:
            # sort order
            self._sort_order_popup()

    def _search_path_popup(self):
        """ show the popup to change the search path """

        # get current path
        current_path = self.setting.search_path

        # show popup
        self.screen.show_text_box_popup(title="input new search path",
                command=self._reflect_to_search_path,
                initial_text=current_path)

    def _sort_order_popup(self):
        """ show the popup to change the sort order """
        
        # show popup
        self.screen.show_menu_popup(title="Sort Order",
                menu_items=self.setting.sort_order_candidate,
                command=self._reflect_sort_order)

    def _reflect_to_search_path(self,new_path):
        """ reflect new path to system's search path """

        # set new path
        self.setting.search_path = new_path
        # reload
        self._update_setting_list()

    def _reflect_sort_order(self, new_order):
        """ reflect new sort order to system's sort order """

        # set new sort order
        self.setting.sort_order = new_order
        # reload
        self._update_setting_list()
    
    def _update_setting_list(self):
        """ reload setting """

        # clear old screen
        self.menu.clear()

        # reload each items
        setting_title = []
        setting_title.append("Search Path : " + self.setting.search_path)
        setting_title.append("Sort Order : " + self.setting.sort_order)
        self.menu.add_item_list(setting_title)


    def _change_to_all_song_mode(self):
        """ the method which changes to all_song mode """

        # change to all_song mode
        self.player.mode = "all_song"

        # stop this screen
        self.screen.stop()


    def _change_to_playlist_mode(self):
        """ the method which changes to playlist mode """
        
        # change to playlist mode
        self.player.mode = "playlist" 

        # stop this screen
        self.screen.stop()



    def _exit_system(self):
        """ exit this music player """

        self.player.is_exit = True
        self.screen.stop()


if __name__ == "__main__":

    player = MusicPlayer()

    config_screen = SettingScreen(player)

    config_screen.screen.start()

