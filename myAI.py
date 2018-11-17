import colorfight
import random

goldArr=[]
engArr=[]
myCells=[]
target=(0,0)


def getMyCells():
    myCells.clear()
    for x in range(g.width):
        for y in range(g.height):
            if g.GetCell(x,y).owner==g.uid:
                myCells.append((x,y))

def base():

    randX = random.randint(g.cellNum*2,g.cellNum*10)
    randY = random.randint(g.cellNum*2,g.cellNum*10)
    sumX=0
    sumY=0
    posX=0
    posY=0
    sumX = sum([pairs[0] for pairs in myCells])
    sumY = sum([pairs[1] for pairs in myCells])
    posX=int((sumX+randX)/g.cellNum)
    posY=int((sumY+randY)/g.cellNum)
    if(g.GetCell(posX,posY).isBase==False):
        print(g.BuildBase(posX,posY))
        print(posX, posY)


def randDirection():
      d = random.choice([(0,1), (0,-1), (1, 0), (-1,0)])
      return d
def attack():

    cell=random.choice(myCells)
    x=cell[0]
    y=cell[1]
    d = randDirection()
    aCell=g.GetCell(x+d[0],y+d[1])
    if aCell != None:
        if aCell.owner != g.uid:
            if g.energy>30:
                print(g.AttackCell(x+d[0], y+d[1]), True)
            else:
                print(g.AttackCell(x+d[0], y+d[1]))


if __name__ == '__main__':

    g = colorfight.Game()


    if g.JoinGame('BREAD'):
        getMyCells()
        counter =0

        while True:
            #getMyCells()

            attack()
            counter=counter+1
            if(g.gold>80 and g.baseNum<3 and g.cellNum>50):
                base()
            if(counter>30):
                getMyCells()
                counter=0
                g.Refresh()



    else:
        print("Failed to join the game!")
