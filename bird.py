class Bird:
    def __init__(self):
        self.x      = 275
        self.y      = 350
        self.width  = 50
        self.height = 50
        
        self.moving = {
            "left":True,
            "right":False,
            "down":True
            }
        
        self.jump       = False
        self.speed      = 7
        self.force_up   = 45
        self.force_down = 3
        self.image      = None
        


    