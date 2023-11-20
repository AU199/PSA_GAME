import pygame
import os
import random

RandomNum = random.randint(0, 4)

pygame.init()

screen = pygame.display.set_mode((700, 600))
pygame.display.set_caption('GAME')
screen.fill((240, 240, 240))
x = 0
g_x = 60
y = 500
g_y = 500
rounds_move = 1
rounds_idle = 0
ax_move = 1
god_move = 0
curr_in = 0
cool_move = 0
cool_ax = 0
cool_god = 0
cool_idle = 0
tree_created = 1
god_entered = 0
c_chart = 0
p_chart = 0
poss = 0
printv = ""
c_c = ""
p_c = ""
p = None
printx = ""
printa = ""
p2 = None
curr_hed = ""
images_m = []
images_i = []
images_e = []
images_ax = []
images_g = []
images_h = []
line_breaks = 0
current_tick = [
    "right", 600, "axe_swing", 2, "entry_god", 2, "speak", "STOP!!", "god",
    "speak", "Why are you trying to cut a tree down?", "god", "speak",
    "So my cattle can graze", "human", "speak",
    " Why can't you do that somewhere else? ", "god", "speak",
    "Because there is nowhere else.", "human", "speak",
    "And why does it even matter!!", "human", "speak", "Why does it matter!?",
    "god", "speak", "Well if you must know", "god", "speak",
    "It disrupts the Carbon Cycle in the rainforest", "god", "speak",
    "Wait, What is the carbon cycle?", "human", "Carbon Chart Start", 2,
    "speak",
    "Well The carbon cycle is the movement of carbon between living and non-living objects on Earth.",
    "god", "Carbon Chart End", 2, "speak",
    "Well, I still don't get why I shouldn't cut down trees", "human", "speak",
    "When You cut trees there are less of them to absorb and store the Carbon from the air.",
    "god", "speak",
    "And when the trees start to decompose they release more Carbon into the atmosphere",
    "god", "speak",
    "leading to a higher amount of greenhouse gases, and other things driving global warming",
    "god", "speak",
    "And a the real life example of this is the Amazon Rainforest.",
    "god", "speak",
    "With deforestation on the rise and more than 1000 kilometers of land leveled",
    "god", "speak",
    "A report from 2022 shows that agriculture is the main reason for this.",
    "god", "speak",
    "speak",
    "","god"
    "clear", "end"
]
god_current_tick = ["wait", 1000, "left", 20]
curr_t = current_tick[1]
font = pygame.font.Font("FONT.ttf", 24)

cloud_line = list(range(0, 700, random.randint(30, 100)))
cloud_y = []
for i in range(len(cloud_line)):
  cloud_y.append(random.randint(0, 200))
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
    gm = 0
    gc += 100

  if cm > 0:
    cm -= 1
  if ci > 0:
    ci -= 1
  if ac > 0:
    ac -= 1
  if gc > 0:
    gc -= 1
  return rm, ri, cm, ci, ac, am, gm, gc


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


def god_enter(move, y):
  image = images_g[0]
  image = pygame.transform.rotozoom(image, 0, 3)
  return image


def line_break(curr_sentence: str):
  if len(curr_sentence) > 25:
    middle_index = len(curr_sentence) // 2
    first_sentence = curr_sentence[:middle_index]
    second_sentence = curr_sentence[middle_index:len(curr_sentence)]
    return first_sentence, second_sentence

  else:
    return curr_sentence


def resize_image(index, images_e):
  image = pygame.transform.rotozoom(images_e[index], 0, 1)
  return image


a = None
image = None
lenr = len(current_tick) - 2
tree = print_tree()
tree_created = 1
line_breaks = 0
curr_line = 1

while True:

  if curr_t < 1:
    line_breaks = 0
    if curr_in < lenr:

      if current_tick[curr_in] != "speak":
        curr_in += 2
      else:
        curr_in += 3
      if current_tick[curr_in]:

        if current_tick[curr_in] == "Carbon Chart Start":
          c_chart = 1
          c_c = resize_image(5, images_e)
        if current_tick[curr_in] == "Carbon Chart End":
          c_chart = 0
        if current_tick[curr_in] == "speak" and line_breaks == 0:
          if len(current_tick[curr_in + 1]) > 50:
            a = line_break(current_tick[curr_in + 1])
            first_letter = a[0]
            second_sentence = a[1]
            if len(a) > 2:
              line_breaks = 2
              third_sentence = a[2]
              printa = third_sentence

            printv = first_letter
            printx = second_sentence
            curr_line += 1
            line_breaks = 1

          else:
            printv = current_tick[curr_in + 1]
            line_breaks = 0

          curr_t += 400 + len(printv) ^ 3
          curr_hed = current_tick[curr_in + 2]
        elif current_tick[curr_in] == "clear":
          printv = ""
          printx = ""
        elif current_tick[curr_in] != "end":
          curr_t = current_tick[curr_in + 1]
    else:
      curr_in = len(current_tick) - 1
  if line_breaks == 1:
    p = write(printv, font)
    print(printx)
    p2 = write(printx, font)
  elif line_breaks == 2:
    p = write(printv, font)
    print(printx)
    p2 = write(printx, font)
    p3 = write(printa, font)
  else:
    p = write(printv, font)
  d = head(curr_hed)
  screen.fill((135, 206, 235))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()

  b = tick(rounds_move, cool_move, cool_idle, rounds_idle, ax_move, cool_ax,
           god_move, cool_god)

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
    a = god_enter(god_move, g_y)
    screen.blit(a, (g_x, g_y))
    g_y += 50
  elif current_tick[curr_in] == "wait" or current_tick[
      curr_in] == "end" or current_tick[curr_in] == "speak":
    a = idle(rounds_idle)
    screen.blit(a, (x, y))
  if god_entered == 1:
    a = images_g[0]
    screen.blit(a, (g_x, g_y))

  for i in range(47):
    screen.blit(b, (posa, 568))

    posa = i * 24

  for i in range(len(cloud_line)):
    screen.blit(c, (cloud_line[i], cloud_y[i]))
  if current_tick[curr_in] == "speak":
    pygame.draw.rect(screen, (0, 0, 0), (70, 0, 670, 100))
  if line_breaks == 1:
    screen.blit(p, (70, 0))
    screen.blit(p2, (80, 40))
  elif line_breaks == 2:
    screen.blit(p, (70, 0))
    screen.blit(p2, (80, 60))
    screen.blit(p3, (80, 80))

  else:
    screen.blit(p, (70, 0))
  if current_tick[curr_in] == "speak":
    if curr_hed == "human":
      screen.blit(d, (-10, 0))
    elif curr_hed == "god":
      screen.blit(d, (-55, -70))
  if tree_created == 1:
    poss = 300
  else:
    poss = 340
  for i in range(5):
    screen.blit(tree, (poss, 266))
    poss += 60
  if c_chart == 1:
    screen.blit(c_c, (400, 300))

  pygame.display.flip()
  if curr_in > 3:
    tree_created = 0
  if current_tick[curr_in] != "axe_swing" or current_tick[
      curr_in] != "god_enter" or line_breaks != 1:
    curr_t -= 1

  else:
    if ax_move == 0:
      print("gp")
      curr_t -= 1

    if god_move == 0:
      print("og")
      curr_t -= 1
      god_entered = 1
