"""

Task 05 (30 points)
Now we’re going to add some more complexity to our class. You are to add the
following:
- Create a new class that inherits from your original class
- Add two new private class variables
    - Override the constructor to only accept these new variables
- Override one of your methods to accept a numeric value and use that in a condition
- Add a class variable that is a number
- Add a new method that will take in a number and add it to with the previously created
numeric value so long as it is within a certain range

Example structure
class Pug
    squishface = true
grossrating = 10
__init__(size, rate, name, squishface, grossrating):
increment_cute(number, grossrating):
if grossrating > 8:
    return false
else:
rate += number
return rate
wrinkles = 25
wrinkle(newwrinkles):
if wrinkles + newwrinkles < 50:
    wrinkles += newwrinkles
else:
print("That's too many wrinkles, man")
return false


"""


class Triangle:
    angleA = 34
    angleB = 55
    angleC = 55
    def __init__(self, angleA, angleB, angleC):
        self.angleA = angleA
        self.angleB = angleB
        self.angleC = angleC

class Square(Triangle):
    degree1 = 60
    degree2 = 60

    def __init__(self, degree1, degree2):
        self.__degree1 = degree1
        self.__degree2 = degree2

    def getDegrees(self, degree1, degree2):
        if degree1 + degree2 > 90:
            return False
        else:
            return True

    degrees3 = 90
    def alwaysarightangle(changeangle, degree1, degree2, degrees3):

        if degrees3 or degree2 or degree1 >= 90:
            return False
        else:
            print("This triangle is obtuse.")
            return True
def main():
    tri1 = Triangle(43, 34, 56)
    square1 = Square(89,43)
    print(tri1.angleA)
    print(square1.alwaysarightangle(90, 45,56))
    print(square1.getDegrees(90, 45))
    print(square1.getDegrees(60, 45))
main()