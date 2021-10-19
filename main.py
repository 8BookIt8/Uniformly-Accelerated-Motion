import pygame

import car as vehicle

pygame.init()

# rgb 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 150, 0)

# 자동차 설정
accel = -1
velocity = 10
car_code = vehicle.Car(accel, velocity, BLACK)
car_formula = vehicle.Car(accel, velocity, GREEN)

# 타임 클락
clock = pygame.time.Clock()
time = 0

# 스크린 설정
screen_width = 1000
screen_height = 562
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Math2 Report')


# 텍스트 설정
font = pygame.font.Font('fonts/font.ttf', 30)
pos_velocity_code = (10, 5)
pos_velocity_formula = (10, 30)
pos_displacement_code = (10, 55)
pos_displacement_formula = (10, 80)

while True: 
    # 클락 설정
    clock.tick(100)
    time += 0.01

    # 프로그램 종료
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()

    # 배경 설정
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, [0, 500], [1000, 500], 5)

    # 자동차 스프라이트
    if car_code.getVelocity() > 0: 
        car_code.move()
    car_code.draw(screen)
    
    car_formula.moveFormula(velocity, time)
    car_formula.draw(screen)

    # 속도 텍스트
    velocity_text = font.render('velocity_code : {}'.format(round(car_code.getVelocity(), 2)), True, BLACK)
    screen.blit(velocity_text, pos_velocity_code)
    formula_text = font.render('velocity_format : {}'.format(round(car_formula.getVelocity(), 2)), True, BLACK)
    screen.blit(formula_text, pos_velocity_formula)

    # 변위 텍스트
    velocity_text = font.render('displacement_code : {}'.format(round(car_code.getDisplacement(), 2)), True, BLACK)
    screen.blit(velocity_text, pos_displacement_code)
    formula_text = font.render('displacement_format : {}'.format(round(car_formula.getDisplacement(), 2)), True, BLACK)
    screen.blit(formula_text, pos_displacement_formula)

    pygame.display.update()