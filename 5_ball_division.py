import pygame
import os

######################################################################
# 1. 기본 초기화
pygame.init()

# 화면 크기 설장
screen_w = 640
screen_h = 480
screen = pygame.display.set_mode((screen_w, screen_h))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Pang")

# FPS
clock = pygame.time.Clock()


######################################################################
# 2. 사용자 게임 초기화 (배경 화면, 게임 이미지, 이동, 속도, 폰트, 시간 등)

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

# 배경 화면 1
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 배경 화면 2 - 스테이지
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_w = stage_size[0]
stage_h = stage_size[1]

# 게임 이미지 1 - 캐릭터
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_w = character_size[0]
character_h = character_size[1]
character_x_pos = (screen_w / 2) - (character_w / 2)
character_y_pos = screen_h - stage_h - character_h

# 게임 이미지 2 - 무기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_w = weapon_size[0]
weapons = []

# 게임 이미지 3 - 공
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))]

ball_speed_y = [-18, -15, -12, -9]

balls = []

balls.append({
    "pos_x" : 50,
    "pos_y" : 50,
    "img_idx" : 0,
    "to_x" : 3,
    "to_y" : -6,
    "init_spd_y" : ball_speed_y[0]})


# 이동 초기값
character_to_x = 0

# 속도 초기값
character_speed = 0.5
weapon_speed = 0.5

# 변수설장
weapon_to_remove = -1
ball_to_remove = -1

# 폰트


# 시간



######################################################################
# 3. 이벤트 처리 

running = True
while running:
    dt = clock.tick(60)

    # 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_w / 2)  - (weapon_w / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0


    # 게임 캐릭터 이동 정의
    character_x_pos += (character_to_x * dt)
    
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos >= screen_w - character_w:
        character_x_pos = screen_w - character_w

    weapons = [ [w[0], w[1] - (weapon_speed * dt)] for w in weapons]
    weapons = [ [w[0], w[1]]for w in weapons if w[1] > 0]
        
    for idx, val in enumerate(balls):
        ball_x_pos = val["pos_x"]
        ball_y_pos = val["pos_y"]
        ball_img_idx = val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_w = ball_size[0]
        ball_h = ball_size[1]

        if ball_y_pos >= screen_h - stage_h - ball_h:
            val["to_y"] = val["init_spd_y"]
        
        if ball_x_pos < 0 or ball_x_pos > screen_w - ball_w:
            val["to_x"] = val["to_x"] * -1

        val["to_y"] += 0.5
        val["pos_x"] += val["to_x"]
        val["pos_y"] += val["to_y"]
        

    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for b_idx, b_val in enumerate(balls):
        ball_x_pos = b_val["pos_x"]
        ball_y_pos = b_val["pos_y"]
        ball_img_idx = b_val["img_idx"]

        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_x_pos
        ball_rect.top = ball_y_pos

        if character_rect.colliderect(ball_rect):
            running = False
            break
        
        for w_idx, w_val in enumerate(weapons):
            weapon_x_pos = w_val[0]
            weapon_y_pos = w_val[1]

            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_x_pos
            weapon_rect.top = weapon_y_pos

            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = w_idx
                ball_to_remove = b_idx

                if ball_img_idx < 3:
                    ball_w = ball_rect.size[0]
                    ball_h = ball_rect.size[1]

                    small_ball_rect = ball_images[b_idx + 1].get_rect()
                    small_ball_w = small_ball_rect.size[0]
                    small_ball_h = small_ball_rect.size[1]

                    balls.append({
                        "pos_x" : ball_x_pos + (ball_w / 2) - (small_ball_w / 2),
                        "pos_y" : ball_y_pos + (ball_h / 2) - (small_ball_h / 2),
                        "img_idx" : ball_img_idx + 1,
                        "to_x" : -3,
                        "to_y" : -6,
                        "init_spd_y" : ball_speed_y[ball_img_idx + 1]}) 

                    balls.append({
                        "pos_x" : ball_x_pos + (ball_w / 2) - (small_ball_w / 2),
                        "pos_y" : ball_y_pos + (ball_h / 2) - (small_ball_h / 2),
                        "img_idx" : ball_img_idx + 1,
                        "to_x" : 3,
                        "to_y" : -6,
                        "init_spd_y" : ball_speed_y[ball_img_idx + 1]}) 

                break

    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1
    
    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1


    # 화면에 그리기
    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    
    screen.blit(stage, (0, screen_h - stage_h))
    screen.blit(character, (character_x_pos, character_y_pos))

    for idx, val in enumerate(balls):
        ball_x_pos = val["pos_x"]
        ball_y_pos = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_x_pos, ball_y_pos))

    pygame.display.update()

######################################################################
# 4. 닫기
pygame.quit()