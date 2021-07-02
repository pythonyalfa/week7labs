"""
Task 02 (10 points)
Now it’s time to add some interactivity to your previous script. Take the class you
    created in the add the following:
- One method that will accept an input, update one of the class variables, and return the
new value
- One method that will accept an input, perform some kind of error checking, update one
of the class variables, and return the new value

Example structure
def set_size(newsize):
    size = newsize
    return size

def increment_cute(number):
    if rate < 10:
        rate += number
    return rate
    else
    return false
"""
class Triangle():

    def __init__(self, angleA, angleB, angleC):
        self.angleA = angleA
        self.angleB = angleB
        self.angleC = angleC

    def get_point1(self, angleA):
        return self.angleA

    def get_point2(self, angleB):
        return self.angleB

    def get_point3(self, angleC):
        return self.angleC

    def checkifRightTriangle(self, angleA, angleB, angleC):
        if angleA == 90 or angleB == 90 or angleC == 90:
            return "This is a right triangle."
        else:
            return False
            
            

    def newAngle(self):
        angleA = input("New angle A : ")
        return angleA


def main():

    tri = Triangle(34, 45, 90)
    print(tri.checkifRightTriangle(90, 34, 22))
    print(tri.checkifRightTriangle(43, 44, 122))
    print(tri.newAngle())
    print(tri.angleA,tri.angleB,tri.angleC)

main()
