import pygame
from pygame.locals import * 
from tkinter import *
from tkinter import messagebox

#General Variables
clickCounter = 0
clickable1,clickable2,clickable3,clickable4,clickable5,clickable6,clickable7,clickable8,clickable9 = True,True,True,True,True,True,True,True,True
c1, c2, c3, c4, c5, c6, c7, c8, c9 = False,False,False,False,False,False,False,False,False
x1, x2, x3, x4, x5, x6, x7, x8, x9 = True,True,True,True,True,True,True,True,True
cArray = [c1,c2,c3,c4,c5,c6,c7,c8,c9]
xArray = [x1,x2,x3,x4,x5,x6,x7,x8,x9]
msgControl = 0
controlArray = [[0,3,6],[1,4,7],[2,5,8],[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6]]

#Colors
RED = (200,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)

#General
pygame.init()
screen = pygame.display.set_mode((420, 420))
pygame.display.set_caption('XOX Game')
done = False
screen.fill(WHITE)

#Image Setup
xImage = pygame.image.load("x.png").convert_alpha()
oImage = pygame.image.load("o.png").convert_alpha()

def xWon():
	global msgControl
	if msgControl == 0:
		Tk().wm_withdraw()
		messagebox.showinfo('Game Over!','X Won')
	msgControl += 1

def yWon():
	global msgControl
	if msgControl == 0:
		Tk().wm_withdraw()
		messagebox.showinfo('Game Over!','Y Won')
	msgControl += 1

def controlStatement(x,y,z):
	global clickable1,clickable2,clickable3,clickable4,clickable5,clickable6,clickable7,clickable8,clickable9
	if cArray[x] == cArray[y] == cArray[z] == True:
		if xArray[x] == xArray[y] == xArray[z] == True:
			clickable1,clickable2,clickable3,clickable4,clickable5,clickable6,clickable7,clickable8,clickable9 = False,False,False,False,False,False,False,False,False
			xWon()
		elif xArray[x] == xArray[y] == xArray[z] == False: 
			clickable1,clickable2,clickable3,clickable4,clickable5,clickable6,clickable7,clickable8,clickable9 = False,False,False,False,False,False,False,False,False
			yWon()
		else:
			pass

def control():
	for fD in controlArray:
		first = fD[0]
		second = fD[1]
		third = fD[2]
		controlStatement(first,second,third)

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				mouseX, mouseY = event.pos

		if clickCounter%2 == 0:
			xTime = True
		else:
			xTime = False
		
		try:
			if (mouseX <= 138 and mouseY <= 138 and clickable1 == True):
				if (xTime == True):
					clickable1 = False
					c1 = True
					screen.blit(xImage, (0,0))
					pygame.display.flip()
					clickCounter += 1
				elif (xTime == False):
					x1 = False
					clickable1 = False
					c1 = True
					screen.blit(oImage, (0,0))
					pygame.display.flip()
					clickCounter += 1

			elif (mouseX >= 140 and mouseX <= 278 and mouseY <= 138 and clickable2 == True):
				if (xTime == True):
					clickable2 = False
					c2 = True
					screen.blit(xImage, (140,0))
					pygame.display.flip()
					clickCounter += 1
				elif (xTime == False):
					x2 = False
					clickable2 = False
					c2 = True
					screen.blit(oImage, (140,0))
					pygame.display.flip()
					clickCounter += 1

			elif (mouseX >= 280 and mouseX <= 418 and mouseY <= 138 and clickable3 == True):
				if (xTime == True):
					clickable3 = False
					c3 = True
					screen.blit(xImage, (280,0))
					pygame.display.flip()
					clickCounter += 1
				elif (xTime == False):
					x3 = False
					clickable3 = False
					c3 = True
					screen.blit(oImage, (280,0))
					pygame.display.flip()
					clickCounter += 1

			elif (mouseX <= 138 and mouseY >= 138 and mouseY <= 278 and clickable4 == True):
				if (xTime == True):
					clickable4 = False
					c4 = True
					screen.blit(xImage, (0,140))
					pygame.display.flip()
					clickCounter += 1
				elif (xTime == False):
					x4 = False
					clickable4 = False
					c4 = True
					screen.blit(oImage, (0,140))
					pygame.display.flip()
					clickCounter += 1

			elif (mouseX >= 140 and mouseX <= 278 and mouseY >= 138 and mouseY <= 278 and clickable5 == True):
				if (xTime == True):
					clickable5 = False
					c5 = True
					screen.blit(xImage, (140,140))
					pygame.display.flip()
					clickCounter += 1
				elif (xTime == False):
					x5 = False
					clickable5 = False
					c5 = True
					screen.blit(oImage, (140,140))
					pygame.display.flip()
					clickCounter += 1

			elif (mouseX >= 280 and mouseX <= 418 and mouseY <= 278 and mouseY >= 138 and clickable6 == True):
				if (xTime == True):
					clickable6 = False
					c6 = True
					screen.blit(xImage, (280,140))
					pygame.display.flip()
					clickCounter += 1
				elif (xTime == False):
					x6 = False
					clickable6 = False
					c6 = True
					screen.blit(oImage, (280,140))
					pygame.display.flip()
					clickCounter += 1

			elif (mouseX <= 138 and mouseY <= 418 and mouseY >= 280 and clickable7 == True):
				if (xTime == True):
					clickable7 = False
					c7 = True
					screen.blit(xImage, (0,280))
					pygame.display.flip()
					clickCounter += 1
				elif (xTime == False):
					x7 = False
					clickable7 = False
					c7 = True
					screen.blit(oImage, (0,280))
					pygame.display.flip()
					clickCounter += 1

			elif (mouseX <= 278 and mouseX >= 140 and mouseY >= 280 and mouseY <= 418 and clickable8 == True):
				if (xTime == True):
					clickable8 = False
					c8 = True
					screen.blit(xImage, (140,280))
					pygame.display.flip()
					clickCounter += 1
				elif (xTime == False):
					x8 = False
					clickable8 = False
					c8 = True
					screen.blit(oImage, (140,280))
					pygame.display.flip()
					clickCounter += 1

			elif (mouseX <= 418 and mouseX >= 280 and mouseY >= 280 and mouseY <= 418 and clickable9 == True):
				if (xTime == True):
					clickable9 = False
					c9 = True
					screen.blit(xImage, (280,280))
					pygame.display.flip()
					clickCounter += 1
				elif (xTime == False):
					x9 = False
					clickable9 = False
					c9 = True
					screen.blit(oImage, (280,280))
					pygame.display.flip()
					clickCounter += 1
			cArray = [c1,c2,c3,c4,c5,c6,c7,c8,c9]
			xArray = [x1,x2,x3,x4,x5,x6,x7,x8,x9]
			control()
		except:
			pass	

	#Objects
	pygame.draw.rect(screen, [0, 0, 0], (0,0,139,139), 1)
	pygame.draw.rect(screen, [0, 0, 0], (140,0,139,139), 1)
	pygame.draw.rect(screen, [0, 0, 0], (280,0,139,139), 1)
	#SecondLine
	pygame.draw.rect(screen, [0, 0, 0], (0,140,139,139), 1)
	pygame.draw.rect(screen, [0, 0, 0], (140,140,139,139), 1)
	pygame.draw.rect(screen, [0, 0, 0], (280,140,139,139), 1)
	#ThirdLine
	pygame.draw.rect(screen, [0, 0, 0], (0,280,139,139), 1)
	pygame.draw.rect(screen, [0, 0, 0], (140,280,139,139), 1)
	pygame.draw.rect(screen, [0, 0, 0], (280,280,139,139), 1)
	
	pygame.display.flip()