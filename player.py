
class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        print game_state["players"][0]["hole_cards"][0]["rank"]
        print game_state["players"][0]["hole_cards"][1]["rank"]
        print game_state["players"]
        return 1000

    def showdown(self, game_state):
        pass

    def get_cards(self, game_state):
        returning_string = ""
        card1_suit = game_state["players"][2]["hole_cards"][0]["suit"]
        card2_suit = game_state["players"][2]["hole_cards"][1]["suit"]
        card1_rank = game_state["players"][2]["hole_cards"][0]["rank"]
        card2_rank = game_state["players"][2]["hole_cards"][1]["rank"]
        if card1_rank == "10":
            card1_rank = "T"
        if card2_rank == "10":
            card2_rank = "T"
        if card1_suit == card2_suit:
            returning_string = "S"
        else:
            returning_string = "O"
        returning_string = returning_string + card1_rank + card2_rank
        return returning_string

