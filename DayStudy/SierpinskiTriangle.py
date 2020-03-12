#Use Recursive calls, draw Sierpinski triangle.

import turtle as t

def tri(tri_len):
  if tri_len <=10:
    for i in range(0,3):
      t.forward(tri_len)
      t.left(120)
    return
  new_len=tri_len/2
  tri(new_len)
  t.forward(new_len)    #Go straight ahead turtle.
  tri(new_len)
  t.backward(new_len)    #Go back straight ahead turtle.
  t.left(60)    #Turtle turn left 60 degree.
  t.forward(new_len)
  t.right(60)    #Turtle turn right 60 degree.
  tri(new_len)
  t.left(60)
  t.backward(new_len)
  t.right(60)

t.speed(10)
tri(150)
#t.hideturtle()
t.done()
