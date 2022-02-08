
#Represents the path taken to reach the goal by keeping track of each node's parent
@staticmethod
def backtrace(end):
    #calculates the total cost 
    cost =0             
    print("------Path to goal-------")
    path = []
    while  end.getParent():
        # print("in while")
        path.append(end)
        end = end.getParent()
        cost = cost+1

    path.append(end)
    path.reverse()
    for node in path :
        node.printState()
    print("Total cost = ",cost)
