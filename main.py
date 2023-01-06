#Tank
from random import randint
from math import *

class Tank():
    def __init__(self, direction, x_dir, y_dir):
        self.direction = direction
        self.x_dir = x_dir
        self.y_dir = y_dir
        self.suviai = [0,0,0,0]



    def north(self):
        self.y_dir += 1
        self.direction = act

    def south(self):
        self.y_dir -= 1
        self.direction = act

    def west(self):
        self.x_dir -= 1
        self.direction = act

    def east(self):
        self.x_dir += 1
        self.direction = act

    def info(self):
        print(f'Kryptis - {self.direction}')
        print(f'Koordinatai : X = {self.x_dir}, Y = {self.y_dir}')
        print(f'Priešo koordenates : X = {enemy.x_enemy}, Y = {enemy.y_enemy}')
        if enemy.x_enemy == self.x_dir or enemy.y_enemy == self.y_dir:
            print('Jus su priešu ant vienos linijos !!!')
        print(f'Iššauta {sum(self.suviai)} kartu')
        print(f'N - {self.suviai[0]}, S - {self.suviai[1]}, W - {self.suviai[2]}, E - {self.suviai[3]}')

    def test_fire(self):
        if enemy.x_enemy == self.x_dir:
            if (self.y_dir > enemy.y_enemy) and self.direction == 's':
                return True
            elif (self.y_dir < enemy.y_enemy) and self.direction == 'n':
                return True
            else:
                return False
        if enemy.y_enemy == self.y_dir:
            if (self.x_dir > enemy.x_enemy) and self.direction == 'w':
                return True
            elif (self.x_dir < enemy.x_enemy) and self.direction == 'e':
                return True
            else:
                return False

    def fire(self):
        match   self.direction:
            case 'n':
                self.suviai[0] += 1
            case 's':
                self.suviai[1] += 1
            case 'w':
                self.suviai[2] += 1
            case 'e':
                self.suviai[3] += 1
class Enemy():
    def __init__(self):
        self.x_enemy = randint(-10, 10)
        self.y_enemy = randint(-10, 10)

def distance():
    if sqrt((leopard.x_dir - enemy.x_enemy) ** 2 + (leopard.y_dir - enemy.y_enemy) ** 2) > 2:
        return True
    else:
        # print('per arti')
        return False


act = ''
target_exist = True
enemy = Enemy()
leopard = Tank('n', 0, 0)

# print(enemy.x_enemy, enemy.y_enemy)
# print(leopard.x_dir, leopard.y_dir)


while True:
    if not target_exist:
        enemy = Enemy()
        while not distance():
            enemy = Enemy()
        target_exist = True

    act = input('Išrink komanda: ')
    if act in 'nswefxi':
        match act:
            case 'n':
                leopard.north()
            case 's':
                leopard.south()
            case 'w':
                leopard.west()
            case 'e':
                leopard.east()
            case 'f':
                leopard.fire()
                if leopard.test_fire():
                    print('Taikinis sunaikintas !!')
                    target_exist = False

            case 'i':
                leopard.info()
            case 'x':
                leopard.info()
                break
    else:
        print ('Netinkanti komanda')

