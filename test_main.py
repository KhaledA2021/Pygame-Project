import pygame
import test_player

pygame.init()
WIN = pygame.display.set_mode((1000, 600))
BACKGROUNDCOLOR = [10,0,24]
WIN.fill(BACKGROUNDCOLOR)
pygame.display.set_caption("Test_Window")
FPS = 60

player = test_player.player()


def main():
    running = True
    frames = pygame.time.Clock()

    while running:
        frames.tick(FPS)

        KEYS = pygame.key.get_pressed()
        player.track_player_buttons(KEYS)
        print(player.get_pos())

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
        pygame.display.update()
    pygame.QUIT()
if __name__ == "__main__":
      main()