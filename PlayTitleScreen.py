import py_cui

class PlayTitleScreen:
    screen : py_cui 
    mode_list : list
    vol : int 
    speed : int 

    def __init__(self):
        self.screen = py_cui.PyCUI(10,10)
        self.screen.set_title("Music Player")
        self.vol = 1 # dummy 
        self.speed = 1 # dummy
        self.mode_list = []

        #mode select tab
        self.mode_list = self.screen.add_checkbox_menu(title="", row=0,column=1,column_span=2)
        self.mode_list.add_item_list(["title play", "playlist"]) 

        #music list
        self.menu = self.screen.add_scroll_menu(title="All Songs", row=1, column=0, row_span=6, column_span=4) 
        for i in range(10):
            self.menu.add_item("test"+str(i))
            
        #player
        # need to consider how to implement it.
        

        #content
    
        #status bar
        self.screen.add_label(title="vol:"+str(self.vol), row=8, column=0,column_span=1).toggle_border()
        self.screen.add_label(title="speed:"+str(self.speed), row=8, column=1, column_span=1).toggle_border()
        self.screen.add_label(title="shuffle: OFF", row=8, column=2, column_span=1).toggle_border()

        #self.screen.add
        

        #key guide
        self.screen.add_label(title="Setting: - key, Create PlayList: -key", row=9, column=0, column_span=3).toggle_border()

if __name__ == "__main__":
    play_title_screen = PlayTitleScreen()
    play_title_screen.screen.start()
    play_title_screen.menu.add_item("this item was added out of the class")
    play_title_screen.screen.start()
