#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 16:02:01 2018

@author: hienh
"""
from Shapes import *
from pylab import random as r

class MovingShape:
    
    def __init__(self,frame,shape,diameter):
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape,diameter)
        
        self.minx = self.diameter
        self.miny = self.diameter
        
        self.maxx = frame.width - self.diameter
        self.maxy = frame.height - self.diameter
        
        #def starting position for shapes
        self.x = self.minx + (r()* (self.maxx - self.minx))
        self.y= self.miny + (r()* (self.maxy - self.miny))
 
        #Move shapes in different direction
        self.dx=5+10*r()
        self.dy=5+10 *r()
        
        #randomising starting posiiton 
        self.goto(self.x,self.y)
        
        
    def goto(self,x,y):
        self.figure.goto(x,y)

            
    def moveTick(self):
    
        self.x= self.x
        self.y= self.y
        
        #bouncing shape when it hits the wall 
    
        if self.x >= self.maxx :
            self.dx = self.dx * -1 
    
        if self.y >= self.maxy:
            self.dy=self.dy *-1
            
        if self.x <= self.minx :
            self.dx = self.dx * -1 
    
        if self.y <= self.miny:
            self.dy=self.dy *-1
            

        self.x= self.x +self.dx
        self.y= self.y+ self.dy 

        self.goto(self.x,self.y)
        
        

class Square(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'square',diameter)
        self.minx = self.diameter/2
        self.miny = self.diameter/2


#Generating different shape      
        
class Diamond(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'diamond',diameter)
        self.diameter =2 *self.diameter
        self.minx = self.diameter/2
        self.miny = self.diameter/2


class Circle(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'circle',diameter)
        
