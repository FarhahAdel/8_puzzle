import array
import heapq
import math
import numpy as np
visited=[]
fron=[]

def aStar(node,flag):
    visited.clear()
    fron.clear()
    visited.append(node)
    heapq.heappush(fron,node)
    
    expanded = 0
    depth = 0
    exit =1
    while fron:
     current=heapq.heappop(fron)   #get the current node with shortest fn
     visited.append(current)       #add it to visited list  
     goal = current.isGoal()         #check if it's a goal state then return
     if current.depth > depth:             
            depth += 1
     if(goal):
      print("GOAL FOUND !")
     
      return current ,expanded , depth
     current.expandNode()
          #get array of all neighbours 
     for n in current.getNeighbours():                 #loop over all neighbours 
         if flag:      #search if each neighbour found in frontier or already visited 
          heu=manhattan(n.getState())   #if not in frontier or not already visited then insert
         else:
             heu=calcHeu(n.getState()) 
         cost= n.getParent().cost +1
         n.cost = cost
         fn=cost+heu                #fn=gn+hn
         n.setFn(fn)                #set fn in node attributes
         n.depth = depth +1
         if searchPq(n):
            heapq.heappush(fron,n)
     expanded = expanded +1
    return 0
def manhattan(state):

    w=np.array(state)           #convert array into matrix 3x3
    current=w.reshape(3,3)
    goal=[['0','1','2'],['3','4','5'],['6','7','8']]    #define goal matrix
    lookup_loc = {}
    for i in range(3):      #generate tuple of all available pairs of movements
        for j in range(3):
            if(goal[i][j]):
                lookup_loc[goal[i][j]] = (i, j)   #goal coordinates
  
    mDistance = 0      
    for i in range(3):
        for j in range(3):
            if(current[i][j]):
                if current[i][j] != goal[i][j]:
                 correct_loc =lookup_loc[current[i][j]]
                 mDistance += (abs(correct_loc[0] - i) + abs(correct_loc[1] - j))
    
    return mDistance

def calcHeu(state):
    
    w=np.array(state)           #convert array into matrix 3x3
    current=w.reshape(3,3)
    goal=[['0','1','2'],['3','4','5'],['6','7','8']]    #define goal matrix
    lookup_loc = {}
    for i in range(3):      #generate tuple of all available pairs of movements
        for j in range(3):
            if(goal[i][j]):
                lookup_loc[goal[i][j]] = (i, j)
          
    dist = 0        #calc total distance using Euclidean Distance
    for i in range(3):
        for j in range(3):
            if(current[i][j]):
                if current[i][j] != goal[i][j]:         
                 correct_loc =lookup_loc[current[i][j]]
                 dist += math.sqrt(math.pow(correct_loc[0]-i,2) + math.pow(correct_loc[1] - j,2))
           
    return dist

def searchPq(node):
    vFound=0
    fFound=0
    for v in visited:       #check if node is already visited
        if node.getState()== v.getState():  #if visited then set flag
         vFound=1 
         break
    if not vFound:      #if flag=0 (not visited)
        for f in fron:      #check if in frontier 
            if node.getState() == f.getState(): #if in front
                if f.fn>node.fn: #check for fn: if fn of current node < in front list 
                    f.setParent(node.getParent()) #then decrease key and change parent
                    f.setFn(node.fn)
                    heapq.heapify(fron)  #re heapify after edit
                    fFound=1                    #set flag
                    break
        if not fFound:          #if not in frontier list and not visited return 1 else 0
            return 1            
    return 0  
