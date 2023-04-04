from random import randint
class game:
    def __init__(self,row=9,column=9):
        self.map = [['0' for a in range(row)]for b in range(column)]
        self.x=randint(0,row-1)
        self.y=randint(0,column-1)
        self.map[self.x][self.y]="5"
        self.keyx=randint(0,row-1)
        self.keyy=randint(0,column-1)
        self.distance = abs(self.x-self.keyx) + abs(self.y-self.keyy)
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
    def move(self,inputt):
        if inputt=="w":
            if self.x!=0:
                self.map[self.x][self.y]="1"
                self.x-=1
                self.map[self.x][self.y]="5"
                print(self)
            else :
                print("wall")
                print(self)
        if inputt=="s":
            if self.x!= len(self.map)-1:
                self.map[self.x][self.y]="1"
                self.x+=1
                self.map[self.x][self.y]="5"
                print(self)
            else :
                print("wall")
                print(self)               
        if inputt=="a":
            if self.y!=0:
                self.map[self.x][self.y]="1"
                self.y-=1
                self.map[self.x][self.y]="5"
                print(self)
            else :
                print("wall")
                print(self)    
        if inputt=="d":
            if self.y!=len(self.map[0])-1:
                self.map[self.x][self.y]="1"
                self.y+=1
                self.map[self.x][self.y]="5"
                print(self)
            else :
                print("wall")
                print(self)  
        if self.x==self.keyx and self.y==self.keyy:
            print('you win!') 
            return 0
    def give_clue(self):
        new_distance = abs(self.x-self.keyx) + abs(self.y-self.keyy)
        if new_distance< self.distance:
            print("hotter")
            self.distance=new_distance
        if new_distance > self.distance:
            print("colder")
            self.distance=new_distance                     
        

b=game(5,5)               
print(b)
c="1"
while(c!=0):
    
    c = b.move(input())
    b.give_clue()
