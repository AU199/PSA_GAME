import pygame
import os

pygame.init()
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption('GAME')

x = 0
y = 500
rounds_move = 1
rounds_idle = 0
cool_move= 0
cool_idle = 0
images = []
images_i = []

for file_name in os.listdir("Movement Right"):
  img = pygame.image.load("Movement Right"+os.sep+file_name).convert()
  images.append(img)

for file_name in os.listdir("Idle"):
  img = pygame.image.load("Idle"+os.sep+file_name).convert()
  images_i.append(img)


print("BREAKPOINT 1")

def check_key(key,r,x):
  
    if key == "right":
    
      image = images[r]
    
      image = pygame.transform.rotozoom(image,0,3)
      x +=0.1

    if key == "left":
      image = images[r]
      image = pygame.transform.flip(image, True, False)
      image = pygame.transform.rotozoom(image,0,3)
      x-=0.1

  
    return image,x
    
def tick(rm,cm,ci,ri):
  if cool_move < 1:
    rm += 1
  
    cm += 50
  
  
  
  if rm > len(images)-1: 
    rm = 0
  
    cm += 50
  
  if cm > 0:
    cm -= 1
  return rm,ri,cm,ci
def idle(r):
  return pygame.transform.rotozoom(images_i[0],0,3)
    
print("BREAKPOINT 2")
a = None
while True:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
    
  b = tick(rounds_move,cool_move,cool_idle,rounds_idle)
  rounds_move = b[0]
  rounds_idle = b[1]
  cool_move = b[2]
  cool_idle = b[3]
  keys=pygame.key.get_pressed()
  if keys[pygame.K_RIGHT]:
    a = check_key("right",rounds_move,x)
    x = a[1]
    screen.blit(a[0],(x,y))
  elif keys[pygame.K_LEFT]:
    a=check_key("left",rounds_move,x)
    x = a[1]
    screen.blit(a[0],(x,y))
  else:
    a = idle(rounds_idle)
    screen.blit(a,(x,y))

  
  
  
  
  pygame.display.flip()
