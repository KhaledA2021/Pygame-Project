import pygame
import test_player
import timer

pygame.init()
WIN = pygame.display.set_mode((1000, 600))
BACKGROUNDCOLOR = [10,0,24]
WIN.fill(BACKGROUNDCOLOR)
pygame.display.set_caption("Test_Window")
FPS = 60

player = test_player.player()

MOOSIC = pygame.mixer.Sound("Creatures-Ov-Deception-_Jsab-Instrumental-Edit_.WAV")
MOOSIC.play(1)



def main():
    running = True
    frames = pygame.time.Clock()

    #Blit/Print func
    def blit_sprites(sprite, sprite_pos, sprite_rot):
        sprite = pygame.transform.rotate(sprite, sprite_rot)
        WIN.fill(BACKGROUNDCOLOR)
        WIN.blit(sprite, sprite_pos)


    while running:
        frames.tick(FPS)


        #Tracks keys and moves player
        KEYS = pygame.key.get_pressed()
        player.track_player_buttons(KEYS)

        #Uses K key to hurt player (BETA TESING)
        KEYS = pygame.key.get_pressed()
        player.collision_check(KEYS)


        #print(player.get_health())
        if player.is_reset() == True:
            #print("Test")
            player.player_reset = False
            MOOSIC.stop()
            MOOSIC.play(1)



        #try:
        player.reduce_timers()
        #except:
         #   print("timer FAILED")



        # Calls Blit Func to move all objects
        blit_sprites(player.get_sprite(), player.get_pos(), player.get_rotate())

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
        pygame.display.update()
    pygame.QUIT()
if __name__ == "__main__":
      main()