import pygame
import timer


class player:

    def __init__(self):
        self.reset_player()

    def get_pos(self):
        return self.pos
    def get_rotate(self):
        return self.rotate
    def get_hitbox(self):
        return self.hitbox
    def get_health(self):
        return self.health
    def get_sprite(self):
        return self.Player_Sprite

    def reset_player(self):
        self.pos = (500,300)
        self.rotate = 0
        self.hitbox = (True, (10,10))
        self.health = 8
        self.Player_Sprite = pygame.image.load("Sprites/ProjectPSprite.PNG")
        self.Player_Sprite = pygame.transform.scale(self.Player_Sprite, (15,15))
        self.test_timer = timer.timer()
        self.test_timer.set_new_time(360)


    def track_player_buttons(self, keys):
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                if keys[pygame.K_x]:
                    self.update_values(2.5, -2.5, 45)
                elif keys[pygame.K_SPACE]:
                    self.update_values(15, -15, 45)
                else:
                    self.update_values(5, -5, 45)
            elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                if keys[pygame.K_x]:
                    self.update_values(-2.5, -2.5, 315)
                elif keys[pygame.K_SPACE]:
                    self.update_values(-15, -15, 315)
                else:
                    self.update_values(-5, -5, 315)
            else:
                if keys[pygame.K_x]:
                    self.update_values(0, -2.5, 0)
                elif keys[pygame.K_SPACE]:
                    self.update_values(0, -15, 0)
                else:
                    self.update_values(0, -5, 0)
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                if keys[pygame.K_x]:
                    self.update_values(2.5, 2.5, 135)
                elif keys[pygame.K_SPACE]:
                    self.update_values(15, 15, 135)
                else:
                    self.update_values(5, 5, 135)
            elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                if keys[pygame.K_x]:
                    self.update_values(-2.5, 2.5, 225)
                elif keys[pygame.K_SPACE]:
                    self.update_values(-15, 15, 225)
                else:
                    self.update_values(-5, 5, 225)
            else:
                if keys[pygame.K_x]:
                    self.update_values(0, 2.5, 180)
                elif keys[pygame.K_SPACE]:
                    self.update_values(0, 15, 180)
                else:
                    self.update_values(0, 5, 180)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if keys[pygame.K_x]:
                self.update_values(2.5, 0, 90)
            elif keys[pygame.K_SPACE]:
                self.update_values(15, 0, 90)
            else:
                self.update_values(5, 0, 90)
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if keys[pygame.K_x]:
                self.update_values(-2.5, 0, 270)
            elif keys[pygame.K_SPACE]:
                self.update_values(-15, 0, 270)
            else:
                self.update_values(-5, 0, 270)
        else:
            self.update_values(0, 0, 0)



    def update_values(self, x_change, y_change, rotation):
        self.pos = (self.pos[0] + x_change, self.pos[1] + y_change)
        if self.pos[0] < 0:
            self.pos = (0, self.pos[1])
        elif self.pos[0] > 985:
            self.pos = (985, self.pos[1])
        if self.pos[1] < 0:
            self.pos = (self.pos[0], 0)
        elif self.pos[1] > 585:
            self.pos = (self.pos[0], 585)
        self.rotate = rotation

    def collision_check(self, keys):
        if self.hitbox[0] == True:
            if keys[pygame.K_k]:
                if self.health == 8:
                    self.Player_Sprite = pygame.image.load("Sprites/ProjectPSprite1H.PNG")
                    self.Player_Sprite = pygame.transform.scale(self.Player_Sprite, (15, 15))
                    self.health -= 1
                elif self.health == 7:
                    self.Player_Sprite = pygame.image.load("Sprites/ProjectPSprite2H.PNG")
                    self.Player_Sprite = pygame.transform.scale(self.Player_Sprite, (15, 15))
                    self.health -= 1
                elif self.health == 6:
                    self.Player_Sprite = pygame.image.load("Sprites/ProjectPSprite3H.PNG")
                    self.Player_Sprite = pygame.transform.scale(self.Player_Sprite, (15, 15))
                    self.health -= 1
                elif self.health == 5:
                    self.Player_Sprite = pygame.image.load("Sprites/ProjectPSprite4H.PNG")
                    self.Player_Sprite = pygame.transform.scale(self.Player_Sprite, (15, 15))
                    self.health -= 1
                elif self. health == 4:
                    self.Player_Sprite = pygame.image.load("Sprites/ProjectPSprite5H.PNG")
                    self.Player_Sprite = pygame.transform.scale(self.Player_Sprite, (15, 15))
                    self.health -= 1
                elif self.health == 3:
                    self.Player_Sprite = pygame.image.load("Sprites/ProjectPSprite6H.PNG")
                    self.Player_Sprite = pygame.transform.scale(self.Player_Sprite, (15, 15))
                    self.health -= 1
                elif self.health == 2:
                    self.Player_Sprite = pygame.image.load("Sprites/ProjectPSprite7H.PNG")
                    self.Player_Sprite = pygame.transform.scale(self.Player_Sprite, (15, 15))
                    self.health -= 1
                elif self.health == 1:
                    self.reset_player()




    def reduce_timers(self):
        self.test_timer.count_down()
        if self.timer.get_current_time == True:
            print("timer DONE")

