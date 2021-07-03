""":cvar

Task 03 (20 points)
Now we’re going to add even more interactivity to your class. Building on what you have
so far, you will now add the following:
- overload the str() and len() methods to return useful information for your class
- overload the equivalence operator (==) such that its use with your class will compare
one of the variables and return true if they are the same and false otherwise

Example structure
__str__():
return name
__len__():
return size
__==__(otherdog):
if rate == otherdog.rate
    return True
else
return False
"""
class Triangle():

    def __init__(self, angleA, angleB, angleC):
        self.angleA = angleA
        self.angleB = angleB
        self.angleC = angleC
        self.length = 4
        self.name = "Teacher"

    def __str__(self):
        return self.name


    def __len__(self):
        return self.length

    def get_point1(self, angleA):
        return self.angleA

    def get_point2(self, angleB):
        return self.angleB

    def get_point3(self, angleC):
        return self.angleC

    def newAngle(self):
        angleA = input("New angle A : ")
        return angleA


def main():
    tri = Triangle(43, 34, 35)
    print(len(tri))                                 # I believe the point of this is to "override" a value with a default value?
    print(tri.angleB)
    print(tri.angleC)
    print(str(tri))                                 # This is another example of overriding. I can see giving a triangle a name,
                                                    # if a name is not part of the calculations, but it is still
                                                    # of some use to have a name or default name for the "triangle"


main()