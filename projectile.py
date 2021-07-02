# Example structure
# class Dog:
#     size = smol
# rate = 10
# name = Schmoopy
# __init__(size, rate, name):
# size = size
# rate = 10


from math import sin, cos, radians


class Projectile:
    def __init__(self, angle, velocity, height):
        self.xpos = 0.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def update(self, time):
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - 9.8 * time
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1

    def gety(self):
        return self.ypos

    def getx(self):
        return self.xpos


def getinputs():
    a = eval(input("Enter the launch angle (in degrees): "))
    v = eval(input("Enter the initial velocity (in meters/sec): "))
    h = eval(input("Enter the initial height (in meters): "))
    t = eval(input("Enter the interval between position calculations: "))
    return a, v, h, t


def main():
    #angle, vel, h0, time = getinputs()
    c = Projectile(60, 50, 20)
    print(c.xpos)
    print(c.ypos)
    print(c.xvel)
    print(c.yvel)

    cball = Projectile(60, 50, 20)

    while cball.gety() >= 0:
        cball.update(1)
    print("\nDistance traveled: {0:0.1f} meters.".format(cball.xpos))

main()