import py_cui

class PlayTitleScreen:
    screen : py_cui 
    mode_list : list
    vol : int 
    speed : int 

    def __init__(self):
        self.screen = py_cui.PyCUI(10,8)
        self.screen.set_title("Music Player")
        self.vol = 1 # dummy 
        self.speed = 1 # dummy
        self.mode_list = []

        #mode select tab
        self.mode_list = self.screen.add_label(title="Mode Select", row=0, column=0, column_span=2).toggle_border() 

        #music list
        self.menu = self.screen.add_scroll_menu(title="All Songs", row=1, column=0, row_span=7, column_span=4) 

        #player
        self.play_titlie_label  = self.screen.add_label(title="title", row=0, column=4, column_span=4).toggle_border()
        self.progress_bar = self.screen.add_slider(title="progress", row=1, column=4, column_span=4, min_val=0, max_val=100)

        # need to consider how to implement it.
        self.start_button = self.screen.add_button(title="start", row=2, column=5)
        self.stop_button = self.screen.add_button(title="stop", row=2, column=6)
        self.move_previous_button = self.screen.add_button(title="<- 5sec", row=2, column=4)
        self.move_next_button = self.screen.add_button(title="5sec ->", row=2, column=7)
        self.skip_next_button = self.screen.add_button(" skip ->>", row=3, column=7)
        self.skip_previous_button = self.screen.add_button("<<- skip",row=3, column=4)

        #content
        self.menu = self.screen.add_scroll_menu(title="Content", row=4,column=4,row_span=4 ,column_span=4)
    
        #status bar
        self.screen.add_label(title="vol:"+str(self.vol), row=8, column=0,column_span=1).toggle_border()
        self.screen.add_label(title="speed:"+str(self.speed), row=8, column=1, column_span=1).toggle_border()
        self.screen.add_label(title="shuffle: OFF", row=8, column=2, column_span=1).toggle_border()
        
        #key guide
        self.screen.add_label(title="Switch Mode: - key", row=0, column=2, column_span=2)
        self.screen.add_label(title="Setting: - key, Create PlayList: -key", row=9, column=0, column_span=3).toggle_border()

    def _update_play_info(self,title:str,time):
        pass

    def _update_all_song_list(self,list_item:list):
        pass


if __name__ == "__main__":
    play_title_screen = PlayTitleScreen()
    play_title_screen.screen.start()
    play_title_screen.menu.add_item("this item was added out of the class")
    play_title_screen.screen.start()
