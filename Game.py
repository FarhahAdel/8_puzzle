from typing import NewType
from Node import *
from a import *
from bfsOp import *
from dfs import *
from solvable import *
from backtrace import*
import time

initialState = input("Please enter the initial game state : ") 
initialState = list(initialState)

if(isSolvable(getNumOfInv(initialState))):
    print("State is solvable")
    print("Please choose which algorithm you would like to use: ")
    print('''1.BFS 
2.DFS
3.A* ''')
    choice = input("Enter your choice: ")
    newNode = Node(initialState,None)
    newNode.setEmptyslot()
    newNode2 = Node(initialState,None)
    newNode2.setEmptyslot()
    start=0
    start1=0
    end=0
    end1=0
    if int(choice) == 1:
     start=time.time()
     finalNode,expanded,depth= bfs(newNode)
     end=time.time()
    elif int(choice) == 2:
     start=time.time()
     finalNode,expanded,depth= dfs(newNode)
     end=time.time()
    elif int(choice) == 3:
     flag = 1
     print("A* Using Manhattan's distance")
     start=time.time()
     finalNode,expanded,depth =aStar(newNode,1)
     end=time.time()
     print("A* Using Euclidean's distance")
     flag = 0 
     start1=time.time()
     finalNode1,expanded1,depth1 = aStar(newNode2,0)
     end1=time.time()
else:
    print("State is unsolvable")
    exit(0)
backtrace(finalNode)
if int(choice)==1 or int(choice)==2:
    print("Time taken= ",end-start)
    print("Expanded Nodes = ",expanded)
    print("Total Depth = ",depth)
else:
    print("Time taken by Manhattan's distance= ",end-start)
    print("Expanded Nodes = ",expanded)
    print("Total Depth = ",depth)

    backtrace(finalNode1)
    print("Time taken by Euclidean's distance= ",end1-start1)
    print("Expanded Nodes = ",expanded1)
    print("Total Depth = ",depth1)

    

       



  




