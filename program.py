import pygame

import util
import color
from algorithms import Algorithm
from button import Button

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

        self.selectionButton = Button(self.window, (color.RED, color.WHITE), 'Selection Sort', (100, 150, 250, 50), self.algo.sort)
        self.bubbleButton = Button(self.window, (color.RED, color.WHITE), 'Bubble Sort', (100, 250, 250, 50), self.algo.sort)
        self.insertionButton = Button(self.window, (color.RED, color.WHITE), 'Insertion Sort', (100, 350, 250, 50), self.algo.sort)
        self.mergeButton = Button(self.window, (color.RED, color.WHITE), 'Merge Sort', (400, 150, 250, 50), self.algo.sort)
        self.quickButton = Button(self.window, (color.RED, color.WHITE), 'Quick Sort', (400, 250, 250, 50), self.algo.sort)
        self.heapButton = Button(self.window, (color.RED, color.WHITE), 'Heap Sort', (400, 350, 250, 50), self.algo.sort)
    
    def init(self):
        self.menu()
    
    def menu(self):
        while self.runMenu:
            pygame.time.delay(50)
            self.clock.tick(self.fps)

            pygame.display.set_caption('Sorting Visualization')
            self.window.fill(color.BLACK)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                print('Ola')

            for event in pygame.event.get():
                if event.type == pygame.QUIT or keys[pygame.K_SPACE]:
                    self.runMenu = False

            self.draw_buttons(self.selectionButton, self.bubbleButton, self.insertionButton, self.mergeButton,
                              self.quickButton, self.heapButton, mouse=pygame.mouse.get_pos()
            )
            self.buttons_actions(self.selectionButton, self.bubbleButton, self.insertionButton, self.mergeButton,
                                 self.quickButton, self.heapButton, mouse=pygame.mouse.get_pos(), click=pygame.mouse.get_pressed()
            )

            pygame.display.update()
    
    def draw_buttons(self, *args, **kwargs):
        for button in args:
            button.draw(kwargs['mouse'])
    
    def buttons_actions(self, *args, **kwargs):
        for button in args:
            button.action(kwargs['mouse'], kwargs['click'])
