import pygame
import random
from pygame import mixer
from player import Player
from alien import Alien
from bullet import Bullet


def create_aliens(number_of_aliens, acc = 3):
    aliens_pos = []
    temporary = []
    aliens = []
    if number_of_aliens>16:
        number_of_aliens =16
    while len(aliens_pos)<number_of_aliens:
        temporary.append(random.randint(1,700))
        temporary = set(temporary)
        
        if len(temporary) == number_of_aliens:
            aliens_pos = list(temporary)
            aliens_pos.sort()
        
        temporary = list(temporary)

    for i in range(len(aliens_pos)):
        if i< 4:
            aliens.append(Alien(aliens_pos[i] + 10*i, 50, acc))
        if i>=4 and i<8:
            aliens.append(Alien(aliens_pos[i] + 5*i, 100, acc))
        if i>=8 and i<16:
            aliens.append(Alien(aliens_pos[i] + 2*i, 150, acc))

    return aliens

def show_score(score, font):
    score = font.render("Score: " + str(score), True, (255,255,255))
    return score

def game_over(font):
    over = font.render("GAME OVER", True, (255,255,255))
    return over

def main():

    ############ Initializing the game #################
    pygame.init()
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    running = True
    ############ Title and ICON ################
    ##### Set the Title
    pygame.display.set_caption("Space Invaders")
    ##### Set the Icon
    ## Load the image of the icon
    icon = pygame.image.load("src/space.png")
    ## set the Icon
    pygame.display.set_icon(icon)
    ############ Background #############
    ##### Set the background
    ## Load the image of the background
    background = pygame.image.load("src/background.png")
    ########### Player Creation #############
    ##### Load the image of the player
    player_image = pygame.image.load("src/player.png")
    ##### create an instance of the class player
    player = Player(370, 480)
    ########### Enemy Creation ##############
    ##### Load the image of the alien
    alien_image = pygame.image.load("src/alien.png")
    ##### create an instance of the class alien
    level = 0
    number_of_aliens = 1
    aliens = create_aliens(number_of_aliens)
    ########### Bullet Creation #############
    ##### Load the image of the bullet
    bullet_image = pygame.image.load("src/missile.png")
    ##### create an instance of the class bullet
    bullet = Bullet(player.get_X() + 16, player.get_y() + 10)
    ########## Score display #############
    score_value = 0
    font = pygame.font.Font("freesansbold.ttf", 32)
    #### Game over
    gameOver = False
    ########## Music ############
    mixer.music.load("src/background.wav")
    mixer.music.play(-1)
    explosion = mixer.Sound("src/explosion.wav")

    while running:

        ## Display a black color on the screen
        screen.fill((0,0,0))
        ## Display the background on top of the black color
        screen.blit(background, (0,0))
    
        for event in pygame.event.get():
            ## Quit condition 
            if event.type == pygame.QUIT:
                running = False
            ## Pressing on the keyboard condition
            if event.type == pygame.KEYDOWN:
                ## Conditions for what key is pressed
                if event.key == pygame.K_LEFT:
                    player.set_movement(-5)
                if event.key == pygame.K_RIGHT:
                    player.set_movement(5)
                if event.key == pygame.K_SPACE:
                    bullet.fire(player.get_X(), player.get_y())
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.set_movement(0)
        # Display the player object on the screen
        player.display(player_image, screen)
        #Check if player is at borders
        player.check_border(0, 736)
        # The player movement
        player.move()
        # Display the alien object on the screen
        for alien in aliens:
            alien.display(alien_image, screen)
            # check if the alien is at the borders
            alien.check_border(0, 736)
            # the alien movement
            alien.move()
            if player.is_hit(alien):
                gameOver = True
                explosion.play()
                break
            if bullet.collision(alien):
                number_of_aliens -= 1
                explosion.play()
                alien.is_hit()
                score_value += 1
                if number_of_aliens == 0:
                    level += 1
                    number_of_aliens = level*2 
                    aliens = create_aliens(number_of_aliens, level + 3)
                bullet = Bullet(player.get_X() + 16, player.get_y() + 10)
        # Display the bullet object on the screen
        bullet.display(bullet_image, screen)
        #Check the border of the bullet
        bullet.check_border(player.get_y())
        #move the bullet
        bullet.move()
        #Display the score
        screen.blit(show_score(score_value, font), (10,10))
        ##game over
        if gameOver:
            screen.fill((0,0,0))
            screen.blit(game_over(font), (300,300))
        # update the screen
        pygame.display.update()
    
    
    # closing pygame
    pygame.quit()

if __name__ == "__main__":
    main()