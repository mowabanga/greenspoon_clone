import pygame as pg
import moderngl as mgl
import sys

class graphicsEngine :
    def __init__(self, win_size=(1600, 900)):
        """init pygame modules
        """
        pg.init()
        #window size
        self.WIN_SIZE = win_size
        
        