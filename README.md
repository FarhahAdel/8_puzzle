# 8_puzzle
solving 8 puzzle game using BFS,DFS and A*

The user is first prompted to enter the initial game state. Our program finds
out if the entered state is solvable or not. If it is, the user is then asked to
choose which algorithm they would like to use.

![image](https://user-images.githubusercontent.com/63178601/153052530-2ca64dad-763e-43b1-ba7b-2539cbcf0b43.png)

Then, according to the chosen algorithm, the puzzle is solved to reach the
goal state. The detailed path to goal is displayed, as well as the total cost,
time taken, number of expanded nodes and total depth.

###### Example: *initial state 1,2,5,3,4,0,6,7,8*

> 1. BFS

![image](https://user-images.githubusercontent.com/63178601/153052621-26e54554-b3e5-4391-8dcf-7ea882a1f239.png)


> 2. DFS

![image](https://user-images.githubusercontent.com/63178601/153052666-ea9f087f-d92a-4225-b4ba-875cc298e08f.png)


> 3. A*(Manhattan distance heuristic)

![image](https://user-images.githubusercontent.com/63178601/153052721-854dd54c-58e7-4a0a-b12e-095564e60fd9.png)


> 4. A*(Euclidean distance heuristic)

![image](https://user-images.githubusercontent.com/63178601/153052761-f6bd6335-de2e-459a-a740-b1402477dd74.png)

A comparison between both heuristics can be seen, in which A*
using Manhattan distance heuristic is proven to be more
admissible then Euclidean distance heuristic.
