import pygame
import os

pygame.init()

screen_w = 640
screen_h = 480
screen = pygame.display.set_mode((screen_w, screen_h))

pygame.display.set_caption("Nado Game")

clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

background = pygame.image.load(os.path.join(image_path, "background.png"))

stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_h = stage.get_rect().size[1]

character = pygame.image.load(os.path.join(image_path, "character.png"))
character_w = character.get_rect().size[0]
character_h = character.get_rect().size[1]
character_x_pos = (screen_w / 2) - (character_w / 2)
character_y_pos = screen_h - stage_h - character_h
to_x = 0
to_y = 0
character_speed = 0.5

weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_w = weapon.get_rect().size[0]
weapon_y = weapon.get_rect().size[1]
weapons = []
weapon_speed = 0.5

ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))]

ball_speed_y = [-18, -15, -12, -9]

balls = []

balls.append([{
    "x_pos" : 50,
    "y_pos" : 50,
    "img_idx" : 0,
    "to_x" : 3,
    "to_y" : -6,
    "init_spd_y" : ball_speed_y[0]
    }])

game_font = pygame.font.Font(None, 40)
game_text = ["Do you want to Start(S) or Quit(Q)?", "Game Over", "Mission Complete"]

step = 0

running = True
while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                step = 1
            elif event.key == pygame.K_q:
                running = False
            elif event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapons.append([character_x_pos + (character_w / 2) - (weapon_w / 2),character_y_pos]) 

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    
    character_x_pos += to_x * dt

    screen.blit(background, (0, 0))

    if step == 0:
        msg = game_font.render(game_text[step], True, (255, 100, 50))
        msg_rect = msg.get_rect(center=(int(screen_w / 2), int(screen_h / 2)))
        screen.blit(msg, msg_rect)

    elif step == 1:
        weapons = [ [w[0], w[1] - (weapon_speed * dt)] for w in weapons ]
        weapons = [ [w[0], w[1]] for w in weapons if w[1] >0]
        
        


        if character_x_pos < 0:
            character_x_pos = 0
        elif character_x_pos > screen_w - character_w:
            character_x_pos = screen_w - character_w

        for w in weapons:
            screen.blit(weapon, (w[0], w[1]))
        screen.blit(stage, (0, screen_h - stage_h))
        screen.blit(character, (character_x_pos, character_y_pos))

        for ball_idx, ball_val in enumerate(balls):
            ball_x_pos = ball_val["x_pos"]
            ball_y_pos = ball_val["y_pos"]
            screen.blit()

    pygame.display.update()

def end():
    pass


pygame.quit()
