# Use Recursive call, draw Square spiral.
import turtle as t    #Using turtle

def spiral(sp_len):
    if sp_len<=5:
        return
    t.forward(sp_len)    #Turtle walk on forward () move.
    t.right(90)    #Draw right(angle 90degree)
    spiral(sp_len - 5)    #Spiral(spiral number, gap size)

t.speed(0)    #Draw maximum speed
spiral(100)
t.hideturtle()    #hideturtle.
t.done()    #Hold Graphic screen