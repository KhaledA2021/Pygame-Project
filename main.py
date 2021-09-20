import pygame

WIN = pygame.display.set_mode((800, 600))
COLOR = [0,125,254]
WIN.fill(COLOR)
pygame.display.set_caption("Free Candy")
FPS = 60
x = "www.columbusistasty.com"

def main():
    running = True
    frames = pygame.time.Clock()
    while running:
        frames.tick(FPS)
        COLOR[0] += 1
        COLOR[1] += 1
        COLOR[2] += 1
        if COLOR[0] == 255:
            COLOR[0] = 0
        if COLOR[1] == 255:
            COLOR[1] = 0
        if COLOR[2] == 255:
            COLOR[2] =0
        WIN.fill(COLOR)
        print(frames)
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
        pygame.display.update()

    pygame.QUIT()

if __name__ == "__main__":
      main()