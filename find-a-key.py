from random import randint
class game:
    def __init__(self,row=9,column=9):
        self.map = [['0' for a in range(row)]for b in range(column)]
        self.x=randint(0,row-1)
        self.map[randint(0,row-1)][randint(0,column-1)]="5"
        self.keyx=randint(0,row-1)
        self.keyy=randint(0,column-1)
        while self.map[self.keyx][self.keyy]=="5":
            self.keyx=randint(0,row-1)
            self.keyy=randint(0,column-1)

    def __repr__(self) -> str:
        b=""
        for row in self.map:
            for instant in row:
                b+=instant+" "
            b+="\n"
         
        return b
    def move(input):

                   

a = game(9,9)
print(a)