from graphics import *
from random import randint

width = 800
height = 800

xParts = randint(3, 5)
yParts = int(xParts/(width*1.0/height))
buffer = 20

points = []

topPoints = []
bottomPoints = []
leftPoints = []
rightPoints = []

#clr1 = [54, 205, 255]
#clr2 = [198, 107, 255]
#clr1= [randint(0, 255), randint(0, 255), randint(0, 255)]
#clr2= [randint(0, 255), randint(0, 255), randint(0, 255)]
clr1 = [255, 255, 255]
clr2 = [0, 102, 66]
clrRange = 10

# OTHER FUNCTIONS -------------------------------------------

def setColour(shape):
  pts = shape.getPoints()
  x = (pts[0].getX() + pts[1].getX() + pts[2].getX())/3
  base = []

  for i in range(3):
    base.append(int((x/width)*(clr2[i]-clr1[i]) + clr1[i]))

  colour = []

  for i in range(3):
    num = randint(base[i] - clrRange, base[i] + clrRange)
    if num < 0:
      num = 0
    if num > 255:
      num = 255
    colour.append(num)

  shape.setFill(color_rgb(colour[0], colour[1], colour[2]))
  shape.setOutline(color_rgb(colour[0], colour[1], colour[2]))

# INPUT -----------------------------------------------------

"""print("RGB of color 1: ")
clr1[0] = int(input(), 10)
clr1[1] = int(input(), 10)
clr1[2] = int(input(), 10)

print("RGB of color 2: ")
clr2[0] = int(input(), 10)
clr2[1] = int(input(), 10)
clr2[2] = int(input(), 10)"""

# REGULAR POINTS --------------------------------------------

for i in range(0, yParts):
  points.append([])  

  for j in range(0, xParts):
    
    x = randint(width*j//xParts + buffer, width*(j+1)//xParts - buffer)
    y = randint(height*i//yParts + buffer, height*(i+1)//yParts - buffer)

    if i != 0 and j != 0:
      y1 = points[i][j-1].getY()
      y2 = points[i-1][j].getY()
      x1 = points[i][j-1].getX()
      x2 = points[i-1][j].getX()

      m = (y2 - y1)/(x2 - x1)
      b = y2 - m*x2

      if y - b < buffer:
        x = width*(j+1)//xParts - (x - width*j//xParts)
        y = height*(i+1)//yParts - (y - height*i//yParts)


    points[i].append(Point(x, y))


# BORDER POINTS ---------------------------------------------

topPoints.append(Point(0, 0))
bottomPoints.append(Point(0, height-1))

for i in range(1, xParts):
  x = randint(width*i//xParts - (width//xParts)//2 + buffer, width*(i)//xParts + (width//xParts)//2 - buffer)
  bottomPoints.append(Point(x, height-1))

for i in range(1, xParts):
  x = randint(width*i//xParts - (width//xParts)//2 + buffer, width*(i)//xParts + (width//xParts)//2 - buffer)
  topPoints.append(Point(x, 0))

topPoints.append(Point(width-1, 0))
bottomPoints.append(Point(width-1, height-1))

leftPoints.append(Point(0, 0))
rightPoints.append(Point(width-1, 0))

for i in range(1, yParts):
  y = randint(height*i//yParts - (height//yParts)//2 + buffer, height*i//yParts + (height//yParts)//2 - buffer)
  rightPoints.append(Point(width-1, y))

for i in range(1, yParts):
  y = randint(height*i//yParts - (height//yParts)//2 + buffer, height*i//yParts + (height//yParts)//2 - buffer)
  leftPoints.append(Point(0, y))

leftPoints.append(Point(0, height-1))
rightPoints.append(Point(width-1, height-1))

# REAL DRAWING --------------------------------------------

win = GraphWin("yeet", width, height)

for i in range(len(points)):
  for j in range(len(points[i])):

    if j != len(points[i])-1 and i != len(points)-1:
      triangle = Polygon(points[i][j], points[i+1][j], points[i][j+1])
      setColour(triangle)
      triangle.draw(win)
    if j != 0 and i != 0:
      triangle = Polygon(points[i][j], points[i-1][j], points[i][j-1])
      setColour(triangle)
      triangle.draw(win)

# top
for i in range(xParts):
  triangle = Polygon(topPoints[i], topPoints[i+1], points[0][i])
  setColour(triangle)
  triangle.draw(win)

  if i < xParts-1:
    triangle = Polygon(topPoints[i+1], points[0][i], points[0][i+1])
    setColour(triangle)
    triangle.draw(win)

# bottom
for i in range(xParts):
  triangle = Polygon(bottomPoints[i], bottomPoints[i+1], points[yParts-1][i])
  setColour(triangle)
  triangle.draw(win)

  if i < xParts-1:
    triangle = Polygon(bottomPoints[i+1], points[yParts-1][i], points[yParts-1][i+1])
    setColour(triangle)
    triangle.draw(win)

# left
for i in range(yParts):
  triangle = Polygon(leftPoints[i], leftPoints[i+1], points[i][0])
  setColour(triangle)
  triangle.draw(win)

  if i < yParts-1:
    triangle = Polygon(leftPoints[i+1], points[i][0], points[i+1][0])
    setColour(triangle)
    triangle.draw(win)

# right
for i in range(len(points)):
  triangle = Polygon(rightPoints[i], rightPoints[i+1], points[i][xParts-1])
  setColour(triangle)
  triangle.draw(win)

  if i < yParts - 1:
    triangle = Polygon(rightPoints[i+1], points[i][xParts-1], points[i+1][xParts-1])
    setColour(triangle)
    triangle.draw(win)

win.getMouse();
  
