""":cvar

Task 04 (30 points)
Now it’s time to get some use out of your class. You will create the following:
    - Deﬁne a new class that inherits from your previous class
- Override one of your methods to provide new functionality
- Deﬁne a new method speciﬁc to this class

Example structure
class RescueDog(Dog)
    increment_cute(number):
if rate < 20:
    rate += number
return rate
else
return false
puppy_dog_eyes():
rate += 1
return rate



"""
class Triangle():
    angleA = 34
    angleB = 55
    angleC = 55
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




class Isosceles(Triangle):
    def checkifRightTriangle(self, angleA, angleB, angleC):
        x = angleA+angleB+angleC
        if x > 180:
            x = "obtuse"

            return x
        else:
                if x < 180:
                    x = "acute"
                return x

    def which(self, angleA, angleB, angleC):
        x = angleA+angleB+angleC
        if x > 180:
            x = "obtuse"
            return x
        else:
            if x < 180:
                x = "acute"
                return x



def main():

    tri = Triangle(45, 34, 3)
    tri1 = Isosceles(43,54,34)
    print(tri1.which(4,4,180))
    print(tri1.which(2,4,90))

main()