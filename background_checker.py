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
                self.screen.update_play_info_from_checker()
                self.player.skip_song_on_playlist(True,self.playlist_index)
    
            #self.screen.update_play_info_from_checker()

            time.sleep(0.1)

