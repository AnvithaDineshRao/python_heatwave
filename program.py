#import library
import pygame
from pygame.locals import *
import time
import random
import sys

width=600
#bound_width=680
cell=20
cellwidth=width/cell                         #no. of cells
FPS=10                                       #frequency per second


pygame.init()                                #start pygame
screen=pygame.display.set_mode((width,width))      #creating a surface/screen
pygame.display.set_caption("PYTHON")                #captioning the screen
myfont = pygame.font.Font('freesansbold.ttf', 18)
myclock=pygame.time.Clock()

#colour codes
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkblue = (0,0,128) 
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
darkgreen = (0, 155, 0)
brown=(165,42,42)


def startscreen():
    pass

def draw_snake(coords):
    #print "draw snake  : "
    for c in coords:
        #print c
        snake=pygame.draw.rect(screen,black,(c[0]*cell,c[1]*cell,cell,cell),0)


def draw_fruit():
    global x;global y                                    #position of apple
    x=(random.randint(0,cellwidth-1))
    y=(random.randint(0,cellwidth-1))
    #print "in draw fruit : ",x,y
    apple=pygame.draw.rect(screen,red, (x*cell,y*cell,cell,cell), 0)

def draw_score(score):
    score_font=pygame.font.Font('freesansbold.ttf', 18)
    label=score_font.render((("SCORE : %d "%score)),True,darkblue)
    screen.blit(label,(500,2))
    pygame.display.flip()
    

#main..

screen.fill(green)
#boundary=pygame.draw.rect(screen,brown,(0,0,width,height),2*cell)
#snake=pygame.draw.rect(screen,black,(200,200,3*cell,cell),0)

dirs=1                                        #direction in which snake moves
score=0
#print "in main : ",x,y
coords=[(15,15),(14,15)]
draw_snake(coords)
draw_fruit()
draw_score(score)

pygame.display.flip()                         #to update screen
while 1:
#checking for eventswhile 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()                      #quit from pygame and surface
            sys.exit(0)                         #quit from python prog
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP and dirs!=0:     #up=2
                dirs=2
            elif event.key==pygame.K_DOWN and dirs!=2:     #down=0
                dirs=0
            elif event.key==pygame.K_LEFT and dirs!=1:     #left=3
                dirs=3
            elif event.key==pygame.K_RIGHT and dirs!=3:     #right=1
                dirs=1
            elif event.key == K_ESCAPE:
                 pygame.quit()                      #quit from pygame and surface
                 sys.exit(0)

    #when you hit the boundary
    if (coords[0][0]==-1 or coords[0][0]==cellwidth or coords[0][1]==-1 or coords[0][1]==cellwidth):
        pygame.quit()
        
    #when the snake bites itself
    for snakebody in coords[1:]:
        if((coords[0][0],coords[0][1])==snakebody):
            pygame.quit()

    #if it encounters a fruit
    if(coords[0][0]==x and coords[0][1]==y):
        #print "fruit: " ,x,y
        draw_fruit()
    #else decrease the size
    else:
        (a,b)= coords.pop()
        pygame.draw.rect(screen,green,(a*cell,b*cell,cell,cell),0)
    
        draw_snake(coords)
        pygame.display.flip()
        
    #move the snake

    if(dirs==0):                                #move down
        coords.insert(0,(coords[0][0],coords[0][1]+1))
    elif (dirs==2):                             #move up
        coords.insert(0,(coords[0][0],coords[0][1]-1))
    elif (dirs==1):                             #move right
        coords.insert(0,(coords[0][0]+1,coords[0][1]))
        #print coords
    elif(dirs==3):                              #move left
        coords.insert(0,(coords[0][0]-1,coords[0][1]))


    
    draw_snake(coords)
    score=len(coords)-2
    draw_score(score)
    pygame.display.flip()  
    myclock.tick(FPS)               #pause the screen for FPS so its not too fast
            
    

