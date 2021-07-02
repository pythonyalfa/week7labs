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