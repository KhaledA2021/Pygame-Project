import pygame

WIN = pygame.display.set_mode((800, 600))
BACKGROUNDCOLOR = [0,0,0]
WIN.fill(BACKGROUNDCOLOR)
pygame.display.set_caption("Free Candy")
FPS = 60

def moveplayer(keys):
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        return 0, 10
    else:
        return 0, 0


def main():
    Playersprite = pygame.image.load("Heart Placeholder.PNG")

    WIN.blit(Playersprite, (800,600))
    running = True
    frames = pygame.time.Clock()


    while running:
        frames.tick(FPS)
        print(frames)

        x_change = 0
        y_change = 0

        WIN.fill(BACKGROUNDCOLOR)
        WIN.blit(Playersprite, (400, 300))

        KEYS = pygame.key.get_pressed()
        x_change , y_change = moveplayer(KEYS)
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
        pygame.display.update()

    pygame.QUIT()

if __name__ == "__main__":
      main()