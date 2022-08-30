import playsound
import pygame
import time 

class Music:
    file_name:str
    artist:str
    playback_time:time
    is_playing:bool

    def __init__(self, name):
        self.file_name =  name
    
    def play(self) -> (str,int):
        # refer to PlaySetting class and
        # do settings to play music in this area

        # I don't know how to change the playback speed with pygame ...
        pygame.mixer.init(44100)
        pygame.mixer.music.load("materials/sunrise-114326.mp3")
        pygame.mixer.music.play(1)
        self.is_playing = True    

    def stop(self) -> None:
        pygame.mixer.music.stop()
        self.is_playing = False

if __name__ == "__main__":
    tmp_music = Music("materials/sunrise-114326.mp3")
    tmp_music.play()
        
    counter = 0
    while(tmp_music.is_playing):
        time.sleep(1)
        tmp_music.playback_time = pygame.mixer.music.get_pos()
        if(not(pygame.mixer.music.get_busy())):
            tmp_music.stop()

    tmp_music.stop()
    
