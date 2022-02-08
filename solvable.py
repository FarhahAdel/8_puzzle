import math
#checks whether the input state is solvable by counting the number of inversions
def getNumOfInv(a):
    invCount=0
    for i in range (0,9):
        for j in range (i+1,9):
            if int(a[i])!=0 and int(a[j])!=0 and int(a[i])>int(a[j]):
                invCount+=1
    return invCount
#@staticmethod
def isSolvable(invCount):
     if invCount%2==0: return 1
     return 0







               
                    


               



