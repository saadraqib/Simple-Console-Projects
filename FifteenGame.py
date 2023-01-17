import random
import os

class FifteenGame:
    def __init__(self, step=0):

        self.map = [3, 12, 6, 13, 7, 4, 15, 8, 1, 9, 14, 10, 2, 5, 11, "-"]
        #self.map = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, "-", 15]  this is just for testing
        random.shuffle(self.map)
        self.space = self.map.index("-")
        self.step = step
        self.print_map()
        self.changing()
        self.step = step

    def print_map(self):
        row1 = self.map[0:4]
        row2 = self.map[4:8]
        row3 = self.map[8:12]
        row4 = self.map[12:16]
        print(f" {row1} \n {row2} \n {row3} \n {row4} ")

    def canNotMove(self, move):
        if move == "U" and self.space in range(0, 4):
            print("Can't move")
            return True
        if move == "D" and self.space in range(12, 16):
            print("Can't move")
            return True
        if move == "R" and self.space in [3, 7, 11, 15]:
            print("Can't move")
            return True
        if move == "L" and self.space in [0, 4, 8, 12]:
            print("Can't move")
            return True
        else:
            return False

    def checkList(self):
        if self.map == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, "-"]:
            return True
        else:
            return False
    def clear(self): return os.system("cls")
    def changing(self):
        while True:
            self.space = self.map.index("-")
            move = input("Move: ").upper()
            if self.canNotMove(move=move) == True:
                self.changing()
                return

            if move == "U":
                # self.map[self.space-4]= "-"
                self.map[self.space], self.map[self.space -
                                               4] = self.map[self.space-4], self.map[self.space]
            elif move == "D":
                self.map[self.space], self.map[self.space +
                                               4] = self.map[self.space+4], self.map[self.space]
            elif move == "R":
                self.map[self.space], self.map[self.space +
                                               1] = self.map[self.space+1], self.map[self.space]

            elif move == "L":
                self.map[self.space], self.map[self.space -
                                               1] = self.map[self.space-1], self.map[self.space]
            else: print("wroong move")
            self.clear()
            self.print_map()
            self.step += 1
            print(f" moves: {self.step} ")
            if self.checkList() == True:
                print("finish")
                self.finish()
                break
                
    def finish(self):
        more = input("Would you like play more?(y/n) ")
        if(more.lower()=='y'):
            FifteenGame()
        else: pass
            

print("""U ---> Up
D ---> Down
R ---> Right
L ---> Left
      """)
game = FifteenGame()
game
#         self.print_map()
# row1 = map[0:4]
# row2 = map[4:8]
# row3 = map[8:12]
# row4 = map[12:16]
# print(f" {row1} \n {row2} \n {row3} \n {row4} ")

# if move == "D":
#     self.map[self.space] = self.map[self.space + 4]
#     self.map[self.space+4] = self.map[self.space]
#     self.print_map()
# if move == "R":
#     self.map[self.space] = self.map[self.space + 1]
#     self.map[self.space+1] = self.map[self.space]
#     self.print_map()
# if move == "L":
#     self.map[self.space] = self.map[self.space - 1]
#     self.map[self.space-1] = self.map[self.space]
#     self.print_map()


# game = FifteenGame()
# game


# x = []


# def array(row, col):
#     for i in range(0, row):
#         x.append([])
#         for j in range(0, col):
#             x[i].append(j)
#     return x


# def split(array):
#     for x in range(0, len(array)):
#         for y in range(0, len(array)):
#             print(array[x][y], end=" | ")
#         print("\n", "-"*len(array)*len(array))
#     return array[x][y]


# x = array(3, 3)
# x[1][1] = "D"
# split(x)
