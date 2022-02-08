stack=[]
def dfs(root):
    
    stack.append(root)
    rootState = root.getState()
    rootState = ''.join(rootState)
    
    #a dictionary to track whether an upcoming node has been visited or not
    distances = {rootState: 0}

    #calculates maximum depth reached 
    depth = 0
    
    #calculates the total cost 
    cost =0             

    while stack:
        vertex=stack.pop()
        goal = vertex.isGoal()
        #increases the depth on traversing a new level
        if vertex.depth > depth:             
            depth += 1
        if(goal):
            print("GOAL FOUND !")
            
            return vertex , cost ,depth
        
        
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
                stack.append(neighbour)
               
                distances[neighbourState] = distances[vertexState] + 1
             
        cost = cost+1
