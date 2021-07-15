import turtle
import time
from pygame import mixer

# Adding music is optional as per your choice.
# Initialize pygame mixer
mixer.pre_init(frequency=48000, size=-16, channels=2, buffer=512)
mixer.init()
mixer.music.load("C:\\Users\\Ashish\\Downloads\\titanic.MP3")

# importing turtle
t = turtle.Turtle()

def curve():
    t.pen(pencolor="pink", pensize=3, speed=5)
    for i in range(200):
        t.rt(1)
        t.fd(1)

def love_sign():
    t.pen(pencolor="white",fillcolor="red", pensize=5, speed=5)
    t.shape("turtle")
    t.shapesize(1,1,1)
    t.begin_fill()
    t.lt(50)
    t.fd(113)
    curve()
    t.lt(120)
    curve()
    t.fd(112)
    t.end_fill()

    t.hideturtle()

def love():
    t.lt(50)
    t.fd(36)
    t.circle(15, 180)
    t.lt(260)
    t.circle(15, 180)
    t.fd(36)
"""def love1():
    t.lt(50)
    t.fd(70)
    t.circle(30, 180)
    t.lt(260)
    t.circle(30, 180)
    t.fd(70)"""

window = turtle.Screen()
window.bgcolor('orange')
window.screensize(800, 700)
window.setup(width=1.0, height=1.0, startx=None, starty=None)

# Play Music
mixer.music.play()

t.penup()
t.goto(-80,300)
time.sleep(1)
t.pendown()
t.shapesize(1,2,1)

# ======="I"=========
t.pen(pencolor="red",fillcolor="dark violet", pensize=3, speed=2)#8=2

t.begin_fill()

t.fd(160)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(60) 
t.lt(90)
# ==Height of the 'I'===
t.fd(110)
t.lt(90)
t.fd(60)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(160)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(60)
t.lt(90)
t.fd(110)
t.left(90)
t.fd(60)
t.rt(90)
t.fd(25)

t.end_fill()

# ===================


t.penup()
t.goto(-550,+100)
t.pendown()


# ====="Love"=====
# ====="L"=======
t.pen(pencolor="white",fillcolor="blue", pensize=3, speed=2)#8=2
t.begin_fill()

t.rt(90)
t.fd(25)
t.rt(90)
t.fd(145)
t.lt(90)
t.fd(70)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(95)
t.rt(90)
t.fd(170)
t.rt(90)

t.end_fill()
# ===============

t.penup()
t.fd(140)

#Gap between "L" and "O"
t.fd(10)

# ====="O"======

"""turtle.pensize(5)
turtle.speed(2)
turtle.color("black")
turtle.begin_fill()
turtle.fillcolor("red")
turtle.left(150)
turtle.forward(180)
turtle.circle(-90, 180)
turtle.setheading(60)
turtle.circle(-90, 180)
turtle.forward(180)
turtle.end_fill()
turtle.mainloop()"""

t.pen(pencolor="white",fillcolor="hot pink", pensize=3, speed=2)
t.begin_fill()

t.rt(90)
t.fd(150)
t.lt(90)
t.pendown()
#t.circle(60)
#make heart
t.lt(50)
t.fd(95)
t.circle(40, 180)
t.lt(260)
t.circle(40, 180)
t.fd(95)
##
t.lt(140)
t.penup()
t.fd(20)
t.rt(90)
t.pendown()
#t.circle(40)
t.rt(90)
t.penup()
t.fd(20)
t.lt(90)

t.end_fill()
# ===========

#Gap between "O" and "V"
t.fd(110)
t.pendown()

# ===="V" part====
t.pen(pencolor="white",fillcolor="dark violet", pensize=3, speed=2)
t.begin_fill()

t.lt(100)
t.fd(135)
t.rt(100)
t.fd(30)
t.rt(80)
t.fd(100)
t.lt(80)
t.fd(5)
t.lt(80)
t.fd(100)
t.rt(80)
t.fd(30)
t.rt(100)
t.fd(135)
t.rt(80)
t.fd(52)
t.lt(180)

