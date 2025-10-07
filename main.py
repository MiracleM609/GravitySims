import math

import pygame,circle,sim1,sim2,sim3,sim4,calc

from sim4 import create_n_objs

pygame.init()





class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1000, 1000))
        self.clock = pygame.time.Clock()
        self.running = True
        #self.c1 = circle.Object(self, 100, 200, 5, 20,m=1,colour="green")
        #self.c2 = circle.Object(self, 400, 400, 20, 20,m=200000000,colour="yellow")
        #self.objs = [self.c1, self.c2]
        self.objs = []
        self.objs_hitbox = []
        #self.objs_hitbox = [self.c1.hitbox, self.c2.hitbox]
        self.nx = []
        self.ny = []
        n = input("enter number of objects: ")
        n = int(n)
        create_n_objs(n,self)

        self.ini_v = -0.1
        #self.nx,self.ny= 0,0
        self.d = False
        self.fast =False

        self.run()
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:self.running=False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:self.running=False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_f:self.fast =True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:self.fast=False

            self.screen.fill((0,0,0))
            self.update()
            pygame.display.set_caption(f"{self.clock.get_fps()}")
            sim4.sim4(self, self.objs,self.ini_v)
            pygame.display.flip()
            print(self.fast)
            if not self.fast:self.clock.tick(60)


    def update(self):
        for obj in self.objs:
            obj.update()
        #pygame.draw.line(self.screen, (255,255,255),(self.c1.x,self.c1.y),(self.c2.x,self.c2.y))




game = Game()
pygame.quit()