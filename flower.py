from turtle import *

speed(0)
bgcolor('black')

for i in range(190):
    color('red')
    circle(190 - i, 90)
    left(90)
    circle(190 - i, 90)
    left(18)
done()