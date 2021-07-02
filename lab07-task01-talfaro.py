# Task 01 (10 points)
# This assignment will be incredibly open ended, this is by design. I want you to have
# some freedom to create something that you are interested in rather than just following
# along with what I tell you to do. Feel free to go as far as you’d like with your script, don’t
# just stop with the bare minimum. And remember to have fun! Scripts will be graded on
# how much fun you have.
# Create a class of your choosing. It can be an animal class or a bankaccount class.
# Choose something that you are passionate about and familiar with and create it. For the
# purposes of illustration, I will be using a dog class as an example. While I would prefer
# you to create your own unique class, you may use a dog class so long as you do not
# copy my code and you are super passionate about dogs. Your class should have the
# following:
# - Three protected class variables to store key information about the class
# - An __init__ constructor that populates the aforementioned class variables
#
# Example structure
# class Dog:
#     size = smol
# rate = 10
# name = Schmoopy
# __init__(size, rate, name):
# size = size
# rate = 10


# At this point I understand the point of a class and objects
# The problem I have is understanding how to call each different function or when you need
# a setter or a getter but I do know that getters and setters do what their names say
# i know its just standar to call them getters and setter, but can be called anything
# just like self doesn't have to be "self", it is just what is common to use


class Order:
    def __init__(self, item, price, quantity):
        self.item = item
        self.price = float(price)
        self.quantity = quantity

    def getPrice(self):
        return self.price

    def getItem(self):
        return self.item

    def getquantity(self):
        return self.quantity


class Menu:
    def __init__(self, itemNum, price):
        self.itemNum = itemNum
        self.price = price

    def getItem(self):
        return self.itemNum

    def getPrice(self):
        return self.price


class Face:
    def __init__(self, haircolor, skincolor, eyecolor, mood):
        self.haircolor = haircolor
        self.skincolor = skincolor
        self.eyecolor = eyecolor
        self.mood = mood

    def getHaircolor(self):
        return self.haircolor

    def getSkincolor(self):
        return self.skincolor

    def getEyecolor(self):
        return self.eyecolor

    def getMood(self):
        return self.mood


class Connections:
    def __init__(self, ip, subnet, geolocation, country):
        self.ip = ip
        self.subnet = subnet
        self.geolocation = "omaha"
        self.country = "united states"

    def getIp(self, ip):
        return ip

    def getSubnet(self):
        return self.subnet

    def getGeolocation(self):
        return self.geolocation

    def getCountry(self):
        return self.country

