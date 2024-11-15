import pygame
import math
import random
from pygame.locals import *
from pygame import mixer
pygame.init()
mixer.init()

clock = pygame.time.Clock()
FPS = 60
	
SCREEN_WIDTH = 1090
SCREEN_HEIGHT = 2180
score=0
	#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Race Game")
file='/storage/emulated/0/Pythonimage/Pygame/'
bg=mixer.music.load(file+'Bg.mp3')
slash = pygame.mixer.Sound(file+'Slash.mp3')
crash_ = pygame.mixer.Sound(file+'Crash.wav')
coin_get = pygame.mixer.Sound(file+'Coin.wav')
mixer.music.play()
	
	#load image
bg = pygame.image.load(file+'pygame_bg.jpg').convert()
rt = pygame.image.load(file+'rt.png')
lt = pygame.image.load(file+'lt.png')
van = pygame.image.load(file+'van.png')
taxi = pygame.image.load(file+'taxi.png')
semi_trailer = pygame.image.load(file+'semi_trailer.png')
pickup_truck = pygame.image.load(file+'pickup_truck.png')
crash = pygame.image.load(file+'crash.png')
car = pygame.image.load(file+'car.png')
coin = pygame.image.load(file+'coin.png')
start_bg = pygame.image.load(file+'Start.png')

list_car = [van,taxi,pickup_truck]
font = pygame.font.Font('freesansbold.ttf', 70)

with open(file+'best_score.txt','r') as f:
	best_score=f.read()
with open(file+'coin_score.txt','r') as f1:
	coin_score=f1.read()
