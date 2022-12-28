#Tank

class Tank():
    def __init__(self,direction,x_dir,y_dir): #, suviai[0], suviai[1], suviai[2], suviai[3]):
        self.direction = direction
        self.x_dir = x_dir
        self.y_dir = y_dir
        self.suviai = [0,0,0,0]
        # self.suviai[0] = suviai[0]
        # self.suviai[1] = suviai[1]
        # self.suviai[2] = suviai[2]
        # self.suviai[3] = suviai[3]


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
        print(f'Iššauta {sum(self.suviai)} kartu')
        print(f'N - {self.suviai[0]}, S - {self.suviai[1]}, W - {self.suviai[2]}, E - {self.suviai[3]}')

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

act = ''
# suviai = [0,0,0,0]

leopard = Tank('',0,0)

while True:
    act = input('Išrink komanda: ')
    if act in 'nswefx':
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
            case 'x':
                leopard.info()
                break
    else:
        print ('Netinkati komanda')

