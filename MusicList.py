import random
from Music import Music 
class MusicList:

    music_list:list 

    def __init__(self) -> None:
        self.music_list = []

    def skip_song_to_previous(self, index:int) -> Music:
        if(index != 0):
            ret_music = self.music_list[index-1] 
        else:#last
            ret_music = self.music_list[len(self_music_list)-1]
        return ret_music 

    def skip_song_to_next(self,index:int) -> Music:
        if(index != len(self.music_list)-1):
            ret_music = self.music_list[index+1] 
        else:#head
            ret_music = self.musci_list[0]
        return ret_music 

    def shuffle_select(self) -> Music:
        return random.choice(self.music_list)

if __name__ == "__main__":
    tmp_list = MusicList()
    tmp_list.music_list.append("a")
    tmp_list.music_list.append("b")
    tmp_list.music_list.append("c")
    tmp_list.music_list.append("d")
    print(tmp_list.music_list) # a,b,c,d 
    print(tmp_list.skip_song_to_next(2)) # d
    print(tmp_list.skip_song_to_previous(2)) #b
    print("random")
    for i in range(10): 
        print(str(i+1)+":"+str(tmp_list.shuffle_select()))



