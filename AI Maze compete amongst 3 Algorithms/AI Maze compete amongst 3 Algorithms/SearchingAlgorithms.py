def DFS(m,start=None):

    # if start is None:
    start=(m.rows,m.cols)
    explored=[start]
    discovered=[start]
    dfsPath={}
    dfsSearch=[]
    while len(discovered)>0:
        currentNode=discovered.pop()
        dfsSearch.append(currentNode)
        if currentNode==(1,1):
            break
        for direction in 'ESNW':
            if m.maze_map[currentNode][direction]==True:
                if direction=='E':
                    childCell=(currentNode[0],currentNode[1]+1)
                elif direction=='W':
                    childCell=(currentNode[0],currentNode[1]-1)
                elif direction=='N':
                    childCell=(currentNode[0]-1,currentNode[1])
                elif direction=='S':
                    childCell=(currentNode[0]+1,currentNode[1])
                if childCell in explored:
                    continue
                explored.append(childCell)
                discovered.append(childCell)
                dfsPath[childCell]=currentNode
    tracePath={}
    cell=(1,1)
    while cell!=start:
        tracePath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return dfsSearch, dfsPath ,tracePath

def BFS(m):
    start=(m.rows,m.cols)
    discovered=[start]
    explored=[start]
    bfsSearch=[]
    bfsPath = {}
    while len(discovered)>0:
        currentNode=discovered.pop(0)
        bfsSearch.append(currentNode)
        if currentNode==(1,1):
            break
        for direction in 'ESNW':
            if m.maze_map[currentNode][direction]==True:
                if direction=='E':
                    childCell=(currentNode[0],currentNode[1]+1)
                elif direction=='W':
                     childCell=(currentNode[0],currentNode[1]-1)
                elif direction=='N':
                     childCell=(currentNode[0]-1,currentNode[1])
                elif direction=='S':
                     childCell=(currentNode[0]+1,currentNode[1])
                if childCell in explored:
                    continue
                discovered.append(childCell)
                explored.append(childCell)
                bfsPath[childCell]=currentNode
    tracePath={}
    cell=(1,1)
    while cell!=start:
        tracePath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return bfsSearch, bfsPath, tracePath

from queue import PriorityQueue

def dijkstra(m): # h is for hurdles M is for maze

    discovered={n:float('inf') for n in m.grid}  #infinity 
    discovered[(m.rows,m.cols)]=0
    explored={}
    revPath={}
    djkPath=[]

    while discovered:
        currentNode=min(discovered,key=discovered.get)
        explored[currentNode]=discovered[currentNode]
        djkPath.append(currentNode)
        if currentNode==(1,1):
            break
        for direction in 'EWNS':
            if m.maze_map[currentNode][direction]==True:
                if direction=='E':
                    childCell=(currentNode[0],currentNode[1]+1)
                elif direction=='W':
                    childCell=(currentNode[0],currentNode[1]-1)
                elif direction=='N':
                    childCell=(currentNode[0]-1,currentNode[1])
                elif direction=='S':
                    childCell=(currentNode[0]+1,currentNode[1])
                if childCell in explored:
                    continue
                tempDist= discovered[currentNode]+1
                

                if tempDist < discovered[childCell]:
                    discovered[childCell]=tempDist
                    revPath[childCell]=currentNode
        discovered.pop(currentNode)


    tracePath={}
    cell=(1,1)
    while cell!=(m.rows,m.cols):
        tracePath[revPath[cell]]=cell
        cell=revPath[cell]


    return djkPath, tracePath,explored[(1,1)]


