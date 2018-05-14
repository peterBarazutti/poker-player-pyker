
class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        allin1 = game_state["players"]["stack"]
        print(allin1)
        return allin1

    def showdown(self, game_state):
        pass


