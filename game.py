from wall import wall
import random
from bird import bird 
class game():
    def __init__(self,height,width,speed = 10):
        self.height = height
        self.width = width 
        self.speed = speed
        self.map = map_creator(height,width)
        self.birdy = bird(self,1,width/5)#fill this in 
        self.wall_count = 0
        self.score = 0
        self.message = ""
        self.walls = [] 
    def frame(self):
        self.score += 5
        if not self.birdy.move(): return False
        if not self.move_board(): return False
        self.wall_count += 1
        if self.wall_count > 40:
            self.add_wall()
            self.wall_count = 0
        self.message += "Score: {}  Wall_count: {}  jump: {}    fall: {}    keys: {}".format(self.score, self.wall_count,self.birdy.jump,self.birdy.fall,self.birdy.keys)
        return True

    def add_wall(self):
        self.walls.append(wall(self,20))
    def move_board(self):
        if len(self.walls) == 0:
            return True
        else: pass

        for wall in self.walls[1:]:
            if not wall.mover():
                return False
        if self.walls[0].x == 0:
            self.walls[0].remove()
            self.walls.pop(0)
        else: 
            if not self.walls[0].mover():
                return False
        return True
    
def map_creator(height,width):  #returns a matrix Height x Width filled with spaces 
    map = []
    for row in range(height):
        map.append([])
        for col in range(width):
            map[row].append(' ')
    for col in range(width):
        map[0][col] = '-'
        map[height-1][col] = '-'
    return map
