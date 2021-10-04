import pygame

pygame.mixer.init()
WIN = pygame.display.set_mode((800, 600))
BACKGROUNDCOLOR = [0,0,0]
WIN.fill(BACKGROUNDCOLOR)
pygame.display.set_caption("Free Candy")
FPS = 60



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
    return current_pos


def main():
#    background_music = pygame.mixer.music.load("BIG_SHOT.mp3")
    Playersprite = pygame.image.load("Heart_Placeholder.PNG")
    Playersprite = pygame.transform.scale(Playersprite, (20, 20))
    current_pos = (400, 300)
    WIN.blit(Playersprite, current_pos)
#    pygame.mixer.music.play(1)


    running = True
    frames = pygame.time.Clock()


    while running:
        frames.tick(FPS)
        print(frames)

        x_change = 0
        y_change = 0

        KEYS = pygame.key.get_pressed()
        x_change , y_change = track_player_buttons(KEYS)
        current_pos = move_player(x_change, y_change, current_pos)

        WIN.fill(BACKGROUNDCOLOR)
        WIN.blit(Playersprite, current_pos)


        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
        pygame.display.update()

    pygame.QUIT()

if __name__ == "__main__":
      main()