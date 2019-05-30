import pygame
import random
from classes import sprite
from classes import player
from classes import enemy
import time


pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Top Down Shooter")


############ todos ##################


############  variabele  ##############

speed = 15
thing1 = 0
shooting1 = False
diretion1 = "none"
shootSpeed = 60
diretion2 = "none"
enemyDirition = "none"
enemyMinSpeed = 2
enemyMaxSpeed = 5
score = 0
bulletRadius = 15
lives = 5
resetLazer = False
onScreen1 = True
onScreen2 = False
onScreen3 = False
onScreen4 = False
onScreen5 = False
isStartButtonPressed = False

#################   create sprites   ######################

spritey_da_sprite = sprite("sprite.png", 400, 500)
spritey_da_sprite.resize(90, 85)
lazer1 = sprite("bullet.png", 0, 0)
lazer1.resize(bulletRadius * 2, bulletRadius * 2)
background = sprite("background.png", 0, 0)
background.resize(800, 600)
enemy1 = sprite("EMEMY.png", 400, 300)
enemy1.resize(60, 55)
enemy2 = sprite("EMEMY.png", 400, 300)
enemy2.resize(60, 55)
enemy3 = sprite("EMEMY.png", 400, 300)
enemy3.resize(60, 55)
enemy4 = sprite("EMEMY.png", 400, 300)
enemy4.resize(60, 55)
enemy5 = sprite("EMEMY.png", 400, 300)
enemy5.resize(60, 55)
starButton = sprite("startButton.png", 400, 300)

#########################   start loop   ###############################
'''
while isStartButtonPressed == False:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        break
    if keys[pygame.K_SPACE]:
        isStartButtonPressed = True

    screen.fill((255, 0, 255))
    starButton.blit()
    pygame.display.flip()
'''
#########################   game loop   ################################

while 1:
    pygame.event.get()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_q]:
        break

    spritey_da_sprite.move(speed)

    ##################   shooting   #####################

    if keys[pygame.K_SPACE]:
        shooting1 = True

    if shooting1 == False:
        lazer1.x = spritey_da_sprite.x + 66.5
        lazer1.y = spritey_da_sprite.y + 5

    if shooting1 == True:
        lazer1.y -= shootSpeed

    if lazer1.x > 800 or lazer1.x < 0:
        shooting1 = False

    if lazer1.y > 600 or lazer1.y < 0:
        shooting1 = False

    if resetLazer == True:
        shooting1 = False

    ###################   colider   ###################

    ###################    enemy stuff    ######################

    if onScreen1:
        enemy1.move(enemyMinSpeed, enemyMaxSpeed)
    if enemy1.y > 700 and onScreen1 == True:
        enemy1.y = 0
        enemy1.x = random.randint(100, 700)
        lives -=1
        print("lives:")
        print(lives)

    if onScreen2:
        enemy2.move(enemyMinSpeed, enemyMaxSpeed)
    if enemy2.y > 700 and onScreen2 == True:
        enemy2.y = 0
        enemy2.x = random.randint(100, 700)
        lives -= 1
        print("lives:")
        print(lives)

    if onScreen3:
        enemy3.move(enemyMinSpeed, enemyMaxSpeed)
    if enemy3.y > 700 and onScreen3 == True:
        enemy3.y = 0
        enemy3.x = random.randint(100, 700)
        lives -= 1
        print("lives:")
        print(lives)

    if onScreen4:
        enemy4.move(enemyMinSpeed, enemyMaxSpeed)
    if enemy4.y > 700 and onScreen4 == True:
        enemy4.y = 0
        enemy4.x = random.randint(100, 700)
        lives -= 1
        print("lives:")
        print(lives)

    if onScreen5:
        enemy5.move(enemyMinSpeed, enemyMaxSpeed)
    if enemy5.y > 700 and onScreen5 == True:
        enemy5.y = 0
        enemy5.x = random.randint(100, 700)
        lives -= 1
        print("lives:")
        print(lives)
    ###################   bliting and stuff   ######################

    if spritey_da_sprite.x > 750:
        spritey_da_sprite.x = 750
    elif spritey_da_sprite.x < -50:
        spritey_da_sprite.x = -50
    elif spritey_da_sprite.y > 550:
        spritey_da_sprite.y = 550
    elif spritey_da_sprite.y < -50:
        spritey_da_sprite.y = -50

    if lives < 0:
        print("YOUR FINAL SCORE IS:")
        print(score)
        break

    screen.fill((255, 255, 255))
    background.blit()
    spritey_da_sprite.blit()
    lazer1.blit()

    enemy1.blit()
    enemy1.drawHitBox()
    onScreen1 = True

    if score > 5:
        onScreen2 = True
        enemy2.blit()
        enemy2.drawHitBox()

    if score > 10:
        onScreen3 = True
        enemy3.blit()
        enemy3.drawHitBox()

    if score > 15:
        onScreen4 = True
        enemy4.blit()
        enemy4.drawHitBox()

    if score > 20:
        onScreen5 = True
        enemy5.blit()
        enemy5.drawHitBox()


    pygame.display.flip()

# # # # # # #
#           #
#           #
#           #
#           #
# # # # # # #
