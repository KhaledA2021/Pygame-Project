import pygame

class Player:
    def __init__(self):

#loads player/health sprites
    Playersprite = pygame.image.load("ProjectPSprite.PNG")
    Playerhealth = pygame.image.load("ProjectPSpriteHealth.PNG")

    Playersprite = pygame.transform.scale(Playersprite, (15, 15))
    Playerhealth = pygame.transform.scale(Playerhealth, (10, 10))

    current_pos = (500, 300)
    health_pos = current_pos

     Rotation = 0
    health_rotate = 0

    WIN.blit(Playersprite, current_pos)
    WIN.blit(Playerhealth, current_pos)


    def track_player_buttons(keys, rotation):
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                if keys[pygame.K_x]:
                    return 2.5, -2.5, 45
                else:
                    return 5, -5, 45
            elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                if keys[pygame.K_x]:
                    return -2.5, -2.5, 315
                else:
                    return -5, -5, 315
            else:
                if keys[pygame.K_x]:
                    return 0, -2.5, 0
                else:
                    return 0, -5, 0
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                if keys[pygame.K_x]:
                    return 2.5, 2.5, 135
                else:
                    return 5, 5, 135
            elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                if keys[pygame.K_x]:
                    return -2.5, 2.5, 225
                else:
                    return -5, 5, 225
            else:
                if keys[pygame.K_x]:
                    return 0, 2.5, 180
                else:
                    return 0, 5, 180
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if keys[pygame.K_x]:
                return 2.5, 0, 90
            else:
                return 5, 0, 90
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if keys[pygame.K_x]:
                return -2.5, 0, 270
            else:
                return -5, 0, 270
        else:
            return 0, 0, rotation


    def move_player(x, y, current_pos):
        current_pos = (current_pos[0] + x, current_pos[1] + y)
        if current_pos[0] < -10:
            current_pos = (-10, current_pos[1])
        if current_pos[0] > 999:
            current_pos = (999, current_pos[1])
        if current_pos[1] < -10:
            current_pos = (current_pos[0], -10)
        if current_pos[1] > 599:
            current_pos = (current_pos[0], 599)
        return current_pos


    wait_time = 0
    stop_dash = False

    follow_health = 0


    print(follow_health)



    x_change = 0
    y_change = 0



    KEYS = pygame.key.get_pressed()
    x_change , y_change, Rotation = track_player_buttons(KEYS, Rotation)
    if stop_dash:
        if wait_time > 20:
            x_change *= 3
            y_change *= 3

    if KEYS[pygame.K_SPACE]:
        if wait_time < 1:
            #current_pos = (current_pos[0]+(x_change*6), current_pos[1]+(y_change*6))
            wait_time = 40
            stop_dash = True

    save_pos = (x_change, y_change)
    save_rotation = Rotation

    current_pos = move_player(x_change, y_change, current_pos)

    if stop_dash:
        if wait_time < 1:
            stop_dash = False
        else:
            wait_time -= 1

    if follow_health > 5:
        health_pos = ((health_pos[0]+save_pos[0]), (health_pos[1]+save_pos[1]))
        health_rotate = save_rotation
        follow_health = 0
    else:
        follow_health += 1


    redraw_screen(BACKGROUNDCOLOR, Playersprite, Rotation, current_pos, Playerhealth, health_rotate, health_pos)

