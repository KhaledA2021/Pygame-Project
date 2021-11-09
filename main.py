import pygame
import time

pygame.mixer.init()
WIN = pygame.display.set_mode((1000, 600))
BACKGROUNDCOLOR = [10,0,24]
WIN.fill(BACKGROUNDCOLOR)
pygame.display.set_caption("Free Candy")
FPS = 60

MOOSIC = pygame.mixer.Sound("Creatures-Ov-Deception-_Jsab-Instrumental-Edit_.WAV")
MOOSIC.play(-1)

timer = time.time()

def track_player_buttons(keys, rotation):
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if keys[pygame.K_x]:
                return 2.5, -2.5, 45
            else:
                return 5, -5, 45
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if keys[pygame.K_x]:
                return -2.5, -2.5, 315
            else:
                return -5, -5, 315
        else:
            if keys[pygame.K_x]:
                return 0, -2.5, 0
            else:
                return 0, -5, 0
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if keys[pygame.K_x]:
                return 2.5, 2.5, 135
            else:
                return 5, 5, 135
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if keys[pygame.K_x]:
                return -2.5, 2.5, 225
            else:
                return -5, 5, 225
        else:
            if keys[pygame.K_x]:
                return 0, 2.5, 180
            else:
                return 0, 5, 180
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if keys[pygame.K_x]:
            return 2.5, 0, 90
        else:
            return 5, 0, 90
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        if keys[pygame.K_x]:
            return -2.5, 0, 270
        else:
            return -5, 0, 270
    else:
        return 0, 0, rotation


def move_player(x, y, current_pos):
    current_pos = (current_pos[0] + x, current_pos[1] + y)
    if current_pos[0] < -10:
        current_pos = (-10, current_pos[1])
    if current_pos[0] > 999:
        current_pos = (999, current_pos[1])
    if current_pos[1] < -10:
        current_pos = (current_pos[0], -10)
    if current_pos[1] > 599:
        current_pos = (current_pos[0], 599)
    return current_pos

def redraw_screen(BACKGROUNDCOLOR, Playersprite, Rotation, current_pos, Playerhealth, health_rotate, health_pos):
    WIN.fill(BACKGROUNDCOLOR)
    Playersprite = pygame.transform.rotate(Playersprite, Rotation)
    Playerhealth = pygame.transform.rotate(Playerhealth, health_rotate)
    WIN.blit(Playerhealth, health_pos)
    WIN.blit(Playersprite, current_pos)

def main():
#    background_music = pygame.mixer.music.load("BIG_SHOT.mp3")
    Playersprite = pygame.image.load("ProjectPSprite.PNG")
    Playerhealth = pygame.image.load("ProjectPSpriteHealth.PNG")

    Playersprite = pygame.transform.scale(Playersprite, (15, 15))
    Playerhealth = pygame.transform.scale(Playerhealth, (10, 10))
    current_pos = (400, 300)
    Rotation = 0
    WIN.blit(Playersprite, current_pos)
    WIN.blit(Playerhealth, current_pos)



    running = True
    frames = pygame.time.Clock()

    wait_time = 0
    stop_dash = False

    while running:
        frames.tick(FPS)
        #print(frames, timer)
        print(wait_time)

        x_change = 0
        y_change = 0

        health_pos = (2.5 + x_change / 0.1, 2.5 + y_change / 0.1)
        health_rotate = Rotation

        KEYS = pygame.key.get_pressed()
        x_change , y_change, Rotation = track_player_buttons(KEYS, Rotation)
        if stop_dash:
            if wait_time > 20:
                x_change *= 3
                y_change *= 3

        if KEYS[pygame.K_SPACE]:
            if wait_time < 1:
                #current_pos = (current_pos[0]+(x_change*6), current_pos[1]+(y_change*6))
                wait_time = 40
                stop_dash = True


        current_pos = move_player(x_change, y_change, current_pos)

        if stop_dash:
            if wait_time < 1:
                stop_dash = False
            else:
                wait_time -= 1


        redraw_screen(BACKGROUNDCOLOR, Playersprite, Rotation, current_pos, Playerhealth, health_rotate, health_pos)



        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
        pygame.display.update()

    pygame.QUIT()

if __name__ == "__main__":
      main()