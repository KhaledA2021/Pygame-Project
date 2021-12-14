import pygame



class player:

    timer = 0

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
    def sprite(self):
        return self.Player_Sprite

    def reset_player(self):
        self.pos = (500, 300)
        self.rotate = 0
        self.hitbox = True
        self.health = 3
        self.Player_Sprite = pygame.image.load("Sprites/ProjectPSprite.PNG")
        self.Player_Sprite = pygame.transform.scale(self.Player_Sprite, (15, 15))


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


    def timer(self, timer_set_time, set_timer, timer):
        if set_timer == True:
            timer = timer_set_time
        elif set_timer == False and timer != 0:
            timer -= timer
            print(timer)


