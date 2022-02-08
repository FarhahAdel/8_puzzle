import copy
from functools import cmp_to_key
class Node :
    def __init__(self,state,parent):
        self._state = state
        self.neighbours = []           #list of all the neighbour nodes of the current state
        self._parent = parent          #parent node of the current state
        self._emptySlotposition = 0    #0's position in the current state
        self.depth = 0                 #node's depth 
        self.fn=0
        self.cost =0
    def setFn(self,fn):
        self.fn=fn

    def getfn(self):
        return self.fn
        
    def __cmp__(self, other):
        return cmp_to_key(self.fn, other.fn)

    def __eq__(self, other):
        return (self.fn == other.fn) 

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return (self.fn < other.fn) 

    def __gt__(self, other):
        return (self.fn > other.fn) 

    def __le__(self, other):
        return (self < other) or (self == other)

    def __ge__(self, other):
        return (self > other) or (self == other)

    def getState(self):
        return self._state
    
    #prints the current node's state
    def printState(self):
        for i in range (0,9):
            if i==3 or i ==6 :
                print("")
            print(self._state[i], end =" ")
        print("\n")
    
    def getParent(self):
        return self._parent
     #possible actions taken from the current state
    def expandNode(self):
        self.moveRight()
        self.moveLeft()
        self.moveUP()
        self.moveDown()

    def getNeighbours(self):
        return self.neighbours 
    
      #checks whether the goal state is acheived or not
    def isGoal(self):
        goal = True
        for i in range(0,len(self._state)-1) :
            if  self._state[i] > self._state[i+1]:
                goal = False
                return goal
        return goal
    
    #find the 0's position in the current state
    def setEmptyslot(self):
        for i in range(0,9) :
            if self._state[i] == '0' :
                self._emptySlotposition = i
                break

    def setParent(self,val):
        self._parent=val

    def moveRight(self):
        if self._emptySlotposition % 3 <2 :
        
            tempState = copy.copy(self._state)
            tempState[self._emptySlotposition] , tempState[self._emptySlotposition+1] =  tempState[self._emptySlotposition+1] , tempState[self._emptySlotposition]
            rightNode = Node(tempState,self)
            rightNode.setEmptyslot()
            self.neighbours.append(rightNode)
            
    def moveLeft(self):
      
        if self._emptySlotposition % 3 >0 :
          
            leftState = copy.copy(self._state)
            leftState[self._emptySlotposition] , leftState[self._emptySlotposition-1] =  leftState[self._emptySlotposition-1] , leftState[self._emptySlotposition]
            leftNode = Node(leftState,self)
            leftNode.setEmptyslot()
            self.neighbours.append(leftNode)
            
        
    def moveUP(self):
        if self._emptySlotposition >2 :
            tempState = copy.copy(self._state)
            tempState[self._emptySlotposition] , tempState[self._emptySlotposition-3] =  tempState[self._emptySlotposition-3] , tempState[self._emptySlotposition]
            upNode = Node(tempState,self)
            upNode.setEmptyslot()
            self.neighbours.append(upNode)
            
        
    def moveDown(self):
        if self._emptySlotposition <6 :
            tempState = copy.copy(self._state)
            tempState[self._emptySlotposition] , tempState[self._emptySlotposition+3] =  tempState[self._emptySlotposition+3] , tempState[self._emptySlotposition]
            downNode = Node(tempState,self)
            downNode.setEmptyslot()
            self.neighbours.append(downNode)
            
        
    

        

    