import py_cui
from music_player import MusicPlayer

class EditPlayListScreen:

    def __init__(self, music_player):
        self.player = music_player
        self.screen = py_cui.PyCUI(18,32)
        self.screen.set_title("Edit Playlist")
    
        self._create_widgets()

    def _create_widgets(self):
        
        # tabs to select play mode
        self.screen.add_button(title="all_song", row=0,
                column=0, column_span=4)
        self.screen.add_button(title="play_list", row=0,
                column=4, column_span=4)

        # the button to exit system
        self.screen.add_button(title="quit", row=0,
                column=8, column_span=2, command=self._exit_system)

    def _exit_system(self):

        self.player.is_exit = True
        self.screen.stop()

if __name__ == "__main__":
    
    player = MusicPlayer()

    edit_screen = EditPlayListScreen(player)

    edit_screen.screen.start()

