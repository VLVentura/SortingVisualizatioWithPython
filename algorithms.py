import pygame
from copy import deepcopy
from random import randint

import util
import color


class Algorithm:
    def __init__(self, window):
        self.window = window

        self.minSize = 50
        self.maxSize = util.WINDOW_HEIGHT

        self.algos = {
            'selection': self.selection_sort,
            'bubble': self.bubble_sort,
            'insertion': self.insertion_sort,
            'merge': self.merge_sort,
            'quick': self.quick_sort,
            'heap': self.heap_sort
        }
        
        self.barSize = util.BAR_SIZE
        self.vector =  [randint(self.minSize, self.maxSize) for i in range(util.N_BARS + 1)]
        self.index_dict = self.create_dict()

    def sort(self, algorithm):
        self.algos[algorithm]()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        run = False

    def selection_sort(self):
        pygame.display.set_caption('Sorting Visualization - Selection Sort')
        for i in range(len(self.vector)):
            minIndex = i
            for j in range(i+1, len(self.vector)):
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()

                if self.vector[minIndex] > self.vector[j]:
                    minIndex = j

            self.window.fill(color.BLACK)
            self.draw(i, minIndex)

            self.vector[i], self.vector[minIndex] = self.vector[minIndex], self.vector[i]

            pygame.time.delay(200)
            self.draw()

        self.draw()
    
    def bubble_sort(self):
        pygame.display.set_caption('Sorting Visualization - Bubble Sort')
        swapped = False
        for i in range(len(self.vector)):
            for j in range(0, len(self.vector) - 1):
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()

                if self.vector[j] > self.vector[j+1]:
                    self.window.fill(color.BLACK)
                    self.draw(j, j + 1)

                    self.vector[j], self.vector[j+1] = self.vector[j+1], self.vector[j]
                    swapped = True

                    pygame.time.delay(100)
                    self.draw()
                
            if swapped == False:
                break

        self.draw()

    def insertion_sort(self):
        pygame.display.set_caption('Sorting Visualization - Insertion Sort')
        for i in range(1, len(self.vector)):
            j = i - 1
            key = self.vector[i]

            self.draw()

            while j>= 0 and key < self.vector[j]:
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()

                self.draw(j, j + 1)
                pygame.time.delay(50)
                
                self.vector[j + 1] = self.vector[j]
                j -= 1
                self.vector[j + 1] = key
                self.window.fill(color.BLACK)
            
            self.draw()

    def merge(self, arr, low, mid, high):
        n1 = mid - low + 1
        n2 = high - mid

        left = [0] * n1
        right = [0] * n2

        for i in range(n1):
            left[i] = arr[low + i]
        for j in range(n2):
            right[j] = arr[mid + 1 + j]

        i = j = 0
        k = low

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        self.draw()

        while i < n1 and j < n2:
            self.draw(self.index_dict[left[i]], self.index_dict[right[j]])
            pygame.time.delay(100)

            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            
            self.window.fill(color.BLACK)
            self.draw()

        while i < n1:
            arr[k] = left[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = right[j]
            j += 1
            k += 1
        
        self.window.fill(color.BLACK)
        self.draw()

    def merge_sort(self, arr=None, low=0, high=util.N_BARS):
        pygame.display.set_caption('Sorting Visualization - Merge Sort')
        if arr == None:
            arr = self.vector

        if low < high:
            mid = (low + high) // 2
            self.merge_sort(arr, low, mid)
            self.merge_sort(arr, mid + 1, high)
            self.merge(arr, low, mid, high)
            
            self.draw() 

    def partition(self, low, high):
        i = low - 1
        pivot = self.vector[high]

        self.draw()

        for j in range(low, high):
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            if self.vector[j] <= pivot:
                i = i + 1
                self.draw(i, j)
                pygame.time.delay(100)

                self.vector[i], self.vector[j] = self.vector[j], self.vector[i]

                self.window.fill(color.BLACK)
                self.draw()

        self.draw(i, j)
        pygame.time.delay(100)

        self.vector[i + 1], self.vector[high] = self.vector[high], self.vector[i + 1]

        self.window.fill(color.BLACK)
        self.draw()
        
        return i + 1

    def quick_sort(self, low=0, high=util.N_BARS):
        pygame.display.set_caption('Sorting Visualization - Quick Sort')
        if low < high:
            part = self.partition(low, high)
            self.quick_sort(low, part - 1)
            self.quick_sort(part + 1, high)

    def heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[largest] < arr[l]:
            largest = l
        
        if r < n and arr[largest] < arr[r]:
            largest = r
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        self.window.fill(color.BLACK)
        self.draw()

        if largest != i:
            self.draw(self.index_dict[arr[i]], self.index_dict[arr[largest]])
            pygame.time.delay(100)

            arr[i], arr[largest] = arr[largest], arr[i]

            self.window.fill(color.BLACK)
            self.draw()

            self.heapify(arr, n, largest)

    def heap_sort(self, arr=None):
        pygame.display.set_caption('Sorting Visualization - Heap Sort')
        if arr == None:
            arr = self.vector

        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n , i)
        
        self.window.fill(color.BLACK)
        self.draw()

        for i in range(n - 1, 0, -1):
            self.draw(self.index_dict[arr[i]], self.index_dict[arr[0]])
            pygame.time.delay(100)

            arr[i], arr[0] = arr[0], arr[i]

            self.window.fill(color.BLACK)
            self.draw()

            self.heapify(arr, i, 0)
                
    def draw(self, blue=None, red=None):
        for i in range(len(self.vector)):
            if i == blue:
                clr = color.BLUE
            elif i == red:
                clr = color.RED
            else:
                clr = color.WHITE

            pygame.draw.rect(self.window, clr, (i * self.barSize, 0, self.barSize, self.vector[i]))
            pygame.draw.rect(self.window, color.BLACK, (i * self.barSize, 0, self.barSize, self.vector[i]), True)

        pygame.display.update()
    
    def create_dict(self):
        dic = dict()
        for i in range(len(self.vector)):
            dic[self.vector[i]] = i
        return dic