import random
from shape import shape 
class wall(shape):
    def __init__(self,game,break_size):
        break_top = random.randint(game.height/5, game.height-game.height/5 -break_size)
        shapes = [wall_creator(game.height,break_top,break_size)]
        shape.__init__(self,0,game.width-1,shapes,game.map)
    def mover(self):
        self.remove()
        self.x -= 1
        if not self.can_insert():
            return False
        else:
            self.insert()
            return True

        
def wall_creator(height,break_top,break_size,fill = "*"):
    mat = []
    mat.append([' '])
    for row in range(1,break_top):
        mat.append([])
        mat[row].append(fill)
    
    for row in range(break_top,break_top+break_size):
        mat.append([])
        mat[row].append(' ')

    for row in range(break_top+break_size,height-1):
        mat.append([])
        mat[row].append(fill)
    mat.append([' '])
    return mat
