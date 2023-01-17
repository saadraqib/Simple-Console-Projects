import os

#"We call this game Three rock(سێ رسکانێ)in Kurdish(ثلاثة أحجار) in Arabic"
print("""_summary_
   This is a game that two opponent play with each other,
   each of them have three rock, and we choose W and R or white and red 
   and in the first they should set thier settings or maps on the 3X3 board 
   after that they move their rocks to specific orders to win like Tic Tac Toe ,
   But this game unlike Tic tac toe, the players should play until one of them
   win the game , the winner should their rocks on one of these orders,
   (R R R or W W W) Vertical or Horizontal or Diagonally
   and the players can move thier rocks with 1-9 
   but when a player press other keys it gives an error and 
   he will try another one between 1-9 digits

""")


class ThreeRock():
    def __init__(self, z=0, w=0):
        self.z = z
        self.w = w

        self.t = self.board()
        self.player()
        self.moveIt()

    def board(self, x=3, y=3):
        self.x = 3
        self.y = 3
        map = []
        for i in range(0, self.x):
            map.append([])
            for j in range(0, self.y):
                map[i].append("-")
            
        return map

    def print_board(self, x):

        for i in x:
            for j in i:
                print(j, end=" ")
            print(" ")

    def changing(self, step):
        self.z = self.w = 0
        # remove this from here and enter in the appropirate function

        if step >= 7:
            self.z = 2
        elif step >= 4:
            self.z = 1
        else:
            self.z = 0
        if step % 3 == 0:
            self.w = 2
        elif (self.z == 1 and step % 2 == 0) or (self.z != 1 and step % 2 != 0):
            self.w = 0
        else:
            self.w = 1

    def clear(self): return os.system("cls")

    def player(self):
        
        self.print_board(self.t)
        self.p1 = set()
        self.p2 = set()
        k = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        while True:
            try:
                step = int(input(f"character except ({self.p1})({self.p2}): "))
            except ValueError:
                print("ERROR: not in base 10")
                step = int(input(f"character except ({self.p1})({self.p2}): "))

            self.changing(step)
            if step not in k:
                print("Invalid nu")

            elif len(k) % 2 == 0:
                self.p2.add(step)
                k.remove(step)
                player = "R"
                self.t[self.z][self.w] = player
                self.clear()
                self.print_board(self.t)

            elif len(k) % 2 != 0:
                self.p1.add(step)
                k.remove(step)
                player = "W"
                self.t[self.z][self.w] = player

                self.clear()
                self.print_board(self.t)

            if len(k) == 3 or step == "0":
                break

    def moveIt(self):
        p = 2
        while True:
            stepFrom = int(input("Move from: "))

            if stepFrom in self.p1 and p % 2 == 0:
                self.p1.remove(stepFrom)
                player = "-"
                self.changing(stepFrom)
                self.t[self.z][self.w] = player
                self.clear()
                self.print_board(self.t)
                stepTo = int(input("Move To: "))
                if ((stepTo == stepFrom + 3 or stepTo == stepFrom - 3) and stepTo not in self.p2) or ((stepTo == stepFrom + 1 or stepTo == stepFrom - 1) and stepTo not in self.p2):
                    self.changing(stepTo)
                    player = "W"
                    self.p1.add(stepTo)
                    self.t[self.z][self.w] = player
                    self.clear()
                    self.print_board(self.t)

                else:
                    stepTo = stepFrom
                    self.p1.add(stepTo)
                    player = "W"
                    self.changing(stepFrom)
                    self.t[self.z][self.w] = player
                    self.clear()
                    self.print_board(self.t)
                    p -= 1

                if self.check(self.p1) == True:
                    print("Player One (W) you won")
                    break

            elif stepFrom in self.p2 and p % 2 != 0:
                self.p2.remove(stepFrom)
                player = "-"
                self.changing(stepFrom)
                self.t[self.z][self.w] = player
                self.clear()
                self.print_board(self.t)
                stepTo = int(input("Move To: "))

                if ((stepTo == stepFrom + 3 or stepTo == stepFrom - 3) and stepTo not in self.p1) or ((stepTo == stepFrom + 1 or stepTo == stepFrom - 1) and stepTo not in self.p1):
                    self.changing(stepTo)
                    player = "R"
                    self.p2.add(stepTo)
                    self.t[self.z][self.w] = player
                    self.clear()
                    self.print_board(self.t)
                else:
                    stepTo = stepFrom
                    self.p2.add(stepTo)
                    player = "R"
                    self.changing(stepFrom)
                    self.t[self.z][self.w] = player
                    self.clear()
                    self.print_board(self.t)
                    p -= 1

                if self.check(self.p2) == True:
                    print("Player Two (R) you won")
                    break

            p += 1

    def check(self, Pl):
        Pl = sorted(Pl)
        lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
                 [2, 5, 8], [3, 6, 9], [3, 5, 7], [1, 5, 9]]
        for i in lists:
            if i == Pl:
                return True
            else:
                continue


game = ThreeRock()
print(game)
