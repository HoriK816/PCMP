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

    def rewrite_playlist_file(self):
        """ reflect elements of the playlist to the source file """

        rewrite_value = []

        for i in range(len(self.music_list)):
            rewrite_value.append(self.music_list[i] + ",\n")

        with open("playlist/"+file_name,"w") as f:
            f.writelines(rewrite_value)


if __name__ == "__main__":
    tmp_playlist = PlayList("test_list") 
    tmp_playlist.load_playlist("test_list.csv")
