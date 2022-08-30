import pygame
import time 
from PlaySetting import PlaySetting

class Music:
    file_name:str
    artist:str
    playback_time:time
    is_playing:bool

    def __init__(self, name):
        self.file_name =  name
    
    def play(self,play_setting) -> (str,int):
        self.setting = play_setting
        pygame.mixer.init(int(44100*self.setting.play_speed)) #fix it!
        pygame.mixer.music.set_volume(play_setting.play_volume)
        pygame.mixer.music.load(self.file_name)
        pygame.mixer.music.play(1)
        self.is_playing = True    

    def stop(self) -> None:
        pygame.mixer.music.stop()
        self.is_playing = False

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
    
