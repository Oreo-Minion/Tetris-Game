import pygame
import sys
pygame.init()
surface = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()
SIZE1 = 40
SIZE2 = 145
background = [[None for topdown in range(21)] for sidetoside in range(10)]
background[0][1] = (255,0, 0)
background[0][19] = (0,250, 244)
background[9][1] = (250, 250, 0)
background[9][19] = (0,0, 244)
#foreground= [[None for topdown in range(21)] for sidetoside in range(10)]
#foreground[4][5] = (255,255, 255)
#make seperate forground for each piece and draw and erase accordingly to player input
##
##
##(x=3,y=2)
##[ [x] ]
##[?, ?, ?, ?, ?, ?]
##[?, ?, x, ?, ?, ?]
##[?, ?, ?, ?, ?, ?]
##[?, ?, ?, ?, ?, ?]
##[?, ?, ?, ?, ?, ?]
##[?, ?, ?, ?, ?, ?]
##[?, ?, ?, ?, ?, ?]
##
##move [0,0] to [3,2]
##move [1,0] to [4,2]
##move [0,1] to [3,3]
##move [1,1] to [4,3]

def drawalayer(layer, x_offset, y_offset): #small , 3,2
        for topdown in range(y_offset, len(layer)+y_offset): # 2
            for sidetoside in range(x_offset, len(layer)+x_offset): #3
                if layer[sidetoside-x_offset][topdown-y_offset]!=None: #small but needs to be in terms of big layer
                    pygame.draw.rect(surface, layer[sidetoside-x_offset][topdown-y_offset], ((sidetoside*SIZE1)+15,(topdown*SIZE1)+15, SIZE1-1, SIZE1-1))
def upanddown():
        for topdown in range(19,-1,-1):
                for sidetoside in range(0,10):
                        if foreground[sidetoside][topdown]!= None:
                                foreground [sidetoside][topdown] = None                                                         
                                foreground [sidetoside][topdown+1] = (255,0,0)

def movement(e, Testbox):
        if e.type == pygame.K_LEFT:
                Testbox.shift(1, 0)
        elif e.type == pygame.K_RIGHT:
                Testbox.shift(-1, 0)
        elif e.type == pygame.K_DOWN:
                Testbox.shift(0, -1)
        
####

class Piece:
        def __init__(self, template):
                self.shape = template
                self.x = 5
                self.y = 0
        def shift(self, dx, dy):
                self.x += dx
                self.y += dy
        def draw(self):
                drawalayer(self.shape, self.x, self.y)
#Coding the Pieces In
tetrimino = [[None for topdown in range(21)] for sidetoside in range(10)]
tetrimino[5][0]=(145, 0, 226)
tetrimino[5][1]=(145, 0, 226)
tetrimino[4][1]=(145, 0, 226)
tetrimino[6][1]=(145, 0, 226)
                                
Lshape1 = [[None for topdown in range(21)] for sidetoside in range(10)]
Lshape1[6][0]=(212, 89, 0)
Lshape1[6][1]=(212, 89, 0)                                
Lshape1[5][1]=(212, 89, 0)                                
Lshape1[4][1]=(212, 89, 0)

Squiggle1 = [[None for topdown in range(21)] for sidetoside in range(10)]
Squiggle1[4][0]=(183, 13, 0)
Squiggle1[5][0]=(183, 13, 0)                                
Squiggle1[5][1]=(183, 13, 0)                              
Squiggle1[6][1]=(183, 13, 0)


Squiggle2 = [[None for topdown in range(21)] for sidetoside in range(10)]
Squiggle2[5][0]=(51, 171, 0)
Squiggle2[6][0]=(51, 171, 0)                                
Squiggle2[5][1]=(51, 171, 0)                              
Squiggle2[4][1]=(51, 171, 0)

Line = [[None for topdown in range(21)] for sidetoside in range(10)]
Line[4][0]=(97, 230, 255)
Line[5][0]=(97, 230, 255)                               
Line[6][0]=(97, 230, 255)                            
Line[7][0]=(97, 230, 255)

Box = [[None for topdown in range(21)] for sidetoside in range(10)]
Box[5][0]=(243, 247, 0)
Box[6][0]=(243, 247, 0)                              
Box[5][1]=(243, 247, 0)                         
Box[6][1]=(243, 247, 0)

Lshape2 = [[None for topdown in range(21)] for sidetoside in range(10)]
Lshape2[4][0]=(33, 62, 210)
Lshape2[4][1]=(33, 62, 210)                              
Lshape2[5][1]=(33, 62, 210)                        
Lshape2[6][1]=(33, 62, 210)

Testbox_shape = [[None for topdown in range(21)] for sidetoside in range(10)]
Testbox_shape[0][0]=(33, 62, 210)
Testbox = Piece(Testbox_shape)

def nextpiece():
        futuredisplay = [[None for topdown1 in range(5)] for sidetoside1 in range(1)]
        futuredisplay[0][0] = (255,0,0)
        futuredisplay[0][4] = (0,0,244)

        for topdown1 in range(0,5):
            for sidetoside1 in range(0,1):
                if futuredisplay[sidetoside1][topdown1]!=None: 
                    pygame.draw.rect(surface, futuredisplay[sidetoside1][topdown1], ((sidetoside1*SIZE2)+505, (topdown1*SIZE2)+15, SIZE2, SIZE2))
                      
def ol():

        #Top Border
        color1= (255,0,0)
        start_pos1= (10,50)
        end_pos1= (420,50)
        width1 = 10
        pygame.draw.line(surface, color1, start_pos1, end_pos1, width1)

        #Bottom Border
        color2= (255,255,0)
        start_pos2= (10,855)
        end_pos2= (420,855)
        width2 = 10
        pygame.draw.line(surface, color2, start_pos2, end_pos2, width2)

        #Left Border
        color3= (100,0,0)
        start_pos3= (10,45)
        end_pos3= (10,855)
        width3 = 10
        pygame.draw.line(surface, color3, start_pos3, end_pos3, width3)

        #Right Border
        color4= (100,100,0)
        start_pos4= (420,45)
        end_pos4= (420,855)
        width4 = 10
        pygame.draw.line(surface, color4, start_pos4, end_pos4, width4)

        #Sneak Peek Border Line 1
        color5= (255,0,0)
        start_pos5= (500,10)
        end_pos5= (650,10)
        width5 = 10
        pygame.draw.line(surface, color5, start_pos5, end_pos5, width5)

        #Sneak Peek Border Line 2
        color6= (255,255,0)
        start_pos6= (500,740)
        end_pos6= (650,740)
        width6 = 10
        pygame.draw.line(surface, color6, start_pos6, end_pos6, width6)

        #Sneak Peek Border Line 3
        color7= (100,0,0)
        start_pos7= (500,5)
        end_pos7= (500,745)
        width7 = 10
        pygame.draw.line(surface, color7, start_pos7, end_pos7, width7)

        #Sneak Peek Border Line 4
        color8= (100,100,0)
        start_pos8= (645,5)
        end_pos8= (645,745)
        width8 = 10
        pygame.draw.line(surface, color8, start_pos8, end_pos8, width8)
        

while True:
        surface.fill((255,255,255))
        drawalayer(background,0,0)
       # upanddown()
        ol()
        nextpiece()
        Testbox.draw()
       # drawalayer(foreground)
        pygame.display.flip()
       # lefttoright()
        clock.tick(60)                        
        for e in pygame.event.get():
                if e.type == pygame.QUIT:
                        sys.exit(0)
                movement(e, Testbox)
                print ("hello")


                        
