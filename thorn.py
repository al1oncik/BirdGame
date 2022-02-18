import random as r


class Thorn:
    def __init__(self):
        self.pos_down = [
                        [0,600],
                        [50,600],
                        [100,600],
                        [150,600],
                        [200,600],
                        [250,600],
                        [300,600],
                        [350,600],
                        [400,600],
                        [450,600],
                        [500,600]
                        ]
        self.pos_up = [
                        [0,0],
                        [50,0],
                        [100,0],
                        [150,0],
                        [200,0],
                        [250,0],
                        [300,0],
                        [350,0],
                        [400,0],
                        [450,0],
                        [500,0]
                    ]

        self.side_y = [50,100,150,200,250,300,350,400,450,500,550]
        
        self.left_x   = 0
        self.right_x  = 500

        self.y = r.choice(self.side_y)
        
        self.side_y = [50,100,150,200,250,300,350,400,450,500,550]

      
    def rand_y(self):
        self.y = r.choice(self.side_y)
        

    