class Alien:
    def __init__(self,x , y, a=3):
        self.alien_x = x
        self.alien_y = y
        self.movement = a
        self.ishit = False

    def get_x(self):
        return self.alien_x

    def get_y(self):
        return self.alien_y

    def move(self):
        self.alien_x += self.movement

    def is_hit(self):
        self.ishit = True
        self.alien_x = 10000
        self.alien_y = 10000
        self.movement = 0

    def check_border(self, border_left, border_right):
        if self.alien_x <= border_left:
            self.movement *= -1
            self.alien_y += 50
        if self.alien_x >= border_right:
            self.movement *= -1
            self.alien_y += 50
            
    def display(self, image, screen):
        if not (self.ishit):
            screen.blit(image, (self.alien_x, self.alien_y))