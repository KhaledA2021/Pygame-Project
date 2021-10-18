import pygame

pygame.mixer.init()
WIN = pygame.display.set_mode((800, 600))
BACKGROUNDCOLOR = [10,0,24]
WIN.fill(BACKGROUNDCOLOR)
pygame.display.set_caption("Free Candy")
FPS = 60

MOOSIC = pygame.mixer.Sound("Stratales - Spaghetti On The Side.WAV")
MOOSIC.play(-1)

def track_player_buttons(keys):
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if keys[pygame.K_x]:
                return 2.5, -2.5
            else:
                return 5, -5
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if keys[pygame.K_x]:
                return -2.5, -2.5
            else:
                return -5, -5
        else:
            if keys[pygame.K_x]:
                return 0, -2.5
            else:
                return 0, -5
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if keys[pygame.K_x]:
                return 2.5, 2.5
            else:
                return 5, 5
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if keys[pygame.K_x]:
                return -2.5, 2.5
            else:
                return -5, 5
        else:
            if keys[pygame.K_x]:
                return 0, 2.5
            else:
                return 0, 5
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if keys[pygame.K_x]:
            return 2.5, 0
        else:
            return 5, 0
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        if keys[pygame.K_x]:
            return -2.5, 0
        else:
            return -5, 0
    else:
        return 0, 0


def move_player(x, y, current_pos):
    current_pos = (current_pos[0] + x, current_pos[1] + y)
    if current_pos[0] < -20:
        current_pos = (-20, current_pos[1])
    if current_pos[0] > 800:
        current_pos = (800, current_pos[1])
    if current_pos[1] < -20:
        current_pos = (current_pos[0], -20)
    if current_pos[1] > 600:
        current_pos = (current_pos[0], 600)
    return current_pos



def main():
#    background_music = pygame.mixer.music.load("BIG_SHOT.mp3")
    Playersprite = pygame.image.load("ProjectPSprite.PNG")
    Playersprite = pygame.transform.scale(Playersprite, (10, 10))
    current_pos = (400, 300)
    Rotation = 0
    WIN.blit(Playersprite, current_pos)



    running = True
    frames = pygame.time.Clock()

    wait_time = 0
    while running:
        frames.tick(FPS)
        print(frames)

        x_change = 0
        y_change = 0

        KEYS = pygame.key.get_pressed()
        x_change , y_change = track_player_buttons(KEYS)
        if KEYS[pygame.K_SPACE]:
            if wait_time == 0:
                x_change = x_change * 2
                y_change = y_change * 2
                wait_time = 30

        current_pos = move_player(x_change, y_change, current_pos)

        if wait_time > 0:
            wait_time =- 1


        WIN.fill(BACKGROUNDCOLOR)
        Playersprite = pygame.transform.rotate(Playersprite, Rotation)
        WIN.blit(Playersprite, current_pos)



        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
        pygame.display.update()

    pygame.QUIT()

if __name__ == "__main__":
      main()