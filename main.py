import pygame #the module that has all the game functionality that will be used 
import sys #to allow the game to quit properly
import random

#Constants 
SCREENWIDTH = 576
SCREENHEIGHT = 1024
FRAMERATE = 100 #number of frames per second 
BIRDXPOS = 100
BIRDYPOS = 512
GRAVITY = 0.30
JUMPHEIGHT = 8
PIPETIME = 900


def drawFloor():
	screen.blit(ground,(groundx,850))
	screen.blit(ground2,(groundx+SCREENWIDTH,850))
	

def createPipe(): 	
	randomPos = random.choice(pipeHeights)
	bottomPipe = pipe.get_rect(topleft = (SCREENWIDTH,SCREENHEIGHT-randomPos))
	topPipe = pipe.get_rect(bottomleft = (SCREENWIDTH,(SCREENHEIGHT-randomPos)-300))
	return bottomPipe,topPipe


def movePipes(pipes):
	for curPipe in pipes: 
		curPipe.centerx -= 3.5
		if curPipe.right < 0:
			pipes.remove(curPipe)	
	return pipes


def drawPipes(pipes):
	for curPipe in pipes: 
		if curPipe.bottom >= 1024: 
			screen.blit(pipe,curPipe)
		else: 
			screen.blit(pygame.transform.flip(pipe,False,True),curPipe)

#initiates pygame
pygame.init()

#creating a display surface 
screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
clock = pygame.time.Clock()

cur_bg = pygame.transform.scale2x(pygame.image.load('assets/background-day.png').convert())

ground = pygame.transform.scale2x(pygame.image.load('assets/base.png').convert())
ground2 = pygame.transform.scale2x(pygame.image.load('assets/base.png').convert())
groundx = 0

bird = pygame.transform.scale2x(pygame.image.load('assets/bluebird-midflap.png').convert())
birdRec = bird.get_rect(center = (BIRDXPOS,BIRDYPOS))
birdMovement = 0

pipe = pygame.transform.scale2x(pygame.image.load('assets/pipe-green.png').convert())	
pipeList = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,PIPETIME) #event that will be triggered every 1.2 seconds
pipeHeights = [300,325,350,375,400,415,425,430,445,450,475,460,455,500]

while True: 
	
	#event loop - have to look for specific types of events 
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			pygame.quit()	#unitializing the game 
			sys.exit()
		if event.type == pygame.KEYDOWN:	#checks if any key has been pressed 
			if event.key == pygame.K_SPACE: 
				birdMovement=0
				birdMovement-= JUMPHEIGHT
		if event.type == pygame.MOUSEBUTTONDOWN: 
			birdMovement=0
			birdMovement-= JUMPHEIGHT
		if event.type == SPAWNPIPE: 
			pipeList.extend(createPipe())
			print(pipeList)

	screen.blit(cur_bg,(0,0))

	#Bird 

	birdMovement += GRAVITY
	birdRec.centery += birdMovement 
	if(birdRec.centery > SCREENHEIGHT):
		birdRec.centery = SCREENHEIGHT
	screen.blit(bird,birdRec)	

	#Pipes 

	pipeList = movePipes(pipeList)
	drawPipes(pipeList)


	# Floor 

	if(groundx == -SCREENWIDTH):
		groundx = 0
	drawFloor()
	groundx -= 4

	#takes anything drawn before, and updates the display with it
	pygame.display.update() 
	clock.tick(FRAMERATE) 
