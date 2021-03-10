from collections import deque

class Node:
    
    def __init__(self,x,y,distance,prev,power):
        self.x = x
        self.y = y
        self.distance = distance
        self.prev = prev
        self.power = power


def solution(map):
    start = Node(0,0,1,"na",True)
    queue = deque([start])
    row = len(map)
    col = len(map[0])
    memo = [[[0 for temp in range(2)] for j in range(col)] for i in range(row)]

    while queue:
        node = queue.popleft()
        x = node.x
        y = node.y
        prev = node.prev
        next = node.distance + 1
        power = node.power
        
        if power:
            path = memo[x][y][1]
            if path==0:
                memo[x][y][1] = node.distance
            else:
                if path<= node.distance:
                    continue
        else:
            path = memo[x][y][0]
            if path==0:
                memo[x][y][0] = node.distance
            else:
                if path<= node.distance:
                    continue
        
        if x == row -1 and y ==col-1:
            return node.distance
        
        if y < col -1 and prev!="right":
            blocked = map[x][y+1]==1
            if blocked:
                if power:
                    queue.append(Node(x,y+1,next,"left",False))
            else:
                queue.append(Node(x,y+1,next,"left",power))

        
        if x < row -1 and prev!="down":
            blocked = map[x+1][y]==1
            if blocked:
                if power:
                    queue.append(Node(x+1,y,next,"up",False))
            else:
                queue.append(Node(x+1,y,next,"up",power))

        if x > 0 and prev!="up":
            blocked = map[x-1][y]==1
            if blocked:
                if power:
                    queue.append(Node(x-1,y,next,"down",False))
            else:
                queue.append(Node(x-1,y,next,"down",power))
                
        if y > 0 and prev!="left":
            blocked = map[x][y-1]==1
            if blocked:
                if power:
                    queue.append(Node(x,y-1,next,"right",False))
            else:
                queue.append(Node(x,y-1,next,"right",power))
          

    return -99