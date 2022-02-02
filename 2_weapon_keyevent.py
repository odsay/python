import pygame
import os

######################################################################
# 1. 기본 초기화
pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

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

# 이동 초기값
character_to_x = 0
motion = 0

# 속도 초기값
character_speed = 0.5
weapon_speed = 0.5

# 폰트


# 시간


######################################################################
# 3. 이벤트 처리

running = True
while running:
    dt = clock.tick(60)
    if abs(motion) < 0.1:
        motion = 0

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
                weapon_x_pos = character_x_pos + (character_w / 2) - (weapon_w / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
        
        if event.type == pygame.JOYAXISMOTION:
            if event.axis < 1:
                motion = event.value * 0.5
                character_to_x = motion
            
    # 게임 캐릭터 이동 정의
    character_x_pos += character_to_x * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_w - character_w:
        character_x_pos = screen_w - character_w

    weapons = [ [w[0], w[1] - (weapon_speed * dt)] for w in weapons]
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]

    # 충돌 처리

    # 화면에 그리기
    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    
    screen.blit(stage, (0, screen_h - stage_h))
    screen.blit(character, (character_x_pos, character_y_pos))


    pygame.display.update()

######################################################################
# 4. 닫기
pygame.quit()