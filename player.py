class Player:
    VERSION = "1.0"
    IS_TWO_PLAYERS = False

    def betRequest(self, game_state):

        try:
            if not self.IS_TWO_PLAYERS:

                if self.is_allin(game_state) and self.call_all_in(game_state):
                    return self.allIn(game_state)

                elif int(game_state["current_buy_in"]) <= int(game_state["big_blind"]):
                    print game_state["minimum_raise"]
                    return int(game_state["minimum_raise"]) * 4

                elif not self.is_allin(game_state) and (self.isHighCards(game_state)
                                                        or self.isPair(game_state)
                                                        or self.is_suited_connector(game_state)
                                                        or int(game_state["players"][2]["stack"] < 100)):
                    return int(game_state["current_buy_in"])

                else:
                    return 0

            else:
                active_player = self.get_active_opponent(game_state)

                if (int(active_player["id"]) == 3 or int(active_player["id"] == 1) or int(active_player["id"] == 0)) and int(game_state["dealer"]) == 2:
                    return 2 * game_state["minimum_raise"]

                elif int(game_state["current_buy_in"]) <= int(game_state["big_blind"]):
                    print game_state["minimum_raise"]
                    return int(game_state["minimum_raise"]) * 4

                elif not self.is_allin(game_state) and (self.isHighCards(game_state)
                                                        or self.isPair(game_state)
                                                        or self.is_suited_connector(game_state)
                                                        or int(game_state["players"][2]["stack"] < 100)):
                    return int(game_state["current_buy_in"])

                else:
                    return 0
        except:
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
        if self.is_two_players_active(game_state) == 2:
            self.IS_TWO_PLAYERS == True

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

        goodValues = ["8", "9", "T", "J", "Q", "K", "A"]

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
            if current_card[1] == "A" or current_card[2] == "A":
                return True

    def is_allin(self, game_state):
        for player in game_state["players"]:
            if player["stack"] == 0 and player["status"] == "active":
                return True

    def get_active_opponent(self, game_state):
        for player in game_state["players"]:
            if player["status"] == "active" and int(player["id"]) != 2:
                return player

    def call_all_in(self, game_state):
        currentCards = self.get_cards(game_state)
        card1 = currentCards[1]
        card2 = currentCards[2]

        goodValues = ["T", "J", "Q", "K", "A"]
        goodValues_offsuit = ["A", "K", "Q", "J"]

        if currentCards[0] == "S":
            if card1 == "A" or card2 == "A":
                return True
            if card1 in goodValues and card2 in goodValues:
                return True
        else:
            if card1 in goodValues_offsuit and card2 in goodValues_offsuit:
                return True

    def is_two_players_active(self, game_state):
        active_players = []
        for player in game_state["players"]:
            if player["status"] == "active":
                active_players.append(player["id"])
        return len(active_players)

    def isAllIn(self, game_state):
        for player in game_state["players"]:
            if player["bet"] > 500:
                return True

    def test_print(self, game_state):
        print "$$$$$$$$$"
        print game_state["players"][2]
        print "$$$$$$$$$"
