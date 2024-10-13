import main
class Pauser:
    def __init__(self, game_check):
        self.pause(game_check)

    def pause(self, game_check):
        main.game_controller((True, False)[game_check])
