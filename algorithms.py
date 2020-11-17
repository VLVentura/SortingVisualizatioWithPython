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
        
        self.barSize = util.BAR_SIZE
        self.vector =  [randint(self.minSize, self.maxSize) for i in range(util.N_BARS + 1)]
        self.index_dict = self.create_dict()

    def sort(self, algorithm, **kwargs):
        pass

    def selection_sort(self):
        pygame.display.set_caption('Sorting Visualization - Selection Sort')
        for i in range(len(self.vector)):
            minIndex = i
            for j in range(i+1, len(self.vector)):
                if self.vector[minIndex] > self.vector[j]:
                    minIndex = j

            self.window.fill(color.BLACK)
            self.draw(i, minIndex)

            self.vector[i], self.vector[minIndex] = self.vector[minIndex], self.vector[i]

            pygame.time.delay(200)
            self.draw()

        self.draw()
    
    def bubble_sort(self, recursive=False):
        pygame.display.set_caption('Sorting Visualization - Bubble Sort')
        swapped = False
        for i in range(len(self.vector)):
            for j in range(0, len(self.vector) - 1):
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

    def insertion_sort(self, recursive=False):
        pygame.display.set_caption('Sorting Visualization - Insertion Sort')
        for i in range(1, len(self.vector)):
            j = i - 1
            key = self.vector[i]

            self.draw()

            while j>= 0 and key < self.vector[j]:
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
        if arr == None:
            arr = self.vector

        if low < high:
            mid = (low + high) // 2
            self.merge_sort(arr, low, mid)
            self.merge_sort(arr, mid + 1, high)
            self.merge(arr, low, mid, high)
            
            self.draw()

    def partition(self, low, high):
        pygame.display.set_caption('Sorting Visualization - Quick Sort')
        i = low - 1
        pivot = self.vector[high]

        self.draw()

        for j in range(low, high):
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

    def heap_sort(self):
        pass

    def counting_sort(self):
        pass

    def radix_sort(self):
        pass

    def bucket_sort(self):
        pass

    def shell_sort(self):
        pass
    
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