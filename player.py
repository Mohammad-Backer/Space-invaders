import math

class Player:

    def __init__(self, x, y):
        self.player_x = x
        self.player_y = y
        self.movement = 0

    def get_X(self):
        return self.player_x

    def get_y(self):
        return self.player_y

    def set_movement(self, move):
        self.movement = move

    def move(self):
        self.player_x += self.movement

    def check_border(self, border_left, border_right):
        if self.player_x <= border_left:
            self.movement = 0
            self.player_x = border_left + 1
        if self.player_x >= border_right:
            self.movement = 0
            self.player_x = border_right - 1

    def is_hit(self, alien):
        distance = math.sqrt(math.pow(self.player_x - alien.get_x(),2) + math.pow(self.player_y - alien.get_y(),2))
        if distance< 35:
            return True
        return False
            

    def display(self, image, screen):
        screen.blit(image, (self.player_x, self.player_y))