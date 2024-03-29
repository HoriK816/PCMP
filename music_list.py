import random
from music import Music 
class MusicList:

    music_list:list 

    def __init__(self) -> None:
        self.music_list = []

    def skip_song_to_previous(self, index:int) -> (int,Music):
        new_index = index

        if(index != 0):
            ret_music_name = self.music_list[index-1] 
            new_index -= 1
        else:#to last
            ret_music_name = self.music_list[len(self.music_list)-1]
            new_index = len(self.music_list)-1
        return new_index, Music(ret_music_name) 

    def skip_song_to_next(self,index:int) -> (int,Music):
        new_index = index 

        if(index != len(self.music_list)-1):
            ret_music_name = self.music_list[index+1] 
            new_index += 1
        else:#head
            ret_music_name = self.music_list[0]
            new_index = 0
        return new_index, Music(ret_music_name) 

    def shuffle_select(self) -> Music:
        ret_music_name = random.choice(self.music_list)
        return Music(ret_music_name)

if __name__ == "__main__":
    tmp_list = MusicList()
    tmp_list.music_list.append("a")
    tmp_list.music_list.append("b")
    tmp_list.music_list.append("c")
    tmp_list.music_list.append("d")
    print(tmp_list.music_list) # a,b,c,d 
    print(tmp_list.skip_song_to_next(2).file_name) # d
    print(tmp_list.skip_song_to_previous(2).file_name) #b
    print("random")
    for i in range(10): 
        print(str(i+1)+":"+str(tmp_list.shuffle_select().file_name))



