import time 
from game import game 
import os 
import threading
from kbr import press

def prs():
    while True:
        time.sleep(0.001)
        game.birdy.keys = press(game.birdy.keys)


def Printer(game):
    text = ""
    text += game.message
    game.message = " "
    for row in range(game.height):
        text += "\n"
        for col in range(game.width):
            text += str(game.map[row][col])
    os.system("clear")
    print (text)
game = game(50,100)
k = threading.Thread(target = prs)
k.start()

while True:
    if not game.frame(): break
    Printer(game)
    time.sleep(0.1)
os.system('clear')
text = str("\n"* (game.height/2) ) + str(' '* ((game.width/2)-5) ) + "Game Over!"
print (text)