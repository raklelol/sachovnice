
import pygame
import serial
import time
pygame.init()
pygame.display.set_caption('Šachy')
sachovnice = [[1,1,1,1,1,1,1,1],
			  [1,1,1,1,1,1,1,1],
			  [0,0,0,0,0,0,0,0],
			  [0,0,0,0,0,0,0,0],
			  [0,0,0,0,0,0,0,0],
			  [0,0,0,0,0,0,0,0],
			  [1,1,1,1,1,1,1,1],
			  [1,1,1,1,1,1,1,1]]

white = (255, 255, 255)
blue = (1, 25, 54)
black = (0, 0, 0)
brown = (179, 127, 79)
green = (173, 234, 153)
odarduino = [1,1,1,1,1,1,1]

#vytvoří plochu programu

display_surface = pygame.display.set_mode()
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0.1)
ser.reset_input_buffer()
minulyline = ""

#tloušťka ohraničení šachovnice
#rozlišení výšky monitoru, získané z pygame [1]>pořadí z listu
#vzdálenost hrací plochy od lévého a horního okraje obrazovky
#rozdělení obrazovky na 9 stejných částí
#velikost sachovnice v počtu políček

velikost = 2
hrana = 10
rozliseniy = display_surface.get_size()[1]
rozlisenix = display_surface.get_size()[0]
okraje = int(rozliseniy/(velikost+1)/2)
rozdeleni = int(rozliseniy/(velikost+1))
zmena = 0

#generace hrací plochy
def plocha():
	#pozadí
	display_surface.fill(green)
	#generace políček
	for x in range(velikost):
		for y in range(velikost):
			if(x%2==y%2): 
				color = brown
			else:
				color = white
			pygame.draw.rect(display_surface, color, pygame.Rect(rozdeleni*x+okraje, rozdeleni*y+okraje, rozdeleni, rozdeleni))
	#ohraničení šachovnice
	pygame.draw.rect(display_surface, black, pygame.Rect(okraje-hrana, okraje-hrana, rozdeleni*velikost+hrana*2, rozdeleni*velikost+hrana*2),  hrana)
	

#generace figurek
def figurky():
	for x in range(velikost):
		for y in range(velikost):
			if(sachovnice[y][x]==1):
				display_surface.blit(img, (int(rozdeleni*x+okraje+rozdeleni*1/8), int(rozdeleni*y+okraje+rozdeleni*0.5/8)))
	
def ledky():
	global zmena
	for x in range(velikost):
		for y in range(velikost):
			if(sachovnice[y][x]==1):
				if zmena == 1:
					vypocet = x*velikost+y+1
					vypocet = str(vypocet)
					#print(vypocet)
					ser.write(vypocet.encode('utf-8'))
					zmena = 0
			if(sachovnice[y][x]==0):
				if zmena == 1:
					vypocet = x*velikost+y+1
					vypocet = str(vypocet)
					#print(vypocet)
					ser.write(vypocet.encode('utf-8'))
					zmena = 0
				
	#print("---------------")
	

#načtení obrázku
#změna rozlišení obrázku

img = pygame.image.load("stickman.png")
img = pygame.transform.scale(img, (int(rozdeleni*3/4), int(rozdeleni*3.5//4)))


ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0.3)
ser.reset_input_buffer()
while True:
	line = ser.readline().decode('utf-8').rstrip()
	if line != minulyline:
		zmena = 1
		odarduino = [int(char) for char in line]
		sachovnice[odarduino[1]][odarduino[0]] = odarduino[2] 
		 
	
	plocha()
	figurky()
	#ser.write(b"2\n")
	ledky()
	pygame.display.update()
	

	#pokud vypnete program tak se vypne 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
			 
			