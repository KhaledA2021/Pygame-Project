'''import pygame
import time
import player

pygame.mixer.init()
WIN = pygame.display.set_mode((1000, 600))
BACKGROUNDCOLOR = [10,0,24]
WIN.fill(BACKGROUNDCOLOR)
pygame.display.set_caption("Free Candy")
FPS = 60

MOOSIC = pygame.mixer.Sound("Creatures-Ov-Deception-_Jsab-Instrumental-Edit_.WAV")
MOOSIC.play(-1)

timer = time.time()


def redraw_screen(BACKGROUNDCOLOR, Playersprite, Rotation, current_pos, Playerhealth, health_rotate, health_pos):
    WIN.fill(BACKGROUNDCOLOR)
    Playersprite = pygame.transform.rotate(Playersprite, Rotation)
    Playerhealth = pygame.transform.rotate(Playerhealth, health_rotate)
    WIN.blit(Playerhealth, health_pos)
    WIN.blit(Playersprite, current_pos)


def main():





    running = True
    frames = pygame.time.Clock()



    while running:
        frames.tick(FPS)
        print(frames, timer)


        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
        pygame.display.update()

    pygame.QUIT()

if __name__ == "__main__":
      main()
'''