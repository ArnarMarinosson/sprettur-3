import random
from math import *
import pygame, sys
from pygame.locals import *

pygame.init()
fps = pygame.time.Clock()

# colors
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,205)
BLACK = (0,0,0)

# globals
WIDTH = 1000
HEIGHT = 500
BALL_RADIUS = 20
PLAYER_DIAMETER = 70
PLAYER_RADIUS = PLAYER_DIAMETER // 2
ball_pos = [0,0]
ball_vel = [0,0]
player1_vel = [0,0]
player2_vel = [0,0]
l_score = 0
r_score = 0

# leikskjárinn
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Hello World')

# Upphafstillingar á bolta
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    if right == False:
        ball_pos = [WIDTH // 10 * 4, HEIGHT // 2]
        ball_vel = [-3,10]
    else:
        ball_pos = [WIDTH // 10 * 6, HEIGHT // 2]
        ball_vel = [3,10]

# Upphafstillingar leikmanna
def init():
    global player1_pos, player2_pos, player1_vel, player2_vel,l_score,r_score  # these are floats
    global score1, score2  # these are ints
    player1_pos = [WIDTH//4,HEIGHT]
    player2_pos = [WIDTH - WIDTH//4,HEIGHT]
    l_score = 0
    r_score = 0
    ball_init(True)


# Teiknum umhverfi og skilgreinum eiginleika hluta
def draw(canvas):
    global player1_pos, player2_pos, ball_pos, ball_vel, l_score, r_score

    canvas.fill(BLACK)
    pygame.draw.line(canvas, WHITE, [WIDTH // 2, 0],[WIDTH // 2, HEIGHT], 1)
    pygame.draw.circle(canvas, WHITE, [WIDTH // 2, HEIGHT // 2], 20, 0)

    # Mark 1
    pygame.draw.line(canvas, WHITE, [WIDTH // 8, 300],[WIDTH // 8, HEIGHT], 4)
    pygame.draw.line(canvas, WHITE, [115, 300],[115, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [105, 300],[105, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [95, 300],[95, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [85, 300],[85, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [75, 300],[75, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [65, 300],[65, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [55, 300],[55, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [45, 300],[45, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [35, 300],[35, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [25, 300],[25, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [15, 300],[15, HEIGHT], 1)

    pygame.draw.line(canvas, WHITE, [WIDTH // 8, 300],[0, 300], 4)
    pygame.draw.line(canvas, WHITE, [WIDTH // 8, 310],[0, 310], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH // 8, 320],[0, 320], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH // 8, 330],[0, 330], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH // 8, 340],[0, 340], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH // 8, 350],[0, 350], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH // 8, 360],[0, 360], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH // 8, 370],[0, 370], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH // 8, 380],[0, 380], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH // 8, 390],[0, 390], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH // 8, 400],[0, 400], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH // 8, 410],[0, 410], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH // 8, 420],[0, 420], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH // 8, 430],[0, 430], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH // 8, 440],[0, 440], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH // 8, 450],[0, 450], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH // 8, 460],[0, 460], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH // 8, 470],[0, 470], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH // 8, 480],[0, 480], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH // 8, 490],[0, 490], 1)

    # Mark 2
    pygame.draw.line(canvas, WHITE, [WIDTH * 0.875, 300],[WIDTH *0.875, HEIGHT], 4)
    pygame.draw.line(canvas, WHITE, [WIDTH-115,300],[WIDTH-115, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH-105, 300],[WIDTH-105, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH-95, 300],[WIDTH-95, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH-85, 300],[WIDTH-85, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH-75, 300],[WIDTH-75, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH-65, 300],[WIDTH-65, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH-55, 300],[WIDTH-55, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH-45, 300],[WIDTH-45, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH-35, 300],[WIDTH-35, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH-25, 300],[WIDTH-25, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH-15, 300],[WIDTH-15, HEIGHT], 1)

    pygame.draw.line(canvas, WHITE, [WIDTH *0.875, 300],[1000, 300], 4)
    pygame.draw.line(canvas, WHITE, [WIDTH * 0.875, 310],[WIDTH,310], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH * 0.875, 320],[WIDTH, 320], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH * 0.875, 330],[WIDTH, 330], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH * 0.875, 340],[WIDTH, 340], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH * 0.875, 350],[WIDTH, 350], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH * 0.875, 360],[WIDTH, 360], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH * 0.875, 370],[WIDTH, 370], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH * 0.875, 380],[WIDTH, 380], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH * 0.875, 390],[WIDTH, 390], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH * 0.875, 400],[WIDTH, 400], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH * 0.875, 410],[WIDTH, 410], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH * 0.875, 420],[WIDTH, 420], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH * 0.875, 430],[WIDTH, 430], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH * 0.875, 440],[WIDTH, 440], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH * 0.875, 450],[WIDTH, 450], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH * 0.875, 460],[WIDTH, 460], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH * 0.875, 470],[WIDTH, 470], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH * 0.875, 480],[WIDTH, 480], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH * 0.875, 490],[WIDTH, 490], 1)

    # x-stefnu hreyfingar leikmanna
    if player1_pos[0] > PLAYER_RADIUS and player1_pos[0] < WIDTH - PLAYER_RADIUS:
        player1_pos[0] += player1_vel[0]

    if player2_pos[0] > PLAYER_RADIUS and player2_pos[0] < WIDTH - PLAYER_RADIUS:
        player2_pos[0] += player2_vel[0]

    # leikmenn hoppa
    if player1_pos[1] == HEIGHT:
        player1_pos[1] += player1_vel[1]
    elif player1_pos[1] < HEIGHT:
        player1_pos[1] += 1

    # Hreyfin boltans
    ball_pos[0] += int(ball_vel[0])
    ball_pos[1] += int(ball_vel[1])

    #Teiknum leikmenn og bolta
    pygame.draw.circle(canvas, RED, ball_pos, 20, 0)
    pygame.draw.circle(canvas, BLUE, player1_pos, PLAYER_RADIUS, 0)
    pygame.draw.circle(canvas, GREEN, player2_pos, PLAYER_RADIUS, 0)

    # Árekstur boltans við jaðar skjásins
    if int(ball_pos[1]) <= BALL_RADIUS:
        ball_vel[1] = -0.9*ball_vel[1]
    if int(ball_pos[1]) >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -0.9*ball_vel[1]
    if int(ball_pos[1]) < HEIGHT-BALL_RADIUS:
        ball_vel[1] = (ball_vel[1]+0.4)*0.981
    if int(ball_pos[0]) <= BALL_RADIUS:
        ball_vel[0] *= -0.9
    if int(ball_pos[0]) >= WIDTH - BALL_RADIUS:
        ball_vel[0] *= -0.9

    # Árekstur boltans og leikmanna
    if int(sqrt((ball_pos[0]-player1_pos[0])**2 + (ball_pos[1]-player1_pos[1])**2)) <= BALL_RADIUS+PLAYER_RADIUS:
        ball_vel[0] *= -1.05
        ball_vel[1] *= -1.4
    if sqrt((ball_pos[0]-player2_pos[0])**2 + (ball_pos[1]-player2_pos[1])**2) <= BALL_RADIUS+PLAYER_RADIUS:
        ball_vel[0] *= -1.05
        ball_vel[1] *= -1.4

    # Teiknum score fyrir stöðu leiksins
    myfont1 = pygame.font.SysFont("Comic Sans MS", 20)
    label1 = myfont1.render("Score "+str(l_score), 1, (255,255,0))
    canvas.blit(label1, (50,20))

    myfont2 = pygame.font.SysFont("Comic Sans MS", 20)
    label2 = myfont2.render("Score "+str(r_score), 1, (255,255,0))
    canvas.blit(label2, (880, 20))


# Lyklaborðs eiginleikar ef takka er ýtt niður
def keydown(event):
    global player1_vel, player2_vel

    if event.key == K_LEFT:
        player2_vel[0] += -8
    elif event.key == K_RIGHT:
        player2_vel[0] += 8
    elif event.key == K_UP:
        player2_vel[1] += -100
    elif event.key == K_a:
        player1_vel[0] += -8
    elif event.key == K_d:
        player1_vel[0] += 8
    elif event.key == K_w:
        player1_vel[1] += -100

# Lyklaborðseiginleikar ef takka er sleppt
def keyup(event):
    global player1_vel, player2_vel

    if event.key == K_LEFT:
        player2_vel[0] += 8
    elif event.key == K_RIGHT:
        player2_vel[0] += -8
    elif event.key == K_UP:
        player2_vel[1] += 0
    elif event.key == K_a:
        player1_vel[0] += 8
    elif event.key == K_d:
        player1_vel[0] += -8
    elif event.key == K_w:
        player1_vel[1] += 0

init()

# Keyrsla leiksins
while True:

    draw(window)

    for event in pygame.event.get():

        if event.type == KEYDOWN:
            keydown(event)
        elif event.type == KEYUP:
            keyup(event)
        elif event.type == MOUSEBUTTONUP:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fps.tick(60)
