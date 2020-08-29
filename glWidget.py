import sys
from OpenGL.GL import *
from PyQt5 import QtCore, QtWidgets, QtOpenGL
from PyQt5.QtWidgets import QOpenGLWidget
import pygame
from math import *
class GlWidget(QOpenGLWidget):
    clickCanvas=0
    vec=[]
    posX=0
    posY=0
    zoom=1.0
    def __init__(self, parent=None):
        QOpenGLWidget.__init__(self, parent)
        self.setMinimumSize(730, 380)

    def drawText(self,px,py,pz, textString,color):
        pygame.init()     
        font = pygame.font.Font(None, 18)
        textSurface = font.render(textString, True, color, (96,96,96,255))     
        textData = pygame.image.tostring(textSurface, "RGBA", True)     
        glRasterPos3d(px,py,pz)     
        glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)
    def drawG54(self,px,py,pz,r,r1,color,segments=36):
        posx, posy,posz = px+0.01,py,pz    
        radius = r
        radius1 = r1
        c=color
        s=segments
        glColor4f(c[0],c[1],c[2],c[3])   
        glBegin(GL_LINE_LOOP)    
        for i in range(s):
            theta=float(2.00)*float(pi)*float(i)/float(s)    
            cosine= float((radius*cos(theta))+posx)    
            sine  = float((radius * sin(theta))+posy)    
            glVertex3f(cosine,sine,posz)
        glEnd()
        glFlush()
        glBegin(GL_LINE_LOOP)    
        for i in range(s):
            theta=float(2.00)*float(pi)*float(i)/float(s)    
            cosine= float((radius1*cos(theta))+posx)    
            sine  = float((radius1 * sin(theta))+posy)    
            glVertex3f(cosine,sine,posz)
        glEnd()
        glFlush()
        glBegin(GL_LINES)
        glVertex3f(float(posx-r),float(posy-r),posz)
        glVertex3f(float(posx+r),float(posy+r),posz)
        glVertex3f(float(posx-r),float(posy+r),posz)
        glVertex3f(float(posx+r),float(posy-r),posz)
        glEnd()
        glFlush()
        self.drawText(posx+1,posy+1,posz,"G54",(0,255,0))

    def drawAxisXZ(self,px,py,pz):
        px=px+0.01
        glBegin(GL_LINES)
        # color X
        glColor3f( 1.0, 0.0, 0.0 )
        # vertities X
        glVertex3f(px+30,py,pz)
        glVertex3f(px,py,pz)
        # color Z
        glColor3f( 0.0, 0.0, 1.0 )
        # vertities Z
        glVertex3f(px,py+30,pz)
        glVertex3f(px,py,pz)
        glEnd()
        glFlush()
        self.drawText(px+20,py+2,pz,"X",(255,0,0,255))
        self.drawText(px+2,py+20,pz,"Z",(0,0,255,255))
    
    def drawHandle(self,pz,s=1,c=(0.0,0.0,0.0,1.0)):
        
        glColor4f(c[0],c[1],c[2],c[3])
        glPolygonMode(GL_FRONT, GL_FILL)
        glBegin(GL_QUADS)
        glVertex3f(-5.0*s,-20*s,pz)
        glVertex3f(0,-20*s,pz) 
        glVertex3f(0,20*s,pz)
        glVertex3f(-5*s,20*s,pz)
        glEnd()
        glFlush()

    def drawWorkpice(self,dia,lang,pz,s=1):
        glColor4f(1.0,1.0,1.0,1.0)
        glBegin(GL_LINE_LOOP)
        glVertex3f(0.02,float(-dia/2),pz)
        glVertex3f(float(lang),float(-dia/2),pz) 
        glVertex3f(float(lang),float(dia/2),pz)
        glVertex3f(0.02,float(dia/2),pz)
        glEnd()
        glFlush()    
    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
         

    def initializeGL(self):
       
        glClearDepth(1.0)              
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-10,100,-50,50,-150,150)
        rValue= 96.0 / 255.0
        gValue= 96.0 / 255.0
        bValue= 96.0 / 255.0
        glClearColor(rValue, gValue, bValue, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        
    # def mousePressEvent(self,e):
    #     self.clickCanvas+=1
    #     pos=e.pos()
    #     windowSize=(730,380)
    #     self.posX=(pos.x() / windowSize[0]*(50+50))-50
    #     self.posY=(pos.y() / windowSize[1]*(50+50))-50
    #     # self.initializeGL()
    #     self.paintGL()
       
    
        

