import playsound
import pygame
import time 

class Music:
    file_name:str
    artist:str
    playback_time:time
    is_playing:bool

    def __init__(self, name) -> None:
        self.file_name =  name
    
    def play(self) -> (str,int):
        pygame.mixer.music.load("sunrise.mp3")
        pygame.mixer.music.play(1)
        self.is_playing = True    

    def stop(self) -> None:
        pygame.mixer.music.stop()
        self.is_playing = False

if __name__ == "__main__":
    pygame.init()
    tmp_music = Music("materials/sunrise-114326.mp3")
    tmp_music.play()
        
    counter = 0
    while(tmp_music.is_playing):
        time.sleep(1)
        tmp_music.playback_time = pygame.mixer.music.get_pos()
        if(not(pygame.mixer.music.get_busy())):
            tmp_music.stop()

    tmp_music.stop()
    
