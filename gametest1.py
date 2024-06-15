import pygame as pg
import sys


SCREEN_SIZE = (1000, 1000)
SCREEN_COLOR = (255, 255, 255)


pg.init()
screen_surface = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("GameTest1")
CLOCK = pg.time.Clock()

player_x = 0
player_y = 0
player_input = {"left": False, "right": False, "up": False, "down": False}
player_vel = [0,0]
player_speed = 5


def check_input(key, value):
    if event.key == pg.K_LEFT:
        player_input["left"] = value
    elif event.key == pg.K_RIGHT:
        player_input["right"] = value
    elif event.key == pg.K_DOWN:
        player_input["down"] = value
    elif event.key == pg.K_UP:
        player_input["up"] = value


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            check_input(event.key, True)
        elif event.type == pg.KEYUP:
            check_input(event.key, False)

    player_vel[0] = player_input["right"] - player_input["left"]
    player_vel[1] = player_input["down"] - player_input["up"]


    screen_surface.fill(SCREEN_COLOR)
    CLOCK.tick(60)
    # Player is circle
    pg.draw.circle(screen_surface, (0, 0, 200), (player_x,player_y), 100)

    player_x += player_vel[0] * player_speed
    player_y += player_vel[1] * player_speed

    
    rect = pg.draw.rect(screen_surface, [255, 0, 0], [50, 50, 90, 90], 1)
    pg.display.flip()
        
pg.quit()
sys.exit()