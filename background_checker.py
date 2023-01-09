import threading
import time
import pygame

class BackgroundChecker(threading.Thread):

    def __init__(self, music_player, screen,
            playlist_index:int, state:bool):
        super().__init__()
        self.player = music_player
        self.screen = screen
        self.is_active = state
        self.playlist_index = playlist_index

    def change_state(self,state):
        self.is_active = state

    def run(self):
        """ call skip method"""
        while self.is_active:
            if not(pygame.mixer.music.get_busy()):
                self.player.skip_song_on_playlist(True,self.playlist_index)
                self._reflect_skip_to_screen()
            time.sleep(0.1)
    

    def _reflect_skip_to_screen(self):
        """ reflect the result of auto_skip to screen """
        self.screen.content.set_selected_item_index(self.player.
                play_index_on_list)
        self.screen.update_play_info()

