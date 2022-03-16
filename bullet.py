import math
from pygame import mixer

class Bullet:
    def __init__(self, x, y):
        self.fired = False
        self.bullet_x = x
        self.bullet_y = y

    def get_x(self):
        return self.bullet_x

    def get_y(self):
        return self.bullet_y

    def move(self):
        if self.fired:
            self.bullet_y -= 10

    def check_border(self, y):
        if self.bullet_y<=0:
            self.fired = False
            self.bullet_y = y + 10

    def fire(self, x, y):
        if self.bullet_y == y + 10:
            self.fired = True
            bullet_sound = mixer.Sound("src/laser.wav")
            bullet_sound.play()
            self.bullet_x = x + 16
            self.bullet_y = y + 10

    def collision(self, alien):
        distance = math.sqrt(math.pow(self.bullet_x - alien.get_x(),2) + math.pow(self.bullet_y - alien.get_y(),2))
        if distance< 35:
            return True
        return False
    
    def display(self, image, screen):
        if self.fired:
            screen.blit(image, (self.bullet_x, self.bullet_y))