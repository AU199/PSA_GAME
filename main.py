import pygame
import os

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('GAME')

rounds_move = 1
cool_dow = 0
images = []

for file_name in os.listdir("Movement Right"):
  img = pygame.image.load("Movement Right"+os.sep+file_name).convert()
  images.append(img)
  

print("BREAKPOINT 1")

def move(r):


  pass
print("BREAKPOINT 2")

while True:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      

  if cool_dow < 1:
    rounds_move += 1
    move(rounds_move)
    cool_dow += 600

          
      
  if rounds_move > len(images)-1: 
    rounds_move = 0
    move(rounds_move)
    cool_dow += 600
    
  if cool_dow > 0:
    cool_dow -= 1

  image = images[rounds_move]

  image = pygame.transform.rotozoom(image,0,3)

  screen.blit(image,(200,200))
  
  
  
  pygame.display.flip()
