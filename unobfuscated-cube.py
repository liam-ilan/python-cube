import os
import math
from time import sleep

# return matrix filled with c
def makeScreen(w, h, c):
  return [[c] * w for _ in range(h)]

# clear terminal
def clear():
  if (os.name == 'posix'):
    os.system('clear')
  else:
    os.system('cls')

# render screen
def renderScreen(screen):
  clear()
  print('\n'.join([''.join(r) for r in screen]))

# draw line on screen from p1 to p2, with filled with c (DDA)
# mutates screen
# (0,0) is top left pixel
# color is color do draw line, given as number from 0 - 7
def drawLine(screen, p1, p2, c, color):
  dx = p2[0] - p1[0]
  dy = p2[1] - p1[1]

  step = max(abs(dx), abs(dy))

  dx /= step
  dy /= step

  x = p1[0]
  y = p1[1]

  for i in range(0, int(step) + 1):
    colorStart = '\033[0;' + str(color + 30) + ';40m'
    colorEnd = '\033[0;0m'

    screen[int(y)][int(x)] = colorStart + c + colorEnd
    x += dx
    y += dy

# edge and background material
edgeChar = '█'
background = ' '

# get terminal size
size = os.get_terminal_size()
w = size.columns
h = size.lines

# update loop
t = 0
while True:

  # make screen
  screen = makeScreen(w, h, background)

  # center
  c = [int(w / 2), int(h / 2)]

  # radius of base
  r = 10

  # "squish" factor of base and ceiling
  s = 2.5

  # vertical distance between base and ceiling
  d = 10

  # base of cube
  p1 = [
    math.cos(t) * r + c[0], 
    math.sin(t) * r / s + d / 2 + c[1]
  ]

  p2 = [
    math.cos(t + math.pi / 2) * r + c[0],
    math.sin(t + math.pi / 2) * r / s + d / 2 + c[1]
  ]

  p3 = [
    math.cos(t + math.pi) * r + c[0],
    math.sin(t + math.pi) * r / s + d / 2 + c[1]
  ]

  p4 = [
    math.cos(t + 3 * math.pi / 2) * r + c[0],
    math.sin(t + 3 * math.pi / 2) * r / s + d / 2 + c[1]
  ]

  # ceiling of cube
  p5 = p1.copy()
  p6 = p2.copy()
  p7 = p3.copy()
  p8 = p4.copy()

  # shift up
  p5[1] -= d
  p6[1] -= d
  p7[1] -= d
  p8[1] -= d

  # base
  drawLine(screen, p1, p2, edgeChar, 1)
  drawLine(screen, p2, p3, edgeChar, 2)
  drawLine(screen, p3, p4, edgeChar, 3)
  drawLine(screen, p4, p1, edgeChar, 4)

  # sides
  drawLine(screen, p1, p5, edgeChar, 1)
  drawLine(screen, p2, p6, edgeChar, 2)
  drawLine(screen, p3, p7, edgeChar, 3)
  drawLine(screen, p4, p8, edgeChar, 4)

  # ceiling
  drawLine(screen, p5, p6, edgeChar, 1)
  drawLine(screen, p6, p7, edgeChar, 2)
  drawLine(screen, p7, p8, edgeChar, 3)
  drawLine(screen, p8, p5, edgeChar, 4)

  # update time step
  sleep(0.15)
  t += 0.1
  
  renderScreen(screen)
