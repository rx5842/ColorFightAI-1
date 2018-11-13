# You need to import colorfight for all the APIs
import colorfight
import random
import math

goldArr=[]
engArr=[]
myCells=[]
target=(0,0)
def goldEnergyArr():

    for x in range (g.width):
        for y in range(g.height):
            c=g.GetCell(x,y)
            if c.cellType=="gold" and c.owner != g.uid:
                goldArr.append((x,y))
            if c.cellType=="energy" and c.owner != g.uid:
                engArr.append((x,y))

def attackMin():
    x=0

def attackTarget(xt,yt):
    myclose=(0,0)
    cdist=10000
    for cell in myCells:
        x=cell[0]
        y=cell[1]
        if(distance(x,y,xt,yt)<cdist):
            cdist=distance(x,y,xt,yt)
            myclose=(x,y)

    print("myclose",myclose)

    if(xt<myclose[0]):
        print(g.AttackCell(myclose[0]-1,myclose[1]))
    if(xt>myclose[0]):
        print(g.AttackCell(myclose[0]+1,myclose[1]))
    if(yt<myclose[1]):
        print(g.AttackCell(myclose[0],myclose[1]-1))
    if(yt>myclose[1]):
        print(g.AttackCell(myclose[0],myclose[1]+1))


def getGold():
    goldEnergyArr()
    myclose=(0,0)
    cdist=10000
    for cell in myCells:
        x=cell[0]
        y=cell[1]
        for gCell in goldArr:
            gx=gCell[0]
            gy=gCell[1]
            if(distance(x,y,gx,gy)<cdist):
                cdist=distance(x,y,gx,gy)
                myclose=(x,y)
                t=(gx,gy)
    return t

def distance(x1, y1, x2, y2):
    return int((math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))))


def getEnergy():
    goldEnergyArr()
    myclose=(0,0)
    cdist=10000
    for cell in myCells:
        x=cell[0]
        y=cell[1]
        for gCell in engArr:
            gx=gCell[0]
            gy=gCell[1]
            if(distance(x,y,gx,gy)<cdist):
                cdist=distance(x,y,gx,gy)
                myclose=(x,y)
                t=(gx,gy)
    return t

def getMyCells():
    for x in range(g.width):
        for y in range(g.height):
            if g.GetCell(x,y).owner==g.uid:
                myCells.append((x,y))



def base():
    if g.gold<60 or g.baseNum>2 or len(myCells)<25:
        return
    sumX=0
    sumY=0
    posX=0
    posY=0

    sumX = sum([pairs[0] for pairs in myCells])
    sumY = sum([pairs[1] for pairs in myCells])
    posX=int(sumX/len(myCells))
    posY=int(sumY/len(myCells))

    print(g.BuildBase(posX,posY))
    #print(posX)
    #print(posY)


if __name__ == '__main__':
    g = colorfight.Game()

    if g.JoinGame('BREAD'):

        goldEnergyArr()

        while True:
            getMyCells()
            #base()
            target=getGold()
            print ("target",target)
            attackTarget(target[0],target[1])


        # while True:
        #     getMyCells()
        #     base()
        #     getGold()
        #
        #     g.Refresh()
    else:
        print("Failed to join the game!")













    # for x in range(g.width):
    #     for y in range(g.height):
    #         # Get a cell
    #         c = g.GetCell(x,y)
    #         # If the cell I got is mine
    #         if c.owner == g.uid:
    #             # Pick a random direction based on current cell
    #
    #             cut=0
    #             crt=0
    #             clt=0
    #             cdt=0
    #
    #             cu = g.GetCell(x,y-1)
    #             if cu!= None:
    #                 cut =  cu.takeTime
    #             cr = g.GetCell(x+1,y)
    #             if cr!= None:
    #                 crt=cr.takeTime
    #             cl = g.GetCell(x-1,y)
    #             if cl!= None:
    #                 clt=cl.takeTime
    #             cd = g.GetCell(x,y+1)
    #             if cd!= None:
    #                 cdt=cd.takeTime
    #
    #             minTime = min(cut,crt,clt,cdt)
    #             minCell =cu
    #
    #             if(cu!=None):
    #                 if(minTime==cu.takeTime or cu.cellType=="gold" or cu.cellType=="energy"):
    #                     minCell=cu
    #             if(cr!=None):
    #                 if(minTime==cr.takeTime or cr.cellType=="gold" or cr.cellType=="energy"):
    #                     minCell=cr
    #             if(cl!=None):
    #                 if(minTime==cl.takeTime or cl.cellType=="gold" or cl.cellType=="energy"):
    #                     minCell=cl
    #             if(cd!=None):
    #                 if(minTime==cd.takeTime or cd.cellType=="gold" or cd.cellType=="energy"):
    #                     minCell=cd
    #
    #
    #
    #             #d = random.choice([(0,1), (0,-1), (1, 0), (-1,0)])
    #             # Get that adjacent cell
    #             #cc = g.GetCell(x+d[0], y+d[1])
    #
    #             if minCell!=None:
    #                 if minCell.owner!=g.uid:
    #                     if g.energy>30:
    #                         print(g.AttackCell(minCell.x,minCell.y,True))
    #                     else:
    #                         print(g.AttackCell(minCell.x,minCell.y))
    #             if g.baseNum < 3 and g.gold>=60:
    #                 print(g.BuildBase(x,y))
    #             # If that cell is valid(current cell + direction could be
    #             #if g.baseNum == 3 and g.gold>50:
    #                 #print(MultiAttack(minCell.x,minCell.y))
