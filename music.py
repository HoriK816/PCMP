import pygame
import time 
from play_setting import PlaySetting

class Music:

    def __init__(self, name):
        self.file_name =  name
        self.is_paused = False

    def play(self,play_setting) -> (str,int):
        """ play the music """

        if not self.is_paused:
            # the current music is paused
            self.setting = play_setting
            pygame.mixer.init(44100)
            pygame.mixer.music.set_volume(play_setting.play_volume)
            pygame.mixer.music.load(self.file_name)
            pygame.mixer.music.play(loops=1)
        else:
            # the current music is not paused
            pygame.mixer.music.set_volume(play_setting.play_volume)
            self._unpause()

    def stop(self) -> None:
        """ stop(pause) current music """ 
        pygame.mixer.music.pause()
        self.is_paused = True

    # you should not to use this method , 'cause the start positions of  
    # pygame.mixer.music.play() is not precise
    def move_five_seconds_to_next(self):
        tmp_time = (pygame.mixer.music.get_pos()//1000)+5
        self.stop()
        pygame.mixer.music.play(1,start=tmp_time)

    # you should not to use this method, 'cause the start position of
    # pygame.mixer.music.play() is not precise
    def move_five_seconds_to_previous(self):
        tmp_time = (pygame.mixer.music.get_pos()//1000)-5
        self.stop()
        pygame.mixer.music.play(1,start=tmp-time)

    def _unpause(self) -> None:
        """ unpause current music """ 
        pygame.mixer.music.unpause()
        self.is_puased = False
    

if __name__ == "__main__":
    tmp_setting = PlaySetting()
    tmp_music = Music("materials/music_for_programming_3-datassette.mp3")
    tmp_music.play(tmp_setting)
    while(tmp_music.is_playing):
        time.sleep(1)
        tmp_music.playback_time = pygame.mixer.music.get_pos()
        if(not(pygame.mixer.music.get_busy())):
            tmp_music.stop()
    tmp_music.stop()
    
