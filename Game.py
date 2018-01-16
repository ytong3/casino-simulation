from Outcome import Outcome
from Bin import Bin
'''
Responsibilities:
1. get bets from Playe
2. spin the Wheel
3. collects losing bets
4. pays winning bets.
'''

class Game:
    def __inti__(self):
        five = Outcome("00-0-1-2-3", 6)
        zero = Bin([Outcome("0",35), five])
