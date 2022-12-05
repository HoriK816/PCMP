import music
from music_list import MusicList

class PlayList(MusicList):
    
    playlist_name : str 

    def __init__(self, name:str):
        super().__init__()
        self.playlist_name = name
         
    def load_playlist(self,file_name:str):
        # add musics to this playlist 

        with open("playlist/"+file_name,"r") as f:
            for line in f:
                self.music_list.append(line.split(",")[0])

    def edit_playList(self, name:str, ope:str, title:str) -> None:
        pass

if __name__ == "__main__":
    tmp_playlist = PlayList("test_list") 
    tmp_playlist.load_playlist("test_list.csv")
