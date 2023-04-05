from find_a_key import board
from keyboard import read_key
import time

game=board()
a="1"
print(game)
while(a!='0'):
    a=read_key()
    game.move(a)
    game.give_clue()
    time.sleep(0.1)
