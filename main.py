
class PokerHand: 

    def __init__(self, players, smallBlind, bigBlind):
        self.pot = smallBlind + bigBlind
        self.button = ''
        self.players = players
        self.totalBets = 0

    def printPotValue(self):
        print('pot is ' , self.pot)
        
    def printPlayers(self):
        print('players still playing ' , self.players)

    def printTotalBets(self):
        print('total bets in this hand is ' , self.totalBets)
    
    def bet(self, betValue, player):
        self.pot = self.pot + betValue
        self.totalBets += 1

    def fold(self, player):
        self.players.remove(player)



tt =  PokerHand(['joao', 'pedro', 'marquinhos'], 2, 5)
tt.printPlayers()
tt.fold('pedro')
tt.printPlayers()
tt.bet(5, 'joao')
tt.printTotalBets()