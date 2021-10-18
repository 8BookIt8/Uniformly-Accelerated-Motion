from os import access
import pygame

class Car(): 
    def __init__(self, accel, velocity): 
        self.width = 120
        self.height = 80
        self.x = 0 - self.width
        self.y = 500 - self.height - 2
        self.color = (0, 147, 0)

        self.accel = accel
        self.velocity = velocity
        self.displacement = 0

    def draw(self, screen): 
        '''
        자동차 스크린에 그리기
        
        Args: 
            screen (float): 자동차가 그려질 스크린
        ''' 
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])

    def move(self): 
        time = 0.01
        dist = self.velocity * time
        self.addDisplacement(dist)
        self.x += dist
        new_velocity = self.velocity + (self.accel * time)
        self.velocity = new_velocity if new_velocity > 0 else 0

    def setAccel(self, accel):
        '''
        가속도 설정
        
        Args: 
            accel (float): 자동차의 가속도
        ''' 
        self.accel = accel
    def getAccel(self): 
        '''
        자동차의 가속도 가져오기

        Returns: 
            accel (float): 자동차의 가속도
        '''
        return self.accel

    def setVelocity(self, velocity): 
        '''
        속도 설정
        
        Args: 
            velocity (float): 자동차의 속도
        ''' 
        self.velocity = velocity
    def getVelocity(self): 
        '''
        자동차의 속도 가져오기

        Returns: 
            velocity (float): 자동차의 속도
        '''
        return self.velocity

    def addDisplacement(self, displacement): 
        '''
        변위 추가
        
        Args: 
            displacement (float): 자동차의 변위
        ''' 
        self.displacement += displacement
    def getDisplacement(self): 
        '''
        자동차의 변위 가져오기

        Returns: 
            displacement (float): 자동차의 변위
        '''
        return self.displacement