t.end_fill()
# ========

t.penup()
t.fd(100)
t.pendown()

# ======"E"=====

t.pen(pencolor="white",fillcolor="dark violet", pensize=3, speed=2)
t.begin_fill()

t.lt(90)
t.fd(135)
t.rt(90)
t.fd(80)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(50)
t.lt(90)
t.fd(30)
t.lt(90)
t.fd(50)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(50)
t.lt(90)
t.fd(30)
t.lt(90)
t.fd(50)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(80)

t.end_fill()
# ========

t.penup()
t.rt(180)
#Gap between "V" and "E"
t.fd(200)
t.pendown()

# =======Y letter=====

t.pen(pencolor="white",fillcolor="dark violet", pensize=3, speed=2)
t.begin_fill()

t.lt(90)
t.fd(55)
t.lt(30)
t.fd(90)
t.rt(120)
t.fd(30)
t.rt(60)
t.fd(55)
t.lt(180)
t.rt(60)
t.fd(60)
t.rt(60)
t.fd(30)
t.rt(120)
t.fd(90)
t.lt(30)
t.fd(60)
t.rt(90)
t.fd(27)
t.rt(180)

t.end_fill()
# =======

t.penup()
t.fd(140)
t.pendown()

# ====="dil"=====

t.pen(pencolor="white",fillcolor="cyan", pensize=3, speed=2)
t.begin_fill()

#t.circle(60)
#making DIL
t.lt(50)
t.fd(95)
t.circle(40, 180)
t.lt(260)
t.circle(40, 180)
t.fd(95)
###
t.lt(140)
t.penup()
t.fd(20)
t.pendown()
t.rt(90)
#t.circle(40)
t.rt(90)
t.penup()
t.fd(20)
t.lt(90)

t.end_fill()
# ===========

# Gap between "O" and "U"
t.fd(120)
t.circle(60, extent=60)
t.pendown()

# =====U part====

t.pen(pencolor="white",fillcolor="dark violet", pensize=3, speed=2)
t.begin_fill()

t.lt(30)
# Height of "U"
t.fd(100)
t.lt(90)
t.fd(25)
t.lt(90)
t.fd(80)
t.circle(-20, extent=180)
t.fd(80)
t.lt(90)
t.fd(25)
t.lt(90)
t.fd(100)
t.circle(45, extent=180)

t.end_fill()
#  ========

t.penup()
# t.goto(300,130)
t.rt(160)
t.fd(65)
t.lt(90)
t.fd(140)
t.lt(90)
t.pendown()

# Calling the function for Love Sign
#love_sign()

t.penup()
t.goto(-215,-200)
t.pendown()

t.penup()
# t.goto(300,130)
t.rt(160)
t.fd(65)
t.lt(90)
t.fd(140)
t.lt(90)
t.pendown()
love()



t.penup()
t.goto(+87,-95)
t.pendown()

t.penup()
# t.goto(300,130)
t.rt(180)
t.fd(65)
t.lt(280)
t.fd(140)
t.lt(32)
t.pendown()
love()

t.penup()
t.goto(-103,+1)
t.pendown()

t.penup()
# t.goto(300,130)
t.rt(180)
t.fd(65)
t.lt(280)
t.fd(140)
t.lt(32)
t.pendown()
love()

t.color("red")
t.penup()
t.goto(-180, -190)
t.pendown()

t.penup()
# t.goto(300,130)
t.rt(180)
t.fd(65)
t.lt(300)
t.fd(140)
t.lt(30)
t.pendown()

#    H
t.begin_fill()
t.color("red")
t.up()
t.left(170)
t.forward(80)
t.write("H", font=('Arial', 24, 'bold'))
t.end_fill()
#love1()
time.sleep(1)