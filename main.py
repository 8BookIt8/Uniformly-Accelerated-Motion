import pygame

import car as vehicle

pygame.init()

# 자동차 설정
accel = -1
velocity = 10
car = vehicle.Car(accel, velocity)

# 타임 클락
clock = pygame.time.Clock()
time = 0

# 스크린 설정
screen_width = 1000
screen_height = 562
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Math2 Report')

# rgb 설정
background_color = (30, 30, 30)
WHITE = (255, 255, 255)

# 텍스트 설정
font = pygame.font.Font('fonts/font.ttf', 30)
pos_code = (10, 5)
pos_formula = (10, 30)

def getFormulaVelocity(): 
    new_velocity = velocity + (accel * time)
    return new_velocity if new_velocity > 0 else 0

displacement = 0
def getFormulaDisplacement(): 
    global displacement
    new_displacement = (velocity * time) + ((accel * (time ** 2)) / 2)
    displacement = new_displacement if new_displacement > displacement else displacement
    return displacement

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
    screen.fill(background_color)
    pygame.draw.line(screen, WHITE, [0, 500], [1000, 500], 5)
    pygame.draw.rect(screen, (255, 255, 255), [50, 500 - 100 + 2, 100, 100])

    # 자동차 스프라이트
    if car.getVelocity() > 0: 
        car.move()
    car.draw(screen)

    # 속도 텍스트
    velocity_text = font.render('velocity : {}'.format(round(car.getVelocity(), 2)), True, (255, 255, 255))
    screen.blit(velocity_text, pos_code)
    formula_text = font.render('format : {}'.format(round(getFormulaVelocity(), 2)), True, (255, 255, 255))
    screen.blit(formula_text, pos_formula)

    # 변위 텍스트
    # velocity_text = font.render('displacement : {}'.format(round(car.getDisplacement(), 2)), True, (255, 255, 255))
    # screen.blit(velocity_text, pos_code)
    # formula_text = font.render('format : {}'.format(round(getFormulaDisplacement(), 2)), True, (255, 255, 255))
    # screen.blit(formula_text, pos_formula)

    pygame.display.update()