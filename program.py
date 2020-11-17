import pygame

import util
import color
from algorithms import Algorithm

class Program:

    WINDOW_HEIGHT = util.WINDOW_HEIGHT
    WINDOW_WIDTH = util.WINDOW_WIDTH

    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((Program.WINDOW_WIDTH, Program.WINDOW_HEIGHT))
        
        self.fps = 10
        self.clock = pygame.time.Clock()

        self.runMenu = True

        self.algo = Algorithm(self.window)
    
    def init(self):
        self.menu()
    
    def menu(self):
        while self.runMenu:
            pygame.time.delay(50)
            self.clock.tick(self.fps)

            pygame.display.set_caption('Sorting Visualization')
            self.window.fill(color.BLACK)

            self.algo.merge_sort()
            pygame.display.update()
