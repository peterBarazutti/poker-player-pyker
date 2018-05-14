
class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        print game_state["players"][0]["hole_cards"][0]["rank"]
        print game_state["players"][0]["hole_cards"][1]["rank"]
        print game_state["players"]
        return 1000

    def showdown(self, game_state):
        pass


