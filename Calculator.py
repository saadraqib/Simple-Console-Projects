

class Calculator:
    def __init__(self):
        self.operate()

    def operate(self):
        self.x = int(input("Enter Number: "))
        self.to_more()

    def to_more(self):
        self.operator = input("operator: ")
        if self.operator == "=":
            print(self.x)
        else:
            self.y = int(input("operated by: "))
            self.operation()
            self.to_more()
            #print("Current Result >>>>"+self.x)
        
        # print(self.x)  give results in every operations, if not only the last result
            

    def operation(self):
        
        if self.operator == "+":
            self.x += self.y
        if self.operator == "-":
            self.x -= self.y
        if self.operator == "/":
            self.x /= self.y
        if self.operator == "*":
            self.x *= self.y
        print(self.print())
        #else: self.operation()
    def print(self):
        return self.x
        


calculator = Calculator()
calculator