def main():
	global best_score,score,coin_score
	score=0
	mixer.music.play()
	x_van = random.randint(200,SCREEN_WIDTH-300)
	y_van = random.randint(0,SCREEN_HEIGHT/2)
	x_taxi = random.randint(200,SCREEN_WIDTH-300)
	y_taxi = random.randint(0,SCREEN_HEIGHT/2)
	x_pickup_truck = random.randint(200,SCREEN_WIDTH-300)
	y_pickup_truck = random.randint(0,SCREEN_HEIGHT/2)
	x_coin = random.randint(200,SCREEN_WIDTH-300)
	y_coin = random.randint(0,SCREEN_HEIGHT/2)
	
	x_car = (SCREEN_WIDTH/2)-50
	y_car = SCREEN_HEIGHT-700
	
	bg_width = bg.get_width()
	bg_height= bg.get_height()
	bg_rect = bg.get_rect()
	
	#define game variables
	scroll = -bg_height
	tiles = math.ceil(SCREEN_HEIGHT  / bg_height) + 1
	
	#game loop
	game_exit=False
	while not game_exit:
	  #event handler
	  MUSIC_END = pygame.USEREVENT+1
	  pygame.mixer.music.set_endevent(MUSIC_END)
	  for event in pygame.event.get():
	    if event.type == pygame.QUIT:
	      game_exit=True
	      
	    if event.type == MUSIC_END:
	    	mixer.music.play()
	  
	  #draw scrolling background
	  for i in range(0, tiles):
	    screen.blit(bg, ( -10,i * bg_height + scroll))
	    
	  #scroll background
	  scroll += 30
	  
	  text1 = font.render('Score :- '+str(score), True, (0,0,0))
	  text2 = font.render(str(coin_score)+' -: Coin', True, (0,0,0))
	  screen.blit(text1,(10,10))
	  screen.blit(text2,(700,10))
	 
	  screen.blit(car, ( x_car,y_car))
	  
	  x,y = pygame.mouse.get_pos()
	  
	  if 0<x<200 and 1400<y<1600:
	    if x_car<220:
	      x_car==220
	    else:
	    	x_car-=8
	    	pygame.mixer.Sound.play(slash)
	    	
	  
	  if 880<x<1080 and 1400<y<1600:
	    if x_car>780:
	      x_car==780
	    else:
	    	x_car+=8
	    	pygame.mixer.Sound.play(slash)
	  pygame.mouse.set_pos([0,0])
	    	 
	  #reset scroll
	  if scroll > 0:
	  	scroll = -bg_height
	  	
	  screen.blit(rt, ( 880,1400))
	  screen.blit(lt, ( 0,1400))
	  
	  screen.blit(list_car[0], ( x_van,y_van))
	  screen.blit(list_car[1], ( x_taxi,y_taxi))
	  screen.blit(list_car[2], ( x_pickup_truck,y_pickup_truck))
	  screen.blit(coin, ( x_coin,y_coin))
	  y_van+=10
	  y_taxi+=10
	  y_pickup_truck+=10
	  y_coin+=3
	  if y_coin>=SCREEN_HEIGHT:
	  	y_coin=0
	  	x_coin = random.randint(200,SCREEN_WIDTH-300)
	  	y_coin = random.randint(-100,-60)
	  if abs(y_coin+60)-abs(y_car)>1 and (abs(x_coin)<abs(x_car)<abs(x_coin+60) or abs(x_car)<abs(x_coin)<abs(x_car+80) ):
	  	pygame.mixer.Sound.play(coin_get)
	  	x_coin = random.randint(200,SCREEN_WIDTH-300)
	  	y_coin = random.randint(-100,-60)
	  	screen.blit(coin, ( x_coin,y_coin))
	  	coin_score=int(coin_score)+1
	  	
	  if ( abs(y_van+190)-abs(y_car)>1 and abs(y_van)-abs(y_car)<175) and (abs(x_van)<abs(x_car)<abs(x_van+90) or abs(x_car)<abs(x_van)<abs(x_car+80) ):
	  	pygame.mixer.Sound.play(crash_)
	  	screen.blit(crash, ( 500,500))
	  	start()
	  	game_exit=True
	  	
	  if (abs(y_taxi+157)-abs(y_car)>1 and abs(y_taxi)-abs(y_car)<175) and (abs(x_taxi)<abs(x_car)<abs(x_taxi+80) or abs(x_car)<abs(x_taxi)<abs(x_car+80) ):
	  	pygame.mixer.Sound.play(crash_)
	  	screen.blit(crash, ( 500,500))
	  	start()
	  	game_exit=True
	  	
	  if ( abs(y_pickup_truck+172)-abs(y_car)>1 and abs(y_pickup_truck)-abs(y_car)<175) and (abs(x_pickup_truck)<abs(x_car)<abs(x_pickup_truck+90) or abs(x_car)<abs(x_pickup_truck)<abs(x_car+80) ):
	  	pygame.mixer.Sound.play(crash_)
	  	screen.blit(crash, ( 500,500))
	  	start()
	  	game_exit=True
	  	
	  if y_van>=SCREEN_HEIGHT:
	  	y_van=0
	  	x_van = random.randint(200,SCREEN_WIDTH-300)
	  	y_van = random.randint(-SCREEN_HEIGHT,-200)
	  	
	  if y_taxi>=SCREEN_HEIGHT:
	  	y_taxi=0
	  	x_taxi = random.randint(200,SCREEN_WIDTH-300)
	  	y_taxi = random.randint(-SCREEN_HEIGHT,-200)
	  	
	  if y_pickup_truck>=SCREEN_HEIGHT:
	  	y_pickup_truck=0
	  	x_pickup_truck = random.randint(200,SCREEN_WIDTH-300)
	  	y_pickup_truck = random.randint(-SCREEN_HEIGHT,-200)
	  	
	  score+=1
	  
	  if int(score)>int(best_score):
	  	best_score=score
	  	with open(file+'best_score.txt','w') as d:
	  		d.write(str(best_score))
	  with open(file+'coin_score.txt','w') as f1:
	  	f1.write(str(coin_score))
	  clock.tick(FPS)
	  pygame.display.update()
	  
def start():
	global score,best_score,coin_score
	game_exits=False
	while not game_exits:
		MUSIC_END = pygame.USEREVENT+1
		pygame.mixer.music.set_endevent(MUSIC_END)
		for event in pygame.event.get():
		     if event.type == pygame.QUIT:
		     	game_exit=True
		     	
		     if event.type == MUSIC_END:
		     	mixer.music.play()
		screen.blit(start_bg, (0,0))
		text3 = font.render('Your Score :- '+str(score), True, (235,200,50))
		text4 = font.render('Best Score :- '+str(best_score), True, (235,200,50))
		text5 = font.render('Total Coin :- '+str(coin_score), True, (235,200,50))
		if score!=0:
			screen.blit(text3,(220,1450))
		screen.blit(text4,(220,1550))
		screen.blit(text5,(220,1650))
		x,y=pygame.mouse.get_pos()
		if 450<x<550 and 950<y<1050:
			main()
			game_exits=True
		pygame.display.update()
		   	
start()
pygame.quit()