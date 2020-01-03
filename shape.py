

#
#"
#.y - location in the y axis of .map
#.x - locaiton in the x axis of .map
#.map - the same map that would be used in the game class 
#.update_specs() after changing the shape_num (to aviod problems with height/width changes)
# '
# '

class shape():
    def __init__(self,y,x,shapes,map,starting_shape = 0):
        self.y = y
        self.x = x
        self.shape_num = starting_shape
        self.shapes = shapes
        self.map = map
        self.update_specs()
        self.insert()
    
    def update_specs(self):#updates the parameters of the shape_num 
        self.height = len(self.shapes[self.shape_num])
        self.width = len(self.shapes[self.shape_num][0])
        #print ("Height: {} Width:{}".format(self.height,self.width))
    
    def can_insert(self):
        for row in range(self.height):
            for col in range(self.width):
                if not self.shapes[self.shape_num][row][col] == ' ' and not self.map[row + self.y][col + self.x] == ' ':
                    return False
        return True
    def insert(self):
        for row in range(self.height):
            for col in range(self.width):
                if not self.shapes[self.shape_num][row][col] == ' ':
                    self.map[row + self.y][col + self.x] = self.shapes[self.shape_num][row][col]
    def remove(self):
        for row in range(self.height):
            for col in range(self.width):
                if not self.shapes[self.shape_num][row][col] == ' ':
                    self.map[row + self.y][col + self.x] = ' '
    
        

    
