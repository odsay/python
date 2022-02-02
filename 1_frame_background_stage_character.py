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
stage_h = stage_size[1]

# 게임 이미지 1 - 캐릭터
character = pygame.image.load(os.path.join(image_path, "character.png")) 
character_size = character.get_rect().size
character_w = character_size[0]
character_h = character_size[1]
character_x_pos = (screen_w / 2) - (character_w / 2)
character_y_pos = screen_h - character_h - stage_h

# 이동 초기값


# 속도 초기값


# 폰트


# 시간


######################################################################
# 3. 이벤트 처리

running = True
while running:
    dt = clock.tick(30)

    # 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # 게임 캐릭터 이동 정의

    # 충돌 처리

    # 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_h - stage_h))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()


######################################################################
# 4. 닫기
pygame.quit()