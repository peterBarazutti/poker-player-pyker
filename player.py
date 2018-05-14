class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):

        if self.isHighCards(game_state) or self.isPair(game_state) or self.is_suited_connector(game_state):
            return self.allIn(game_state)
        else:
            return 0
        # if self.isHighCards(game_state) or self.isPair(game_state):
        #     if self.havePair(game_state):
        #         return self.allIn(game_state)
        #     else:
        #         if (game_state["current_buy_in"] > game_state["big_blind"]):
        #             if (game_state["current_buy_in"] / self.allIn(game_state)) * 100 < 15:
        #                 return game_state["current_buy_in"]
        #             else:
        #                 return 0
        #         else:
        #             return game_state["minimum_raise"]
        # else:
        #     return 0

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

    def isPair(self, game_state):
        currentCards = self.get_cards(game_state)
        card1 = currentCards[1]
        card2 = currentCards[2]
        if card1 == card2:
            if int(card1) > 4:
                return True

    def isHighCards(self, game_state):
        currentCards = self.get_cards(game_state)
        card1 = currentCards[1]
        card2 = currentCards[2]

        goodValues = ["T", "J", "Q", "K", "A"]

        if card1 in goodValues and card2 in goodValues:
            return True

    def allIn(self, game_state):
        return int(game_state["players"][2]["stack"])

    def getCardsFromTable(self, game_state):
        listOfCards = []
        for card in game_state["community_cards"]:
            if (card["rank"] == "10"):
                listOfCards.append("T")
            else:
                listOfCards.append(card["rank"])
        return listOfCards

    def havePair(self, game_state):
        currentCards = self.get_cards(game_state)
        card1 = currentCards[1]
        card2 = currentCards[2]

        cardsOnTable = self.getCardsFromTable(game_state)

        return card1 in cardsOnTable or card2 in cardsOnTable

    def is_suited_connector(self, game_state):
        current_card = self.get_cards(game_state)
        if current_card[0] == "S":
            first_card = current_card[1]
            second_card = current_card[2]
            if first_card.isalpha():
                first_card = 10
            else:
                first_card = int(first_card)
            if second_card.isalpha():
                second_card = 10
            else:
                second_card = int(second_card)
            if abs(first_card - second_card) <= 2 and (first_card + second_card) > 10:
                return True


    # def if_small_blind_open(self, game_state):
    #     if game_state["players"][2]
    #     for i in game_state["players"]:
    #         if game_state["players"][i]["bet"] > 0:





    def isAllIn(self, game_state):
        for player in game_state["players"]:
            if player["bet"] > 500:
                return True


    def test_print(self, game_state):
        print "$$$$$$$$$"
        print game_state["players"][2]
        print "$$$$$$$$$"
