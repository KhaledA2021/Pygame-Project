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
    def is_reset(self):
        return self.player_reset

    def reset_player(self):
        self.player_reset = True
        self.pos = (500,300)
        self.rotate = 0
        self.hitbox = (True, (10,10))
        self.health = 8
        self.Player_Sprite = pygame.image.load("Sprites/ProjectPSprite.PNG")
        self.Player_Sprite = pygame.transform.scale(self.Player_Sprite, (15, 15))
        self.health_cooldown_timer = timer.timer()
        self.dash_cooldown_timer = timer.timer()
        self.dash_length_timer = timer.timer()

    def track_player_buttons(self, keys):
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                if keys[pygame.K_x]:
                    self.update_values(2.5, -2.5, 45)
                elif keys[pygame.K_SPACE]:
                    if self.dash_cooldown_timer.remaining_time is None or self.dash_cooldown_timer.remaining_time <= 0:
                        self.update_values(15, -15, 45)
                        self.dash_length_timer.set_new_time(.5)
                else:
                    self.update_values(5, -5, 45)
            elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                if keys[pygame.K_x]:
                    self.update_values(-2.5, -2.5, 315)
                elif keys[pygame.K_SPACE]:
                    if self.dash_cooldown_timer.remaining_time is None or self.dash_cooldown_timer.remaining_time <= 0:
                        self.update_values(-15, -15, 315)
                        self.dash_length_timer.set_new_time(.5)
                else:
                    self.update_values(-5, -5, 315)
            else:
                if keys[pygame.K_x]:
                    self.update_values(0, -2.5, 0)
                elif keys[pygame.K_SPACE]:
                    if self.dash_cooldown_timer.remaining_time is None or self.dash_cooldown_timer.remaining_time <= 0:
                        self.update_values(0, -15, 0)
                        self.dash_length_timer.set_new_time(.5)
                else:
                    self.update_values(0, -5, 0)
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                if keys[pygame.K_x]:
                    self.update_values(2.5, 2.5, 135)
                elif keys[pygame.K_SPACE]:
                    if self.dash_cooldown_timer.remaining_time is None or self.dash_cooldown_timer.remaining_time <= 0:
                        self.update_values(15, 15, 135)
                        self.dash_length_timer.set_new_time(.5)
                else:
                    self.update_values(5, 5, 135)
            elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                if keys[pygame.K_x]:
                    self.update_values(-2.5, 2.5, 225)
                elif keys[pygame.K_SPACE]:
                    if self.dash_cooldown_timer.remaining_time is None or self.dash_cooldown_timer.remaining_time <= 0:
                        self.update_values(-15, 15, 225)
                        self.dash_length_timer.set_new_time(.5)
                else:
                    self.update_values(-5, 5, 225)
            else:
                if keys[pygame.K_x]:
                    self.update_values(0, 2.5, 180)
                elif keys[pygame.K_SPACE]:
                    if self.dash_cooldown_timer.remaining_time is None or self.dash_cooldown_timer.remaining_time <= 0:
                        self.update_values(0, 15, 180)
                        self.dash_length_timer.set_new_time(.5)
                else:
                    self.update_values(0, 5, 180)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if keys[pygame.K_x]:
                self.update_values(2.5, 0, 90)
            elif keys[pygame.K_SPACE]:
                if self.dash_cooldown_timer.remaining_time is None or self.dash_cooldown_timer.remaining_time <= 0:
                    self.update_values(15, 0, 90)
                    self.dash_length_timer.set_new_time(.5)
            else:
                self.update_values(5, 0, 90)
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if keys[pygame.K_x]:
                self.update_values(-2.5, 0, 270)
            elif keys[pygame.K_SPACE]:
                if self.dash_cooldown_timer.remaining_time is None or self.dash_cooldown_timer.remaining_time <= 0:
                    self.update_values(-15, 0, 270)
                    self.dash_length_timer.set_new_time(.5)
            else:
                self.update_values(-5, 0, 270)
        else:
            self.update_values(0, 0, 0)

    def update_values(self, x_change, y_change, rotation):
        #if self.dash_length_timer.remaining_time is None:
        try:
            if self.dash_length_timer.remaining_time <= 0:
                self.dash_cooldown_timer.set_new_time(1)
        except:
            print("DASH LENGTH ERROR")

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
                if self.health_cooldown_timer.remaining_time is None or self.health_cooldown_timer.remaining_time <= 0:
                    if self.health == 8:
                        self.Player_Sprite = pygame.image.load("Sprites/ProjectPSprite1H.PNG")
                        self.Player_Sprite = pygame.transform.scale(self.Player_Sprite, (15, 15))
                        self.health -= 1
                        self.health_cooldown_timer.set_new_time(2)
                    elif self.health == 7:
                        self.Player_Sprite = pygame.image.load("Sprites/ProjectPSprite2H.PNG")
                        self.Player_Sprite = pygame.transform.scale(self.Player_Sprite, (15, 15))
                        self.health -= 1
                        self.health_cooldown_timer.set_new_time(2)
                    elif self.health == 6:
                        self.Player_Sprite = pygame.image.load("Sprites/ProjectPSprite3H.PNG")
                        self.Player_Sprite = pygame.transform.scale(self.Player_Sprite, (15, 15))
                        self.health -= 1
                        self.health_cooldown_timer.set_new_time(2)
                    elif self.health == 5:
                        self.Player_Sprite = pygame.image.load("Sprites/ProjectPSprite4H.PNG")
                        self.Player_Sprite = pygame.transform.scale(self.Player_Sprite, (15, 15))
                        self.health -= 1
                        self.health_cooldown_timer.set_new_time(2)
                    elif self.health == 4:
                        self.Player_Sprite = pygame.image.load("Sprites/ProjectPSprite5H.PNG")
                        self.Player_Sprite = pygame.transform.scale(self.Player_Sprite, (15, 15))
                        self.health -= 1
                        self.health_cooldown_timer.set_new_time(2)
                    elif self.health == 3:
                        self.Player_Sprite = pygame.image.load("Sprites/ProjectPSprite6H.PNG")
                        self.Player_Sprite = pygame.transform.scale(self.Player_Sprite, (15, 15))
                        self.health -= 1
                        self.health_cooldown_timer.set_new_time(2)
                    elif self.health == 2:
                        self.Player_Sprite = pygame.image.load("Sprites/ProjectPSprite7H.PNG")
                        self.Player_Sprite = pygame.transform.scale(self.Player_Sprite, (15, 15))
                        self.health -= 1
                        self.health_cooldown_timer.set_new_time(2)
                    elif self.health == 1:
                        self.reset_player()
                        self.health_cooldown_timer.set_new_time(2)

    def reduce_timers(self):
        if self.health_cooldown_timer.count_down() == True:
            print("Health Cooldown Timer Done")
        if self.dash_cooldown_timer.count_down() == True:
            print("Dash Cooldown Timer Done")
        if self.dash_length_timer.count_down() == True:
            print("Dash Length Timer Done")



