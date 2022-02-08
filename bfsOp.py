from collections import deque
from math import cos    
#@staticmethod

def bfs(root):
    #calculates maximum depth reached 
    depth = 0
    
    #calculates the total cost 
    cost =0     
    queue = deque([root])
    
    rootState = root.getState()
    rootState = ''.join(rootState)
    

    #a dictionary to track whether an upcoming node has been visited or not
    distances = {rootState: 0}

    while queue:
        vertex = queue.popleft()
        #increases the depth on traversing a new level
        if vertex.depth > depth:             
            depth += 1
        goal = vertex.isGoal()
        if(goal):
          print("GOAL FOUND !")
        
          
          return vertex , cost , depth
        vertex.expandNode()
        vertexState = vertex.getState()
        vertexState = ''.join(vertexState)

        #check whether the current state's neighbours have been visited before or not
        for neighbour in vertex.getNeighbours():
            neighbourState = neighbour.getState()
            neighbourState = ''.join(neighbourState)
            if neighbourState not in distances:
                #assign the depth of the neighbours nodes 
                neighbour.depth = depth+1
                queue.append(neighbour)
               
                distances[neighbourState] = distances[vertexState] + 1
        cost = cost+1
   