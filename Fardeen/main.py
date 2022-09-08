import pygame
import os
import sys


screen_width = 1244
screen_height = 1016
SCREEN  = pygame.display.set_mode((screen_width, screen_height))

TRACK = pygame.image.load(os.path.join("assets", "track.png"))

#car class for defining car object
class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load(os.path.join("assets", "car.png"))
        self.image = self.original_image
        self.rect = self.image.get_rect(center = (490, 820))
        self.drive_state = False
        self.vel_vector = pygame.math.Vcetor2(0.8, 0)
        self.angle = 0

    #updates the position and angle every time called 
    def update(self):
        self.drive()
        self.update()

    #changes the pos of car accordingly
    def drive(self):
        if self.drive_state:
            self.rect.center += self.vel_vector * 6

    def rotate(self):
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 0.1)


car = pygame.sprite.GroupSingle(Car())

#main function
def eval_genomes():
    run = True
    while run: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.blit(TRACK, (0,0))

        #taking input from the user 
        user_input = pygame.key.get_pressed()
        if sum(pygame.key.get_pressed) <= 1:
            car.sprite.drive_state = False

        #drive
        if user_input[pygame.K_UP]:
            car.sprite.drive_state= True

eval_genomes()
        