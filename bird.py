
from shape import shape
#.keys = the list of keys that are being pressed (since the last processed frame)
#.move - moves the birdy safely (and returns True if succeeded)
#.sets the next action for the bird (to jump or to fall, + indicators for how much to jump/fall)
#.gravity makes birdy fall/jump based on .jump and .fall indicators left move move_set
shapes = [
    [
        ['\\','/'],
        ['/','\\']
    ]
]
class bird(shape):
    def __init__(self,game,y,x):
        shape.__init__(self,y,x,shapes,game.map)
        self.keys = []
        self.jump = 0
        self.fall = 0
        self.game = game
    
    def move(self):
        self.remove()
        self.move_set()
        self.gravity()
        if self.can_insert():
            self.insert()
            return True
        else:
            return False
    def move_set(self):
        if 'u' in self.keys:    #setting how much birdy should rise/fall
            self.jump = 10
        if 'd' in self.keys:
            self.jump = 0
        else: pass
        self.keys = []
    def gravity(self):
        if self.jump > 0:
            self.jump_once()
            if self.jump > 5:
                self.jump_once()
        else: 
            self.fall_once()
            if self.fall > 5:
                self.fall_once()
    
    def fall_once(self):        #move the player down once 
        self.fall += 1
        self.y += 1
        """if self.can_insert():
            return True
        else: 
            return False"""
    def jump_once(self):        #move the player up one space 
        self.fall = 0
        self.jump -= 1
        self.y -= 1
        """
        if self.can_insert():
            return True
        else: 
            return False"""
