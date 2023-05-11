from find_a_key import board
from keyboard import read_key
import time
from display import display

game=board()
display(game.map)
running=True
a=""
print(game)
while(running):
    a=read_key()
    print(a)
    game.move(a)
    display(game.map)
    game.give_clue()
    time.sleep(0.2)
    if a=='0':
        running=False
