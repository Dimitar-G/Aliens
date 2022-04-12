import pygame
import random

# Initialise
pygame.init()

# Set screen
# screen_width = pygame.display.Info().current_w
# screen_height = pygame.display.Info().current_h - 70
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Aliens")
pygame.display.set_icon(pygame.image.load("icon.png"))

# Player
ufoImg = pygame.image.load("ufo.png")
playerImg = pygame.transform.smoothscale(ufoImg, (50, 50))
playerX, playerY = 10, 10
playerChange = 0.5


def player(x, y):
    screen.blit(playerImg, (x, y))


# Goal
earthImg = pygame.image.load("earth.png")
goalImg = pygame.transform.smoothscale(earthImg, (60, 60))
goalX = screen_width - 100
goalY = screen_height - 100


def goal():
    screen.blit(goalImg, (goalX, goalY))


# Stars
starLargeImg = pygame.image.load("star1.png")
starImg = pygame.transform.smoothscale(starLargeImg, (40, 40))
stars = list()
for _ in range(5):
    stars.append((random.randint(50, screen_width - 100), random.randint(50, screen_height - 100)))
taken_stars = 0


def generateStars(remaining_stars):
    for star in remaining_stars:
        screen.blit(starImg, star)


# Evil aliens
evilLargeImg = pygame.image.load("evil.png")
evilImg = pygame.transform.smoothscale(evilLargeImg, (50, 50))
alienSpeed = 0.5
alien1X, alien1Y = 0, 100
alien2X, alien2Y = screen_width, 240
alien3X, alien3Y = 0, 380
alien4X, alien4Y = screen_width, 500


def generateAliens():
    screen.blit(evilImg, (alien1X, alien1Y))
    screen.blit(evilImg, (alien2X, alien2Y))
    screen.blit(evilImg, (alien3X, alien3Y))
    screen.blit(evilImg, (alien4X, alien4Y))


running = True

# Game running loop
while running:

    # screen color
    screen.fill((0, 255, 255))

    # events loop
    for event in pygame.event.get():
        # X button (close game)
        if event.type == pygame.QUIT:
            running = False

    # continuous movement when key is pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        playerY -= playerChange
    if keys[pygame.K_DOWN]:
        playerY += playerChange
    if keys[pygame.K_LEFT]:
        playerX -= playerChange
    if keys[pygame.K_RIGHT]:
        playerX += playerChange

    # check borders
    if playerX <= 0:
        playerX = 0
    if playerY <= 0:
        playerY = 0
    if playerX >= screen_width - 50:
        playerX = screen_width - 50
    if playerY >= screen_height - 50:
        playerY = screen_height - 50

    # checking aliens
    alien1X += alienSpeed
    alien2X -= alienSpeed
    alien3X += alienSpeed
    alien4X -= alienSpeed
    if alien1X > screen_width:
        alien1X = 0
    if alien2X < 0:
        alien2X = screen_width
    if alien3X > screen_width:
        alien3X = 0
    if alien4X < 0:
        alien4X = screen_width

    generateAliens()

    # checking stars
    for s in stars:
        if playerX in range(s[0] - 50, s[0] + 50) and playerY in range(s[1] - 50, s[1] + 50):
            stars.remove(s)
            taken_stars += 1
            print("Points: " + str(taken_stars))

    # rendering player and goal
    goal()
    generateStars(stars)
    player(playerX, playerY)

    # checking goal
    if taken_stars == 5 and playerX in range(goalX - 50, goalX + 50) and playerY in range(goalY - 50, goalY + 50):
        winLargeImg = pygame.image.load("you_win.png")
        winImg = pygame.transform.smoothscale(winLargeImg, (screen_height - 200, screen_height - 200))
        screen.blit(winImg, (200, 100))
        running = False

    if alien1X - 30 <= playerX <= alien1X + 30 and alien1Y - 30 <= playerY <= alien1Y + 30 or alien2X - 30 <= playerX <= alien2X + 30 and alien2Y - 30 <= playerY <= alien2Y + 30 or alien3X - 30 <= playerX <= alien3X + 30 and alien3Y - 30 <= playerY <= alien3Y + 30 or alien4X - 30 <= playerX <= alien4X + 30 and alien4Y - 30 <= playerY <= alien4Y + 30:
        print("You lost..")
        lostLargeImg = pygame.image.load("game-over.png")
        lostImg = pygame.transform.smoothscale(lostLargeImg, (screen_height - 200, screen_height - 200))
        screen.blit(lostImg, (200, 100))
        running = False

    # updating screen
    pygame.display.update()


# Game ended
running = True
while running:
    # events loop
    for event in pygame.event.get():
        # X button (close game)
        if event.type == pygame.QUIT:
            running = False
