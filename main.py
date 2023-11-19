import pygame
import os
import random

RandomNum = random.randint(0, 4)

pygame.init()

screen = pygame.display.set_mode((700, 600))
pygame.display.set_caption('GAME')
screen.fill((240, 240, 240))
x = 0
g_x = 0
y = 500
g_y = 0
rounds_move = 1
rounds_idle = 0
ax_move = 1
god_move = 0
curr_in = 0
cool_move = 0
cool_ax = 0
cool_god = 0
cool_idle = 0
tree_created = 0
god_entered = 0

printv = ""
curr_hed = ""
images_m = []
images_i = []
images_e = []
images_ax = []
images_g = []
images_h = []
current_tick = [
    "right", 600, "axe_swing", 2,"entry_god",2, "speak", "STOP!!", "god", "speak",
    "Why are you cutting a tree down", "god", "speak",
    "So that I can graze my cattle", "human", "speak", "", "", "clear", "end"
]
god_current_tick = ["wait", 1000, "left", 20]
curr_t = current_tick[1]
jump = 0
font = pygame.font.Font("FONT.ttf", 24)

cloud_line = list(range(0, 700, random.randint(30, 100)))
cloud_y = []
for i in range(len(cloud_line)):
  cloud_y.append(random.randint(150, 200))
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
for file_name in os.listdir("Axe-Swing-Animations"):
  image = pygame.image.load("Axe-Swing-Animations" + os.sep +
                            file_name).convert_alpha()
  images_ax.append(image)
for file_name in os.listdir("God_Assets"):
  image = pygame.image.load("God_Assets" + os.sep + file_name).convert_alpha()
  images_g.append(image)
for file_name in os.listdir("Talking_heads"):
  image = pygame.image.load("Talking_heads" + os.sep +
                            file_name).convert_alpha()
  images_h.append(image)


def write(sentence, font):
  ret = font.render(sentence, True, (240, 240, 240))

  return ret


def check_key(key, r, x):
  image = None

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


def tick(rm, cm, ci, ri, am, ac, gm, gc):
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

  if ac < 1:
    am += 1
    ac += 100
  if gm < 1:
    gc += 1
    gm += 100
  if am > len(images_m) - 1:
    am = 0

    cm += 10
  if gm > len(images_e) - 1:
    gm =0
    gc += 100

  if cm > 0:
    cm -= 1
  if ci > 0:
    ci -= 1
  if ac > 0:
    ac -= 1
  if gc >0:
    gc -=1 
  return rm, ri, cm, ci, ac, am, gm,gc


def idle(r):
  image = images_i[r]

  image = pygame.transform.rotozoom(image, 0, 3)
  return image


def axe_swing(curr):

  image = images_ax[curr]
  image = pygame.transform.rotozoom(image, 0, 3)
  return image


def print_grass():

  image = pygame.transform.rotozoom(images_e[2], 0, 2)

  return image


def print_clouds():
  image = pygame.transform.rotozoom(images_e[4], 0, 2)

  return image


def print_tree():
  tree_image = images_e[3]
  zoomed_tree = pygame.transform.rotozoom(tree_image, 0, 10)
  return zoomed_tree


def god(key, r, x):
  image = images_g[r]
  if key == "left":
    image = pygame.transform.flip(image, True, False)
    image = pygame.transform.rotozoom(image, 0, 3)
    x -= 0.5
  if key == "right":
    image = pygame.transform.rotozoom(image, 0, 3)
    x += 0.5
  return image, x


def head(talker):
  image = None
  if talker == "human":
    image = images_h[1]
  elif talker == "god":
    image = images_h[0]
  else:
    return None
  return pygame.transform.rotozoom(image, 0, 3)

def god_enter(r,y):
  image = images_g[r]
  image = pygame.transform.rotozoom(image, 0, 3)
  image = pygame.transform.flip(image,True,False)
  return image


a = None
image = None
lenr = len(current_tick) - 2
tree = print_tree()
tree_created = 1
while True:

  if curr_t < 1:

    if curr_in < lenr:
      print(current_tick[curr_in])
      if current_tick[curr_in] != "speak":
        curr_in += 2
      else:
        curr_in += 3
      if current_tick[curr_in]:
        print(curr_in, current_tick[curr_in])
        if current_tick[curr_in] == "speak":
          printv = current_tick[curr_in + 1]
          curr_hed = current_tick[curr_in + 2]
          curr_t += 400 + len(printv) ^ 3
          
        elif current_tick[curr_in] == "clear":
          printv = ""
        elif current_tick[curr_in] != "end":
          curr_t = current_tick[curr_in + 1]
    else:
      curr_in = len(current_tick) - 1
  p = write(printv, font)
  d = head(curr_hed)
  screen.fill((135, 206, 235))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()

  b = tick(rounds_move, cool_move, cool_idle, rounds_idle, ax_move, cool_ax, 
           god_move,cool_god)

  rounds_move = b[0]
  rounds_idle = b[1]
  cool_move = b[2]
  cool_idle = b[3]
  cool_ax = b[4]
  ax_move = b[5]
  god_move = b[6]
  cool_god = b[7]
  b = print_grass()
  c = print_clouds()
  posa = -25

  if current_tick[curr_in] == "right":
    a = check_key("right", rounds_move, x)
    x = a[1]
    screen.blit(a[0], (x, y))
  elif current_tick[curr_in] == "left":
    a = check_key("left", rounds_move, x)
    x = a[1]
    screen.blit(a[0], (x, y))
  elif current_tick[curr_in] == "axe_swing":
    a = axe_swing(ax_move)
    screen.blit(a, (x - 40, y - 50))
  elif current_tick[curr_in] == "god enter":
    a = god_enter(god_move,g_y)
    screen.blit(a, (g_x, g_y))
    g_y +=50

  elif current_tick[curr_in] == "wait" or current_tick[
      curr_in] == "end" or current_tick[curr_in] == "speak":
    a = idle(rounds_idle)
    screen.blit(a, (x, y))

  for i in range(47):
    screen.blit(b, (posa, 568))

    posa = i * 24

  for i in range(len(cloud_line)):
    screen.blit(c, (cloud_line[i], cloud_y[i]))
  if current_tick[curr_in] == "speak":
    pygame.draw.rect(screen, (0, 0, 0), (70, 0, 500, 100))
  screen.blit(p, (70, 0))
  if current_tick[curr_in] == "speak":
    if curr_hed == "human":
      screen.blit(d, (-10, 0))
    elif curr_hed == "god":
      screen.blit(d, (-55, -70))
  if tree_created == 1:
    screen.blit(tree, (300, 266))
    

  pygame.display.flip()
  if current_tick[curr_in] != "axe_swing" or current_tick[curr_in] != "god enter":
    curr_t -= 1
  else:
    if ax_move == 0:  
      print("gp")
      curr_t -= 1
      tree_created = 0
    if curr_in == 0:
      print("og")
      curr_t -= 1
      god_entered = 0
