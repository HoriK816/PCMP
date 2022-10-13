class PlaySetting:
    play_speed : float
    play_volume : float

    def __init__(self):
        self.play_speed = 1.0
        self.play_volume = 1.0

    def change_speed(self, speed:float) -> None:
        self.play_speed = speed

    def change_volume(self, volume:float) -> None:
        self.play_volume = volume        

if __name__ == "__main__":
    play_setting = PlaySetting()
    print(play_setting.play_speed)
    print(play_setting.play_volume)
