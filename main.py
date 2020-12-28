from classes import People
from classes import Students
from classes import Pupils
from classes import Workers
from classes import Qualification


lena = People("Lena", 30)
lena.show_info()
lena.action()

print("----------")

oleg = Students("Oleg", 18, 1, 100)
oleg.show_info()
oleg.action()

print("----------")

igor = Pupils("Igor", 15, 9, "math")
igor.show_info()
igor.action()

print("----------")

stas = Workers("Stas", 45, 500, 7)
stas.show_info()
stas.action()

print("----------")

vasya = Qualification("Vasya", 50, 300, 20, 3)
vasya.show_info()
vasya.action()

print("----------")

petya = Qualification("Vasya", 50, 300, 15)
petya.show_info()
petya.action()
