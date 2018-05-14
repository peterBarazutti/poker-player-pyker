
class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        allin = game_state["players"]["stack"]
        return allin

    def showdown(self, game_state):
        pass


