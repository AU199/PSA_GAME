import pygame
import os

pygame.init()

screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption('GAME')
screen.fill((240, 240, 240))
x = 0
y = 500
rounds_move = 1
rounds_idle = 0
cool_move = 0
cool_idle = 0
images_m = []
images_i = []
images_e = []
jump = 0
font = pygame.font.Font("FONT.ttf",24)

grass_line = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

posa = -40
posb = 0

for file_name in os.listdir("Movement Right"):
  img = pygame.image.load("Movement Right" + os.sep +
                          file_name).convert_alpha()
  images_m.append(img)

for file_name in os.listdir("Idle"):
  img = pygame.image.load("Idle" + os.sep + file_name).convert_alpha()
  images_i.append(img)
images_i.append(pygame.image.load("Idle/New Piskel-2.png.png"))

for file_name in os.listdir("EXTRAS"):
  print(file_name)
  img = pygame.image.load("EXTRAS" + os.sep + file_name).convert_alpha()
  images_e.append(img)

print("BREAKPOINT 1")

def write(sentence,font):
  ret = font.render(sentence,True,(240,240,240))
  return ret
  

def check_key(key, r, x):

  if key == "right":

    image = images_m[r]

    image = pygame.transform.rotozoom(image, 0, 3)
    x += 0.5

  if key == "left":
    image = images_m[r]
    image = pygame.transform.flip(image, True, False)
    image = pygame.transform.rotozoom(image, 0, 3)
    x -= 0.5

  return image, x


def tick(rm, cm, ci, ri):
  if cm < 1:
    rm += 1

    cm += 10
  if ci < 1:
    ri += 1
    ci += 140

  if rm > len(images_m) - 1:
    rm = 0

    cm += 10
  if ri > len(images_i) - 1:
    ri = 0
    ci += 140

  if cm > 0:
    cm -= 1
  if ci > 0:
    ci -= 1
  return rm, ri, cm, ci


def idle(r):
  image = images_i[r]

  image = pygame.transform.rotozoom(image, 0, 3)
  return image


def print_grass():

  image = pygame.transform.rotozoom(images_e[0], 0, 3.5)

  return image


print(images_e[0])

print("BREAKPOINT 2")
a = None
image = None
while True:
  p = write("HELLO DOES THIS WORK",font)
  screen.fill((40, 50, 240))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()

  b = tick(rounds_move, cool_move, cool_idle, rounds_idle)

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